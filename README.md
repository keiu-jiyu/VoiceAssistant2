# 📝 GitHub README.md

```markdown
# 🎙️ AI 语音助手

基于 LiveKit + 阿里云 NLS + 通义千问的实时语音对话系统

## ✨ 功能特性

- 🎤 **实时语音识别**：使用阿里云语音识别服务（NLS）
- 🤖 **智能对话**：接入阿里云通义千问大模型
- 🔊 **语音合成**：阿里云语音合成（TTS）
- 📡 **实时通信**：基于 LiveKit 的低延迟音视频传输
- 🌐 **Web 界面**：React 前端，简洁易用

---

## 🏗️ 技术栈

### 后端
- **Python 3.10+**
- **FastAPI** - 高性能 Web 框架
- **LiveKit SDK** - 实时音视频
- **阿里云 SDK** - NLS 语音服务
- **Dashscope** - 通义千问 API

### 前端
- **React 18**
- **LiveKit Components** - 音视频组件
- **Create React App** - 项目脚手架

---

## 📦 项目结构

```
voice-assistant/
├── backend/                 # 后端服务
│   ├── api/                # API 服务器
│   │   ├── server.py       # FastAPI 主程序
│   │   └── endpoints/      # API 路由
│   │       └── token.py    # Token 生成
│   ├── agent/              # AI Agent
│   │   ├── server.py       # Agent 主程序
│   │   └── worker.py       # 语音处理工作流
│   ├── core/               # 核心配置
│   │   └── config.py       # 环境配置
│   ├── services/           # 业务服务
│   │   ├── livekit_service.py
│   │   ├── aliyun_stt.py   # 语音识别
│   │   ├── aliyun_tts.py   # 语音合成
│   │   └── llm_service.py  # LLM 对话
│   ├── requirements.txt    # Python 依赖
│   └── .env               # 环境变量（需创建）
│
└── frontend/               # 前端应用
    ├── public/
    ├── src/
    │   ├── App.jsx         # 主组件
    │   ├── index.js        # 入口文件
    │   └── index.css       # 样式
    ├── .env               # 环境变量（需创建）
    └── package.json        # 依赖配置
```

---

## 🚀 快速开始

### 1️⃣ 克隆项目

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2️⃣ 配置后端

#### 安装依赖

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

#### 配置环境变量

创建 `backend/.env` 文件：

```env
# ============ API 服务配置 ============
DEBUG=false
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=1

# ============ LiveKit Cloud 配置 ============
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=APIxxxxxxxxxxxxx
LIVEKIT_API_SECRET=xxxxxxxxxxxxxxxxx
LIVEKIT_ROOM_NAME=voice-room

# ============ 阿里云通义千问配置 ============
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxx
QWEN_MODEL=qwen-plus

# ============ 阿里云语音服务 NLS 配置 ============
# 方式1: 直接使用 Token（测试用，24小时有效）
# ALIYUN_NLS_TOKEN=your_nls_token

# 方式2: 使用 AccessKey（生产推荐，自动刷新）
ALIYUN_ACCESS_KEY_ID=LTAI5xxxxxxxxxx
ALIYUN_ACCESS_KEY_SECRET=xxxxxxxxxxxxxxxxx
ALIYUN_APP_KEY=your_app_key

# ============ 日志配置 ============
LOG_LEVEL=INFO
LOG_DIR=logs
```

#### 启动服务

```bash
# 终端 1：启动 API 服务器
python api/server.py api

# 终端 2：启动 AI Agent
python agent/server.py agent
```

---

### 3️⃣ 配置前端

#### 安装依赖

```bash
cd frontend
npm install
```

#### 配置环境变量

创建 `frontend/.env` 文件：

```env
REACT_APP_API_URL=http://localhost:8000
```

#### 启动应用

```bash
npm start
```

浏览器自动打开 `http://localhost:3000`

---

## 🔑 获取必需的 API Keys

### 1. LiveKit Cloud（免费额度）

