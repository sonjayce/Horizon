# 🔒 私有仓库 GitHub Pages 配置指南

## 📋 当前状态

- ✅ 仓库已改为私有: `sonjayce/Horizon`
- ⚠️ GitHub Pages 需要重新配置
- ✅ gh-pages 分支存在

---

## 🚀 配置步骤

### 步骤 1：进入 Pages 设置

访问: https://github.com/sonjayce/Horizon/settings/pages

或从仓库页面:
```
Settings → Pages
```

---

### 步骤 2：选择部署源

在 **Source** 部分:

```
┌─────────────────────────────────────────┐
│ Source:                                  │
│                                         │
│ ● Deploy from a branch  ◄── 选择这个     │
└─────────────────────────────────────────┘
```

---

### 步骤 3：选择分支

```
Branch: gh-pages  ◄── 选择这个分支
Folder: / (root)  ◄── 保持默认
```

---

### 步骤 4：设置 Pages 可见性

点击 **Save** 后，会弹出可见性设置:

```
┌──────────────────────────────────────────────────┐
│ GitHub Pages visibility                          │
├──────────────────────────────────────────────────┤
│                                                  │
│ ● Public          ◄── 选择这个（保持公开）       │
│ ○ Private                                           │
│                                                  │
│ If you make this site private, only people with   │
│ access to this repository will be able to see it. │
│                                                  │
│ [Save]                                           │
└──────────────────────────────────────────────────┘
```

**重要**: 选择 **Public**，让网站保持公开访问

---

### 步骤 5：等待部署

- ⏱️ 等待 2-5 分钟
- 页面顶部会显示绿色横幅

---

### 步骤 6：验证

访问: https://sonjayce.github.io/Horizon/

应该能正常显示网站 ✅

---

## 🔐 隐私保护说明

### 私有仓库的优势

| 方面 | 私有仓库 | 公开仓库 |
|------|---------|---------|
| 代码可见性 | 🔒 只有你能看 | 🌍 所有人可见 |
| 订阅者列表 | 🔒 私有 | 🌍 公开 |
| 配置细节 | 🔒 私有 | 🌍 公开 |
| GitHub Pages | ✅ 可公开 | ✅ 可公开 |
| GitHub Actions | ✅ 正常 | ✅ 正常 |

### GitHub Pages 可见性

即使仓库是私有的，Pages 仍可选择:

- **Public**: 网站公开，但代码私有
- **Private**: 网站也私有（需要登录才能访问）

**推荐**: 保持 **Public**，让网站可以公开访问

---

## ✅ 配置检查清单

- [ ] 仓库已改为私有
- [ ] GitHub Pages 选择 Deploy from a branch
- [ ] Branch: gh-pages
- [ ] Folder: / (root)
- [ ] Pages 可见性选择 Public
- [ ] 等待 2-5 分钟
- [ ] 访问 https://sonjayce.github.io/Horizon/ 验证

---

## 🔍 故障排查

### Q: Pages 设置找不到？

确保:
1. 仓库是私有状态
2. gh-pages 分支存在
3. Settings → Pages 选项可用

### Q: 网站显示 404？

1. 确认 gh-pages 分支有 index.html
2. 确认 Pages 已启用
3. 强制刷新: Ctrl + F5

### Q: 想重新公开仓库？

```bash
gh repo edit sonjayce/Horizon --visibility public --accept-visibility-change-consequences
```
