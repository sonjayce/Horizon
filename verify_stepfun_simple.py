#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简单验证 StepFun 集成"""

import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=" * 60)
print("  StepFun 集成验证")
print("=" * 60)
print()

all_passed = True

# 1. 检查 AIProvider 枚举
print("[1] 检查 AIProvider.STEPFUN...")
with open('src/models.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'STEPFUN = "stepfun"' in content:
        print("      [OK] AIProvider.STEPFUN 已添加")
    else:
        print("      [FAIL] AIProvider.STEPFUN 未找到")
        all_passed = False
print()

# 2. 检查 AI_PROVIDER_DEFAULTS
print("[2] 检查 AI_PROVIDER_DEFAULTS[STEPFUN]...")
if 'AIProvider.STEPFUN:' in content:
    print("      [OK] AI_PROVIDER_DEFAULTS 包含 STEPFUN")
    # 提取并显示配置
    import re
    pattern = r'AIProvider\.STEPFUN:\s*\{(.*?)\}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        print("      配置内容:")
        for line in match.group(1).strip().split('\n'):
            if line.strip():
                print(f"        {line.strip()}")
else:
    print("      [FAIL] AI_PROVIDER_DEFAULTS 未包含 STEPFUN")
    all_passed = False
print()

# 3. 检查 _DEFAULT_API_KEY_ENVS
print("[3] 检查 _DEFAULT_API_KEY_ENVS...")
with open('src/ai/client.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'AIProvider.STEPFUN: "STEPFUN_API_KEY"' in content:
        print("      [OK] _DEFAULT_API_KEY_ENVS 包含 STEPFUN")
    else:
        print("      [FAIL] _DEFAULT_API_KEY_ENVS 未包含 STEPFUN")
        all_passed = False
print()

# 4. 检查 StepFunClient 类
print("[4] 检查 StepFunClient 类...")
if 'class StepFunClient(AIClient):' in content:
    print("      [OK] StepFunClient 类已定义")
    # 检查关键方法
    if 'async def complete(' in content:
        print("      [OK] complete 方法已实现")
    if 'reasoning_content' in content:
        print("      [OK] reasoning_content 处理已实现")
    if 'record_usage(' in content and '"stepfun"' in content:
        print("      [OK] token 统计已实现")
else:
    print("      [FAIL] StepFunClient 类未找到")
    all_passed = False
print()

# 5. 检查 _create_single_client
print("[5] 检查 _create_single_client 工厂函数...")
if 'AIProvider.STEPFUN:' in content and 'return StepFunClient(config)' in content:
    print("      [OK] _create_single_client 支持 STEPFUN")
else:
    print("      [FAIL] _create_single_client 未正确支持 STEPFUN")
    all_passed = False
print()

# 6. 检查文档
print("[6] 检查文档更新...")
with open('docs/configuration.md', 'r', encoding='utf-8') as f:
    doc_content = f.read()
    if 'StepFun' in doc_content or 'stepfun' in doc_content:
        print("      [OK] 文档包含 StepFun 说明")
    else:
        print("      [FAIL] 文档未包含 StepFun 说明")
        all_passed = False
print()

# 总结
print("=" * 60)
if all_passed:
    print("[SUCCESS] 所有检查通过！")
    print()
    print("StepFun 已成功集成到 Horizon！")
    print()
    print("使用步骤:")
    print("  1. 在 .env 文件中设置 STEPFUN_API_KEY")
    print("  2. 在 data/config.json 中配置:")
    print('     "ai": {')
    print('       "provider": "stepfun",')
    print('       "model": "step-3.7-flash",')
    print('       "api_key_env": "STEPFUN_API_KEY"')
    print("     }")
else:
    print("[FAILED] 部分检查失败")
print("=" * 60)

sys.exit(0 if all_passed else 1)
