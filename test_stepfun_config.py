#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证 StepFun 配置并测试连接"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv
load_dotenv()

import asyncio


async def test_configuration():
    """测试配置和连接"""

    print("=" * 60)
    print("  StepFun 配置验证")
    print("=" * 60)
    print()

    # 1. 检查环境变量
    print("[1] 检查环境变量...")
    api_key = os.getenv("STEPFUN_API_KEY")
    if not api_key:
        print("      [FAIL] STEPFUN_API_KEY 未设置")
        return False

    print(f"      [OK] STEPFUN_API_KEY 已设置 (长度: {len(api_key)})")
    print(f"      [INFO] 密钥前缀: {api_key[:15]}...")
    print()

    # 2. 加载配置
    print("[2] 加载配置...")
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        from models import AIProvider, AIConfig
        from ai.client import create_ai_client

        config = AIConfig(
            provider=AIProvider.STEPFUN,
            model="step-3.7-flash",
            api_key_env="STEPFUN_API_KEY",
            temperature=0.3,
            max_tokens=100,
        )
        print(f"      [OK] 配置加载成功")
        print(f"      - Provider: {config.provider.value}")
        print(f"      - Model: {config.model}")
        print(f"      - Temperature: {config.temperature}")
    except Exception as e:
        print(f"      [FAIL] 配置加载失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    print()

    # 3. 创建客户端
    print("[3] 创建 StepFun 客户端...")
    try:
        client = create_ai_client(config)
        print(f"      [OK] 客户端创建成功")
        print(f"      - 类型: {type(client).__name__}")
        print(f"      - Base URL: {client.client.base_url}")
    except Exception as e:
        print(f"      [FAIL] 客户端创建失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    print()

    # 4. 测试 API 调用
    print("[4] 测试 API 调用...")
    print("      正在调用 StepFun API...")
    try:
        response = await client.complete(
            system="你是一个友好的AI助手。请用简洁的语言回答问题。",
            user="你好！请用一句话介绍一下你自己。"
        )

        print(f"      [OK] API 调用成功！")
        print()
        print("      💬 StepFun 回复:")
        print(f"      \"{response}\"")
        print()
        return True

    except Exception as e:
        error_msg = str(e)
        print(f"      [FAIL] API 调用失败")
        print(f"      错误: {error_msg}")
        print()

        if "ConnectError" in error_msg or "Connection error" in error_msg:
            print("      💡 网络连接问题")
            print()
            print("      可能的原因:")
            print("      1. 网络连接问题 - 检查网络连接")
            print("      2. 需要代理 - 如果在中国大陆，可能需要配置代理")
            print()
            print("      建议:")
            print("      在 .env 文件中取消代理配置的注释:")
            print("      HTTP_PROXY=http://127.0.0.1:7897")
            print("      HTTPS_PROXY=http://127.0.0.1:7897")
            print()
            print("      (根据您的实际代理地址修改)")
            return False
        else:
            print("      其他错误，请检查 API 密钥或配置")
            import traceback
            traceback.print_exc()
            return False


async def main():
    success = await test_configuration()

    print("=" * 60)
    if success:
        print("[SUCCESS] StepFun 配置验证通过！")
        print()
        print("✅ StepFun 已成功配置并可以正常使用")
        print()
        print("下一步:")
        print("  - 运行 Horizon: uv run horizon --hours 24 --languages zh")
        print("  - 查看文档: docs/configuration.md")
    else:
        print("[FAILED] 配置验证失败")
        print()
        print("请检查:")
        print("  1. API 密钥是否正确")
        print("  2. 网络连接是否正常")
        print("  3. 是否需要配置代理")
    print("=" * 60)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
