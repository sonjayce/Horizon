#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""诊断 QQ 邮箱配置问题"""

import os
import sys
import smtplib
import ssl
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

def test_smtp_connection():
    """测试 SMTP 连接"""
    print("=" * 60)
    print("  QQ 邮箱 SMTP 连接测试")
    print("=" * 60)
    print()

    # 检查环境变量
    email = "3304408721@qq.com"
    password = os.getenv("EMAIL_PASSWORD")

    print("📋 配置检查:")
    print(f"   邮箱地址: {email}")
    print(f"   授权码已设置: {'✅ 是' if password else '❌ 否'}")

    if not password:
        print("\n❌ 错误: EMAIL_PASSWORD 未设置")
        return False

    print(f"   授权码长度: {len(password)} 字符")
    print(f"   授权码前3位: {password[:3]}...")
    print()

    # 测试 SMTP 连接
    print("🔌 测试 SMTP 连接...")
    print(f"   服务器: smtp.qq.com:465")

    try:
        context = ssl.create_default_context()
        print("   ✓ SSL 上下文创建成功")

        with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context, timeout=10) as server:
            print("   ✓ 连接到 smtp.qq.com:465")

            print("   🔐 尝试登录...")
            try:
                server.login(email, password)
                print("   ✅ 登录成功！")

                # 尝试发送测试邮件
                print("\n📧 尝试发送测试邮件...")
                msg = f"""From: {email}
To: {email}
Subject: Horizon Test Email
Content-Type: text/plain; charset=utf-8

This is a test email from Horizon.
If you receive this, your QQ email configuration is working!

Time: {os.times()}
"""

                server.sendmail(email, [email], msg.encode('utf-8'))
                print("   ✅ 测试邮件发送成功！")
                print("\n请检查收件箱（包括垃圾邮件文件夹）")
                return True

            except smtplib.SMTPAuthenticationError as e:
                print(f"   ❌ 登录失败: {e}")
                print("\n可能的原因:")
                print("   1. 授权码错误 - 请确认 ggruaojjlmshdabd 是正确的 QQ 邮箱授权码")
                print("   2. 未开启 SMTP 服务 - 请在 QQ 邮箱设置中开启")
                print("   3. 授权码已过期 - 请重新生成授权码")
                return False

    except smtplib.SMTPConnectError as e:
        print(f"   ❌ 连接失败: {e}")
        print("   请检查网络连接或防火墙设置")
        return False

    except Exception as e:
        print(f"   ❌ 未知错误: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_qq_email_settings():
    """检查 QQ 邮箱设置说明"""
    print("\n" + "=" * 60)
    print("  QQ 邮箱配置指南")
    print("=" * 60)
    print()
    print("1️⃣  登录 QQ 邮箱网页版")
    print("   https://mail.qq.com")
    print()
    print("2️⃣  进入设置 → 账户")
    print()
    print("3️⃣  找到 'POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务'")
    print()
    print("4️⃣  开启以下服务:")
    print("   ✅ IMAP/SMTP服务")
    print("   ✅ POP3/SMTP服务")
    print()
    print("5️⃣  生成授权码:")
    print("   - 点击 '生成授权码' 按钮")
    print("   - 按提示发送短信验证")
    print("   - 获得16位授权码（如: xxxxxxxxxxxxxxxx）")
    print()
    print("6️⃣  更新 .env 文件:")
    print("   EMAIL_PASSWORD=你的16位授权码")
    print()
    print("⚠️  注意: 授权码不是 QQ 密码！")
    print("   密码格式: 16位字母数字组合")
    print()

if __name__ == "__main__":
    success = test_smtp_connection()

    check_qq_email_settings()

    print("=" * 60)
    if success:
        print("✅ 测试通过 - 邮件配置正常")
    else:
        print("❌ 测试失败 - 请按上述指南检查配置")
    print("=" * 60)

    sys.exit(0 if success else 1)
