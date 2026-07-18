#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 StepFun API"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv

load_dotenv()

def test_stepfun():
    """测试 StepFun API"""

    api_key = os.getenv("STEPFUN_API_KEY")
    base_url = "https://api.stepfun.com/step_plan/v1"

    print("=" * 60)
    print("  StepFun API 测试")
    print("=" * 60)
    print()

    # 检查 API Key
    print("🔑 API Key 检查:")
    if not api_key:
        print("  ❌ STEPFUN_API_KEY 未设置")
        return False

    print(f"  ✅ API Key 长度: {len(api_key)} 字符")
    print(f"  ✅ API Key 前缀: {api_key[:10]}...")
    print()

    # 导入 OpenAI 客户端
    print("📦 检查依赖...")
    try:
        from openai import OpenAI
        print("  ✅ openai 已安装")
    except ImportError:
        print("  ❌ openai 未安装")
        print("  正在安装...")
        os.system("uv add openai")
        return False
    print()

    # 配置客户端
    print("⚙️  配置 API 客户端...")
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        print(f"  ✅ 客户端配置成功")
        print(f"  📍 Base URL: {base_url}")
    except Exception as e:
        print(f"  ❌ 配置失败: {e}")
        return False
    print()

    # 测试调用
    print("🧪 测试 API 调用...")
    try:
        response = client.chat.completions.create(
            model="step-3.7-flash",
            messages=[
                {"role": "user", "content": "你好！请用一句话介绍一下你自己。"}
            ],
            temperature=0.3,
            max_tokens=100
        )

        print("✅ API 调用成功！")
        print()
        print("💬 StepFun 回复:")
        print(f"  \"{response.choices[0].message.content}\"")
        print()

        # 显示使用统计
        print("📊 Token 使用统计:")
        if hasattr(response, 'usage'):
            usage = response.usage
            print(f"  输入 tokens: {usage.prompt_tokens}")
            print(f"  输出 tokens: {usage.completion_tokens}")
            print(f"  总计: {usage.total_tokens}")
        print()

        return True

    except Exception as e:
        print(f"❌ API 调用失败: {e}")
        print()
        print("可能的原因:")
        print("  1. API Key 无效")
        print("  2. 账户余额不足")
        print("  3. 网络连接问题")
        print("  4. API 服务暂时不可用")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_stepfun()

    print("=" * 60)
    if success:
        print("✅ StepFun API 配置成功！")
        print()
        print("下一步:")
        print("  uv run horizon --hours 1 --languages zh")
    else:
        print("❌ StepFun API 配置失败")
    print("=" * 60)

    sys.exit(0 if success else 1)
