#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简单的 StepFun 连接测试"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv
load_dotenv()


def test_stepfun_connection():
    """测试 StepFun API 连接"""

    print("=" * 60)
    print("  StepFun API 连接测试")
    print("=" * 60)
    print()

    # 1. 检查 API Key
    print("[1] 检查 API 密钥...")
    api_key = os.getenv("STEPFUN_API_KEY")
    if not api_key:
        print("      [FAIL] STEPFUN_API_KEY 未设置")
        return False

    print(f"      [OK] 密钥长度: {len(api_key)}")
    print(f"      [INFO] 密钥前缀: {api_key[:20]}...")
    print()

    # 2. 导入 OpenAI 客户端
    print("[2] 检查依赖...")
    try:
        from openai import OpenAI
        print("      [OK] openai 库已安装")
    except ImportError:
        print("      [FAIL] openai 库未安装")
        print("      正在安装...")
        os.system("uv add openai")
        return False
    print()

    # 3. 配置客户端
    print("[3] 配置客户端...")
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.stepfun.com/v1"
        )
        print("      [OK] 客户端配置成功")
        print(f"      - Base URL: https://api.stepfun.com/v1")
        print(f"      - Model: step-3.7-flash")
    except Exception as e:
        print(f"      [FAIL] 客户端配置失败: {e}")
        return False
    print()

    # 4. 测试 API 调用
    print("[4] 测试 API 调用...")
    print("      正在发送测试请求...")
    try:
        response = client.chat.completions.create(
            model="step-3.7-flash",
            messages=[
                {"role": "system", "content": "你是一个友好的AI助手。"},
                {"role": "user", "content": "你好！请用一句话介绍一下你自己。"}
            ],
            temperature=0.3,
            max_tokens=100
        )

        print("      [OK] API 调用成功！")
        print()
        print("      💬 StepFun 回复:")
        print(f"      \"{response.choices[0].message.content}\"")
        print()

        # 显示使用统计
        print("      [INFO] Token 使用统计:")
        if hasattr(response, 'usage'):
            usage = response.usage
            print(f"      - 输入 tokens: {usage.prompt_tokens}")
            print(f"      - 输出 tokens: {usage.completion_tokens}")
            print(f"      - 总计: {usage.total_tokens}")
        print()

        return True

    except Exception as e:
        print(f"      [FAIL] API 调用失败")
        print(f"      错误: {str(e)}")
        print()

        if "ConnectError" in str(e) or "Connection error" in str(e):
            print("      💡 网络连接问题")
            print()
            print("      解决方案:")
            print("      1. 检查网络连接")
            print("      2. 配置代理（如果需要）:")
            print("         编辑 .env 文件，取消注释:")
            print("         HTTP_PROXY=http://127.0.0.1:7897")
            print("         HTTPS_PROXY=http://127.0.0.1:7897")
            print()
            print("         注意: 将代理地址改为您实际的代理地址")
            return False
        elif "401" in str(e) or "403" in str(e):
            print("      💡 认证失败")
            print()
            print("      可能的原因:")
            print("      1. API 密钥无效")
            print("      2. API 密钥已过期")
            print("      3. 账户权限不足")
            print()
            print("      建议: 登录 StepFun 控制台验证密钥")
            return False
        else:
            print("      其他错误，请检查:")
            print("      - API 密钥是否正确")
            print("      - 账户是否有足够余额")
            print("      - API 服务是否可用")
            import traceback
            traceback.print_exc()
            return False


if __name__ == "__main__":
    success = test_stepfun_connection()

    print("=" * 60)
    if success:
        print("[SUCCESS] StepFun API 连接测试通过！")
        print()
        print("✅ 配置验证成功，StepFun 已可以正常使用")
        print()
        print("当前配置:")
        print("  - Provider: stepfun")
        print("  - Model: step-3.7-flash")
        print("  - API Key: 已配置")
        print()
        print("运行 Horizon:")
        print("  uv run horizon --hours 24 --languages zh")
    else:
        print("[FAILED] StepFun API 连接测试失败")
        print()
        print("请检查上述错误信息并解决问题")
    print("=" * 60)

    sys.exit(0 if success else 1)