1. 访问 https://cloud.livekit.io/
2. 注册/登录账号
3. 创建项目
4. 获取：
   - `LIVEKIT_URL`（WebSocket URL）
   - `LIVEKIT_API_KEY`
   - `LIVEKIT_API_SECRET`

### 2. 阿里云通义千问

1. 访问 https://dashscope.aliyun.com/
2. 开通服务（有免费额度）
3. 获取 `DASHSCOPE_API_KEY`

### 3. 阿里云语音服务（NLS）

1. 访问 https://nls-portal.console.aliyun.com/
2. 开通服务
3. 创建项目，获取 `ALIYUN_APP_KEY`
4. 创建 AccessKey（推荐）或使用 24 小时 Token

---

## 📖 使用说明

1. **启动服务**：确保后端两个服务都已启动
2. **打开网页**：访问 `http://localhost:3000`
3. **授权麦克风**：浏览器会请求麦克风权限
4. **开始对话**：
   - 点击"连接"按钮
   - 等待连接成功（状态变为"已连接"）
   - 直接说话即可，AI 会实时回复

---

## 🐛 常见问题

### 1. WebSocket 401 错误

**原因**：LiveKit API Key/Secret 不正确

**解决**：
- 检查 `.env` 中的 `LIVEKIT_API_KEY` 和 `LIVEKIT_API_SECRET`
- 确保没有多余空格
- 重新从 LiveKit Cloud 复制

### 2. 麦克风无法连接

**原因**：浏览器权限或 HTTPS 问题

**解决**：
- 确保允许麦克风权限
- 使用 `localhost` 或 HTTPS 访问
- 检查浏览器控制台错误

### 3. AI 无响应

**原因**：通义千问 API 配置错误

**解决**：
- 检查 `DASHSCOPE_API_KEY` 是否正确
- 确认账户有可用额度
- 查看后端日志排查错误

### 4. 语音识别失败

**原因**：阿里云 NLS 配置问题

**解决**：
- 检查 `ALIYUN_ACCESS_KEY_ID`、`ALIYUN_ACCESS_KEY_SECRET`
- 确认 `ALIYUN_APP_KEY` 正确
- 确保服务已开通并有额度

---

## 📊 系统架构

```
┌─────────────┐      WebSocket       ┌──────────────┐
│   浏览器    │ ←─────────────────→ │  LiveKit     │
│  (React)    │      音视频流        │   Cloud      │
└─────────────┘                      └──────────────┘
       │                                     ↑
       │ HTTP/REST                           │
       ↓                                     │
┌─────────────┐                             │
│  API Server │                             │
│  (FastAPI)  │                             │
└─────────────┘                             │
                                            │
                                            │
┌───────────────────────────────────────────┘
│
│  ┌─────────────────────────────────────┐
│  │         AI Agent Worker              │
│  │  ┌────────────────────────────────┐ │
│  │  │  1. 语音识别 (阿里云 STT)     │ │
│  │  │  2. 对话生成 (通义千问)       │ │
│  │  │  3. 语音合成 (阿里云 TTS)     │ │
│  │  └────────────────────────────────┘ │
│  └─────────────────────────────────────┘
└─────────────────────────────────────────┘
```

---

## 🛠️ 开发

### 添加新功能

1. **后端**：在 `backend/agent/worker.py` 修改对话流程
2. **前端**：在 `frontend/src/App.jsx` 添加 UI 组件
3. **配置**：在 `.env` 和 `config.py` 添加新配置项

### 调试

```bash
# 后端日志
tail -f backend/logs/app.log

# 前端控制台
# 打开浏览器开发者工具 (F12)
```

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📧 联系方式

- GitHub: zhao,jiyu
- Email: jiyuzhao521@outlook.com

---

## 🙏 致谢

- [LiveKit](https://livekit.io/) - 实时通信基础设施
- [阿里云](https://www.aliyun.com/) - 语音服务和 AI 能力
- [FastAPI](https://fastapi.tiangolo.com/) - 现代 Python Web 框架

---

⭐ 如果这个项目对你有帮助，请给个 Star！
