#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证 StepFun 集成是否完整"""

import sys
import os
import importlib.util

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 使用 importlib 直接加载模块，避免相对导入问题
def load_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def verify_integration():
    """验证所有 StepFun 集成点"""
    print("=" * 60)
    print("  StepFun 集成验证")
    print("=" * 60)
    print()

    all_passed = True

    # 1. 验证 AIProvider 枚举
    print("[1] 验证 AIProvider 枚举...")
    try:
        from models import AIProvider
        assert hasattr(AIProvider, 'STEPFUN'), "AIProvider 缺少 STEPFUN"
        assert AIProvider.STEPFUN.value == "stepfun", "STEPFUN value 不正确"
        print("   ✅ AIProvider.STEPFUN 存在且值正确")
    except Exception as e:
        print(f"   ❌ 失败: {e}")
        all_passed = False
    print()

    # 2. 验证 AI_PROVIDER_DEFAULTS
    print("[2] 验证 AI_PROVIDER_DEFAULTS...")
    try:
        from models import AI_PROVIDER_DEFAULTS, AIProvider
        stepfun_defaults = AI_PROVIDER_DEFAULTS.get(AIProvider.STEPFUN)
        assert stepfun_defaults is not None, "AI_PROVIDER_DEFAULTS 缺少 STEPFUN"
        assert stepfun_defaults["model"] == "step-3.7-flash", "默认 model 不正确"
        assert stepfun_defaults["api_key_env"] == "STEPFUN_API_KEY", "默认 api_key_env 不正确"
        assert stepfun_defaults["base_url"] == "https://api.stepfun.com/v1", "默认 base_url 不正确"
        print("   [OK] AI_PROVIDER_DEFAULTS[STEPFUN] 配置正确")
        print(f"      - model: {stepfun_defaults['model']}")
        print(f"      - api_key_env: {stepfun_defaults['api_key_env']}")
        print(f"      - base_url: {stepfun_defaults['base_url']}")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        all_passed = False
    print()

    # 3. 验证 _DEFAULT_API_KEY_ENVS
    print("[3] 验证 _DEFAULT_API_KEY_ENVS...")
    try:
        from ai.client import _DEFAULT_API_KEY_ENVS, AIProvider as AP
        assert AIProvider.STEPFUN in _DEFAULT_API_KEY_ENVS, "_DEFAULT_API_KEY_ENVS 缺少 STEPFUN"
        assert _DEFAULT_API_KEY_ENVS[AIProvider.STEPFUN] == "STEPFUN_API_KEY", "环境变量名不正确"
        print("   [OK] _DEFAULT_API_KEY_ENVS[STEPFUN] 配置正确")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        all_passed = False
    print()

    # 4. 验证 StepFunClient 类
    print("[4] 验证 StepFunClient 类...")
    try:
        from ai.client import StepFunClient, AIClient
        assert issubclass(StepFunClient, AIClient), "StepFunClient 应该继承 AIClient"
        assert hasattr(StepFunClient, '__init__'), "StepFunClient 缺少 __init__"
        assert hasattr(StepFunClient, 'complete'), "StepFunClient 缺少 complete 方法"
        print("   [OK] StepFunClient 类结构正确")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        all_passed = False
    print()

    # 5. 验证 _create_single_client 工厂函数
    print("[5] 验证 _create_single_client 工厂函数...")
    try:
        from ai.client import _create_single_client
        from models import AIConfig, AIProvider
        config = AIConfig(
            provider=AIProvider.STEPFUN,
            model="step-3.7-flash",
            api_key_env="STEPFUN_API_KEY",
            temperature=0.3,
            max_tokens=100,
        )
        client = _create_single_client(config)
        from ai.client import StepFunClient
        assert isinstance(client, StepFunClient), "工厂函数应该返回 StepFunClient"
        print("   [OK] _create_single_client 正确返回 StepFunClient")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    print()

    # 6. 验证 create_ai_client 工厂函数
    print("[6] 验证 create_ai_client 工厂函数...")
    try:
        from ai.client import create_ai_client
        config = AIConfig(
            provider=AIProvider.STEPFUN,
            model="step-3.7-flash",
            api_key_env="STEPFUN_API_KEY",
            temperature=0.3,
            max_tokens=100,
        )
        client = create_ai_client(config)
        from ai.client import StepFunClient
        assert isinstance(client, StepFunClient), "create_ai_client 应该返回 StepFunClient"
        print("   [OK] create_ai_client 正确返回 StepFunClient")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    print()

    # 7. 验证 reasoning_content 处理
    print("[7] 验证 reasoning_content 处理逻辑...")
    try:
        from ai.client import OpenAIClient
        # 检查 OpenAIClient 中是否有 StepFun 的特殊处理
        has_stepfun_handling = (
            hasattr(OpenAIClient, '_USE_REASONING_AS_CONTENT') and
            "stepfun" in OpenAIClient._USE_REASONING_AS_CONTENT
        )
        # 或者通过 _REASONING_BASE_URLS
        has_base_url_handling = (
            hasattr(OpenAIClient, '_REASONING_BASE_URLS') and
            "https://api.stepfun.com/v1" in OpenAIClient._REASONING_BASE_URLS
        )
        if has_stepfun_handling or has_base_url_handling:
            print("   [OK] OpenAIClient 中已有 StepFun reasoning_content 处理")
        else:
            print("   [WARN] 警告: OpenAIClient 中未找到 StepFun 特殊处理（如果使用 OpenAIClient 需要此配置）")
    except Exception as e:
        print(f"   [FAIL] 失败: {e}")
        all_passed = False
    print()

    return all_passed


if __name__ == "__main__":
    success = verify_integration()

    print("=" * 60)
    if success:
        print("[SUCCESS] 所有集成点验证通过！")
        print()
        print("StepFun 已完全集成到 Horizon 中，可以正常使用了。")
    else:
        print("[FAILED] 部分集成点验证失败，请检查上面的错误信息。")
    print("=" * 60)

    sys.exit(0 if success else 1)
