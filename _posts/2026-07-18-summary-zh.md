---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 37 条内容中筛选出 14 条重要资讯。

---

1. [GPT-5.6 填补凸优化领域 30 年空白](#item-1) ⭐️ 9.0/10
2. [LG 显示器通过 Windows Update 静默安装软件，未经用户同意](#item-2) ⭐️ 9.0/10
3. [中国 Kimi K3 模型通过蒸馏对标前沿模型](#item-3) ⭐️ 9.0/10
4. [美国拟设类似 FINRA 的 AI 监管机构](#item-4) ⭐️ 9.0/10
5. [Fable 5 对阵 GPT-5.6 Sol：NP 难问题上的/goal 指令效果评估](#item-5) ⭐️ 8.0/10
6. [Stack Overflow 衰落：AI 影响与社区壁垒](#item-6) ⭐️ 8.0/10
7. [PHK 发表告别文，反思自行车棚效应](#item-7) ⭐️ 8.0/10
8. [Anthropic 将 Claude Fable 5 永久纳入订阅计划](#item-8) ⭐️ 8.0/10
9. [指控：DeepMind/Kaggle 大奖颁给无意义的 AI 提交](#item-9) ⭐️ 8.0/10
10. [Meta 计划向 Anthropic 出租 AI 算力，潜在交易达百亿美元](#item-10) ⭐️ 8.0/10
11. [SpaceX 与五角大楼谈判 AI 算力交易](#item-11) ⭐️ 8.0/10
12. [OpenRouter 被传收购，估值超 13 亿美元](#item-12) ⭐️ 8.0/10
13. [台积电 A14 制程良率性能接近 90%，进度超前](#item-13) ⭐️ 8.0/10
14. [B 站展示开源 AI 伙伴 Project N.E.K.O.](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 填补凸优化领域 30 年空白](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

大型语言模型 GPT-5.6 通过单一提示词被用于证明凸优化中一个存在 30 年的未解决问题，建立了在球形域上最小化凸 Lipschitz 函数的时间复杂度上界。 这一突破表明人工智能能够解决长期存在的数学问题，可能加速研究进程，并改变数学家的工作方向，使其更专注于创新性方法。 根据社区讨论，该成果使用的是 GPT-5.6 的“Sol Pro”变体，而非更高级的“Ultra”版本，且该问题虽比最近的 CDC 证明更为小众，但仍是一项实实在在的贡献。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，研究在凸集上最小化凸函数，广泛应用于工程和机器学习。所指的 30 年空白是一个关于最小化凸 Lipschitz 函数最优时间复杂度的未解决问题，此前仅知道下界。球形域的限制并不严格，因为任何有界域都可以通过变量变换得到。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48957779">GPT-5.6 used a prompt to close a 30-year gap in convex optimization | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论指出，虽然解决的问题较为冷门，但代表了真正的进步。关于此类 AI 证明是否会使研究人员过时，或者是否会促使研究转向更高层次问题，存在争论。一些用户注意到所使用的模型变体（Sol Pro 与 Ultra），并讨论了其对数学研究和软件开发的启示。

**标签**: `#AI`, `#convex optimization`, `#mathematics`, `#breakthrough`

---

<a id="item-2"></a>
## [LG 显示器通过 Windows Update 静默安装软件，未经用户同意](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

当连接到 Windows PC 时，LG 显示器会自动通过 Windows Update 安装软件（包括 McAfee 试用版），且未经用户同意。用户发现并报告了这一行为，引发了严重的隐私和安全担忧。 这个问题将合法硬件变成了安装不需要软件的途径，类似恶意软件行为。它可能影响数百万 LG 显示器用户，并暴露了 Windows 设备元数据交付系统的更大漏洞。 软件在显示器通过 HDMI 插入时立即安装，随系统启动运行，具有完全的系统访问权限和网络访问权限，且无需用户交互。用户发现可通过组策略或设备安装设置禁用自动下载制造商应用的变通方法。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 自动提供驱动程序和固件以确保硬件兼容性。但它也可以通过设备元数据安装来自硬件供应商的额外软件，这一功能依赖于微软对供应商的信任。这次事件表明，LG 滥用了这种信任，未经用户同意推送促销软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://windowsforum.com/threads/lg-monitor-app-installer-pushes-mcafee-ads-on-windows-11.439030/">LG Monitor App Installer Pushes McAfee Ads on... | Windows Forum</a></li>
<li><a href="https://support.microsoft.com/en-us/windows/update-drivers-through-device-manager-in-windows-ec62f46c-ff14-c91d-eead-d7126dc1f7b6">Update drivers through Device Manager in Windows - Microsoft...</a></li>

</ul>
</details>

**社区讨论**: 社区高度关注，许多用户将此行为比作恶意软件。用户提供了详细的变通方法，并争论责任是否完全在于 LG，还是微软也应对允许此类安装负责。一些人强调这是 Windows 系统性的安全问题，类似于过去的自动运行漏洞。

**标签**: `#security`, `#privacy`, `#windows-update`, `#lg`, `#malware`

---

<a id="item-3"></a>
## [中国 Kimi K3 模型通过蒸馏对标前沿模型](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

中国开发的 Kimi K3 模型通过模型蒸馏技术，在性能上达到了与 ChatGPT 5.6 和 Opus 4.8 等前沿模型相当的水平，拥有 2.8 万亿参数，定价为每百万 tokens 输入 3 美元、输出 15 美元。 这表明蒸馏技术能使后来者迅速赶超前沿实验室，挑战美国在人工智能领域的领先地位，并引发关于开放权重模型扩散的国家安全担忧。 Kimi K3 拥有 2.8 万亿参数，定价上与 ChatGPT 5.6 Sol（5 美元/30 美元）和 Opus 4.8（5 美元/25 美元）相比具有竞争力，但社区测试显示它在 19 美元的计划下执行单个任务消耗了近 5 小时的使用时间。

hackernews · sbochins · 7月18日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**背景**: 模型蒸馏从大型“教师”模型向小型“学生”模型传递知识，实现高效部署。开放权重模型公开训练参数，使更多人能使用。前沿模型指当前最强大的人工智能系统，通常需要大量算力和数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.datacamp.com/blog/frontier-models">Frontier Models Explained: What Defines the Cutting Edge of AI</a></li>

</ul>
</details>

**社区讨论**: 评论者 nickysielicki 认为蒸馏不可避免且不是“攻击”，montroser 警告可能像 Napster 时代那样进行国家安全打击。credit\_guy 指出参数数量和定价相当，SwellJoe 则报告了实际使用中运行时间很长。

**标签**: `#AI`, `#open-source`, `#model distillation`, `#national security`, `#frontier models`

---

<a id="item-4"></a>
## [美国拟设类似 FINRA 的 AI 监管机构](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 9.0/10

特朗普政府正考虑建立一个类似于 FINRA 的独立 AI 监管机构，负责审查顶尖 AI 模型的安全性。该提案由财政部长斯科特·贝森特牵头，白宫幕僚长苏茜·威尔斯正在审阅。 这标志着 AI 治理的重大转变，提议建立一个自我监管组织，以平衡华尔街的安全担忧和硅谷的创新利益。这可能为美国如何监管先进 AI 树立先例，并可能影响全球标准。 拟议的机构将向 SEC 汇报，类似于 FINRA 与证券监管机构的关系。值得注意的是，Anthropic 和 OpenAI 此前曾对政府要求修改或限制其最新模型表示异议，凸显了行业紧张局势。

telegram · zaihuapd · 7月18日 05:45

**背景**: FINRA（金融业监管局）是一个私营的自我监管组织，在 SEC 的监督下监管经纪公司和交易所市场。拟议的 AI 监管机构将采用类似模式，由行业资助，对先进 AI 模型进行安全审查。这一做法与 Google DeepMind CEO 德米斯·哈萨比斯的建议方向一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FINRA">FINRA</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#policy`, `#Trump administration`, `#FINRA`, `#model safety`

---

<a id="item-5"></a>
## [Fable 5 对阵 GPT-5.6 Sol：NP 难问题上的/goal 指令效果评估](https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/) ⭐️ 8.0/10

Charles Azam 的一篇博客文章评估了在 NP 难问题上使用/goal 指令是否能提升 Fable 5（Anthropic）和 GPT-5.6 Sol（OpenAI）的性能。结果表明/goal 只能提供边际收益，且效果依赖于搜索策略；Ultra 模式可能更有效。 这项对比突出了领先 AI 模型在解决 NP 难问题（对优化任务至关重要）上的实际差异。研究结果也为提示工程策略提供了参考，表明像/goal 这样的简单指令相比更复杂的代理方法效果有限。 该博客使用特定的 NP 难问题进行基准测试，衡量成功率和解决方案质量。GPT-5.6 Sol 拥有 1.05M 上下文窗口和 128k 输出令牌，而 Fable 5 是 Anthropic 在 FrontierBench 编程评测中得分最高的模型。/goal 指令是一种设定明确目标的提示技术。

hackernews · couAUIA · 7月18日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=48956879)

**背景**: NP 难问题在计算上难以处理，通常需要启发式或基于搜索的方法。现代大型语言模型（如 GPT-5.6 Sol 和 Fable 5）可用于生成解决这类问题的代码或策略。/goal 指令是一种简单的提示添加，旨在聚焦模型行为；然而，更高级的方法（如 Ultra 模式，使用多个并行代理并进行对抗性审查）可能效果更好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://simtheory.ai/model-card/gpt-5.6-sol/">GPT - 5 . 6 Sol - AI Model Details | Simtheory</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Anthropic 的 Claude（Fable 5）在编码任务上正落后于 OpenAI 的 Codex，用户抱怨速度慢且问题解决能力不足。还有人认为/goal 在短会话中可能有帮助，但在长会话中效果不佳，并且 GPT 模型在 AtCoder Heuristics 等竞赛中的表现表明它们天生更擅长优化问题。

**标签**: `#AI comparison`, `#LLM evaluation`, `#NP-hard problem`, `#coding assistant`, `#goal directive`

---

<a id="item-6"></a>
## [Stack Overflow 衰落：AI 影响与社区壁垒](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

来自 Stack Exchange Data Explorer 的图表显示 Stack Overflow 活动显著下降，这被归因于 ChatGPT 等 AI 工具的兴起以及网站自身的 restrictive 社区政策。 这一趋势凸显了 AI 驱动的替代方案和不良的社区治理如何侵蚀一个曾经占主导地位的平台，影响依赖 Stack Overflow 寻求帮助的数百万开发者。 该图表显示活动下降，尤其是在 2021 年被 Prosus 收购和 2022 年底 ChatGPT 发布之后，一些用户报告在尝试访问数据时遇到速率限制。

hackernews · secretslol · 7月18日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=48956949)

**背景**: Stack Overflow 是一个面向程序员的问答平台，用户在此提出和回答技术问题。其严格的审核和踩文化为新手设置了高门槛，而 ChatGPT 等 AI 工具提供了无需社交摩擦的直接答案。

**社区讨论**: 评论者普遍认为 Stack Overflow 的严格政策和缺乏社区感驱走了用户，有人指出该网站因不鼓励对话而&\#x27;自掘坟墓&\#x27;。对 Prosus 的收购也被视为一个转折点。

**标签**: `#Stack Overflow`, `#AI impact`, `#community decline`, `#software engineering`

---

<a id="item-7"></a>
## [PHK 发表告别文，反思自行车棚效应](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

Poul-Henning Kamp \(PHK\) 在 ACM Queue 上发表了一篇题为《再见，感谢所有的自行车棚》的反思文章，重新审视了他于 1999 年提出的自行车棚现象。 这篇文章重新激发了关于软件工程中一个基本反模式的讨论，提醒团队优先处理重要决策而非琐事，从而提升项目效率。 PHK 最初用自行车棚隐喻来解释人们为何会在诸如车棚颜色等琐碎问题上花费过多时间，而忽略复杂的技术决策；本文以告别作形式呈现。

hackernews · Ygg2 · 7月18日 17:27 · [社区讨论](https://news.ycombinator.com/item?id=48960155)

**背景**: 自行车棚，又称琐事定律，描述了人们对琐碎问题给予不成比例关注的现象。PHK 在 1999 年的 FreeBSD FAQ 中引入了该术语。这一概念在软件工程中被广泛用于警示注意力分配不当。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Law_of_triviality">Law of triviality - Wikipedia</a></li>
<li><a href="https://fourweekmba.com/bikeshedding/">What Is Bikeshedding And Why It Matters In Business - FourWeekMBA</a></li>

</ul>
</details>

**社区讨论**: 评论者对这篇文章表示赞赏，一些人强调了可逆决策概念作为解决自行车棚效应的方法。其他人提到了 PHK 的贡献如 MD5crypt。还出现了关于年龄限制和科技领域性别问题的旁支讨论。

**标签**: `#software engineering`, `#bikeshedding`, `#project management`, `#community`

---

<a id="item-8"></a>
## [Anthropic 将 Claude Fable 5 永久纳入订阅计划](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic 宣布自 7 月 20 日起，Claude Fable 5 将永久纳入 Max 和 Team Premium 计划，使用限制为 50%，这一决定推翻了此前因 GPT-5.6 Sol 和 Kimi 3 的竞争压力而将模型从订阅中移除的计划。 此举确保订阅用户继续使用 Anthropic 的最佳模型，使订阅计划在与 OpenAI 和 Kimi 的竞争中保持竞争力，并缓解了用户对失去顶级 AI 能力访问权限的担忧。 每月 20 美元的订阅计划仍不包含 Fable 5；只有 Max（每月 100/200 美元）和 Team Premium 订阅用户受益。Pro 和 Team Standard 用户可获得一次性 100 美元积分，并通过使用额度访问 Fable。

rss · Simon Willison · 7月18日 06:00

**背景**: Claude Fable 5 是 Anthropic 旗下的 Mythos 级大型语言模型，擅长编程和自主任务。由于计算容量限制，该模型最初计划从订阅中移除，但 OpenAI 的 GPT-5.6 Sol（在基准测试中优于 Fable 5）和 Kimi 3 等竞品的推出迫使 Anthropic 改变了策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#Fable 5`, `#GPT-5.6`

---

<a id="item-9"></a>
## [指控：DeepMind/Kaggle 大奖颁给无意义的 AI 提交](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

一位 Reddit 用户声称，由 Google DeepMind 赞助的 Kaggle 竞赛&\#x27;衡量向 AGI 进展&\#x27;的获奖提交（获得 25,000 美元大奖）内容不连贯、结构糟糕，该用户基于对论文、方法论、代码和数据的详细审查提出了这一指控。 这一指控引发了关于高知名度 AI 竞赛评估标准诚信性的严重质疑，尤其是由 DeepMind 等领先组织赞助的竞赛，可能削弱对社区驱动基准开发的信任。 该提交涉及向 LLM 呈现其他 LLM 关于某个棘手情况的五个主张的替代观点，但用户描述最终的论文是&\#x27;氛围感的意大利面条堆&\#x27;，篇幅是规定格式的十倍，且没有明显的严谨分析。

reddit · r/MachineLearning · /u/TheWerkmeister · 7月18日 15:10

**背景**: Kaggle 竞赛是知名平台，数据科学家和机器学习从业者在此竞争解决问题，通常由大型科技公司赞助。&\#x27;衡量向 AGI 进展&\#x27;竞赛特别要求参与者设计基于认知科学的新型 AI 基准。此事件凸显了评估主观或创造性提交的挑战，因为严谨性难以量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/googledeepmind_how-do-we-measure-progress-toward-agi-it-activity-7439782084551806976-0e2M">How do we measure progress toward AGI ? It takes a village – and...</a></li>
<li><a href="https://www.mindstudio.ai/blog/google-agi-benchmark-10-cognitive-dimensions">How Google&#x27;s New AGI Benchmark Measures Intelligence Across 10 Cognitive Dimensions | MindStudio</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子引发了讨论，一些评论支持用户的分析并质疑评委的监督，而另一些则支持组织者的立场，认为审查得当、结果是主观的。讨论反映了对 AI 研究竞赛中可重复性和质量控制的广泛担忧。

**标签**: `#AI ethics`, `#Kaggle`, `#DeepMind`, `#research integrity`, `#LLM evaluation`

---

<a id="item-10"></a>
## [Meta 计划向 Anthropic 出租 AI 算力，潜在交易达百亿美元](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta 正与 AI 初创公司 Anthropic 谈判，计划将其 AI 数据中心算力出租给后者，潜在交易规模达 100 亿美元，为期两年。Anthropic 于 2026 年 6 月提出该方案，Meta 正在评估中。 这笔交易凸显了 AI 算力的极度稀缺性，可能为 Meta 开辟新的收入来源，同时验证其大规模数据中心投资的合理性。这也反映了大型科技公司向 AI 初创企业出租闲置算力的趋势日益增长。 如果最终达成协议，Anthropic 将按月向 Meta 付款，双方均有权提前退出。谈判仍处于早期阶段，不一定能达成交易；Meta 今年计划投入高达 1450 亿美元，其中大部分用于 AI 和数据中心建设。

telegram · zaihuapd · 7月18日 01:14

**背景**: AI 算力（即 &\#x27;compute&\#x27;）已成为训练和运行大型语言模型的关键且稀缺的资源。Meta、微软、谷歌等大型科技公司正投入数十亿美元建设数据中心，而出租闲置算力已成为一种抵消成本并满足市场需求的方式。

**标签**: `#AI`, `#cloud computing`, `#Meta`, `#Anthropic`, `#data centers`

---

<a id="item-11"></a>
## [SpaceX 与五角大楼谈判 AI 算力交易](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX 正与美国国防部谈判，拟提供用于运行人工智能模型的数据中心算力，交易金额可能高达数十亿美元。 这笔交易凸显了 AI 基础设施对国家安全的重要性，并可能显著扩大 SpaceX 在国防领域的作用，影响云计算市场格局。 谈判仍在进行中，存在破裂可能。五角大楼近期已批准 SpaceX 与亚马逊、谷歌、微软和甲骨文等公司在机密环境中使用 AI 模型。此外，SpaceX 近月还与 Anthropic 和谷歌签署了类似的算力供应协议。

telegram · zaihuapd · 7月18日 01:44

**背景**: 五角大楼正加速获取云计算能力，以支持国安部门及日常作战中的 AI 应用。SpaceX 近期也在扩展其云计算业务，不仅限于卫星发射，此次谈判标志着其可能成为国防云市场的重要参与者。

**标签**: `#SpaceX`, `#AI算力`, `#五角大楼`, `#国家安全`, `#云计算`

---

<a id="item-12"></a>
## [OpenRouter 被传收购，估值超 13 亿美元](https://www.theinformation.com/articles/startup-openrouter-fields-multi-billion-dollar-takeover-interest) ⭐️ 8.0/10

AI 模型路由平台 OpenRouter 据报道已吸引多家大型科技公司的收购兴趣，估值超过 13 亿美元。 这一潜在收购案标志着 AI 基础设施领域的重大整合，并验证了模型路由市场的重要性，该市场对于优化 AI 模型使用至关重要。 OpenRouter 路由超过 400 个模型，服务约 800 万用户，每月处理约 100 万亿 token，到 2026 年初年化收入约 5000 万美元。

telegram · zaihuapd · 7月18日 03:45

**背景**: OpenRouter 是一个 AI 模型路由平台，充当中介角色，将用户查询导向最适合的 AI 模型，以优化成本、速度或质量。Token 是 AI 模型处理文本的基本单位，一个 token 大约相当于 4 个英文字符。该平台处理海量 token，表明其使用量巨大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.augmentcode.com/tools/model-routing-platforms-ai-agent-systems">5 Best Model Routing Platforms for AI Agent Systems | Augment Code</a></li>
<li><a href="https://www.braintrust.dev/articles/best-llm-routers-2026">Best LLM routers and model routing platforms in 2026 - Articles - Braintrust</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens? The Language and Currency Powering Modern AI | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#acquisition`, `#model routing`, `#OpenRouter`, `#venture capital`

---

<a id="item-13"></a>
## [台积电 A14 制程良率性能接近 90%，进度超前](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 8.0/10

台积电在财报电话会上宣布，其 A14（1.4 纳米级）制程的器件性能已达到目标水平约 90%，256 Mb SRAM 良率也接近 90%，而 4 月份这两项数据分别为 85%以上和 80%以上。CEO 魏哲家透露，智能手机、AI 和高性能计算客户兴趣强烈，新设计流片进度快于计划。 这一里程碑证明了台积电在先进半导体制造领域的领先地位，A14 预计相比 N2 可提升 10%至 15%的性能或降低 25%至 30%的功耗。该进展可能加速 1.4nm 技术在 AI 加速器、高端智能手机和 HPC 芯片中的应用，有望改变行业路线图。 A14 计划于 2028 年下半年量产，目前进度大幅领先同期 N2。该制程采用第二代 GAA 纳米片晶体管，可沿用 N2 积累的经验，逻辑晶体管密度提升 23%。

telegram · zaihuapd · 7月18日 05:00

**背景**: GAA（全环绕栅极）纳米片晶体管是 FinFET 技术的接班人，能在先进节点提供更好的静电控制和更低的漏电流。台积电的 A14 是 1.4 纳米级制程，代表其继即将量产的 N2（2 纳米）节点之后的下一步。早期阶段的高良率和性能表明工艺成熟度较高，这对经济高效的量产至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://community.aijishu.com/a/1060000000394639">FinFET接班人，详解 GAA ...</a></li>
<li><a href="https://www.163.com/dy/article/I1FRKMC90511CPMT.html">FinFET接班人，详解 GAA 的机遇和挑战|栅极|电容|fet...</a></li>
<li><a href="https://mp.ofweek.com/ee/a256714604647">每片晶圆30万元也照买！ 苹果抢占 1 . 4 纳 米 制 程 深层布局曝光 - 维科号V</a></li>

</ul>
</details>

**标签**: `#半导体`, `#台积电`, `#先进制程`, `#A14`, `#良率`

---

<a id="item-14"></a>
## [B 站展示开源 AI 伙伴 Project N.E.K.O.](https://finance.sina.com.cn/roll/2026-07-18/doc-iniifanf8394663.shtml) ⭐️ 8.0/10

在 2026 年上海世界人工智能大会上，哔哩哔哩展示了“猫娘计划”（Project N.E.K.O.），这是一个开源的主动式全模态 AI 伙伴，能通过屏幕捕获理解桌面内容并主动发起对话。 该项目展示了开源 AI 伙伴的重大进展，结合了多模态感知、本地处理以保护隐私以及主动对话能力，GitHub 超过 1,000 星标和 Steam 超过 10,000 用户表明社区兴趣浓厚。 Project N.E.K.O.支持 Live2D 和 VRM 角色引擎、通过 VoiceClone 进行声线克隆，并采用 UI、AI 大脑与记忆系统分离的架构，用户可将核心数据完全保留在本地。

telegram · zaihuapd · 7月18日 06:45

**背景**: Live2D 是一种从静态图像创建 2D 动画的技术，常用于虚拟角色。VRM 是一种为 VR 应用设计的标准化 3D 化身文件格式。VoiceClone 指基于 AI 的声音克隆，能从短音频样本中复制人的声音。这些技术共同实现了个性化、交互式 AI 伙伴的创建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=GJiYwbz1xd0">Live 2 D Body Angles Tutorial for Beginners - YouTube</a></li>
<li><a href="https://vrm.dev/en/">3D humanoid avatar file format for VR | VRM</a></li>
<li><a href="https://voicecloneai.app/blog/how-ai-voice-cloning-works">How AI Voice Cloning Works: A Complete Guide... | VoiceClone AI</a></li>

</ul>
</details>

**标签**: `#AI companion`, `#open-source`, `#multi-modal`, `#voice cloning`, `#community-driven`

---