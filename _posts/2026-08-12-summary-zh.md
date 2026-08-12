---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 38 条内容中筛选出 25 条重要资讯。

---

1. [Qwen3.8-2.4T-A95B：2.4 万亿参数的 MoE 模型，性能接近前沿水平](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Pro 0813 正式版发布](#item-2) ⭐️ 8.0/10
3. [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](#item-3) ⭐️ 8.0/10
4. [xAI 发布 Grok 4.6，引发 API 系统提示与竞争格局讨论](#item-4) ⭐️ 8.0/10
5. [AI 可能正在淘汰中层软件工程师岗位](#item-5) ⭐️ 8.0/10
6. [车牌读取器搜索应需搜查令](#item-6) ⭐️ 8.0/10
7. [高尔斯探讨大型语言模型擅长何种数学问题](#item-7) ⭐️ 8.0/10
8. [自然语言文本不存在无损转换](#item-8) ⭐️ 8.0/10
9. [Adam 破坏旋转不变性，在因子化模型中丢失 GD 的低秩偏置](#item-9) ⭐️ 8.0/10
10. [LTX-2.5 开源视频模型发布，单张 RTX 5090 即可本地运行](#item-10) ⭐️ 8.0/10
11. [腾讯 Q2 营收 2048 亿超预期，AI 资本开支激增致自由现金流转负](#item-11) ⭐️ 8.0/10
12. [微信发布资源效率优先的 WeLM 大语言模型家族](#item-12) ⭐️ 8.0/10
13. [为什么 Chrome 中微缩 JPEG 看起来不一样](#item-13) ⭐️ 7.0/10
14. [uBlock Origin 放弃屏蔽 Facebook 广告，称军备竞赛不断升级](#item-14) ⭐️ 7.0/10
15. [Grok 4.6 在 Artificial Analysis 智能指数上获得 61 分](#item-15) ⭐️ 7.0/10
16. [工程师警告：AI 生成的代码可能复杂到无人能懂](#item-16) ⭐️ 7.0/10
17. [新网站按旅行体验而非 CORE 评级给 CS 会议排名](#item-17) ⭐️ 7.0/10
18. [Zed 推出多人编码环境 Delta，支持与 AI 智能体协作](#item-18) ⭐️ 6.0/10
19. [2026 年日食网络摄像头：冰岛与西班牙实时直播](#item-19) ⭐️ 6.0/10
20. [AmigaDOS 开发者 Tim King 逝世](#item-20) ⭐️ 6.0/10
21. [微软据报拟将 Windows OEM 授权费上调 7%至 10%](#item-21) ⭐️ 6.0/10
22. [马斯克：未来所有特斯拉将搭载星链，Cybercab 率先集成天线](#item-22) ⭐️ 6.0/10
23. [Codex 活跃用户突破 1000 万，Tibo 预告明日惊喜](#item-23) ⭐️ 6.0/10
24. [ChatGPT 测试$20 套餐用户付费$8 重置用量](#item-24) ⭐️ 6.0/10
25. [企业级 SSD 占 NAND 出货量 48% 长江存储首进前三](#item-25) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B：2.4 万亿参数的 MoE 模型，性能接近前沿水平](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个混合专家（MoE）语言模型，总参数 2.4 万亿，激活参数 950 亿。该开源权重在 Hugging Face 上提供 BF16 和 FP8 版本，模型卡声称性能介于 Opus 和 Fable 之间。 此次发布将开源 MoE 模型推向了新的规模，直接挑战 Kimi k3 和 DeepSeek V4 等专有模型。相对较小的激活参数（950 亿）使得经过激进量化后可以在高端消费硬件上部署，这标志着超大规模稀疏模型的趋势。 该模型的原生上下文长度为 262,144 个 token，可扩展至 1,010,000 个 token，但开源权重版本不支持视觉输入和 1M 上下文。目前只提供 BF16 和 FP8 版本；没有针对 4 位量化的量化感知训练，因此社区量化（如约 1.3TB）需要额外的校准数据。许可证允许内部使用或年收入低于 5000 万美元的公司免费使用。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）是一种神经网络架构，每个 token 只激活一部分参数，从而使模型规模扩展到万亿参数的同时保持推理计算可控。在 MoE 模型中，总参数指加载到内存中的所有专家，而激活参数是每个 token 实际使用的少数参数，这就是为什么一个 2.4 万亿参数、950 亿激活参数的模型在激进量化后可以运行在单个 GPU 上。量化可以减小模型体积和内存占用，但可能降低质量；FP8 在当代加速器上支持广泛，而像 INT4 这样更低的位宽通常需要量化感知训练以避免精度损失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>
<li><a href="https://rcrtech.com/semiconductor-news/llms-quantization-fp8-fp4-int8/">LLMs and quantization: FP8, FP4, and INT8 explained</a></li>

</ul>
</details>

**社区讨论**: 评论者对该模型的性能声明印象深刻，但也指出了服务部署的挑战：模型比 Kimi k3 更大，发布时仅有 BF16 和 FP8 版本，且缺少量化感知训练意味着有效的 4 位量化需要大量算力和校准数据。一些评论者强调 1 位量化版本（397GB）可以在消费级硬件上达到 Opus 4.5 级别的性能，而其他人则开玩笑说要在 Intel N100 上运行它。还有人对于开源版本缺少官方 Qwen3.8-Max 的视觉输入和 1M 上下文表示失望。

**标签**: `#AI`, `#LLM`, `#Qwen`, `#MoE`, `#Machine Learning`

---

<a id="item-2"></a>
## [DeepSeek V4 Pro 0813 正式版发布](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek V4 Pro（版本号 0813）的生产版本，结束了近四个月的预览期。该模型现已在 OpenRouter 上线，并新增对 Responses API 格式的支持，版本号变更为 DeepSeek-V4-Pro-0813。 这次发布让开发者能够以极低的成本使用旗舰级开源权重模型，延续了 DeepSeek 以低价挑战西方竞品的模式。社区的大量讨论和实际测试结果表明，它可能成为对成本敏感的开发任务的首选方案。 DeepSeek V4 Pro 0813 是一个大规模混合专家（MoE）模型，拥有 1,048,576 token 的上下文窗口和 384,000 token 的最大输出长度。其定价为每百万输入 token 0.435 美元、每百万输出 token 0.87 美元；这是经过约四个月预览后的正式可用（GA）版本。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家中国人工智能公司，由梁文锋于 2023 年创立，并由对冲基金 High-Flyer 资助。该公司以极低的训练和推理成本发布开源权重的大型语言模型而闻名，例如 DeepSeek-R1 和 DeepSeek-V3——据报道后者的训练成本仅约 600 万美元，远低于 OpenAI 或 Meta 的同类模型。这些模型通常采用混合专家（MoE）等技术构建，并在出口受限的 AI 芯片上训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些用户称赞该模型的性价比并迫切希望尝试，而一位开发者报告称 DeepSeek V4 Pro 耗时 12 分钟、花费 0.12 美元但产出有 bug，相比之下 Grok 4.6 用时 3 分 18 秒、花费 1.41 美元且无 bug。另一位评论者批评新闻链接指向 OpenRouter 而不是官方文档或基准测试，还有用户提到测试输出中的渲染问题。

**标签**: `#DeepSeek`, `#AI Models`, `#LLM`, `#Cost Efficiency`, `#Hacker News`

---

<a id="item-3"></a>
## [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 发布了一份事后分析，指出其控制平面反复出现的数据库损坏是由一个 16 年前的 SQLite WAL 重置竞态条件导致的。该公司资助了一个开源的 SQLite VFS 垫片，帮助隔离了该错误，SQLite 团队在调查过程中还发现了第二个过时表达式索引错误。 这个错误在十多年间躲过了 SQLite 以广泛测试著称的测试套件，凸显了即使是最经受过考验的数据库代码中，也可能会隐藏着多么微妙的并发错误。Tailscale 的做法也展示了公司如何资助有针对性的开源调试工具，让更广泛的社区也能复用。 该错误只会在多个并发连接访问 WAL 模式数据库时发生，尽管 Tailscale 采用的是单写入者设计。VFS 垫片与录制回放调试功能相结合，帮助复现并追踪了竞态条件，最终定位到 WAL 索引结构。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 是一款嵌入式关系数据库，支持预写式日志（WAL），这种协议通过允许多个读取者与单个写入者并发来提高并发性。在 WAL 模式下，共享的 WAL 索引文件协调各数据库连接之间的事务，而重置阶段的一个竞态条件可能在特定时序下损坏该索引。Tailscale 资助了一个开源的 SQLite VFS 垫片——一个拦截文件操作的层——以帮助复现和隔离该错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug: A Data Corruption Race That Hid for 15...</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，评论者称赞 Tailscale 资助开源调试并撰写了详细的事后分析。一些人强调了这种新颖的资助模式，另一些人则好奇为什么单写入者设计仍然会遇到数据竞态；还有少数人指出支持 SQLite 持续维护的价值。

**标签**: `#sqlite`, `#database`, `#debugging`, `#tailscale`, `#open-source`

---

<a id="item-4"></a>
## [xAI 发布 Grok 4.6，引发 API 系统提示与竞争格局讨论](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI 宣布了 Grok 4.6，这是对其前沿聊天机器人模型的一次增量更新，已通过 API 和 Cursor 订阅提供。该发布立即在 Hacker News 上引发广泛讨论，特别是关于 API 添加默认系统提示符并覆盖用户指令的问题。 此次发布凸显了 xAI 作为重要前沿模型竞争对手的日益增长的地位，可能为 OpenAI 和 Anthropic 提供高性价比的替代方案。围绕系统提示行为的激烈争论也凸显了行业对用户控制、透明度以及基准测试达成方式的普遍担忧。 用户报告称，xAI API 会在每个请求中附加默认系统提示符，其中“不得提及这些指南”的指令可能覆盖用户提供的系统提示，导致模型拒绝回答。社区对比认为，Grok 4.6 在速度、简洁性和价格方面与 GPT-5.6-Sol 和 Kimi K3 等模型相比具有竞争力。

hackernews · iLuddite · 8月12日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=49274027)

**背景**: Grok 是 xAI 开发的 AI 聊天机器人，基于大型语言模型构建，旨在与 OpenAI 的 GPT 和 Google 的 Gemini 竞争。系统提示符是 LLM 中预定义的指令，用于指导模型行为并优先于用户输入，因此其设计和执行方式成为关键的治理问题。Grok 4.6 的 API 系统提示争议反映了供应商控制与用户自主权之间的广泛矛盾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_%28chatbot%29">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://x.ai/">SpaceXAI — Creators of Grok, the AI Chatbot</a></li>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：一些人称赞 Grok 4.6 的速度、简洁性和定价，另一些人则对 API 默认系统提示覆盖用户指令表示担忧。一些怀疑者质疑各实验室快速取得的基准提升是否真实，还是源于知识蒸馏或基准测试作弊；也有人认为尽管 Grok 评价两极分化，它构成了健康的竞争。

**标签**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#model release`

---

<a id="item-5"></a>
## [AI 可能正在淘汰中层软件工程师岗位](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

Florian Herrengt 发表博客文章，认为 AI 编码工具正在通过自动化常规编码任务来淘汰中层软件工程工作，同时放大强工程师和弱工程师的生产力。该文章引发了广泛讨论，共有 584 条评论，争论这一趋势对职业的影响。 这一点很重要，因为它反映了一种日益增长的看法，即 AI 助手正在重塑软件工程就业市场，可能压缩职业阶梯并改变工程团队的组织方式。如果属实，它可能影响招聘实践、薪资水平以及开发者保持竞争力所需的技能。 核心观点是 AI 正在‘移除软件工程的中产阶层’——不是消除所有岗位，而是减少对主要实现定义明确任务的开发者的需求。评论者指出，这可能导致‘糟糕的’工程师放大其糟糕的产出，并减少通过 Jira 工单进行的传统高级工程师到初级工程师的交接需求。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994)

**背景**: 软件工程通常被视为一个拥有庞大中层梯队的领域：高级工程师设计系统并将工作拆分为工单，中层和初级工程师编写代码并解决孤立问题，通常依赖搜索引擎和 Stack Overflow 等问答网站。如今，GitHub Copilot 和 ChatGPT 等 AI 编码助手可以根据自然语言提示生成样板代码、修复常见错误，甚至实现小功能。该博客文章认为，这种自动化正在使中层岗位变得多余，只在一端留下高技能架构师，另一端留下低成本或提示驱动的工人。这场辩论是更大范围讨论的一部分，即生成式 AI 将如何改变知识工作和科技行业的就业未来。

**社区讨论**: 评论者的观点既有赞同也有怀疑。一些人同意 AI 可能放大不投入的‘糟糕’工程师的负面影响，而另一些人质疑目前是否已有确凿的岗位流失证据。有评论者将这一趋势重新解读为‘Stack Overflow 工程师的自动化’，认为高级工程师将直接处理工作，而不是交接给初级工程师。还有多人强调不要将批判性思维外包给 LLM，以及继续学习基础知识的重要性。

**标签**: `#AI`, `#Software Engineering`, `#Future of Work`, `#LLMs`, `#Tech Industry`

---

<a id="item-6"></a>
## [车牌读取器搜索应需搜查令](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/) ⭐️ 8.0/10

一篇观点文章主张，对自动车牌识别器（ALPR）数据的搜索应获得搜查令，引发了关于大规模监控和警方问责制的讨论。 这一点很重要，因为 ALPR 能对车辆进行持续的位置追踪，而要求搜查令将对这个强大的监控工具施加司法监督。这场讨论可能影响城市和警察部门如何处理 ALPR 数据，以及是否采用新的隐私保护技术。 ALPR 设备本质上是可以重新编程的通用联网摄像头，不仅限于读取车牌，而且已有警察滥用存储位置数据的案例。评论者还提出了零知识证明和同态加密等加密方法，以便在不泄露位置历史的情况下进行验证。

hackernews · apwheele · 8月12日 14:43 · [社区讨论](https://news.ycombinator.com/item?id=49273165)

**背景**: 自动车牌识别器（ALPR）是能够捕获车牌和位置的摄像头，通常安装在巡逻车或固定杆上，数据可存储多年。隐私倡导者认为这实现了大规模监控，而执法部门声称这有助于破案。在没有搜查令的情况下，警方通常可以自由搜索这些数据；一些司法管辖区将其视为公共记录，适用信息自由法（FOIL）。零知识证明和同态加密等加密技术是更广泛的努力的一部分，目的是在不暴露个人行踪的情况下让这些数据可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sls.eff.org/technologies/automated-license-plate-readers-alprs">Automated License Plate Readers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论对 ALPR 表达了强烈的不信任，有评论指出它们是通用摄像头，可能被纳入大规模监控网络。一位读者提出了一种密码学系统，让车牌显示由车管所签发的私钥派生的滚动数字，以防被追踪。其他人则认为，如果大规模监控本身就是问题，那么仅凭搜查令要求是不够的；还有评论者批评文章对公共空间摄像头不可避免性的悲观论调。

**标签**: `#privacy`, `#surveillance`, `#law-enforcement`, `#cryptography`, `#public-policy`

---

<a id="item-7"></a>
## [高尔斯探讨大型语言模型擅长何种数学问题](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

在一篇新博客文章中，数学家蒂莫西·高尔斯（Timothy Gowers）探讨了大型语言模型（LLM）究竟能解决哪些类型的数学问题，并将其优势与采样（sampling）和测试时扩展（test-time scaling）联系起来。他还质疑 LLM 何时能产出真正新颖、优雅的证明，而不仅仅是在庞大的可能性空间中进行搜索。 由于高尔斯是菲尔兹奖得主和著名数学家，他的分析在人工智能和数学界都具有分量。他对测试时扩展和采样的关注，有助于厘清基于 LLM 的工具在哪些方面可靠，以及在研究型数学中可能在哪些方面存在不足。 据报道，这篇文章从未使用“测试时扩展”（test-time scaling）一词，但评论者指出其论点本质上就是围绕这一概念。一位评论者引用了谷歌的 AlphaCode：该系统生成数百万个候选程序并筛选出少量提交，在 2022 年击败了普通人类程序员，是采样驱动成功的早期例子。

hackernews · ColinWright · 8月12日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49270022)

**背景**: 测试时扩展（test-time scaling）是指在推理阶段分配额外的计算资源——例如让模型生成大量候选解或“思考”更长时间——以提升推理能力；随着预训练算力增长放缓，它已成为一个重要的研究方向。采样（sampling）是 LLM 从概率分布中选择下一个词元的过程；生成大量样本并加以筛选，可以显著提升数学和编程任务的表现。这些概念是理解 LLM 为何能处理某些数学问题、以及为何产出出人意料却又优美的证明仍然困难得多的核心所在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.24235">[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?</a></li>
<li><a href="https://testtimescaling.github.io/">What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.1278/">Balancing Diversity and Risk in LLM Sampling: How to Select ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认真参与了高尔斯的论证。有人指出，这篇文章实际上讲的是测试时扩展，并强调早期基于采样的成果（如 AlphaCode）才是第一批令人惊讶的胜利；也有人同意高尔斯的观点，认为真正达到人类水平的证明将是可识别的。还有人分享了 AI 数学成就的列表，并好奇 LLM 在处理时序逻辑或反例搜索方面会表现如何。

**标签**: `#LLMs`, `#mathematics`, `#AI research`, `#test-time scaling`, `#proofs`

---

<a id="item-8"></a>
## [自然语言文本不存在无损转换](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/) ⭐️ 8.0/10

Sophie Alpert 发布了面向工程师的 AI 辅助写作可接受使用内部政策，主张自然语言文本不存在无损转换。Simon Willison 重点推荐并认可了这一政策，称其至关重要。 该指南为负责任地在写作中使用 LLM 提供了实用、具体的原则，强调作者必须为每一句话负责。它对工程师和技术写作者尤其有参考价值，并可能影响团队关于 AI 辅助文档的规范。 核心规则是作者必须为每一个观点和句子负责，不能以“这是 AI 写的”来搪塞含糊之处。“无损转换不存在”这一观点指出，任何缺乏作者详细心智表征的 AI 改写都必然会丢失信息。

rss · Simon Willison · 8月11日 23:48

**背景**: 无损转换是数据压缩中的一个概念，指原始数据可以被完美重建。Alpert 将这一概念应用到自然语言上，认为每一次改写或重述都会改变含义，而由缺乏作者精确意图的 AI 来完成时，信息就会丢失。这一背景很重要，因为 AI 写作工具正越来越多地被工程师和技术写作者使用，因此需要明确的问责政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/">There are no lossless transformations of natural-language text</a></li>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural-language text</a></li>

</ul>
</details>

**标签**: `#AI writing`, `#LLM`, `#software engineering`, `#documentation`, `#responsibility`

---

<a id="item-9"></a>
## [Adam 破坏旋转不变性，在因子化模型中丢失 GD 的低秩偏置](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

一项 Reddit 分析表明，Adam 的逐坐标二阶矩破坏了因子化模型的旋转不变性，使其丢失了梯度下降所具有的隐式低秩偏置。在对九种更新规则的系统测试中，只有 GD、共享标量 Adam、Muon 和 Shampoo 保留了该偏置，而 Adam、RMSProp、Lion、signum 和 Adafactor 则没有。 这一发现提供了一种机制性解释，说明为何某些优化器能保留有助于深度学习泛化的低秩简单性偏置，而另一些则不能。它可能指导优化器的设计，使其保持理想的归纳偏置，尤其是在矩阵感知和深度线性网络等任务中。 该分析在匹配训练损失的欠定矩阵感知任务上测试了九种更新规则，形成了两个清晰的聚类。一个将 Adam 的分母从逐坐标插值到共享标量的单参数族表现出单调恢复，Muon 在约 4% 谱尾能量处出现令人惊讶的交叉行为；作者还发现，将他们自己优化器中的逐坐标裁剪改为全局范数裁剪后，恢复误差从 0.347 降至 0.220。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**背景**: 在因子化模型中，权重矩阵写作 W = UVᵀ，损失函数对因子的正交旋转变换具有不变性，而梯度下降尊重这一对称性。然而，Adam 的逐坐标二阶矩归一化破坏了这种不变性，从而丧失了有助于泛化的隐式低秩偏置。Muon 是一种较新的优化器，在大语言模型训练中表现强劲；Shampoo 是一种预条件张量优化器，两者都保留了这种不变性。基于梯度的方法的低秩简单性偏置是深度学习中已被广泛研究的现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2103.10427">[2103.10427] The Low-Rank Simplicity Bias in Deep Networks SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks The Low-Rank Simplicity Bias in Deep Networks - arXiv.org SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks The Low-rank Simplicity Bias in Deep Networks THE L -R SIMPLICITY BIAS IN DEEP NETWORKS - GitHub Pages</a></li>
<li><a href="https://grokipedia.com/page/muon-optimizer">Muon optimizer</a></li>
<li><a href="https://arxiv.org/abs/1802.09568">[1802.09568] Shampoo: Preconditioned Stochastic Tensor Optimization</a></li>

</ul>
</details>

**标签**: `#optimization`, `#deep learning`, `#matrix factorization`, `#Adam`, `#low-rank`

---

<a id="item-10"></a>
## [LTX-2.5 开源视频模型发布，单张 RTX 5090 即可本地运行](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX 发布了开源视频生成基础模型 LTX-2.5，开放权重、训练代码与推理管线。该模型支持文生视频与图生视频，并可在单张 RTX 5090 上本地运行。 这一发布是开源视频生成的里程碑，使高质量视频生成能在消费级硬件上本地推理，大幅降低开发者和小团队的接入门槛。年收入低于 1000 万美元可免费商用，且评测结果领先，有望加速创意与 AI 内容工作流中的采用。 LTX-2.5 采用新的扩散视频解码器和 Gemma 4 12B 文本编码器。在 98 个文生视频提示词的自动化瑕疵评测中，LTX 2.5 Pro 在十款模型中排名第一；该模型还支持一次生成多镜头场景，并可导出电影级 EXR。

telegram · zaihuapd · 8月12日 02:15

**背景**: 视频生成模型通常需要大型服务器集群，且多为闭源，限制了实验与本地使用。像 LTX-2.5 这样的开源发布为研究者和创作者提供了本地替代方案。Gemma 4 12B 是 Google DeepMind 发布的开源多模态模型，可原生处理文本、图像、音频和视频，无需独立编码器；扩散视频解码器则负责将潜变量表示转换为连贯的视频帧。所引用的评测采用自动化评分，而非人工判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX&#x27;s Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/gemma-4-12B · Hugging Face</a></li>
<li><a href="https://www.labellerr.com/blog/gemma-4-12b-run-locally-and-fine-tune/">Gemma 4 12B : Run Locally, Fine-Tune, Benchmark Performance</a></li>

</ul>
</details>

**标签**: `#video-generation`, `#open-source`, `#AI`, `#local-inference`, `#LTX`

---

<a id="item-11"></a>
## [腾讯 Q2 营收 2048 亿超预期，AI 资本开支激增致自由现金流转负](https://wallstreetcn.com/articles/3779275) ⭐️ 8.0/10

腾讯公布 Q2 营收达 2048 亿元人民币，同比增长 11%，略超彭博预期；但资本开支同比近翻三倍至 528 亿元，主要用于 AI 算力基础设施，导致自由现金流录得-138 亿元。 此举标志着腾讯战略重心转向 AI 基础设施投入而非短期现金回报，与全球大型科技公司的趋势一致。尽管营收增长强劲，但自由现金流转负反映出 AI 竞赛加剧，可能影响未来利润和投资者信心。 净利润仅增 0.7%至 560 亿元，低于市场预期。公司称剔除 AI 算力预付款后自由现金流为 376 亿元；营销服务收入同比增长 22%领跑，本土游戏增长 17%，国际游戏受汇率影响微降 0.8%。

telegram · zaihuapd · 8月12日 10:30

**背景**: 腾讯正加快布局 AI 基础设施，包括 AI 算力投入以及 AI 办公智能体 WorkBuddy 等产品，后者据称在中国桌面端 AI 办公智能体月访问量中排名第一。为抢占 AI 制高点，中国科技巨头普遍大规模投入 AI 数据中心和算力预付款，导致资本开支激增，这也是腾讯现金流变化的主要原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://workbuddy365.com.cn/">WorkBuddy官网 | AI办公智能体 腾讯出品 功能介绍</a></li>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>
<li><a href="https://xueqiu.com/1540104684/403488053">xueqiu.com/1540104684/403488053</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#Earnings`, `#AI Infrastructure`, `#Capital Expenditure`, `#Free Cash Flow`

---

<a id="item-12"></a>
## [微信发布资源效率优先的 WeLM 大语言模型家族](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 8.0/10

微信 AI 团队发布了以资源效率为核心的通用大语言模型家族 WeLM 系列。其中 WeLM-80B（3B 激活）已应用于微信 AI 智能体小微，而研发中的 WeLM-617B（23B 激活）面向微信生态中的复杂任务。 此次发布表明头部科技公司正利用 MoE 架构，以更少的激活参数实现有竞争力的性能，有望大幅降低大规模大语言模型部署的算力成本。由于 WeLM 已落地于微信 AI 智能体，这一集成将影响数亿用户，并可能推动行业加速采用类似的高效方案。 WeLM-80B 总参数量为 800 亿，但每个 token 仅激活 30 亿参数；研发中的 WeLM-617B 激活 230 亿参数。后者计划用于小程序智能开发以及微信 AI 智能体的小工具生成等场景。

telegram · zaihuapd · 8月12日 13:58

**背景**: WeLM（微信语言模型）是腾讯微信团队研发的预训练语言模型系列；2022 年初代 10B 参数模型据称可达到比它大 25 倍模型相当的性能。混合专家（MoE）是一种机器学习技术，通过路由器为每个输入选择部分专家网络，使每个 token 只激活全部参数中的一小部分，从而在保留模型容量的同时提升效率。WeLM 团队博客提到，一个 80B-A3B 的 MoE 模型在不到 14 万亿 token 上训练，就能达到与同规模及更大系统竞争的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://welm.weixin.qq.com/en/">WeLM Blog</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#WeChat`, `#AI`, `#resource efficiency`

---

<a id="item-13"></a>
## [为什么 Chrome 中微缩 JPEG 看起来不一样](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

一篇技术博客文章解释了 Chrome 之所以让微小 JPEG 显示效果不同，是因为它在解码时进行了缩小（decode-time downscaling），即在解码过程中直接缩小图像，而不是解码后再缩放。作者建议直接提供与显示尺寸匹配的图片，而不是依赖浏览器缩放。 这种细微的渲染差异会导致图片在不同浏览器中显得更模糊或更清晰，对注重视觉一致性的 Web 开发者来说很重要。它还凸显了一个更广泛的性能最佳实践：提供尺寸合适的图片可以节省带宽和解码时间。 Chrome 和 Firefox 使用不同的缩放算法，因此即使都采用解码时缩小的方法，也可能产生肉眼可见的差异。文章建议不要将 JPEG 用于图标等界面元素，开发者应使用分辨率合适的资源，而不是超大图片。

hackernews · gutechh · 8月12日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49272549)

**背景**: JPEG 是一种有损图像格式，主要适合照片；PNG 则无损且支持透明，因此常用于图标。现代浏览器在渲染管线中会解码并缩放图像，Chrome 的优化解码路径为了效率可能在解码过程中直接缩小图像。Chromium 项目通过 RenderingNG 工作记录了其渲染架构，包括图像处理相关环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/chromium/renderingng-architecture">RenderingNG architecture | Chromium | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/chromium/renderingng">RenderingNG | Chromium | Chrome for Developers</a></li>
<li><a href="https://stackoverflow.com/questions/3343090/which-is-the-fastest-decoder-for-jpeg-full-scale-decoding">c++ - Which is the fastest decoder for jpeg full- scale ... - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 PNG 也可能受影响，而且 Chrome 的这一改动曾导致 Electron 应用图标显示异常。还有人提到 Firefox 正在开发低分辨率解压支持，并指出 Chrome 与 Firefox 使用不同缩放算法，有人更偏好 Firefox 更锐利的效果。也有评论提到可用 CSS 的 image-rendering 属性作为解决办法。

**标签**: `#jpeg`, `#browser`, `#image-scaling`, `#chrome`, `#web-performance`

---

<a id="item-14"></a>
## [uBlock Origin 放弃屏蔽 Facebook 广告，称军备竞赛不断升级](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 7.0/10

uBlock Origin 已正式停止尝试屏蔽 Facebook 广告，承认该平台的反广告屏蔽措施使其在技术上难以实现。这一决定由 Neowin 报道，并在 r/uBlockOrigin 子版块中引发了讨论。 这标志着广告屏蔽军备竞赛中的一次标志性挫败，表明即使是一流的过滤列表也可能被资源雄厚的平台压垮。这会影响数百万依赖 uBlock Origin 在 Facebook 上获得隐私和更干净浏览体验的用户，并可能促使开发者转向基于 AI 的广告检测，而非传统的过滤列表。 Facebook 广告是以第一方内容的形式从同一域名提供，并动态渲染，这使得用静态过滤规则几乎无法将其与普通帖子区分开来。uBlock Origin 的维护者和社区认为，要跟上 Facebook 的反屏蔽技术所需付出的努力已不可持续。这一决定不影响 uBlock Origin 在其他网站上的广告屏蔽功能。

hackernews · Markoff · 8月12日 11:28 · [社区讨论](https://news.ycombinator.com/item?id=49270726)

**背景**: uBlock Origin 是一款免费开源浏览器扩展，拥有超过 1000 万用户，以低内存和 CPU 占用率而闻名，同时能屏蔽广告和追踪器。传统广告拦截器依赖已知广告域名的过滤列表，但 Facebook 将广告直接嵌入信息流，并通过自己的基础设施提供广告。Facebook 的帮助中心明确表示，用户无法完全屏蔽 Facebook 广告，而且平台不断更改代码以规避广告屏蔽工具。这些背景解释了为什么 uBlock Origin 的决定是不可避免的，而非令人意外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://www.facebook.com/help/146952742043748">Can you block or hide ads showing on your Facebook account | Facebook Help Center</a></li>
<li><a href="https://www.cloudwards.net/stop-ads-on-facebook/">How to Get Rid of Ads on Facebook: 8 Proven Ways for 2026</a></li>

</ul>
</details>

**社区讨论**: Reddit 评论者大多支持这一决定，认为这是在一场必败之战中的务实撤退。一位用户预测，终极广告拦截器将使用计算机视觉来检测并遮盖广告，而其他人则认为，真正唯一的逃避方式是彻底离开 Facebook。还有人指出，Facebook 广告平台的技术复杂程度已达到“令人作呕”的水平，并分享了对旧式广告替换工具的怀旧回忆。

**标签**: `#ad-blocking`, `#uBlock Origin`, `#Facebook`, `#privacy`, `#arms race`

---

<a id="item-15"></a>
## [Grok 4.6 在 Artificial Analysis 智能指数上获得 61 分](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis) ⭐️ 7.0/10

SpaceXAI 的最新模型 Grok 4.6 在 Artificial Analysis 智能指数上获得了 61 分。该模型现已通过 SpaceXAI 的 API 和 grok.com 提供，缓存读取价格为每百万 token 0.50 美元，高于 Grok 4.5 的 0.30 美元。 这一分数使 Grok 4.6 跻身前沿 AI 模型之列，社区反馈显示它已成为编码任务的日常工具，常与 Cursor 或 Grok Build 搭配使用。然而，缓存读取价格几乎翻倍，可能会影响 API 使用量较大的开发者。 Artificial Analysis 智能指数是一个综合基准，包括 GDPval-AA v2、Terminal-Bench v2.1 和 Humanity&\#x27;s Last Exam 等测试。据社区评论，在重度编码会话中，缓存读取/写入费用通常占 token 账单的 80% 左右，因此从 0.30 美元涨到 0.50 美元的影响很大。

hackernews · wertyk · 8月12日 16:54 · [社区讨论](https://news.ycombinator.com/item?id=49275385)

**背景**: Artificial Analysis 智能指数是一个综合基准，用于衡量语言模型在推理、编码、知识、指令遵循、科学推理和多步任务等方面的能力。Grok 是由 SpaceXAI（前身为 xAI）构建的 AI 助手，Grok 4.6 是该系列的最新模型，可通过专属 API 和 grok.com 使用。开发者经常参考此类指数来比较前沿模型，并决定将其集成到哪些工具中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://docs.x.ai/developers/models">Models | SpaceXAI Docs</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model &amp; API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对 Grok 4.6 在编码方面的表现持积极看法：有人说它比 Claude 更善于沟通，且比 Claude Code 更快；还有人强调 Cursor 的订阅是使用 Grok 的高性价比方式。一位用户指出缓存读取价格几乎翻倍，从 0.30 美元涨到 0.50 美元，而重度编码会话中大部分 token 账单来自缓存读取/写入。另一位评论者开玩笑说，如果这么容易达到前沿水平，这让他们看好 Gemini。

**标签**: `#AI`, `#benchmarks`, `#Grok`, `#LLM`, `#pricing`

---

<a id="item-16"></a>
## [工程师警告：AI 生成的代码可能复杂到无人能懂](https://simonwillison.net/2026/Aug/12/florian-herrengt/) ⭐️ 7.0/10

Florian Herrengt 发表博文，认为由 AI 生成的代码库可能变得极其混乱，以至于任何人甚至像 Fable 这样的 AI 都无法理解，从而可能消除对中产阶级软件工程师的需求。Simon Willison 于 2026 年 8 月 12 日在其博客上引用了这段话。 这凸显了 AI 辅助编程快速普及中的一个关键风险：代码库可能积累出难以管理的复杂性，使维护和调试越来越困难。它可能重塑软件工程岗位，尤其是传统上负责连接业务逻辑与实现的中级开发者。 这段话特别提到 Anthropic 的 AI 模型 Fable 无法修复一个反复出现的 bug，而开发者也承认不知道数据来自哪里，只能依赖 Claude 生成代码。文章的核心论点是‘认知债务’——代码虽能运行，但没有人真正理解它。

rss · Simon Willison · 8月12日 15:08

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，于 2023 年 3 月作为聊天机器人首次发布；Fable 是 Anthropic 较新的模型（与 Claude Fable 5 一同发布），在引文中被设想为调试工具。像这样的 AI 辅助编程工具可以快速生成大量代码，但如果开发者盲目信任 AI 输出而不去理解，代码库可能变得难以维护——这就是所谓的‘认知债务’。Simon Willison 是知名开发者兼博主，经常分享关于 AI 与软件工程的深刻评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#software-engineering`, `#developer-productivity`, `#future-of-work`

---

<a id="item-17"></a>
## [新网站按旅行体验而非 CORE 评级给 CS 会议排名](https://www.reddit.com/r/MachineLearning/comments/1vmbdk6/i_built_an_honest_cs_conference_ranking_sorted_by/) ⭐️ 7.0/10

一位开发者推出了 Honest CS Rankings（honestcsrankings.org）网站，该网站根据目的地质量——天气、安全、成本、可达性和城市氛围——对约 540 个即将举行的 CORE 排名会议进行排序，而非按 CORE 等级排序。该工具包含筛选器、基于常住城市的距离选项、&\#x27;爆冷&\#x27;标签、.ics 日历导出以及与合著者分享的深层链接。 该工具填补了一个实际空白：研究人员在选择投稿和参会地点时通常会考虑主办城市，即使排名是首要指标。通过让目的地吸引力变得透明且可定制，它可能影响投稿决策，提高一些被低估地点的参会率，并引发关于会议质量的更广泛讨论，而不仅仅关注排名本身。 该网站使用会议当月的真实气候数据、全球和平指数（Global Peace Index）评估安全，以及世界银行的价格水平评估成本。需要注意的例外情况：ICML/ICLR 2027 尚未公布所以未收录，COLM 因 CORE 未对其进行评级而缺失，并且从 WikiCFP 抓取的尾部小型会议数据可能存在错误。

reddit · r/MachineLearning · /u/JohnAZoidberg77 · 8月12日 11:23

**背景**: CORE（澳大利亚计算机研究教育协会）会议排名是一个广泛使用的系统，它将计算领域的会议划分为 A\*、A、B、C 等级，影响研究人员和机构对会议声望的看法。WikiCFP 是一个社区驱动的维基，汇总会议、研讨会和期刊的征稿启事，学者们常用来查找即将到来的截止日期。全球和平指数（GPI）由经济与和平研究所编制，按国家和平程度排名，可作为会议目的地安全性的参考。研究人员在参考正式排名的同时，也常常考虑主办城市的宜居性和差旅便利性，这正是该工具试图解决的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.core.edu.au/conference-portal">CORE Rankings Portal - core.edu.au</a></li>
<li><a href="http://www.wikicfp.com/">WikiCFP : Call For Papers of Conferences, Workshops and Journals</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Peace_Index">Global Peace Index</a></li>

</ul>
</details>

**标签**: `#conference rankings`, `#CS conferences`, `#travel`, `#ML community`, `#tools`

---

<a id="item-18"></a>
## [Zed 推出多人编码环境 Delta，支持与 AI 智能体协作](https://zed.dev/blog/introducing-delta) ⭐️ 6.0/10

Zed 推出了 Delta，一个面向 AI 智能体协作与代码审查的多人编码环境。该功能目前处于私有测试阶段，基于专有的实时数据库 DeltaDB，保持代码与对话线程同步。 此举表明行业正推动 AI 智能体协作变得更加交互和透明，通过让开发者查看变更背后的对话记录来解决 AI 代码质量问题。然而，社区反响不一，反映出关于多人编码是否真有实际需求、还是为不存在的问题寻找解决方案的广泛争论。 Delta 目前处于私有测试阶段，其核心功能包括：实时协作的多人在线对话，以及“对话即文档”，即在 AI 智能体的对话流中直接内联评论。该功能基于专有的实时数据库 DeltaDB，可在软件演进过程中同步代码与对话上下文。

hackernews · khy · 8月12日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49276574)

**背景**: Zed 是一款用 Rust 编写的开源高性能代码编辑器，由 Atom 联合创始人 Nathan Sobo 和 Zed Industries 开发。该编辑器一直强调多人协作编辑与 AI 辅助功能，基础使用免费，而 AI 功能需要付费。Delta 进一步拓展了这一多人协作理念，专门用于与 AI 智能体一起编码并审查其工作过程——团队不仅看到最终改动，还能查看智能体在改动过程中产生的完整对话与上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zed.dev/">Zed — Your last next editor</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zed_%28text_editor%29">Zed (text editor) - Wikipedia</a></li>
<li><a href="https://news.linxi.com.au/news/zed-launches-delta-a-multiplayer-coding-environment-for-ai-agents">Zed launches Delta multiplayer coding environment with AI ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一。一些评论者质疑多人编码的实用价值，称其是‘没有实际用途的酷技术’，并表示编码通常是一种单人活动。另一些人则对此感兴趣，尤其是能在智能体对话中内联评论的能力，这可能有助于指导初级开发者并审查 AI 生成的 PR。此外，还有部分用户批评博客页面本身的低对比度设计，称阅读体验很差。

**标签**: `#Zed`, `#code editor`, `#collaborative editing`, `#AI`, `#developer tools`

---

<a id="item-19"></a>
## [2026 年日食网络摄像头：冰岛与西班牙实时直播](https://jonty.github.io/2026_eclipse_webcams/) ⭐️ 6.0/10

一个快速搭建的网站汇总了冰岛和西班牙的实时网络摄像头画面，让观众远程观看 2026 年日全食。该网站由开发者 jonty 创建，在 Hacker News 上分享后迅速引发热议。 这个网站让任何有互联网连接的人都能不受地理位置限制地观看罕见的天文事件。它也说明了简单的工具如何围绕共同体验建立社区。 该网站是一个基础的网络摄像头聚合器，而非受控的直播流，作者 jonty 表示它在大流量下可能会崩溃。观众可以看到位于 2026 年日食全食带上的冰岛和西班牙的摄像头画面。

hackernews · zoenolan · 8月12日 11:53 · [社区讨论](https://news.ycombinator.com/item?id=49270953)

**背景**: 日全食是指月球完全遮住太阳，露出暗淡的日冕。2026 年的日全食将经过冰岛和西班牙，因此这两个地方成为实时摄像头观测的关键地点。jonty 此前也为 2024 年美国日食制作过类似的摄像头聚合页面，并在日全食开始前几分钟才完成。

**社区讨论**: 评论者们热情洋溢并分享个人经历：aljgz 描述了自己为 2024 年日食前往加拿大旅行的经历，并把日食视为人生里程碑；orsenthil 提到泰勒斯（Thales of Miletus）首次正确预测日食的历史意义。另一位评论者 alkyon 说通过双筒望远镜看到了粉色日珥，1970-01-01 则提到太阳能电池板监测数据也是一个有趣的观察视角。总体气氛积极正面，大家对这个快速上线的资源和共同的体验表示赞赏。

**标签**: `#Eclipse`, `#Webcams`, `#Astronomy`, `#Event`, `#Hacker News`

---

<a id="item-20"></a>
## [AmigaDOS 开发者 Tim King 逝世](https://amiga-news.de/en/news/AN-2026-08-00070-EN.html) ⭐️ 6.0/10

AmigaDOS（AmigaOS 的磁盘操作系统）的关键开发者之一 Tim King 已经去世。Amiga 社区的成员们正在分享对他的回忆和感激之情。 King 在 AmigaDOS 上的工作为 Amiga 系列计算机提供了动力，影响了 1980 至 1990 年代的一代程序员和创意工作者。他的离世凸显了早期个人计算先驱者的持久遗产。 AmigaDOS 基于 MetaComCo 对 TRIPOS 的移植，最初用 BCPL 编写，从 AmigaOS 2.x 开始用 C 重写。一位评论者回忆 King 是 UK Online 的创始人，讨论中还分享了一段 2021 年 10 月对他的采访。

hackernews · doener · 8月12日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49272655)

**背景**: Amiga 是 Commodore 于 1985 年推出的个人计算机系列，以其先进的图形和声音硬件而闻名。AmigaDOS 为 AmigaOS 提供了文件系统、命令行界面和磁盘管理，其命令行环境让许多用户接触到了计算基础知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AmigaDOS">AmigaDOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amiga_computer">Amiga computer</a></li>

</ul>
</details>

**社区讨论**: 评论者们分享了个人回忆和感激之情，一位用户认为 AmigaDOS 是他学习 Linux 命令行的入门工具。另一个人回忆 King 是 UK Online 友好而乐于助人的创始人，还有人发布了 2021 年采访的链接供大家了解更多。

**标签**: `#Amiga`, `#Obituary`, `#Retro Computing`, `#AmigaDOS`, `#History`

---

<a id="item-21"></a>
## [微软据报拟将 Windows OEM 授权费上调 7%至 10%](https://www.techspot.com/news/113430-microsoft-raises-windows-oem-fees-pc-makers-7.html) ⭐️ 6.0/10

据报道，微软计划自 2026 年 7 月起将部分 PC 厂商的 Windows OEM 授权费上调 7%至 10%，涨幅高于往年常见的个位数。零售版 Windows 11 价格不受影响。 此次授权费上调可能进一步推高 PC 售价，尤其是那些已受元件成本上涨挤压的入门级机型。PC 厂商、消费者以及整个 Windows 生态系统都可能受到影响。 具体涨幅因厂商和产品线而异，部分原本售价 600 至 800 美元的机型已接近 1000 美元。微软尚未对相关报道公开置评。

telegram · zaihuapd · 8月12日 02:32

**背景**: Windows OEM 授权是戴尔、惠普等 PC 厂商预装在硬件上的 Windows 版本，它在首次激活后锁定于该设备，不可转移；而零售版授权则更灵活。PC 行业一直面临内存等元件成本上涨的压力，这已经对价格敏感的市场造成了挤压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.partitionwizard.com/clone-disk/win10-oem-vs-retail.html">Learn the Difference Between Windows 10 OEM and Retail</a></li>
<li><a href="https://www.bbirdg.com/blogs/tech/windows-oem-vs-retail-difference">Windows OEM vs Retail: Which license should you buy?</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Windows`, `#OEM`, `#Pricing`, `#PC Industry`

---

<a id="item-22"></a>
## [马斯克：未来所有特斯拉将搭载星链，Cybercab 率先集成天线](https://www.techspot.com/news/113429-elon-musk-every-tesla-have-starlink-starting.html) ⭐️ 6.0/10

马斯克在财报电话会议上宣布，未来所有特斯拉车型都将配备星链连接，率先实现的是 Cybercab，该车已在车顶后部展示了集成式 Starlink V5 天线。Cybercab 的卫星链接速度超过 375 Mbps，可支持导航、客服、车队管理以及乘客观看 4K 视频，但尚未公布量产时间。 这一举措使卫星连接成为特斯拉未来全系车型的标准配置，这对需要无处不在的信号的 Robotaxi 运营至关重要。同时，它也可能促使其他汽车制造商在自动驾驶和车载娱乐领域采用卫星连接技术。 Cybercab 是一款专为自动驾驶设计的车辆，没有方向盘和踏板，其 V5 天线内置于车顶后部，而非外置安装。V5 天线的设计更小、更轻、制造成本更低，这有助于在特斯拉各车型中实现大规模普及。

telegram · zaihuapd · 8月12日 03:53

**背景**: 星链是 SpaceX 的卫星互联网星座，从低地球轨道提供高速、低延迟的宽带服务，目前已用于房车和船舶等车辆。特斯拉 Cybercab 是一款 2024 年发布的双座自动驾驶电动车，专为 Robotaxi 服务设计，没有手动控制装置。集成式 Starlink V5 天线标志着卫星硬件从售后加装转向乘用车的工厂预装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://hypebeast.com/2026/8/tesla-cybercab-debuts-with-integrated-starlink-v5">Tesla Cybercab With Starlink V 5 Antenna Revealed | Hypebeast</a></li>
<li><a href="https://otontechnology.com/starlink-v5-dish-smaller-lighter-efficient/">SpaceX&#x27;s Starlink V 5 Ships With Half the Antenna Elements</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#Starlink`, `#Satellite`, `#Connectivity`, `#Robotaxi`

---

<a id="item-23"></a>
## [Codex 活跃用户突破 1000 万，Tibo 预告明日惊喜](https://x.com/thsottiaux/status/2087423996115681767) ⭐️ 6.0/10

OpenAI 的编程智能体 Codex 活跃用户已突破 1000 万。Tibo 在 X 上发文称团队此前一直保持沉默，并预告明天将公布一个惊喜。 活跃用户突破 1000 万，使 Codex 成为 AI 编程智能体市场的重要参与者，加剧了面向开发者的 AI 工具之间的竞争。即将公布的惊喜可能预示着与更广泛开发者生态相关的新功能或新里程碑。 Tibo 此前承诺，每当 Codex 活跃用户增加 100 万就进行一次“重置”，直到达到 1000 万。他表示目前用户量已大幅超过这一数字，团队之前一直保持沉默，直到这次发布惊喜预告。

telegram · zaihuapd · 8月12日 08:01

**背景**: Codex 是 OpenAI 开发的 AI 编程智能体，用于编写代码、修复 bug 等软件工程任务。它于 2025 年 4 月以 Codex CLI 形式发布，可通过 ChatGPT 网页应用、Windows 和 macOS 桌面应用以及多种 IDE 集成使用。需要注意的是，OpenAI 早期还有一个基于 GPT-3、用 GitHub 上的 Python 代码训练的同名 Codex 语言模型，但那是不同的产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28language_model%29">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Codex`, `#OpenAI`, `#AI`, `#Product Milestone`, `#Announcement`

---

<a id="item-24"></a>
## [ChatGPT 测试$20 套餐用户付费$8 重置用量](https://www.reddit.com/r/ChatGPT/comments/1vks54h/its_here/) ⭐️ 6.0/10

据报道，ChatGPT 正在测试一项功能，允许 Plus（每月 20 美元）用户额外支付 8 美元来重置用量限制。该选项是在一位 Reddit 用户用尽额度后出现的，表明正在灰度测试中。 这一定价变化可能影响频繁达到用量上限的重度 ChatGPT Plus 用户，也表明 OpenAI 正在探索在固定订阅之外增加收入的方式。它还可能为 AI 工具如何收取超量使用费树立先例。 该重置选项仅在 20 美元套餐中被观察到，而 200 美元套餐的重置价格尚不清楚。此功能处于灰度测试阶段，尚未对所有用户开放。

telegram · zaihuapd · 8月12日 08:24

**背景**: 灰度测试是一种部署策略，将新功能先发布给一小部分用户，然后再全面推广，以便开发者收集反馈和发现问题。在这个案例中，OpenAI 似乎正在测试一项付费附加服务，让用户在达到用量限制后可以继续使用，而不必等到下一个计费周期。这与许多 SaaS 产品在用户超出套餐限制时收取超额费用的做法类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.volcengine.com/articles/7534568638654005291">微信+DeepSeek...</a></li>
<li><a href="https://watermelonwater.tech/insights/gptimage2%E7%81%B0%E6%B5%8B-nanobanana%E8%BF%8E%E5%BC%BA%E6%95%8C/">GPT-Image-2 灰 度 测 试 全面解析：细节与真实感双重突破，Nano...</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#定价`, `#AI服务`, `#灰度测试`

---

<a id="item-25"></a>
## [企业级 SSD 占 NAND 出货量 48% 长江存储首进前三](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 6.0/10

Counterpoint Research 数据显示，2026 年第二季度企业级 SSD 占全球 NAND 闪存出货量的 48%，同比接近翻倍，行业营收同比增长五倍。长江存储（YMTC）以 14% 的出货份额首次超越铠侠，跃居第三。 AI 推理工作负载正推动存储需求向企业级产品转移，重塑 NAND 市场格局，使数据中心 SSD 成为主要需求来源。长江存储进入出货量前三，表明中国存储厂商在全球市场的份额正在上升，但其营收排名仍受制于偏消费级的产品结构。 三星以 25% 的份额领跑，SK 海力士以 22% 紧随其后，长江存储以 14% 排名第三。尽管出货量进入前三，长江存储因产品多偏消费级，营收仅排第五；Counterpoint 预计到 2026 年底，企业级 SSD 将消耗超过一半的 NAND 比特出货量。

telegram · zaihuapd · 8月12日 11:00

**背景**: NAND 闪存是一种无需供电即可保留数据的非易失性存储技术，是 SSD 的基础。企业级 SSD 针对数据中心设计，在耐用性、性能和可靠性上优于消费级 SSD，而 AI 推理负载正在加速这类产品的需求增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.crucial.com/articles/for-businesses/enterprise-ssds-ultimate-guide">Ultimate guide to enterprise SSDs - crucial.com</a></li>
<li><a href="https://www.ibm.com/think/topics/nand-flash">What is NAND Flash Memory? | IBM</a></li>
<li><a href="https://www.crucial.com/articles/for-businesses/consumer-ssds-vs-enterprise-ssds">Consumer vs. Enterprise SSDs: What’s the Difference</a></li>

</ul>
</details>

**标签**: `#NAND`, `#SSD`, `#storage`, `#semiconductors`, `#AI`

---