#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 Gemini API 配置"""

import os
import sys
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

def test_gemini_api():
    """测试 Gemini API 连接"""

    api_key = os.getenv("GOOGLE_API_KEY")

    print("=" * 60)
    print("  Gemini API 配置测试")
    print("=" * 60)
    print()

    # 检查 API Key
    print("📋 API Key 检查:")
    if not api_key:
        print("  ❌ GOOGLE_API_KEY 未设置")
        return False

    print(f"  ✅ API Key 已设置")
    print(f"  🔑 Key 长度: {len(api_key)} 字符")
    print(f"  🔑 Key 前缀: {api_key[:10]}...")
    print()

    # 测试导入
    print("📦 检查依赖...")
    try:
        import google.generativeai as genai
        print("  ✅ google-generativeai 已安装")
    except ImportError:
        print("  ❌ google-generativeai 未安装")
        print("  正在安装...")
        os.system("pip install google-generativeai")
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
    print("🧪 测试 API 调用...")
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')

        response = model.generate_content(
            "你好！请用一句话介绍一下你自己。",
            generation_config={
                'temperature': 0.3,
                'max_output_tokens': 100,
            }
        )

        print("  ✅ API 调用成功！")
        print()
        print("💬 Gemini 回复:")
        print(f"  \"{response.text}\"")
        print()

        return True

    except Exception as e:
        print(f"  ❌ API 调用失败: {e}")
        print()
        print("可能的原因:")
        print("  1. API Key 无效或已过期")
        print("  2. API 配额已用完")
        print("  3. 网络连接问题")
        print("  4. 地区限制（某些地区无法访问）")
        import traceback
        traceback.print_exc()
        return False

def show_gemini_info():
    """显示 Gemini 信息"""
    print()
    print("=" * 60)
    print("  Gemini API 信息")
    print("=" * 60)
    print()
    print("📊 免费额度:")
    print("  ├── 15 次/分钟")
    print("  ├── 1500 次/天")
    print("  └── 完全免费")
    print()
    print("💡 当前配置:")
    print("  ├── 模型: gemini-2.0-flash")
    print("  ├── 温度: 0.3")
    print("  └── Max Tokens: 8192")
    print()
    print("🔗 相关链接:")
    print("  ├── API Key 管理: https://aistudio.google.com/apikey")
    print("  ├── 使用统计: https://aistudio.google.com/apikey")
    print("  └── 文档: https://ai.google.dev/docs")
    print()

if __name__ == "__main__":
    success = test_gemini_api()
    show_gemini_info()

    print("=" * 60)
    if success:
        print("✅ Gemini API 配置成功！")
    else:
        print("❌ Gemini API 配置失败")
    print("=" * 60)

    sys.exit(0 if success else 1)
