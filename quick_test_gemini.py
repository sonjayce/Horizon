#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""快速测试 Gemini API"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv

load_dotenv()

# 检查配置
api_key = os.getenv("GOOGLE_API_KEY")

print("=" * 60)
print("  Gemini API 快速测试")
print("=" * 60)
print()

print("📋 配置检查:")
print(f"  ✅ GOOGLE_API_KEY 长度: {len(api_key)} 字符")
print(f"  ✅ API Key 前缀: {api_key[:15]}...")
print()

# 导入测试
try:
    import google.generativeai as genai
    print("✅ google-generativeai 已安装")
except ImportError:
    print("❌ google-generativeai 未安装")
    exit(1)

# 配置
try:
    genai.configure(api_key=api_key)
    print("✅ API 配置成功")
except Exception as e:
    print(f"❌ API 配置失败: {e}")
    exit(1)

# 测试调用
print()
print("🧪 测试 API 调用...")
try:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(
        "你好！请用一句话介绍一下你自己。",
        generation_config={'temperature': 0.3, 'max_output_tokens': 100}
    )

    print("✅ API 调用成功！")
    print()
    print("💬 Gemini 回复:")
    print(f"  \"{response.text}\"")
    print()

except Exception as e:
    print(f"❌ API 调用失败: {e}")
    print()
    print("可能的原因:")
    print("  1. API Key 无效")
    print("  2. 配额已用完")
    print("  3. 网络问题")
    exit(1)

print("=" * 60)
print("✅ 所有测试通过！Gemini API 配置正确！")
print("=" * 60)
print()
print("下一步:")
print("  uv run horizon --hours 1 --languages zh")
