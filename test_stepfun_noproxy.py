#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 StepFun API（强制不使用代理）"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from dotenv import load_dotenv
load_dotenv()

# 强制清除所有代理环境变量
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('ALL_PROXY', None)
os.environ.pop('all_proxy', None)


def test_stepfun_no_proxy():
    """不使用代理测试 StepFun API"""

    print("=" * 60)
    print("  StepFun API 测试（不使用代理）")
    print("=" * 60)
    print()

    print("[配置]")
    print(f"  http_proxy: {os.environ.get('http_proxy', '未设置')}")
    print(f"  https_proxy: {os.environ.get('https_proxy', '未设置')}")
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

    # 2. 导入 OpenAI
    print("[2] 导入 OpenAI 客户端...")
    try:
        from openai import OpenAI
        print("      [OK] openai 库已导入")
    except ImportError:
        print("      [FAIL] openai 库未安装")
        return False
    print()

    # 3. 配置客户端（不使用代理）
    print("[3] 配置 OpenAI 客户端...")
    try:
        # 显式设置 proxies 为 None
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.stepfun.com/v1",
            http_client=None,  # 使用默认客户端
        )
        print("      [OK] 客户端配置成功")
    except Exception as e:
        print(f"      [FAIL] 配置失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    print()

    # 4. 测试 API
    print("[4] 发送测试请求...")
    print("      模型: step-3.7-flash")
    print("      请求: 一句话介绍自己")
    try:
        response = client.chat.completions.create(
            model="step-3.7-flash",
            messages=[
                {"role": "system", "content": "你是AI助手"},
                {"role": "user", "content": "你好！请用一句话介绍你自己"}
            ],
            temperature=0.3,
            max_tokens=100,
            timeout=30.0
        )

        print("      [OK] 请求成功！")
        print()
        print("      💬 回复内容:")
        print(f"      \"{response.choices[0].message.content}\"")
        print()

        # 显示使用统计
        if hasattr(response, 'usage'):
            print("      [INFO] Token 使用:")
            print(f"      输入: {response.usage.prompt_tokens}")
            print(f"      输出: {response.usage.completion_tokens}")
            print(f"      总计: {response.usage.total_tokens}")
        print()

        return True

    except Exception as e:
        print(f"      [FAIL] 请求失败: {e}")
        print()

        error_str = str(e)
        if "ConnectionError" in error_str or "ConnectError" in error_str:
            print("      💡 连接错误")
            print()
            print("      可能的原因:")
            print("      1. API 服务暂时不可用")
            print("      2. 网络问题（Docker 网络、防火墙等）")
            print("      3. API 密钥可能无效")
            print()
            print("      建议:")
            print("      - 检查网络连接")
            print("      - 验证 API 密钥是否有效")
            print("      - 稍后重试")
        elif "401" in error_str or "403" in error_str:
            print("      💡 认证失败")
            print("      - API 密钥无效或已过期")
            print("      - 账户权限不足")
        else:
            print("      其他错误")
            import traceback
            traceback.print_exc()

        return False


if __name__ == "__main__":
    success = test_stepfun_no_proxy()

    print("=" * 60)
    if success:
        print("[SUCCESS] StepFun API 测试通过！")
    else:
        print("[FAILED] StepFun API 测试失败")
    print("=" * 60)

    sys.exit(0 if success else 1)
