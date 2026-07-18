# 📧 Horizon 邮件系统配置说明

## 📋 邮件角色说明

### **3304408721@qq.com 的角色**

```
┌─────────────────────────────────────────┐
│ 邮件地址: 3304408721@qq.com             │
├─────────────────────────────────────────┤
│ ✅ 角色: 【发件人】                     │
│    From: Horizon Daily <3304408721@qq.com>
│                                         │
│ ❌ 不会自动作为【收件人】               │
│    除非手动添加到订阅者列表             │
└─────────────────────────────────────────┘
```

### **邮件发送流程**

```
1. Horizon 读取 data/subscribers.json
    ↓
2. 遍历订阅者列表
    ↓
3. 每个订阅者发送一封邮件
   From: Horizon Daily <3304408721@qq.com>
   To: 订阅者邮箱
    ↓
4. 如果订阅者列表包含 3304408721@qq.com
   → 会发送给自己
    ↓
5. 如果订阅者列表不包含 3304408721@qq.com
   → 不会发送给自己
```

---

## 📊 当前配置

### **发件人配置** (`data/config.json`)

```json
{
  "email": {
    "enabled": true,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 465,
    "email_address": "3304408721@qq.com",  // ← 发件人
    "password_env": "EMAIL_PASSWORD",
    "sender_name": "Horizon Daily",
    "subscribe_keyword": "SUBSCRIBE",
    "unsubscribe_keyword": "UNSUBSCRIBE"
  }
}
```

### **订阅者配置** (`data/subscribers.json`)

```json
{
  "subscribers": [
    "3489073251@qq.com"
  ]
}
```

**当前收件人**: `3489073251@qq.com`
**不会发送给自己**: ✅ `3304408721@qq.com` 不在列表中

---

## 🎯 邮件发送规则

### **规则 1：发件人 ≠ 收件人**

```
3304408721@qq.com（发件人）
    ↓ 发送给
订阅者列表中的邮箱
```

### **规则 2：订阅者列表决定收件人**

```
data/subscribers.json
    ↓
["3489073251@qq.com"]
    ↓
只发送给这个邮箱
```

### **规则 3：本地运行 vs GitHub Actions**

#### **本地运行**
```
D:\code\Horizon\
├── data/
│   ├── config.json          ← 配置
│   ├── subscribers.json     ← 订阅者（本地独立）
│   └── summaries/
└── uv run horizon
```

**订阅者来源**: `data/subscribers.json`

#### **GitHub Actions 运行**
```
GitHub Runner (临时环境)
    ↓
检出代码
    ↓
data/subscribers.json（从 main 分支读取）
    ↓
运行结束后丢弃
```

**订阅者来源**: GitHub 上的 `data/subscribers.json`

---

## 📝 管理订阅者

### **查看订阅者**

```bash
# 本地查看
cat data/subscribers.json

# 或使用 type (Windows)
type data\subscribers.json
```

### **添加订阅者**

编辑 `data/subscribers.json`：

```json
{
  "subscribers": [
    "3489073251@qq.com",
    "user1@example.com",
    "user2@gmail.com"
  ]
}
```

### **用户自动订阅**

用户发送邮件到 `3304408721@qq.com`：
```
收件人: 3304408721@qq.com
主题: SUBSCRIBE
内容: （任意）
```

Horizon 会自动：
1. 读取收件箱
2. 提取发件人邮箱
3. 添加到订阅者列表
4. 发送确认邮件

---

## 🚀 测试邮件发送

### **方法 1：使用测试脚本**

```bash
cd D:\code\Horizon
uv run python send_test_email.py
```

这会发送到 `test_subscribers` 中指定的邮箱（默认：`3489073251@qq.com`）

### **方法 2：运行完整 Horizon**

```bash
cd D:\code\Horizon

# 本地运行并发送邮件给订阅者
uv run horizon --languages zh
```

**预期行为**：
- ✅ 发送给 `3489073251@qq.com`
- ❌ 不会发送给 `3304408721@qq.com`（除非在订阅者列表中）

---

## ⚠️ 常见问题

### **Q1: 为什么我会收到邮件？**

**原因**: 你的邮箱 `3304408721@qq.com` 在订阅者列表中

**解决方法**:
1. 检查 `data/subscribers.json`
2. 如果包含 `3304408721@qq.com`，删除它
3. 重新运行

### **Q2: 订阅者列表是空的会发送吗？**

**不会**。代码逻辑：

```python
# src/services/email.py 第 156 行
if not self.config.enabled or not subscribers:
    return  # 订阅者为空直接返回，不发送
```

### **Q3: 本地和 GitHub Actions 的订阅者会同步吗？**

**不会**。两者完全独立：

```
本地: data/subscribers.json（本地文件）
GitHub Actions: data/subscribers.json（GitHub 仓库版本）
```

**如果需要同步**：
- 手动编辑 GitHub 上的 `data/subscribers.json`
- 或使用 GitHub 网页界面修改

---

## ✅ 当前配置确认

### **订阅者列表**

```json
{
  "subscribers": ["3489073251@qq.com"]
}
```

**结果**:
- ✅ 日报发送给 `3489073251@qq.com`
- ✅ 不会发送给 `3304408721@qq.com`

### **发件人**

```
From: Horizon Daily <3304408721@qq.com>
```

**结果**:
- ✅ 使用 QQ 邮箱 SMTP 发送
- ✅ 发件人显示为 `Horizon Daily`

---

## 🔒 安全建议

### **1. 不要在订阅者列表中添加发件人**

```json
// ❌ 不推荐
{
  "subscribers": ["3304408721@qq.com"]
}

// ✅ 推荐
{
  "subscribers": ["3489073251@qq.com"]
}
```

### **2. 定期检查订阅者列表**

```bash
# 查看当前订阅者
cat data/subscribers.json
```

### **3. 使用测试脚本验证**

```bash
uv run python send_test_email.py
```

---

## 📞 订阅者操作

### **用户订阅**

1. 发送邮件到 `3304408721@qq.com`
2. 主题：`SUBSCRIBE`
3. 自动添加到订阅者列表

### **用户退订**

1. 发送邮件到 `3304408721@qq.com`
2. 主题：`UNSUBSCRIBE`
3. 自动从订阅者列表移除

---

**配置完成！** ✅

当前只会发送给 `3489073251@qq.com`，不会发送给 `3304408721@qq.com`。

如果需要调整订阅者，直接编辑 `data/subscribers.json` 即可。
