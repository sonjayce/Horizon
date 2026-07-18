#!/bin/bash
# 手动创建并推送 gh-pages 分支

set -e

echo "=========================================="
echo "  手动创建 gh-pages 分支"
echo "=========================================="
echo ""

# 检查是否在正确的目录
if [ ! -d ".git" ]; then
    echo "❌ 错误: 请在 Horizon 项目根目录运行此脚本"
    exit 1
fi

echo "📋 检查当前状态..."
git status
echo ""

# 获取远程分支列表
echo "📡 检查远程分支..."
git ls-remote origin | grep gh-pages

if [ $? -eq 0 ]; then
    echo ""
    echo "⚠️  gh-pages 分支已存在于远程仓库"
    echo "跳过创建，直接更新..."
else
    echo ""
    echo "🔨 创建 gh-pages 分支..."
fi

# 方法 1: 检查是否有 gh-pages 分支
if git ls-remote --heads origin gh-pages | grep -q gh-pages; then
    echo "✓ gh-pages 分支已存在，切换到该分支..."
    git checkout gh-pages
    git pull origin gh-pages
else
    echo "✓ gh-pages 分支不存在，创建新分支..."
    git checkout --orphan gh-pages
fi

# 清理工作目录
echo "🧹 清理工作目录..."
git rm -rf . 2>/dev/null || true

# 复制 docs 目录内容
echo "📂 复制 docs/ 目录内容..."
cp -r docs/* .

# 创建 .nojekyll 文件（防止 GitHub Pages 使用 Jekyll）
echo "# Horizon GitHub Pages" > .nojekyll

# 添加所有文件
echo "➕ 添加文件到 git..."
git add -A

# 提交
echo "💾 提交更改..."
git commit -m "docs: 部署到 GitHub Pages

- 自动部署 Horizon 日报到 GitHub Pages
- 部署时间: $(date '+%Y-%m-%d %H:%M:%S')
- 触发方式: 手动创建 gh-pages 分支"

# 推送到远程
echo "🚀 推送到 GitHub..."
git push -u origin gh-pages

echo ""
echo "=========================================="
echo "✅ gh-pages 分支创建/更新成功！"
echo "=========================================="
echo ""
echo "下一步："
echo "1. 访问 https://github.com/<你的用户名>/Horizon/settings/pages"
echo "2. 选择 Source: Deploy from a branch"
echo "3. Branch: gh-pages"
echo "4. 点击 Save"
echo "5. 等待 2-5 分钟"
echo "6. 访问 https://<你的用户名>.github.io/Horizon/"
echo ""
