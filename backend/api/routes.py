# backend/api/routes.py

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
import logging
import uuid
from livekit import api
from services.livekit_service import LiveKitService
from core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()
livekit_service = LiveKitService()


@router.get("/token")
async def get_token():
    """生成 LiveKit Token"""
    try:
        # ✅ 正确的 Token 生成方式
        token = api.AccessToken(
            api_key=settings.LIVEKIT_API_KEY,
            api_secret=settings.LIVEKIT_API_SECRET
        )

        # ✅ 设置身份和房间权限
        token.with_identity("user-web-client")
        token.with_name("Web User")

        # ✅ 添加房间权限（重要！）
        token.with_grants(api.VideoGrants(
            room_join=True,
            room=settings.ROOM_NAME,
            can_publish=True,  # ✅ 允许发布音视频
            can_subscribe=True,  # ✅ 允许订阅音视频
            can_publish_data=True  # ✅ 允许发布数据
        ))

        # ✅ 生成 JWT Token
        jwt_token = token.to_jwt()

        logger.info(f"✅ Token 生成成功: room={settings.ROOM_NAME}")

        return {
            "token": jwt_token,
            "url": settings.LIVEKIT_URL,
            "room": settings.ROOM_NAME
        }

    except Exception as e:
        logger.error(f"❌ Token 生成失败: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
