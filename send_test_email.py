#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发送测试邮件到指定邮箱"""

import os
import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def send_test_email():
    """发送测试邮件"""

    # 配置
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    email_address = "3304408721@qq.com"
    password = os.getenv("EMAIL_PASSWORD")
    to_email = "3489073251@qq.com"

    print("=" * 60)
    print("  QQ 邮箱发送测试")
    print("=" * 60)
    print()
    print(f"发件人: {email_address}")
    print(f"收件人: {to_email}")
    print(f"SMTP服务器: {smtp_server}:{smtp_port}")
    print()

    if not password:
        print("❌ 错误: EMAIL_PASSWORD 环境变量未设置")
        return False

    # 创建邮件
    msg = MIMEMultipart('alternative')
    msg['From'] = f"Horizon Daily <{email_address}>"
    msg['To'] = to_email
    msg['Subject'] = "🎉 Horizon 测试邮件 - 配置验证"

    # 纯文本版本
    text_content = """
Horizon 测试邮件
================

这是一封测试邮件，用于验证 QQ 邮箱配置是否正确。

如果你收到这封邮件，说明：
✅ SMTP 配置正确
✅ 发送功能正常
✅ 授权码有效

发件人: 3304408721@qq.com
时间: 2025-07-18

---
Horizon Daily - 你的 AI 新闻雷达
"""

    # HTML 版本
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
        }
        .container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            padding: 30px;
            color: white;
        }
        h1 {
            margin: 0 0 20px 0;
            font-size: 28px;
        }
        .content {
            background: white;
            border-radius: 8px;
            padding: 25px;
            margin-top: 20px;
            color: #333;
        }
        .checklist {
            list-style: none;
            padding: 0;
        }
        .checklist li {
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        .checklist li:last-child {
            border-bottom: none;
        }
        .success {
            color: #10b981;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #999;
            font-size: 14px;
        }
        .badge {
            display: inline-block;
            background: #f0f0f0;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 5px 5px 5px 0;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Horizon 测试邮件</h1>
    </div>

    <div class="content">
        <p>你好！</p>
        <p>这是一封来自 <strong>Horizon</strong> 的测试邮件，用于验证 QQ 邮箱配置是否正确。</p>

        <h3>✅ 验证项目</h3>
        <ul class="checklist">
            <li class="success">✓ SMTP 配置正确</li>
            <li class="success">✓ 邮件发送功能正常</li>
            <li class="success">✓ 授权码有效</li>
        </ul>

        <h3>📧 邮件信息</h3>
        <p><span class="badge">发件人: 3304408721@qq.com</span>
           <span class="badge">收件人: 3489073251@qq.com</span></p>

        <div class="footer">
            <p><strong>Horizon Daily</strong></p>
            <p>你的 AI 新闻雷达 | https://github.com/Thysrael/Horizon</p>
        </div>
    </div>
</body>
</html>
"""

    # 添加邮件内容
    msg.attach(MIMEText(text_content, 'plain', 'utf-8'))
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))

    # 发送邮件
    try:
        print("🔌 连接到 SMTP 服务器...")
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=10) as server:
            print(f"✓ 已连接到 {smtp_server}:{smtp_port}")

            print("🔐 登录中...")
            server.login(email_address, password)
            print("✓ 登录成功")

            print(f"\n📧 发送邮件到 {to_email}...")
            server.sendmail(email_address, [to_email], msg.as_string())
            print("✓ 邮件发送成功！")
            print()
            print("=" * 60)
            print("✅ 发送成功")
            print("=" * 60)
            print()
            print(f"请检查 {to_email} 的收件箱（包括垃圾邮件）")
            print()
            return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ 认证失败: {e}")
        print()
        print("可能的原因:")
        print("  1. 授权码错误")
        print("  2. SMTP/IMAP 服务未开启")
        print("  3. 需要在 QQ 邮箱设置中生成新的授权码")
        return False

    except Exception as e:
        print(f"❌ 发送失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = send_test_email()
    sys.exit(0 if success else 1)
