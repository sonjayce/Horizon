#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通过代理测试 Gemini API"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv

load_dotenv()

def test_with_proxy():
    """通过代理测试 Gemini API"""

    # 获取代理配置
    http_proxy = os.getenv("HTTP_PROXY") or os.getenv("http_proxy")
    https_proxy = os.getenv("HTTPS_PROXY") or os.getenv("https_proxy")

    print("=" * 60)
    print("  Gemini API 代理测试")
    print("=" * 60)
    print()

    # 检查代理
    print("🔌 代理配置检查:")
    if http_proxy:
        print(f"  ✅ HTTP_PROXY: {http_proxy}")
    else:
        print("  ⚠️  HTTP_PROXY 未设置")

    if https_proxy:
        print(f"  ✅ HTTPS_PROXY: {https_proxy}")
    else:
        print("  ⚠️  HTTPS_PROXY 未设置")

    if not http_proxy and not https_proxy:
        print()
        print("❌ 错误：未配置代理")
        print()
        print("请先在 .env 文件中配置代理：")
        print("  HTTPS_PROXY=http://127.0.0.1:7890")
        print()
        print("常见代理端口：")
        print("  - Clash: 7890")
        print("  - Shadowsocks: 1080")
        print("  - V2Ray: 10809")
        return False

    print()

    # 检查 API Key
    api_key = os.getenv("GOOGLE_API_KEY")
    print("🔑 API Key 检查:")
    if not api_key:
        print("  ❌ GOOGLE_API_KEY 未设置")
        return False
    print(f"  ✅ API Key 长度: {len(api_key)} 字符")
    print(f"  ✅ API Key 前缀: {api_key[:15]}...")
    print()

    # 导入测试
    print("📦 检查依赖...")
    try:
        import google.generativeai as genai
        print("  ✅ google-generativeai 已安装")
    except ImportError:
        print("  ❌ google-generativeai 未安装")
        print("  运行: uv add google-generativeai")
        return False
    print()

    # 配置 API
    print("⚙️  配置 API...")
    try:
        genai.configure(api_key=api_key)
        print("  ✅ API 配置成功")
    except Exception as e:
        print(f"  ❌ API 配置失败: {e}")
        return False
    print()

    # 测试调用
    print("🧪 测试 API 调用（通过代理）...")
    print(f"  代理: {https_proxy or http_proxy}")
    print()

    try:
        model = genai.GenerativeModel('gemini-2.0-flash')

        response = model.generate_content(
            "你好！请用一句话介绍一下你自己。",
            generation_config={
                'temperature': 0.3,
                'max_output_tokens': 100,
            }
        )

        print("✅ API 调用成功！")
        print()
        print("💬 Gemini 回复:")
        print(f"  \"{response.text}\"")
        print()

        # 显示使用统计
        print("📊 Token 使用统计:")
        if hasattr(response, 'usage_metadata'):
            usage = response.usage_metadata
            print(f"  输入 tokens: {usage.prompt_token_count}")
            print(f"  输出 tokens: {usage.candidates_token_count}")
            print(f"  总计: {usage.total_token_count}")
        print()

        return True

    except Exception as e:
        print(f"❌ API 调用失败: {e}")
        print()
        print("可能的原因:")
        print("  1. 代理服务器未运行")
        print("  2. 代理端口错误")
        print("  3. API Key 无效")
        print("  4. 网络连接问题")
        print()
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_with_proxy()

    print("=" * 60)
    if success:
        print("✅ 代理配置正确！Gemini 可以正常使用！")
    else:
        print("❌ 测试失败")
        print()
        print("请检查:")
        print("  1. 代理软件是否正在运行")
        print("  2. .env 中的代理配置是否正确")
        print("  3. 尝试重启代理软件")
    print("=" * 60)

    sys.exit(0 if success else 1)
