@echo off
REM 手动创建并推送 gh-pages 分支
REM 适用于 Windows 系统

echo ==========================================
echo   手动创建 gh-pages 分支
echo ==========================================
echo.

REM 检查是否在正确的目录
if not exist .git (
    echo ❌ 错误: 请在 Horizon 项目根目录运行此脚本
    pause
    exit /b 1
)

echo 📋 检查当前状态...
git status
echo.

echo 📡 检查远程分支...
git ls-remote origin | findstr gh-pages

if %errorlevel% equ 0 (
    echo.
    echo ⚠️  gh-pages 分支已存在
    echo 切换到该分支...
    git checkout gh-pages
    git pull origin gh-pages
) else (
    echo.
    echo 🔨 创建新的 gh-pages 分支...
    git checkout --orphan gh-pages
)

echo 🧹 清理工作目录...
git rm -rf . 2>nul

echo 📂 复制 docs\ 目录内容...
copy docs\* .\ /Y

echo ➕ 创建 .nojekyll 文件...
echo # Horizon GitHub Pages > .nojekyll

echo 💾 添加文件到 git...
git add -A

echo 📝 提交更改...
git commit -m "docs: 部署到 GitHub Pages

- 自动部署 Horizon 日报到 GitHub Pages
- 部署时间: %date% %time%
- 触发方式: 手动创建 gh-pages 分支"

echo 🚀 推送到 GitHub...
git push -u origin gh-pages

echo.
echo ==========================================
echo ✅ gh-pages 分支创建成功！
echo ==========================================
echo.
echo 下一步：
echo 1. 访问 https://github.com/你的用户名/Horizon/settings/pages
echo 2. 选择 Source: Deploy from a branch
echo 3. Branch: gh-pages
echo 4. 点击 Save
echo 5. 等待 2-5 分钟
echo 6. 访问 https://你的用户名.github.io/Horizon/
echo.
pause
