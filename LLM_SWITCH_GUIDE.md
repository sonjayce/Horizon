## 切换到 Claude

### 步骤 1：修改配置文件

编辑 `data/config.json`：

```json
{
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY",
    "temperature": 0.3,
    "max_tokens": 8192,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `claude-sonnet-4.5-20250929`（推荐，性价比高）
- `claude-3-5-sonnet-20241022`
- `claude-3-opus-20240229`
- `claude-3-haiku-20240307`

### 步骤 2：设置环境变量

在 `.env` 文件添加：

```bash
ANTHROPIC_API_KEY=sk-ant-xxx
```

删除或注释掉旧的 API Key：

```bash
# DEEPSEEK_API_KEY=xxx  ← 注释掉或删除
ANTHROPIC_API_KEY=sk-ant-xxx  ← 添加这个
```

### 步骤 3：测试

```bash
cd D:\code\Horizon
uv run horizon --hours 1 --languages zh
```

---

## OpenAI GPT

### 配置

```json
{
  "ai": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key_env": "OPENAI_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `gpt-4`（推荐）
- `gpt-4-turbo`
- `gpt-4o`
- `gpt-3.5-turbo`（便宜）

**环境变量**：
```bash
OPENAI_API_KEY=sk-xxx
```

---

## Google Gemini

### 配置

```json
{
  "ai": {
    "provider": "gemini",
    "model": "gemini-2.0-flash",
    "api_key_env": "GOOGLE_API_KEY",
    "temperature": 0.3,
    "max_tokens": 8192,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `gemini-2.0-flash`（推荐，快且免费额度多）
- `gemini-2.0-pro`
- `gemini-1.5-pro`

**环境变量**：
```bash
GOOGLE_API_KEY=AIzaxxx
```

---

## DeepSeek（当前使用）

### 配置

```json
{
  "ai": {
    "provider": "deepseek",
    "model": "deepseek-v4-flash",
    "api_key_env": "DEEPSEEK_API_KEY",
    "temperature": 0.3,
    "max_tokens": 8192,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `deepseek-v4-flash`（当前使用，性价比高）
- `deepseek-v4`
- `deepseek-chat`

**环境变量**：
```bash
DEEPSEEK_API_KEY=sk-xxx
```

---

## 阿里云 DashScope

### 配置

```json
{
  "ai": {
    "provider": "ali",
    "model": "qwen-plus",
    "api_key_env": "DASHSCOPE_API_KEY",
    "temperature": 0.3,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `qwen-plus`（推荐）
- `qwen-max`
- `qwen-turbo`

**环境变量**：
```bash
DASHSCOPE_API_KEY=sk-xxx
```

---

## MiniMax

### 配置

```json
{
  "ai": {
    "provider": "minimax",
    "model": "MiniMax-M3",
    "api_key_env": "MINIMAX_API_KEY",
    "base_url": "https://api.minimax.io/v1",
    "temperature": 0.3,
    "max_tokens": 8192,
    "throttle_sec": 0
  }
}
```

**可选模型**：
- `MiniMax-M3`（推荐）
- `MiniMax-M2.7`
- `MiniMax-M2.7-highspeed`

**环境变量**：
```bash
MINIMAX_API_KEY=xxx
```

---

## 豆包（Doubao）

### 配置

```json
{
  "ai": {
    "provider": "doubao",
    "model": "doubao-pro-4k",
    "api_key_env": "DOUBAO_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096,
    "throttle_sec": 0
  }
}
```

**环境变量**：
```bash
DOUBAO_API_KEY=xxx
```

---

## 本地 Ollama（完全免费）

### 配置

```json
{
  "ai": {
    "provider": "ollama",
    "model": "llama3.1",
    "api_key_env": "",
    "base_url": "http://localhost:11434/v1",
    "temperature": 0.3,
    "max_tokens": 4096,
    "throttle_sec": 0
  }
}
```

**前提**：
1. 安装 Ollama：https://ollama.com
2. 下载模型：`ollama pull llama3.1`
3. 运行 Ollama 服务

**可选模型**：
- `llama3.1`（推荐）
- `llama3.1:70b`（更强但需要更多资源）
- `mistral`
- `codellama`

**优势**：
- ✅ 完全免费
- ✅ 数据不出本地
- ✅ 无限调用

**劣势**：
- ⚠️ 需要本地运行
- ⚠️ 质量可能不如云端 API

---

## 🔧 **高级配置**

### **配置多个 LLM（自动切换）**

```json
{
  "ai": {
    "provider": "anthropic",
    "provider_chain": ["openai", "deepseek"],
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY"
  }
}
```

**作用**：
- 主模型：Claude
- 如果 Claude 失败，自动切换到 OpenAI
- 再失败切换到 DeepSeek

### **调整温度**

```json
{
  "ai": {
    "temperature": 0.3  // 0 = 确定性，1 = 创造性
  }
}
```

**推荐值**：
- `0.0-0.3`：事实性任务（评分、总结）
- `0.3-0.7`：平衡（通用）
- `0.7-1.0`：创造性任务

### **调整并发**

```json
{
  "ai": {
    "analysis_concurrency": 5,      // 评分并发数
    "enrichment_concurrency": 3    // 增强并发数
  }
}
```

**注意**：过高并发可能导致 API 限流

---

## 📊 **模型对比**

| 模型 | 质量 | 速度 | 成本 | 推荐场景 |
|------|------|------|------|---------|
| **Claude Sonnet** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 通用，推荐 |
| **GPT-4** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 高质量需求 |
| **DeepSeek-V4** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 性价比高 |
| **Gemini Flash** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 快且免费 |
| **Qwen-Plus** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 中文友好 |
| **Ollama** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | 本地免费 |

---

## 🚀 **快速切换示例**

### **从 DeepSeek 切换到 Claude**

```bash
# 1. 编辑配置文件
data/config.json

# 2. 修改 provider 和 model
{
  "ai": {
    "provider": "anthropic",           // ← 改这里
    "model": "claude-sonnet-4.5-20250929",  // ← 改这里
    "api_key_env": "ANTHROPIC_API_KEY"      // ← 改这里
  }
}

# 3. 更新环境变量
# 编辑 .env 文件
ANTHROPIC_API_KEY=sk-ant-xxx  # ← 添加

# 4. 测试
uv run horizon --hours 1 --languages zh
```

---

## ✅ **验证配置**

### **检查当前配置**

```bash
cat data/config.json | grep -A 5 '"ai"'
```

### **测试 LLM 连接**

```bash
uv run horizon --dry-run
```

会显示：
```
✓ AI Client: Anthropic (claude-sonnet-4.5-20250929)
✓ API 连接成功
```

---

## 💡 **推荐配置**

### **方案 A：高质量（推荐）**

```json
{
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY"
  }
}
```

**成本**：约 $1-2/月

---

### **方案 B：性价比（当前）**

```json
{
  "ai": {
    "provider": "deepseek",
    "model": "deepseek-v4-flash",
    "api_key_env": "DEEPSEEK_API_KEY"
  }
}
```

**成本**：约 ¥2-10/月

---

### **方案 C：免费**

```json
{
  "ai": {
    "provider": "gemini",
    "model": "gemini-2.0-flash",
    "api_key_env": "GOOGLE_API_KEY"
  }
}
```

**成本**：免费额度内

---

## 🔐 **安全提示**

### **API Key 管理**

1. **永远不要硬编码 API Key**
   ```json
   // ❌ 错误
   "api_key_env": "sk-ant-xxx"
   
   // ✅ 正确
   "api_key_env": "ANTHROPIC_API_KEY"
   ```

2. **使用环境变量**
   ```bash
   # .env 文件
   ANTHROPIC_API_KEY=sk-ant-xxx
   ```

3. **不要提交 .env 到 Git**
   - `.env` 已在 `.gitignore` 中

---

**想换成哪个模型？** 告诉我，我帮你配置！🚀
