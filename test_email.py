#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试邮件发送功能的脚本"""

import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
from src.models import EmailConfig
from src.services.email import EmailManager

# 设置 UTF-8 编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 加载环境变量
load_dotenv()

def test_email():
    """测试发送邮件"""

    # 检查环境变量
    email_pwd = os.getenv("EMAIL_PASSWORD")
    if not email_pwd:
        print("❌ 错误：EMAIL_PASSWORD 环境变量未设置")
        print("请确保 .env 文件包含 EMAIL_PASSWORD=xxx")
        return False

    # 创建邮件配置
    config = EmailConfig(
        enabled=True,
        smtp_server="smtp.qq.com",
        smtp_port=465,
        smtp_username=None,
        imap_enabled=True,
        imap_server="imap.qq.com",
        imap_port=993,
        "email_address": "3304408721@qq.com",
        password_env="EMAIL_PASSWORD",
        sender_name="Horizon Daily",
        subscribe_keyword="SUBSCRIBE",
        unsubscribe_keyword="UNSUBSCRIBE"
    )

    # 创建邮件管理器
    manager = EmailManager(config)

    # 测试内容
    test_summary = """# 🎉 Horizon 邮件测试

## ✅ 测试成功

这是一封**测试邮件**，用于验证 QQ 邮箱配置是否正确。

### 功能验证

- ✅ SMTP 发送正常
- ✅ 邮件格式正确
- ✅ 订阅功能可用

### 样本内容

这是一段**正文内容**，用于测试 Markdown 渲染效果。

- 列表项 1
- 列表项 2
- 列表项 3

### 代码块测试

```python
print("Hello, Horizon!")
```

### 链接测试

访问 [Horizon GitHub](https://github.com/Thysrael/Horizon)

---

**Horizon Daily** | 你的 AI 新闻雷达
"""

    # 测试收件人（可以是自己的邮箱）
    test_subscribers = ["3304408721@qq.com"]

    print("📧 开始发送测试邮件...")
    print(f"   发件人: {config.email_address}")
    print(f"   收件人: {', '.join(test_subscribers)}")
    print(f"   SMTP: {config.smtp_server}:{config.smtp_port}")

    try:
        manager.send_daily_summary(
            summary_md=test_summary,
            subject="✅ Horizon 邮件测试 - 配置成功",
            subscribers=test_subscribers
        )
        print("\n✅ 邮件发送成功！请检查收件箱（包括垃圾邮件文件夹）")
        return True

    except Exception as e:
        print(f"\n❌ 邮件发送失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("  Horizon 邮件功能测试")
    print("=" * 60)
    print()

    success = test_email()

    print()
    print("=" * 60)
    if success:
        print("✅ 测试完成 - 邮件配置正常")
    else:
        print("❌ 测试失败 - 请检查配置")
    print("=" * 60)

    sys.exit(0 if success else 1)
