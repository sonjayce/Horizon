---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 35 条内容中筛选出 21 条重要资讯。

---

1. [GLM-5.3：具备涌现式网络攻防能力的前沿编程模型](#item-1) ⭐️ 9.0/10
2. [研究者将《毁灭战士》渲染器编译进 Transformer 权重](#item-2) ⭐️ 9.0/10
3. [Qwen 3.8 27B 开源大模型获本地运行好评](#item-3) ⭐️ 8.0/10
4. [Opus 5 的省略式写作与面向智能体的训练令用户困扰](#item-4) ⭐️ 8.0/10
5. [Chrome 切换 Manifest V3 后，Firefox 成为最后一个支持 uBlock Origin 的主流浏览器](#item-5) ⭐️ 8.0/10
6. [AI 机器人实验室年测数百万人体组织，或取代动物测试](#item-6) ⭐️ 8.0/10
7. [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](#item-7) ⭐️ 8.0/10
8. [美国法官责令谷歌一周内取消第三方应用商店安装障碍](#item-8) ⭐️ 8.0/10
9. [PostgreSQL 修复 to\_char 高危堆溢出漏洞，可致任意代码执行](#item-9) ⭐️ 8.0/10
10. [苹果联合阿里训练中国专属 AI 模型，或成首个获批外企](#item-10) ⭐️ 8.0/10
11. [RustDesk 实现 Wayland 真正的无人值守远程访问](#item-11) ⭐️ 7.0/10
12. [谷歌借同态加密让隐私 AI 走向实用](#item-12) ⭐️ 7.0/10
13. [Mixed Bread 发布 Toast 1，一款专为搜索设计的 LLM](#item-13) ⭐️ 7.0/10
14. [讽刺网站恶搞恼人的网页设计模式](#item-14) ⭐️ 7.0/10
15. [别分类，去幻觉！用向量嵌入给内容打标签的巧妙技巧](#item-15) ⭐️ 7.0/10
16. [torch-preflight：一个可发现 PyTorch 训练错误并估算显存的静态检查工具](#item-16) ⭐️ 7.0/10
17. [苹果提议美国 App Store 外部购买抽成 5%–15%](#item-17) ⭐️ 7.0/10
18. [中信接近以 15 亿美元收购阿里游戏部门灵犀](#item-18) ⭐️ 7.0/10
19. [Tom Yeh 教授通过数学讲解 AI 原理](#item-19) ⭐️ 6.0/10
20. [开源 oncothresh 库在临床阈值下评估肿瘤 AI 模型](#item-20) ⭐️ 6.0/10
21. [Hermes Agent 推出 Bot Mode，支持多机器人协作](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GLM-5.3：具备涌现式网络攻防能力的前沿编程模型](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.AI 发布了 GLM-5.3，这是基于 GLM-5.2 底座并通过后训练改进的旗舰编程模型，在 Z.ai Code Bench 上声称提升 50%，并在 Terminal-Bench 3.0 和 Agents&\#x27; Last Exam \(CLI\) 上达到开源 SOTA。该模型还展现出涌现式网络能力，包括自主安全研究、漏洞发现和 0-day 漏洞利用开发。 此次发布标志着 AI 编程模型向自主网络安全领域延伸的重要一步，加剧了关于红队演练、漏洞披露和 AI 安全性的争论。它将影响开发者、安全研究人员和企业，尤其是在该模型开源权重的情况下。 GLM-5.3 与 GLM-5.2 共用同一底座模型，所有提升都来自后训练，并支持 100 万 token 的上下文。社区用户报告称，它可以自主执行红队安全研究，包括对 WordPress 插件和内核的 0-day 漏洞利用，并且 Z.AI 已上线 cvd.z.ai 用于协调漏洞披露。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**背景**: GLM 是由智谱 AI（Z.AI）开发的大语言模型系列，以开放权重著称。‘涌现能力’指的是只有足够大的模型中才会出现、而较小模型不具备的能力。GLM-5.3 基于 GLM-5.2 底座，通过后训练提升，能够处理长周期编程和智能体任务。随着模型能够自主发现和利用软件漏洞，这也带来了新的安全和披露挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM-5.3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://openlm.ai/glm-5.1/">GLM-5.3 | OpenLM.ai</a></li>
<li><a href="https://cset.georgetown.edu/article/emergent-abilities-in-large-language-models-an-explainer/">Emergent Abilities in Large Language Models: An Explainer | Center for Security and Emerging Technology</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体兴奋但意见不一：一些用户报告了令人印象深刻的自主红队测试结果，称该模型‘不可思议’，另一些人则担心大规模扫描开源软件以及未披露 0-day 的伦理问题。一些评论者指出 GLM-5.3 本质上仍是 GLM-5.2 加上后训练改进，且仍逊于 Sol 和 Fable 等模型，也有人赞赏 Z.AI 更偏学术的沟通风格。

**标签**: `#AI`, `#LLM`, `#cybersecurity`, `#coding`, `#GLM`

---

<a id="item-2"></a>
## [研究者将《毁灭战士》渲染器编译进 Transformer 权重](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 9.0/10

一名开发者使用自己编写的编译器 torchwright，将《毁灭战士》的渲染算法转换成一个 210 亿参数的 Transformer 模型，全程无需训练。模型输出像素绘制命令，机械执行这些命令即可还原 E1M1 开场景画面。 这是一个新颖的概念验证，表明算法计算可以直接编译进神经网络权重，为可解释性和模型设计提供了新视角。它展示了 Transformer 可以充当通用计算设备，可能启发未来在无需梯度训练的情况下进行神经执行的研究。 渲染一帧需要 3614 个 token 的提示词加上 53747 个生成 token，在 NVIDIA B200 GPU 上耗时约 40 分钟——即每天约 35 帧，而原版《毁灭战士》在 486 电脑上可达 35 FPS。生成的 checkpoint 是标准的 transformers checkpoint，无需 trust\_remote\_code 即可在 Hugging Face 加载，宿主解析程序仅 43 行 Python 代码。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**背景**: Transformer 是一种基于多头注意力机制的神经网络架构，通常在大规模数据集上训练以预测序列中的下一个 token。这个项目换了一种方式：使用编译器 torchwright 将计算图调度为 16 层、隐藏层大小为 512 的解码器，所有权重直接由源图计算得出，无需任何训练。通过把《毁灭战士》的渲染算法表示为这种图，网络本身变成一段可执行程序，在输入场景数据后输出绘制指令，将经典渲染与神经计算连接起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/physicsrob/torchwright">physicsrob/torchwright: A compiler that transforms computation ...</a></li>
<li><a href="https://medium.com/data-science-collective/i-built-a-tiny-computer-inside-a-transformer-e3000a0019b3">I Built a Tiny Computer Inside a Transformer | by Sean Moran | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_%28deep_learning%29">Transformer (deep learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#transformers`, `#compiler`, `#computation graphs`, `#neural execution`, `#Doom`

---

<a id="item-3"></a>
## [Qwen 3.8 27B 开源大模型获本地运行好评](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

阿里巴巴 Qwen 团队发布了 Qwen3.8-27B，这是一个 270 亿参数的稠密混合注意力模型，提供 FP8 版本，社区用户已在笔记本和单 GPU 上本地运行。社区测试显示其推理和创意生成能力很强，有用户称它是继 Gemma 4 之后第二个通过其私有基准的本地模型。 它的意义在于，一个前沿实验室级别的开源模型现在可以在单块消费级 GPU 上运行，将高级推理能力带入本地和注重隐私的工作流。这与仅提供 API 的 Qwen 3.8-Max 以及 Kimi K3 自托管需要数 TB 存储的情况形成鲜明对比。 这个 270 亿参数的稠密模型属于基于混合注意力架构的 Qwen3.8 系列；vLLM 示例显示它可在 24.6 GiB 内存中运行，支持 1M 上下文下的 660 万 KV tokens。运行需求约为：BF16 下 54GB VRAM、FP8 下约 27GB、4-bit 下约 14–16GB（均未计 KV cache），早期用户还报告其思维链推理速度较慢，且显存使用效率不如 Gemma 4。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: Qwen 是阿里巴巴的开源大语言模型系列；Qwen3.8 是最新一代，包含像 27B 这样的稠密模型，以及 2.4T 参数的 MoE 旗舰模型。它采用混合注意力架构，将全注意力和更高效的注意力机制结合以处理长上下文。FP8 量化降低了显存和带宽需求，llama.cpp 和 vLLM 等工具让用户可以在本地 PC 或单 GPU 上部署，而无需依赖云 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>
<li><a href="https://www.amd.com/en/blogs/2026/run-qwen-3-8-27b-on-amd-ryzen-ai-max-and-radeon-graphics-cards-day-0.html">Run Qwen 3.8 27B on AMD Ryzen™ AI Max Agentic PCs and Radeon ™ GPUs</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B | vLLM Recipes</a></li>

</ul>
</details>

**社区讨论**: 评测者总体对该模型的推理和创造力印象深刻，但反馈也有保留。一位测试者指出，它在私有基准上正确推理需要多花约 5 倍的 token，并在启用 MTP 的情况下耗时 12 分 30 秒，且显存使用效率似乎不如 Gemma 4；另一位用户则称赞它能画出结构正确的骑自行车鹈鹕。一些用户还担心其独特的笔记式思维痕迹，希望在 Ollama 中能关闭思考功能，并分享了社区修改的 Jinja 模板以减少思考、修复工具调用。

**标签**: `#AI`, `#LLM`, `#Qwen`, `#local-models`, `#benchmarking`

---

<a id="item-4"></a>
## [Opus 5 的省略式写作与面向智能体的训练令用户困扰](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

一篇博客文章和 Hacker News 讨论指出，Anthropic 的 Opus 5 模型生成过于省略、抽象的文字，其后期训练似乎面向其他 AI 智能体而非人类可读性，导致它用起来感觉更差。这场讨论拥有超过 726 分和 661 条评论，反映出一种日益强烈的感受：Opus 5 虽然能力更强，却更不好用。 这表明行业正把前沿大模型优化为面向智能体之间的通信，可能牺牲人类用户体验。这直接影响 Claude 等大模型的日常使用者，并可能促使他们改用旧版或竞品。 用户反馈 Opus 5 写作过于省略，使用无生命主语和“反转式”结尾；有人已换回 Claude 4.8 或转用 OpenAI 的 Sol。评论区还指出，该模型过度“坦白错误”且话多。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: 省略式写作（elliptical writing）会省略由语境暗示的词或短语，使 AI 文本显得简练但抽象。后期训练（post-training）是通过强化学习和偏好优化微调基础模型；如果奖励来自智能体评估而非人类反馈，输出就会偏向“智能体语言”。智能体 AI（agentic AI）指由专门智能体组成的自主系统，能主动发起任务与协作，从而降低了对人类友好交互的重视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trinka.ai/blog/what-is-elliptical-construction-in-academic-writing/amp/">What is Elliptical Construction in Academic Writing? Trinka 1</a></li>
<li><a href="https://www.hostinger.com/in/tutorials/what-is-agentic-ai">What is agentic AI ?</a></li>

</ul>
</details>

**社区讨论**: 评论者大多表示认同：很多人觉得 Opus 5 令人疲惫且过于省略，甚至调侃它使用“智能体语言”，并且“总是&\#x27;诚实&\#x27;地&\#x27;坦白&\#x27;错误”。有人换回 4.8 或转向 OpenAI，还有人引用了一段特别抽象的原文。大家就“为了能力提升是否值得牺牲用户体验”展开激烈讨论，并指出该问题在 Hacker News 上讨论还不够多。

**标签**: `#AI/ML`, `#LLMs`, `#UX`, `#Anthropic`, `#Agentic AI`

---

<a id="item-5"></a>
## [Chrome 切换 Manifest V3 后，Firefox 成为最后一个支持 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 8.0/10

Chrome 强制推行 Manifest V3 后，原版 uBlock Origin 扩展在 Chrome 及其他基于 Chromium 的浏览器中已无法使用，Firefox 成为唯一一个仍能完整支持该扩展的主流浏览器。Firefox 仍允许 uBlock Origin 所依赖的强大的 webRequest 拦截 API。 这意义重大，因为广告拦截仍是浏览器扩展最流行的用途之一，而 Google 的政策变更实际上削弱了占多数的 Chrome 用户的广告拦截能力。这也加剧了 Chrome 与 Firefox 的竞争，可能会促使注重隐私的用户转用其他浏览器。 据维基百科数据，截至 2026 年 6 月，uBlock Origin 在 Chrome 上有超过 2900 万活跃用户，在 Firefox 上有超过 1060 万。Chrome 用户现在被引导使用 uBlock Origin Lite，这是一个符合 Manifest V3 的版本，与原始版本相比过滤能力有所降低。

hackernews · DemiGuru · 8月14日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49303202)

**背景**: Manifest V3 是 Chrome 最新的扩展平台，旨在改善隐私、安全性和性能，但它限制了 uBlock Origin 等内容拦截器用于拦截网络请求的 webRequest API。Firefox 选择不强制执行这些限制，因此原版广告拦截扩展仍可正常工作。其结果是，Firefox 成为目前唯一一个仍可使用完整版 uBlock Origin 的主流浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">UBlock Origin</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞扬 Firefox 对 uBlock Origin 的持续支持及代码审查，同时批评 Google 的 Manifest V3 限制是权力扩张。有人建议通过以未打包扩展方式加载 uBlock Origin 等变通方法，但也指出这样很麻烦。整体舆论强烈反对 Google，支持 Firefox。

**标签**: `#browsers`, `#ad-blocking`, `#Firefox`, `#Chrome`, `#Manifest V3`

---

<a id="item-6"></a>
## [AI 机器人实验室年测数百万人体组织，或取代动物测试](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

Vivodyne 推出了由 12 个机器人“蜂巢”实验室组成的网络，每年可开展 310 万项活体人体组织实验，约为美国全部临床试验总量的一倍。该 AI 平台培养人体组织并设计实验，以更好地预测药物疗效和安全性。 如果成功，这种方法有望大幅减少对动物测试的依赖，目前约有 90%进入临床试验的药物在通过动物测试后仍告失败。它解决了药物研发的关键瓶颈，可能加速更安全、更有效疗法的问世。 每个“蜂巢”都是一座完整的实验室，可同时对 1 万个人体组织进行测试，以端到端的机器人一致性生成单细胞分辨率的表型组、转录组和蛋白质组数据，周期为 1-2 周。该平台将这些数据输入强化学习循环，使 AI 能够迭代优化实验假设。

telegram · zaihuapd · 8月14日 01:48

**背景**: 动物测试长期以来一直是临床前研究的标准步骤，但其对人类反应的预测能力较差，导致临床试验失败率居高不下。类器官和组织工程技术已成为更接近人类生理的替代方案，自动化技术正使其可扩展用于高通量药物筛选。Vivodyne 的平台将上述趋势与 AI 设计实验相结合，让人类生物学可以大规模计算化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://biobuzz.io/news/penn-born-vivodyne-launches-what-it-calls-the-worlds-largest-human-biological-datacenter/">Penn-Born Vivodyne Launches What It Calls the World&#x27;s Largest ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-026-40231-0">A modular platform for automated organoid culture and ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotechnology`, `#drug discovery`, `#lab automation`, `#animal testing alternatives`

---

<a id="item-7"></a>
## [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室开源了 dots3-note preview，这是 dots3 系列首个开放权重模型。该模型总参数 280B，每次仅激活 16B 参数，支持 512K 上下文，可处理文字、图片、视频和音频。 此次发布为开源社区带来了一款推理高效的超大规模 MoE 模型，有望降低前沿能力的使用门槛。同时，它引入了新的强化学习方法 TEMPO 和两个真实场景智能体基准，可能推动智能体的训练与评测发展。 模型权重已在 Hugging Face 开源，同时发布了 VibeSearchBench 和 VibeLifeBench 两个面向长程智能体任务的双语基准。据公告，TEMPO 通过自批判和测试时价值估计来训练长程智能体，但本次搜索结果中未提供官方技术细节。

telegram · zaihuapd · 8月14日 08:27

**背景**: 混合专家（MoE）模型将计算分配给多个专门子网络，因此总参数量可达数千亿，但每次处理一个 token 只激活其中一部分，从而大幅降低推理成本。强化学习（RL）常用于预训练之后，使大模型与人类偏好对齐，并提升推理和智能体能力。新发布的 VibeSearchBench 和 VibeLifeBench 基准旨在评估智能体在真实、长程场景下的表现，而非简单的单轮任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vibebench.github.io/VibeSearchBench.github.io/">VibeSearchBench — Benchmarking Long-horizon Proactive Search ...</a></li>
<li><a href="https://arxiv.org/abs/2605.27882">[2605.27882] VibeSearchBench: Benchmarking Long-horizon ...</a></li>
<li><a href="https://arxiv.org/abs/2608.10875">VibeLifeBench: Can Your Life Agent Be Proactive and ...</a></li>

</ul>
</details>

**标签**: `#MoE`, `#open-source`, `#reinforcement-learning`, `#LLM`, `#Xiaohongshu`

---

<a id="item-8"></a>
## [美国法官责令谷歌一周内取消第三方应用商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10

美国地区法官 James Donato 命令谷歌简化竞争性安卓应用商店的安装流程，删除 Play Store 中多余的步骤和警告弹窗。谷歌须在一周内完成修改，此命令源自 Epic 诉谷歌反垄断案的判决。 这项裁决直接对谷歌 Play Store 执行反垄断补救措施，可能让竞争对手的应用商店更容易触达安卓用户。它可能重塑安卓应用分发格局，并影响全球正在进行的应用商店监管。 多余的障碍包括多步安装流程——用户须先点击“查看详情”才能看到“安装”按钮，以及法院认为蓄意反竞争的警告弹窗。除非上级法院暂缓执行，谷歌必须在一周内遵守该命令。

telegram · zaihuapd · 8月14日 09:55

**背景**: 在安卓上，用户可以通过“侧载”方式绕过 Google Play 安装 APK 文件，但系统会显示警告提示。Google Play Protect 也会扫描应用是否存在有害行为。Epic 诉谷歌案认定谷歌通过其商店政策非法垄断了安卓应用分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sideloading">Sideloading - Wikipedia</a></li>
<li><a href="https://www.androidcentral.com/what-sideloading">What is sideloading? [Android A to Z] | Android Central</a></li>
<li><a href="https://support.google.com/googleplay/answer/2812853?hl=en">Use Google Play Protect to help keep your apps... - Google Play Help</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#google`, `#android`, `#app-store`, `#legal`

---

<a id="item-9"></a>
## [PostgreSQL 修复 to\_char 高危堆溢出漏洞，可致任意代码执行](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 披露了 CVE-2026-14669，这是 to\_char\(timestamptz\) 函数中的高危堆缓冲区溢出漏洞，可使已认证的低权限用户执行任意代码。已在所有受支持分支中发布修复，包括 18.6、17.11、16.15、15.19 和 14.24。 该漏洞十分严重，因为它可将低权限数据库访问升级为以 PostgreSQL 服务进程操作系统权限执行任意代码，对数据的机密性和完整性构成严重威胁。运行受影响版本的组织应立即修补，因为利用只需一个低权限数据库账户。 该漏洞在 to\_char\(timestamptz\) 处理超长 POSIX 时区缩写时触发堆缓冲区溢出。CVSS 评分为 8.8；由于 18.5 因回归问题未正式发布，18 系列用户应直接升级至 18.6，其他用户应升级至 17.11、16.15、15.19 或 14.24。

telegram · zaihuapd · 8月14日 14:35

**背景**: to\_char 是 PostgreSQL 的格式化函数，可将时间戳、间隔和数字转换为格式化字符串；timestamptz 是 PostgreSQL 对带时区时间戳的扩展类型。此次更新属于小版本发布，无需转储数据库或运行 pg\_upgrade，只需替换程序文件并重启服务。该漏洞源于 to\_char 在处理超长时区缩写字符串时的具体方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/functions-formatting.html">PostgreSQL: Documentation: 18: 9.8. Data Type Formatting Functions</a></li>
<li><a href="https://www.postgresql.org/docs/current/datatype-datetime.html">PostgreSQL: Documentation: 18: 8.5. Date/Time Types</a></li>
<li><a href="https://www.postgresql.org/docs/current/pgupgrade.html">PostgreSQL : Documentation: 18: pg _ upgrade</a></li>

</ul>
</details>

**标签**: `#security`, `#postgresql`, `#CVE`, `#vulnerability`, `#database`

---

<a id="item-10"></a>
## [苹果联合阿里训练中国专属 AI 模型，或成首个获批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

苹果已在阿里巴巴支持下，专门为中国市场训练了一款大语言模型，不再沿用此前依赖第三方模型的策略。Apple Intelligence 预计将在未来数月随 iOS 更新在华上线，中国网信办已对其生成式 AI 服务进行备案。 若获批准，苹果将成为首家获北京许可在华提供自有 AI 模型的外国公司，为外企在中国监管框架下落地 AI 树立标杆。此举也使苹果能更好地掌控这一重要市场的 AI 体验。 该模型专为中国市场打造，阿里巴巴为这一项目提供支持。中国网信办已于上月对生成式 AI 服务进行备案，这是面向公众发布前的必要步骤；Apple Intelligence 将随未来的 iOS 更新上线。

telegram · zaihuapd · 8月14日 14:47

**背景**: Apple Intelligence 是苹果集成在 iOS、iPadOS 和 macOS 中的 AI 功能套件，iPhone 上需要 A17 Pro 或更新的芯片支持。在中国大陆，生成式 AI 服务必须根据网信办的《生成式人工智能服务管理暂行办法》完成安全评估和算法备案后，才能向公众提供，这是外企面临的关键监管门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>
<li><a href="https://www.pertamapartners.com/insights/china-ai-regulations">China AI Regulations 2026: Rules Companies Must Follow</a></li>
<li><a href="https://multigrid.ai/learn/china-generative-ai-measures-filing">China&#x27;s Generative AI Measures: the Registration and Filing ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#Regulation`

---

<a id="item-11"></a>
## [RustDesk 实现 Wayland 真正的无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 宣布支持在 Wayland 上进行真正的无人值守远程访问。这解决了以前常见的限制，过去需要用户在现场或与权限提示交互。 Wayland 是许多现代 Linux 发行版的默认显示服务器，其安全模型此前会阻止无人值守会话。这次更新使 RustDesk 用户能够远程管理无头或无人在场的 Wayland 机器，提高了自托管远程支持的可行性。 公告在提供的摘要中没有说明版本号或发布日期。一位社区成员还指出，自托管的 RustDesk 仍缺少加密连接，这是 GitHub 上的一个未解决问题。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**背景**: RustDesk 是一款开源远程桌面应用程序，允许用户部署自己的服务器以获得数据主权和灵活性。Wayland 是一种显示服务器通信协议，旨在作为 X Window 系统的安全替代品；其设计隔离了输入和输出，这使得传统的基于 X11 的工具更难实现无人值守远程访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/">RustDesk: Open-Source Remote Desktop with Self-Hosted Server ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wayland_%28protocol%29">Wayland (protocol) - Wikipedia</a></li>
<li><a href="https://wayland.freedesktop.org/">Wayland</a></li>

</ul>
</details>

**社区讨论**: 总体反应热烈，一位用户表示两天前刚遇到这个问题，很高兴看到它得到解决。其他人提出了注意事项，例如自托管模式缺少加密（通过 GitHub issue 链接），以及询问 RustDesk 与 VNC 或基于 SSH 的替代方案（如通过 Tailscale 使用 Remmina）相比如何。

**标签**: `#remote-desktop`, `#wayland`, `#rustdesk`, `#open-source`, `#security`

---

<a id="item-12"></a>
## [谷歌借同态加密让隐私 AI 走向实用](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 7.0/10

谷歌宣布正在让同态加密在隐私 AI 领域变得实用，从而无需解密即可直接对加密数据进行计算。这一公告将其视为迈向可用的、保护隐私的 AI 服务的重要一步。 如果同态加密真正具备商业可行性，它就能在医疗记录等敏感数据上实现保护隐私的机器学习，从而消除数据共享的一大障碍。在隐私法规趋严、用户对数据控制权要求更高的背景下，这对整个 AI 行业也很重要。 同态加密仍然具有极高的计算开销——推理任务的开销约为原始计算的 1000 倍——这严重限制了其商业可行性。Hacker News 社区还质疑其巨大的能源成本，并指出真正私密的 AI 可以在用户本地硬件上运行，而不是在大型数据中心中运行。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**背景**: 同态加密是一种无需事先解密即可对加密数据进行计算的加密形式；解密后的结果与对明文执行相同操作得到的输出一致。它被视为实现隐私保护外包存储和计算的关键技术，使服务能够在数据不暴露的情况下分析敏感数据，即使服务提供商的系统被攻破，数据也仍然安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑态度：有人称谷歌是头号反隐私的科技巨头，也有人指出约 1000 倍的开销让同态加密“不太具有商业可行性”，并警告其巨大的能源消耗。少数人承认，如果这一说法属实，即使模型本身不占优势，谷歌也可能重新回到竞争行列。

**标签**: `#homomorphic encryption`, `#AI privacy`, `#Google`, `#security`, `#machine learning`

---

<a id="item-13"></a>
## [Mixed Bread 发布 Toast 1，一款专为搜索设计的 LLM](https://www.mixedbread.com/blog/toast-1) ⭐️ 7.0/10

Mixed Bread 推出了 Toast 1，这是一款专为搜索而设计的大语言模型，旨在提升搜索质量。这一发布引发了关于其设计选择以及与通用模型之间权衡的讨论。 这一事件意义重大，因为它探索了人工智能的新前沿：使用专门构建的搜索模型，而非依赖通用大模型加插件的方案。如果成功，Toast 1 可能会影响搜索引擎和 AI 助手处理复杂查询的方式，从而影响开发者和最终用户。 值得注意的是，该模型并未开放权重，公开的技术细节有限。社区成员将其与现有的搜索服务（如 Perplexity、带搜索的 Gemini 和 Parallel AI）进行比较，并质疑它与专门的检索增强生成（RAG）流水线有何不同。

hackernews · mplappert · 8月14日 15:07 · [社区讨论](https://news.ycombinator.com/item?id=49299746)

**背景**: 专门化大语言模型是通过在特定领域数据上训练或微调，以执行范围更窄的任务，与 GPT-4 等通用模型形成对比。根据 Arya AI 的说法，领域专用 LLM 接触行业术语和上下文，从而在目标应用中提供更高的准确性和效率。业界正在经历从扩大通用 LLM 规模转向构建更小、更专业的模型的转变，这已在行业分析中被提及。Toast 1 似乎就是这一趋势的产物，它专门针对搜索问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.blog/2024/12/05/four-approaches-to-creating-a-specialized-llm/">Four approaches to creating a specialized LLM - Stack Overflow</a></li>
<li><a href="https://arya.ai/blog/domain-specific-llm-examples-and-benefits">What is a Domain-Specific LLM ? Examples and Benefits</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对这一想法总体表示热情，但也提出了关切。有评论者称赞这一概念对复杂查询来说是‘稳赢’的，还有人遗憾它不是开放权重模型，并询问它与 Perplexity、带搜索的 Gemini 和 Parallel AI 相比如何。其他人则开玩笑地希望它是硬件创业公司，并要求文章进一步解释‘Mixedbread Search’。

**标签**: `#LLM`, `#Search`, `#AI`, `#Mixed Bread`, `#Specialized Models`

---

<a id="item-14"></a>
## [讽刺网站恶搞恼人的网页设计模式](https://lxe.github.io/everywebsite/) ⭐️ 7.0/10

《Every Fucking Website》是一个讽刺性单页网站，模仿了弹窗、Cookie 横幅和自动播放视频等常见的侵入式网页设计模式。它于 2020 年发布，在 Hacker News 上引发了 392 条关于 UX 黑暗模式和网页性能的讨论。 这个讽刺作品揭示了欺骗性设计模式在现代网页开发中已经变得多么普遍和习以为常。它引发了关于转化率优化与用户体验之间张力的宝贵讨论，影响设计师、开发者和广大网民。 尽管模仿了臃肿的网站，这个页面本身加载迅速且响应灵敏，JavaScript 只来自 lxe.github.io。评论者指出它遗漏了一些常见的烦人设计，例如随滚动跟随并在点击后取消静音的自动播放视频，以及手机上“在应用中打开”的提示。

hackernews · doubletwoyou · 8月14日 14:31 · [社区讨论](https://news.ycombinator.com/item?id=49299222)

**背景**: 黑暗模式（dark patterns）是刻意设计用来诱骗用户做出本不会做的事情的界面，例如购买不需要的产品或订阅周期性账单。该术语由用户体验设计师 Harry Brignull 于 2010 年提出。这个讽刺网站以反讽的方式使用这些模式，批评现代网页设计，并提高人们对敌视用户行为的认识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者开玩笑说这个恶搞页面加载太快、使用的第三方域名太少，还有人指出它应该使用 8 到 18 个域名。其他人则提出它还缺少一些黑暗模式，比如应用安装提示和 Google 登录弹窗。一位电商创始人分享说，类似的弹窗确实提高了转化率，但代价是“轻微的自厌”，并称之为“切斯特顿弹窗”。

**标签**: `#web design`, `#user experience`, `#satire`, `#dark patterns`, `#web development`

---

<a id="item-15"></a>
## [别分类，去幻觉！用向量嵌入给内容打标签的巧妙技巧](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

道格·特恩布尔（Doug Turnbull）提出了一种技巧：先让 LLM 在不看现有标签库的情况下“幻觉”出候选标签，再用向量嵌入把这些候选映射到最接近的真实标签。西蒙·威利森（Simon Willison）认为这能很实用地解决他博客中 1,856 个历史标签的匹配问题。 这种方法避免了每次请求都把整个标签词表发给 LLM，从而降低提示词长度、成本和复杂度。它为做搜索、标签和内容分类的开发者提供了一种简单的方式，把新内容映射到已有分类体系。 该技巧让模型根据目标标签的示例格式（例如“Furniture / Living Room Furniture / Coffee Tables &amp; End Tables / Coffee Tables”）生成全新的、从未出现过的分类。随后把这些幻觉标签转成嵌入向量，通过向量相似度匹配到最接近的现有标签。

rss · Simon Willison · 8月14日 21:54

**背景**: 用 LLM 做分类通常需要把全部候选标签都展示给模型，当一个站点有数千个标签时这很不现实。该方案与 HyDE（假设性文档嵌入）思路相似：HyDE 通过生成假设文档来进行无需相关性标注的零样本检索。在这里，LLM“幻觉”出的标签起占位作用，再通过嵌入向量锚定到真实标签库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zilliz.com/learn/improve-rag-and-information-retrieval-with-hyde-hypothetical-document-embeddings">Better RAG with HyDE - Hypothetical Document Embeddings</a></li>
<li><a href="https://lancedb.github.io/documentation/rag/advanced_techniques/hyde.html">HyDE - LanceDB</a></li>

</ul>
</details>

**标签**: `#llm`, `#embeddings`, `#tagging`, `#search`, `#vector-databases`

---

<a id="item-16"></a>
## [torch-preflight：一个可发现 PyTorch 训练错误并估算显存的静态检查工具](https://www.reddit.com/r/MachineLearning/comments/1vo8vv0/a_linter_for_pytorch_torchpreflight_p/) ⭐️ 7.0/10

作者发布了 torch-preflight，这是一个针对 PyTorch 的新型 linter，通过静态分析来检测常见训练错误，例如缺少 zero\_grad\(\) 调用、由 losses.append\(loss\) 导致的 autograd 计算图保留，以及在 DDP 中未使用 DistributedSampler 等问题。它无需导入或执行用户代码即可估算显存使用量，并可通过 pip install torch-preflight 安装。 这些错误通常会浪费大量 GPU 机时并导致训练任务失败，因此在代码运行前就能发现它们的工具对 PyTorch 开发者很有价值。显存估算还能帮助开发者在为云端实例付费之前判断训练能否在该 GPU 上跑通，这在成本高昂的机器学习工作流中越来越重要。 该工具目前实现了 13 条 lint 规则，并且无需 GPU 或安装 PyTorch 即可分析代码。作者报告称，显存估算结果与实测峰值误差在 4% 以内，但这一数据仅来自单块 T4 GPU 上的四个模型；此外误报仍然是一个隐忧，目前最大的测试目标仅仅是 PyTorch 源码树。

reddit · r/MachineLearning · /u/LeJanbandhu · 8月14日 14:30

**背景**: PyTorch 的 autograd 系统会在反向传播过程中动态构建计算图来计算梯度。常见误区包括：将 loss 张量直接存入 Python 列表而不 detach，导致计算图被保留、内存持续增长；以及在训练循环中忘记调用 optimizer.zero\_grad\(\)，使得梯度跨迭代累积。在分布式训练中，DistributedDataParallel \(DDP\) 需要搭配 DistributedSampler，才能确保每个 rank 训练不同的数据子集。Linter 通过静态分析读取代码而不会执行代码，因此运行快速且安全，适合在 CI 或本地使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html">Getting Started with Distributed Data Parallel — PyTorch Tutorials...</a></li>
<li><a href="https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html">A Gentle Introduction to torch.autograd — PyTorch Tutorials 2 ...</a></li>
<li><a href="https://shivgahlout.github.io/2021-05-18-distributed-computing/">Distributed Computing with PyTorch</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#linter`, `#machine learning`, `#developer tools`, `#static analysis`

---

<a id="item-17"></a>
## [苹果提议美国 App Store 外部购买抽成 5%–15%](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 7.0/10

苹果已向美国法院提交外部购买抽成方案：标准应用抽成 15%，订阅续费及部分合作项目抽成 10%，小型企业计划应用抽成 5%。该方案是 Epic Games 反垄断案持续诉讼的一部分。 该方案将决定开发者在引导用户通过外部支付链接交易时需向苹果支付多少费用，这是应用商店反垄断争议的核心问题。法院设定的费率可能为美国应用商店经济树立先例，并影响开发者收入。 费率按类别区分：标准应用抽成 15%，视频/新闻合作项目及订阅续费抽成 10%，小型企业计划开发者抽成 5%。最高法院近期驳回了苹果暂停下级法院费率审理的请求，苹果预计在 9 月 14 日前提交书面意见。

telegram · zaihuapd · 8月14日 02:33

**背景**: 苹果应用商店的标准抽成为大多数交易 30%，而年收入低于 100 万美元的小型企业计划开发者享受 15%的优惠费率。Epic Games 诉讼质疑苹果的应用内购买要求和抽成制度，最终法院裁定苹果必须允许外部购买链接，并由法院设定相应的抽成结构。这份文件正是苹果为美国外部链接购买提出的定价方案。开发者和分析师密切关注此案，因为类似的规则已在欧盟《数字市场法》下生效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://applemagazine.com/apple-app-store-fees-external-purchases/">Apple Proposes 15% App Store Fees for External Purchases</a></li>
<li><a href="https://developer.apple.com/app-store/small-business-program/">App Store Small Business Program - Apple Developer</a></li>
<li><a href="https://www.forasoft.com/blog/article/how-to-avoid-apple-pay-commission-204">Apple App Store Commission : How to Pay Less in 2026</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#Epic Games`, `#Antitrust`, `#Commissions`

---

<a id="item-18"></a>
## [中信接近以 15 亿美元收购阿里游戏部门灵犀](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 7.0/10

中信集团旗下的私募机构信宸资本（Trustar Capital）接近收购阿里巴巴旗下游戏业务灵犀互娱，交易估值或超 15 亿美元。信宸资本在击败多家游戏公司等竞购者后成为最可能的买家，但磋商仍在进行，尚未做出最终决定。 这笔收购凸显了阿里巴巴在 CEO 吴泳铭推动下正剥离非核心资产、聚焦 AI 与云计算的战略转向。对于信宸资本而言，这将标志着其大举进入游戏行业，并成为中国游戏业规模较大的私募股权交易之一。 灵犀的旗舰游戏《三国志·战略版》是与日本光荣特库摩（Koei Tecmo）合作开发的大型多人在线策略游戏。交易仍在进行中，最终估值和完成仍有待进一步协商。

telegram · zaihuapd · 8月14日 10:24

**背景**: 信宸资本是中信资本控股有限公司的关联企业，后者是一家 2002 年成立的、总部位于香港的另类投资机构，也是亚洲领先的私募股权平台之一。阿里巴巴作为中国科技巨头，通过灵犀互娱进入游戏行业，并凭借其热门策略游戏在中国市场声名鹊起。在 CEO 吴泳铭的领导下，阿里巴巴一直在剥离非核心业务，以聚焦人工智能和云服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Trustar_Capital">Trustar Capital</a></li>
<li><a href="https://www.scmp.com/tech/apps-social/article/3089422/alibabas-romance-three-kingdoms-strategy-edition-its-first-real">Is Alibaba’s Romance of the Three Kingdoms : Strategy Edition its...</a></li>
<li><a href="https://technode.com/2024/12/09/alibaba-executive-apologizes-after-his-internal-speech-at-lingxi-interactive-sparks-controversy/">Alibaba executive apologizes after controversial speech to Lingxi ...</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#M&amp;A`, `#gaming`, `#tech-industry`, `#acquisition`

---

<a id="item-19"></a>
## [Tom Yeh 教授通过数学讲解 AI 原理](https://www.byhand.ai/) ⭐️ 6.0/10

Tom Yeh 教授的 AI by Hand 是 Substack 上的研究性出版物，通过数学和算法层面的讲解来教授模型可解释性与可说明性。该平台提供免费文章、直播研讨会，并可通过付费会员访问完整研究库。 AI by Hand 通过在最基础层面让人理解复杂模型，回应了 AI 领域日益增长的透明性需求。它帮助学生、开发者和研究人员掌握模型的工作原理，推动负责任的 AI 发展。 该出版物托管在 Substack 上，拥有数万订阅者；AI by Hand 学院提供课堂式体验，让成员手写、手绘并手算 AI。完整研究库需要会员资格才能访问，这也让一些读者感到困惑。

hackernews · sans\_souse · 8月14日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49300568)

**背景**: 可解释性（interpretability）与可说明性（explainability）是理解 AI 决策的两种相关方法：前者侧重拆解模型内部结构，后者侧重用人类可理解的方式解释结果。Tom Yeh 的项目提倡“动手学习”，即亲手推算数学和算法，而非只依赖高层库。这种动手方式在 AI 教育中很常见，类似用 NumPy 从零搭建神经网络的做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.byhand.ai/">AI by Hand ️ | Prof. Tom Yeh | Substack</a></li>
<li><a href="https://byhand.mykajabi.com/">AI by Hand ️ Academy</a></li>

</ul>
</details>

**社区讨论**: 评论者总体反应积极，推荐了如“Train your own LLM”和 No Starch Press 的《Deep Learning》等补充资源。有些人对订阅付费墙表示困惑，还有用户分享了自己的开源项目 ml-by-hand，其灵感同样来自“我无法创造的东西，我就无法理解”这一理念。

**标签**: `#AI education`, `#interpretability`, `#explainability`, `#machine learning`

---

<a id="item-20"></a>
## [开源 oncothresh 库在临床阈值下评估肿瘤 AI 模型](https://www.reddit.com/r/MachineLearning/comments/1vod2c8/opensource_python_library_nocode_web_dashboard/) ⭐️ 6.0/10

作者发布了 oncothresh v0.1，这是一个开源 Python 库，以及配套的无代码 Web 仪表板（oncothresh-web），用于在特定临床决策阈值下评估肿瘤 AI 模型。这些工具可计算切断点处的灵敏度/特异度/PPV/NPV、bootstrap 置信区间、阈值-灵敏度曲线、边界加权校准、决策曲线净收益以及需检人数等指标。 大多数肿瘤 AI 评估指标（如 AUC、ICC、MAE）衡量的是整体一致性，但临床医生需要知道模型在决定患者分诊、活检或治疗的那个确切阈值上的可靠性。通过聚焦临床阈值并进行不确定性量化，oncothresh 填补了 PathBench 和 PathBench-MIL 等病理基准留下的空白，有望促进 AI 在癌症诊疗中的安全应用。 oncothresh 刻意保持轻量依赖，仅使用 numpy、scipy、scikit-learn 和 pydantic，面向肿瘤细胞占比、Ki-67、TMB 和 PD-L1 评分等任务，这些任务需要将连续输出在固定阈值处变为“是/否”决策。配套 Web 仪表板通过 docker compose 在本地运行，无云依赖；整个项目目前为 v0.1，作者欢迎对决策曲线分析或校准数学边角情况的反馈。

reddit · r/MachineLearning · /u/adom2989 · 8月14日 17:06

**背景**: 临床 AI 模型通常输出连续的风险评分，但实际决策需要一个触发行动（如活检或治疗）的阈值。AUC 等标准分类指标汇总所有阈值下的性能，可能掩盖模型在临床相关点上的真实表现。决策曲线分析、净收益和需检人数等概念有助于量化临床效用，使模型评估与实际的诊疗决策保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://physicianaihandbook.com/implementation/evaluation.html">Clinical AI Evaluation: Evidence, Validation, and Monitoring</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decision_curve_analysis">Decision curve analysis - Wikipedia</a></li>
<li><a href="https://drlogy.com/calculator/faq/how-do-you-calculate-the-number-needed-to-test">How do you calculate the Number Needed to Test? | Drlogy</a></li>

</ul>
</details>

**标签**: `#medical AI`, `#oncology`, `#ML evaluation`, `#Python library`, `#open-source`

---

<a id="item-21"></a>
## [Hermes Agent 推出 Bot Mode，支持多机器人协作](https://x.com/Teknium/status/2088003994904113614) ⭐️ 6.0/10

Hermes Agent 推出了 Bot Mode，这是一个新的桌面插件，可将每个 agent 配置文件转变为一个独立的机器人，拥有自己的任务、描述和头像，并支持机器人之间的互相通信。该功能将通过 GitHub 插件在 Hermes Desktop 上开展为期 1 天的公开测试，作者收集反馈后再并入正式桌面应用。 这一功能意义重大，因为它在流行的开源 AI agent 中引入了实用的多智能体协作模式，让独立机器人能够分工并相互通信。这有望降低在桌面端构建多 agent 工作流的门槛，也反映出行业向面向用户的多智能体系统发展的趋势。 Bot Mode 以桌面插件形式实现，无需修改核心代码，新增了一个 Bots 面板，列出带有头像、消息预览和时间戳的 agent 配置文件，便于快速切换。每个机器人都有自己的聊天、头像、个性、日常任务和 bot 间消息功能；该功能在并入正式 Hermes Desktop 应用前，会进行为期 1 天的公开测试以收集反馈。

telegram · zaihuapd · 8月14日 04:13

**背景**: Hermes Agent 是 Nous Research 推出的开源 AI agent，具备持久记忆、可复用技能、定时任务、工具调用和多平台消息功能。Hermes Desktop 是面向 macOS、Windows 和 Linux 的原生桌面应用，为 Hermes Agent 提供聊天、配置和管理的界面。Bot Mode 在此基础上增加了多 agent 名单功能，使机器人能够独立运行并互相发送消息，这是朝着更自主、更协作的 AI 工作流迈出的一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hermes-agent.ai/">Hermes Agent — Open-Source AI Agent with Memory, Skills, and Cron</a></li>
<li><a href="https://github.com/NousResearch/Hermes-Bot-Mode/blob/main/README.md">Hermes - Bot - Mode /README.md at main...</a></li>
<li><a href="https://www.stork.ai/en/hermes-desktop">Hermes Desktop Review (2026) | Stork.AI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#multi-agent systems`, `#Hermes`, `#feature announcement`

---