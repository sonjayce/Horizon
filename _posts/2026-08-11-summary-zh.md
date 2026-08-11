---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 37 条内容中筛选出 22 条重要资讯。

---

1. [新攻击可窃取主流 LLM API 的加密推理痕迹](#item-1) ⭐️ 9.0/10
2. [Meta 发布 30B 开源权重智能体模型 Muse Glimmer](#item-2) ⭐️ 9.0/10
3. [压缩即预测：机器学习的信息论视角](#item-3) ⭐️ 8.0/10
4. [英伟达发布 Nemotron 3.5 Lightning 小模型与 NeMo Switchyard 智能路由库](#item-4) ⭐️ 8.0/10
5. [Mojo 1.0 发布：兼具 Python 易用性与 C 级性能](#item-5) ⭐️ 8.0/10
6. [英伟达的风险生意：AI 算力需求与 CUDA 护城河受审视](#item-6) ⭐️ 8.0/10
7. [伦敦地铁启动实时面部识别试点](#item-7) ⭐️ 8.0/10
8. [解耦下降：一种保证测试误差与训练误差一致的新训练方法](#item-8) ⭐️ 8.0/10
9. [HyperSAE：用庞加莱几何改进稀疏自编码器，减少死潜变量](#item-9) ⭐️ 8.0/10
10. [SK 海力士重启大连二厂，NAND 产能提升五成](#item-10) ⭐️ 8.0/10
11. [修复 macOS 虚拟机内核选择：llama.cpp 在 Apple Silicon 上提速 11 倍](#item-11) ⭐️ 7.0/10
12. [苹果研发验证照片源自 iPhone 相机的技术](#item-12) ⭐️ 7.0/10
13. [Anthropic 将从 2026 年 8 月起为 Claude 内容添加 AI 水印](#item-13) ⭐️ 7.0/10
14. [iOS 27 测试版 5 预埋中国版 Apple 智能隐私说明](#item-14) ⭐️ 7.0/10
15. [Amkor 据称拟出售中国业务股份，估值或达 15 亿美元](#item-15) ⭐️ 7.0/10
16. [字节跳动新设 AI 数据与安全一级部门，与 Seed、Flow 并列](#item-16) ⭐️ 7.0/10
17. [Cloudflare 报告：2026 上半年超 1Tbps 攻击激增](#item-17) ⭐️ 7.0/10
18. [OpenAI 伦理负责人上任不到一年即离职](#item-18) ⭐️ 6.0/10
19. [AAAI 2027 评审：代码提交缺席令人意外](#item-19) ⭐️ 6.0/10
20. [Anthropic 宣布 Claude Sonnet 5 促销定价永久生效](#item-20) ⭐️ 6.0/10
21. [ZCode 用户数突破百万，重置 GLM Coding Plan 使用限额](#item-21) ⭐️ 6.0/10
22. [石墨烯驱动软性镜片问世，有望革新相机与医疗设备](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [新攻击可窃取主流 LLM API 的加密推理痕迹](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

一篇新的安全论文证明，来自 Anthropic、OpenAI 和 Google 的加密思维链推理块可以被重放到较弱的同系列模型中，并通过越狱攻击恢复出明文形式的隐藏推理。此后，所有提供商都已修补该漏洞。 这表明仅靠加密无法可靠地保护 LLM API 中的专有推理痕迹，对模型隐私和知识产权构成威胁。这影响到依赖 API 推理的开发者与企业，并引发了关于隐藏思维链是否应被暴露的讨论。 该攻击之所以有效，是因为同一系列的模型共享相同的加密密钥，使轨迹可以在不同模型间转移。Claude Haiku 4.5 是最容易攻击的目标，论文附录中包含原始推理痕迹，例如 GPT-5.5 规划 CSS 代码的示例。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链（CoT）是一种提示工程技术，通过让模型在给出最终答案前逐步生成中间推理过程，来提高其在复杂任务上的表现。为保护专有方法，主流提供商会对这些推理块进行加密，但重放攻击可在不同上下文中复用捕获的响应，而越狱技术则绕过安全防护，迫使模型泄露隐藏输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.03373">Demystifying Long Chain-of-Thought Reasoning in LLMs Understanding Chain-of-Thought in LLMs through Information Theory Chain of Preference Optimization: Improving Chain-of-Thought ... Chain-of-Thought Prompting: Step-by-Step Reasoning with LLMs Demystifying Long Chain-of-Thought Reasoning - OpenReview ICML Poster Understanding Chain-of-Thought in LLMs through ... What is chain of thought (CoT) prompting? - IBM</a></li>
<li><a href="https://www.lakera.ai/blog/jailbreaking-large-language-models-guide">Jailbreaking Large Language Models: Techniques, Examples ...</a></li>

</ul>
</details>

**社区讨论**: 评论意见不一：有人认为使用模型输出进行训练应属正常，并批评‘窃取’的提法；也有人分享了独立的利用方法，例如通过开发者提示词解密压缩数据。一些评论者开玩笑说，未来的模型将拒绝在无企业 API 权限的情况下透露推理过程，还有人怀疑该漏洞是否被有意保留。

**标签**: `#LLM`, `#security`, `#privacy`, `#chain-of-thought`, `#AI`

---

<a id="item-2"></a>
## [Meta 发布 30B 开源权重智能体模型 Muse Glimmer](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 9.0/10

Meta 推出了 Muse Glimmer，这是一款拥有 300 亿参数、以 Apache 2.0 宽松许可证发布的开源权重模型，专为智能体任务、可靠工具调用和多步推理优化。该模型已可通过 LM Studio 本地使用，提供 18.16 GB 量化版本，并支持视觉输入。 此次发布意义重大，因为它采用了宽松的 Apache 2.0 许可证，不同于 Meta 早先的 Llama 许可，对商业和研究用途都很有吸引力。该模型面向日益增长的本地可运行智能体模型需求，能够处理复杂的多轮工作流和工具调用，有望加速 AI 智能体的开发。 这款 300 亿参数模型在 32 GB 及以上内存的设备上运行良好，其量化版本约 18.16 GB。Meta 称其在 DeepSearch QA、MCP-Atlas、τ-Bench 和 SWE-Bench 等基准测试中表现优异，并且该模型还支持视觉任务，如图像描述。

rss · Simon Willison · 8月10日 23:56

**背景**: 智能体 AI 模型旨在通过调用工具、编写代码和反复处理用户请求来自主完成多步骤任务。MCP-Atlas 等基准测试评估模型在真实 MCP 服务器和工具上的工具使用能力，τ-Bench 则模拟用户与智能体之间使用领域特定 API 的动态对话，DeepSearch QA 则评估深度研究能力。采用 Apache 2.0 等宽松许可证的开源权重模型允许开发者自由部署和修改，这与更具限制性的许可证形成了鲜明对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/mcp-atlas">MCP Atlas Leaderboard</a></li>
<li><a href="https://github.com/sierra-research/tau-bench">GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2406.12045">[2406.12045] $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Meta`, `#Model Release`, `#Agentic`

---

<a id="item-3"></a>
## [压缩即预测：机器学习的信息论视角](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

ngrok 博客文章《压缩即预测》探讨了机器学习中数据压缩与预测之间的概念等价性。文章认为，用其中一个来理解另一个，可以揭示其与信息论、算法复杂性和泛化之间的深层联系。 这一讨论之所以重要，是因为把机器学习视为压缩，可以将模型质量与奥卡姆剃刀和最小描述长度原理联系起来，为思考泛化和过拟合提供了一条有原则的路径。它引起了 AI/ML 领域的广泛共鸣，从大语言模型训练到模型选择都适用。 文章建立在重要文献之上，包括 David MacKay 的《信息论、推理与学习算法》、Jürgen Schmidhuber 关于压缩进展的研究，以及 Grant Sanderson 的《压缩即智能》视频系列。评论中提出的一个关键细微差别是：只有当训练分布恰好代表所有未来问题时，压缩才等于预测；在分布漂移下，有损压缩可能丢弃罕见但重要的边缘情况。

hackernews · nikolay · 8月11日 19:49 · [社区讨论](https://news.ycombinator.com/item?id=49263497)

**背景**: 这些观点源于算法信息论：一个数据集的柯尔莫哥洛夫复杂度是生成它的最短程序长度；所罗门诺夫归纳则通过偏好算法描述更短的理论来形式化奥卡姆剃刀。这些概念支撑了最小描述长度（MDL）原理，即最佳模型是最有效压缩数据的模型。它们共同为“将预测和学习视为压缩的形式”提供了理论基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solomonoff_induction">Solomonoff induction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov_complexity">Kolmogorov complexity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Minimum_description_length">Minimum description length</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞这篇文章，并指出这一观点有深厚的思想渊源——MacKay 的剑桥课程、Schmidhuber 的早期工作、Ted Chiang 的《ChatGPT 是网络的一张模糊 JPEG》一文，以及 Grant Sanderson 的视频系列。最具实质性的反驳观点来自一位评论者：只有当数据分布能完美代表所有未来情况时，压缩才等同于预测，而有损压缩可能会忽略对泛化很重要的罕见边缘情况。

**标签**: `#compression`, `#prediction`, `#information theory`, `#machine learning`, `#generalization`

---

<a id="item-4"></a>
## [英伟达发布 Nemotron 3.5 Lightning 小模型与 NeMo Switchyard 智能路由库](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 8.0/10

英伟达推出了 Nemotron 3.5 Lightning——一个 300 亿参数的开源混合专家（MoE）模型，仅激活 30 亿参数，专为代理式工作流中的快速低延迟执行而设计。与此同时，英伟达发布了 NeMo Switchyard，一个开源库，可智能地将每个请求路由到最合适的模型。 这一发布凸显了行业正更广泛地向小型高效语言模型转变，这类模型能够以更低成本为常驻 AI 代理提供动力。通过将轻量级 MoE 模型与模型路由层相结合，英伟达正在帮助开发者构建能够在准确性、延迟和基础设施成本之间取得平衡的多模型系统。 Nemotron 3.5 Lightning 总参数量为 300 亿，但仅激活 30 亿，并针对大规模、低延迟的代理执行进行了优化；该模型在 Hugging Face 上提供 BF16 和 NVFP4 格式。NeMo Switchyard 支持多种路由策略，并可在代理会话期间保持路由状态，以满足需要一致模型选择的场景。

hackernews · droidjj · 8月11日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49263340)

**背景**: 混合专家（MoE）模型每个 token 只激活其参数的一部分，这样既能保持推理速度较快和内存效率较高，又能保留大模型的容量。NeMo Switchyard 通过充当智能路由层，解决了在生产环境中部署多个模型的难题，与 LLM 应用的网关系统思路类似。这一消息建立在英伟达更广泛的 NeMo 框架之上，该框架用于构建、定制和部署生成式 AI 模型；不过 Nemotron 模型也可以通过 MLX 等标准平台在该框架之外使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>
<li><a href="https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/">Route AI Agents Across Models with NVIDIA NeMo Switchyard</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Switchyard">GitHub - NVIDIA- NeMo / Switchyard · GitHub</a></li>

</ul>
</details>

**社区讨论**: 用户反应总体积极，有人称赞向更小、更高效模型的推进，还有人称 Nemotron 3.5 Lightning 可以通过 MLX 在 Apple Silicon 上运行，尽管速度较慢。同时也存在有建设性的担忧：一位用户询问 NeMo Switchyard 在路由时如何处理提示缓存，另一位用户则批评英伟达的基准图表未包含 Qwen 模型系列。还出现了一些关于极简写作的无关评论。

**标签**: `#NVIDIA`, `#Nemotron`, `#small language models`, `#model routing`, `#open source`

---

<a id="item-5"></a>
## [Mojo 1.0 发布：兼具 Python 易用性与 C 级性能](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 8.0/10

Modular 于 2026 年 5 月下旬正式发布 Mojo 1.0，标志着该语言的首个稳定版本。这个版本被视为一个关键里程碑，因为该语言旨在结合 Python 的易用性与 C 级性能，主要面向 AI/ML 系统。 Mojo 1.0 对一种可能在 AI 基础设施领域挑战成熟系统编程语言的语言来说，是一个重要里程碑。它可能为开发者提供一条更高生产力的高性能计算路径，同时保留类似 Python 的可读性，从而对 AI/ML 工具链和采用产生影响。 Mojo 基于 MLIR 编译器框架而非直接基于 LLVM，因此能够面向 CPU、GPU、TPU 和其他加速器。目前编译器仍是专有的，但 Modular 重申将在 2026 年将其开源，同时该语言也有了新的官方网站 mojolang.org。

hackernews · dayanruben · 8月11日 16:56 · [社区讨论](https://news.ycombinator.com/item?id=49261128)

**背景**: Mojo 是由 Modular 公司开发的系统编程语言，该公司由 Chris Lattner（Swift 的最初设计者）创立。它使用类似 Python 的语法，但加入了受 Rust 启发的静态类型和借用检查。最初计划成为 Python 的超集，但这一目标已被暂停；该语言现在专注于高性能 CPU、GPU 和加速器编程。Mojo 的设计利用 MLIR 来实现高级编译器优化和广泛的硬件支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区的反馈褒贬不一。一些用户质疑使用闭源编译器的语言的价值，另一些用户则对 Mojo 的确切用途及其与 Python 的关系感到困惑。还有人批评“Python 超集”目标被淡化，并呼吁更早开源编译器。尽管如此，不少评论者表示仍对 Mojo 的未来抱有希望。

**标签**: `#Mojo`, `#Programming Languages`, `#AI/ML`, `#Compilers`, `#Performance`

---

<a id="item-6"></a>
## [英伟达的风险生意：AI 算力需求与 CUDA 护城河受审视](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 8.0/10

这篇文章分析了英伟达的战略风险，质疑 AI 算力需求增长的可持续性以及其 CUDA 软件生态优势的脆弱性。文章指出，虽然对更多算力的一阶需求是真实的，但关于需求增长的二阶假设可能被夸大。 这很重要，因为英伟达的估值以及更广泛的 AI 基础设施繁荣依赖于持续的需求增长和其软件护城河的持久性。如果这些假设动摇，可能会影响投资者、AI 初创公司以及 AMD 和谷歌 TPU 等竞争对手。 该分析区分了一阶假设（对更多算力的需求存在）和二阶假设（需求的增长率），后者更可能被夸大。评论者指出，虽然 CUDA 在机器学习研究中根深蒂固，但开发体验不佳，而且英伟达正在扩展到机器人领域，并面临与中国的地缘政治动态。

hackernews · jonbaer · 8月11日 10:02 · [社区讨论](https://news.ycombinator.com/item?id=49255710)

**背景**: CUDA 是英伟达专有的并行计算平台和 API，允许软件利用 GPU 进行通用处理，包括 AI 和科学计算。它包含编译器、库和开发者工具，并支持 C、C++、Python 和 Julia 等语言。英伟达的软件生态常被视为其关键护城河，因为 CUDA 已深度整合到 AI 研究和生产工作流中，使 AMD 等竞争对手难以取代。然而，该分析质疑这种生态优势是否既强大又脆弱，尤其是在需求增长假设受到审视之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_CUDA">Nvidia CUDA</a></li>
<li><a href="https://www.rownix.dev/en/articles/nvidia-cuda-ai-infrastructure-moat">Is Nvidia&#x27;s Moat The Chip, Or The CUDA Ecosystem ? | Rownix&#x27;s Blog</a></li>
<li><a href="https://www.chipstrat.com/p/can-amd-bridge-nvidias-software-moat">Can AMD Bridge Nvidia’s Software Moat? - by Austin Lyons</a></li>

</ul>
</details>

**社区讨论**: 评论体现了细致的辩论。有人同意 CUDA 在机器学习研究中的根深蒂固是真实的，但实际使用 CUDA C/C++的开发体验很差。另一些人则认为对算力的一阶需求是真实的，但二阶增长预期可能被夸大。还有关于英伟达进军机器人领域以及与中国的地缘政治维度的讨论。

**标签**: `#Nvidia`, `#AI infrastructure`, `#business strategy`, `#CUDA`, `#semiconductors`

---

<a id="item-7"></a>
## [伦敦地铁启动实时面部识别试点](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 8.0/10

英国交通警察局（BTP）已将实时面部识别（LFR）试点扩大到伦敦地铁站，实时扫描乘客面部。 此举将大规模监控技术引入全球最繁忙的交通网络之一，引发严重的隐私和公民自由担忧。其结果可能为英国乃至其他地区在公共场所部署面部识别开创先例。 该试点将 BTP 现有的 LFR 工作扩展到伦敦地铁站，摄像头将面部与通缉人员名单进行实时比对。批评者认为该技术准确率低，且缺乏明确的终止试点的失败标准。

hackernews · BlueBerry2001 · 8月11日 09:40 · [社区讨论](https://news.ycombinator.com/item?id=49255496)

**背景**: 实时面部识别通过 CCTV 摄像头捕捉面部，并即时与图像数据库进行比对。BTP 称其目的是识别通缉犯，但公民自由组织警告称，这项技术会导致普通公众被无孔不入地追踪。随着非接触式银行卡成为进站的主要方式，伦敦地铁也早已不再是完全匿名的出行环境。

**社区讨论**: 评论者大多持批评态度，称此举侵犯隐私、是“奥威尔式”的发展。有人质疑试点毫无意义，因为没有现实中的失败条件；也有人指出，随着非接触式支付普及，地铁匿名出行早已不复存在。还有评论讽刺称这能解决街头犯罪，甚至将其与中国监控社会作比较。

**标签**: `#facial recognition`, `#surveillance`, `#privacy`, `#biometrics`, `#civil liberties`

---

<a id="item-8"></a>
## [解耦下降：一种保证测试误差与训练误差一致的新训练方法](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

作者提出了一种名为解耦下降（Decoupled Descent, DD）的新型训练算法，该算法基于带有 Onsager 校正的近似消息传递（AMP）理论，能够保证在每个参数迭代处训练误差渐近等于测试误差。该方法在风格化的高斯混合模型和高维 XOR 模型上得到了验证，并与标准梯度下降形成对比。 这直接解决了深度学习中一个常见的痛点——泛化差距，即训练误差下降而测试误差可能停滞甚至上升的问题。通过保证训练-测试一致性，DD 允许在不牺牲训练数据的情况下进行验证，并为最优停止和超参数调优带来了新的可能性。 DD 利用了 AMP 理论中的低维状态演化递推，使算法的动态过程变得透明且易于处理。该论文属于理论性质，重点研究风格化的高维问题；扩展到非常大规模的模型仍是未来工作，作者计划发布一个兼容 PyTorch 的软件包。

reddit · r/MachineLearning · /u/mlovik1 · 8月11日 21:06

**背景**: 近似消息传递（AMP）是一类用于高维统计估计问题（如压缩感知和线性回归）的迭代算法，凭借状态演化在大系统极限下具有严格的性能保证。AMP 的一个关键组成部分是 Onsager 校正，这是一个“记忆”项，用于将当前迭代与过去的误差去相关，确保每一步都具有理想的统计性质。解耦下降将 AMP 原理应用于神经网络训练，通过显式跟踪状态演化来防止训练误差与测试误差之间出现任何失配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate ...</a></li>
<li><a href="https://arxiv.org/abs/2201.07487">[2201.07487] A Concise Tutorial on Approximate Message Passing</a></li>
<li><a href="https://www.machinebrief.com/news/decoupled-descent-bridging-the-training-test-gap-la4u">Decoupled Descent: Bridging the Training-Test Gap</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#training methods`, `#approximate message passing`, `#generalization`, `#theory`

---

<a id="item-9"></a>
## [HyperSAE：用庞加莱几何改进稀疏自编码器，减少死潜变量](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/) ⭐️ 8.0/10

HyperSAE 是一个 PyTorch 库，采用解耦双速设计：训练时将字典权重投影到庞加莱球，前向传播仍保持欧几里得形式。在 Gemma-2-2B 上，重建 MSE 降低 9.8%，死潜变量从 3.8% 降至 0.2%，且推理开销为零。 这对机制可解释性具有重要意义，因为大语言模型上的大规模稀疏自编码器普遍存在特征碰撞和死潜变量问题。通过引入双曲几何，HyperSAE 在完全不增加推理开销的前提下，提供了一种提升重建质量和特征利用率的新方法。 该库使用 TriPartite 损失，结合重建损失、L1 稀疏性和蕴含锥损失；蕴含锥损失将父概念放在原点附近，子概念放在边界附近。此外还包含共激活队列追踪和单类训练器接口，论文与基准代码均已开源。

reddit · r/MachineLearning · /u/visha1v · 8月11日 18:37 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/)

**背景**: 稀疏自编码器（SAE）是机制可解释性中的主流技术，用于将神经表示分解为稀疏且可解释的特征。标准 SAE 将字典原子嵌入欧几里得空间，其体积呈多项式增长，大字典容易导致特征碰撞和死潜变量。双曲几何，尤其是庞加莱球模型，能以低失真嵌入层级结构，恰好符合大语言模型学到的分支概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2205.13984">Information measures and geometry of the hyperbolic exponential families of Poincaré and hyperboloid distributions</a></li>
<li><a href="https://www.lesswrong.com/posts/CJPqwXoFtgkKPRay8/an-intuitive-explanation-of-sparse-autoencoders-for">An Intuitive Explanation of Sparse Autoencoders for Mechanistic ...</a></li>
<li><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05671.pdf">HYPE: Hyperbolic Entailment Filtering for</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#interpretability`, `#sparse autoencoders`, `#hyperbolic geometry`, `#PyTorch`

---

<a id="item-10"></a>
## [SK 海力士重启大连二厂，NAND 产能提升五成](https://en.sedaily.com/finance/2026/08/11/sk-hynix-to-boost-china-nand-output-50-percent-with-dalian) ⭐️ 8.0/10

SK 海力士已重启其位于中国大连的第二座 NAND 闪存工厂建设，当地产能将提升约 50%。设备搬入计划于今年底启动，预计明年上半年实现量产，新产线月产能约 5 万片晶圆。 在 AI 驱动的企业级 SSD 需求激增背景下，此次扩产将巩固 SK 海力士在 NAND 市场的地位。大连工厂增加的供应量有望缓解当前 NAND 供应紧张状况，并影响全球存储芯片价格走势。 大连二厂于四年前开工，但因内存行业下行周期而长期停工。SK 海力士正采取双轨策略：大连工厂采用成熟技术生产 100 层级 NAND，清州工厂则聚焦 300 层以上高堆叠产品；过去一年 NAND 价格已上涨近十倍。

telegram · zaihuapd · 8月11日 16:21

**背景**: NAND 闪存是一种用于 SSD 的非易失性存储技术，3D NAND 通过垂直堆叠存储单元层数来提升密度，目前产品层数已超过 200 层。企业级 SSD 是为数据中心和服务器设计的高性能存储设备，AI 工作负载大幅提升了存储容量和带宽需求。SK 海力士是全球领先的存储器制造商之一，在韩国和中国均设有生产基地。此次大连扩产反映了整个行业对 AI 驱动存储需求的应对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.atpinc.com/blog/3d-nand-ssd-sd-flash-memory-storage-what-is">3 D NAND SSD : Breaking Scaling Limitations of 2D planar NAND</a></li>
<li><a href="https://www.everpuredata.com/knowledge/what-is-3d-nand.html">What Is 3 D NAND and How Does It Work? | Everpure</a></li>
<li><a href="https://www.newegg.com/Enterprise-SSDs/SubCategory/ID-2021">Enterprise SSDs, Enterprise Solid State Drives - Newegg.com</a></li>

</ul>
</details>

**标签**: `#NAND`, `#SK Hynix`, `#semiconductors`, `#memory`, `#AI infrastructure`

---

<a id="item-11"></a>
## [修复 macOS 虚拟机内核选择：llama.cpp 在 Apple Silicon 上提速 11 倍](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 7.0/10

trycua 的一篇博客文章展示了在 Apple Silicon 上的 macOS 虚拟机中修复内核选择后，llama.cpp 的 LLM 推理速度最高可提升 11.08 倍，生成 token 的速度最高可提升 16.36 倍，而对比对象是同一工作负载在未修改的虚拟机中的表现。 这件事很重要，因为它表明虚拟机配置会显著影响 LLM 推理的 Metal/GPU 性能，为在 macOS 虚拟化环境中运行 llama.cpp 的开发者提供了一个可观的优化方向。同时它也澄清了这是一项针对 Virtualization.framework 虚拟机的针对性修复，并非对所有 Apple Silicon 用户的 llama.cpp 通用加速。 这一提速源于确保虚拟机选择了正确的 GPU 内核，而非对 llama.cpp 本身的任何修改；该修复绕过了 Virtualization.framework 导致 llama.cpp 选中次优内核的问题。对比对象是在相同工作负载下未修改的虚拟机，因此这一收益仅适用于此类虚拟机环境，不适用于裸机或其他虚拟化方案。

hackernews · frabonacci · 8月11日 14:50 · [社区讨论](https://news.ycombinator.com/item?id=49259339)

**背景**: Apple 的 Virtualization.framework 允许开发者在 Apple Silicon 上运行 macOS 和 Linux 虚拟机，它向客户机提供一个半虚拟化的虚拟图形设备，通过宿主内核栈将 Metal 工作提交到物理 GPU 上执行。llama.cpp 是一个开源的 C/C++ LLM 推理实现，可通过 Metal 将计算卸载到 Apple GPU。在虚拟机中，虚拟图形设备可能暴露一个功能裁剪后的 Metal 配置，导致 llama.cpp 选择并非针对宿主 GPU 最优调校的算法与内核；修复内核选择问题后即可恢复接近原生的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md">cua/blog/gpu-passthrough-macos-vms.md at main · trycua/cua</a></li>
<li><a href="https://developer.apple.com/documentation/virtualization">Virtualization | Apple Developer Documentation</a></li>
<li><a href="https://arstechnica.com/gadgets/2022/07/how-to-use-free-virtualization-apps-to-safely-test-the-macos-ventura-betas/">Apple’s Virtualization framework is a great, free way to test new macOS betas - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 评论区指出标题可能具有误导性，因为这一提速仅适用于 Virtualization.framework 虚拟机，而非所有 llama.cpp 用户。还有人质疑为什么 Apple 的 Virtualization.framework 暴露的是较低的 Metal 配置，而不是报告宿主 GPU 的全部能力；另有一些人推测未来 M 系列芯片中的神经加速器是否会下放到基础型号。

**标签**: `#llama.cpp`, `#Apple Silicon`, `#macOS VMs`, `#GPU passthrough`, `#LLM inference`

---

<a id="item-12"></a>
## [苹果研发验证照片源自 iPhone 相机的技术](https://9to5mac.com/2026/08/10/apple-is-working-on-a-way-to-authenticate-that-a-photo-came-from-an-iphone-camera/) ⭐️ 7.0/10

苹果正在开发一种设备级认证系统，在 iOS 27 beta 5 的代码中被发现名为“Apple Reference Image”，用于验证照片是否由 iPhone 相机拍摄。该系统将利用与相机硬件绑定的唯一数据，配合系统签名和加密认证来确立照片来源。 随着生成式 AI 让逼真的伪造图片越来越容易制作，硬件支持的认证机制有望帮助恢复对照片真实性的信任，并为行业树立先例。这将影响普通用户、记者以及依赖视觉验证的内容平台。 该技术目前仅存在于测试版操作系统的早期代码中，苹果尚未发布官方公告、发布日期或具体实现方案。据报道，其核心是利用与拍摄每张照片的 iPhone 相机硬件绑定的唯一数据，再结合系统级签名和加密认证。

telegram · zaihuapd · 8月11日 01:53

**背景**: 图像认证与溯源旨在确定照片的来源以及是否被篡改。现有的开放技术标准如 C2PA，已经用于追踪媒体的来源与溯源，而苹果的方法则是将验证直接绑定到相机传感器和设备固件，将这一理念延伸到硬件层面。这一点之所以重要，是因为生成式 AI 如今能够创造出足以以假乱真的合成图像，容易导致虚假信息传播，因此硬件级验证或可成为一种安全保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/10/apple-is-working-on-a-way-to-authenticate-that-a-photo-came-from-an-iphone-camera/">Apple is working on a way to authenticate that a photo came from an iPhone camera - 9to5Mac</a></li>
<li><a href="https://www.androidinfotech.com/apple-photo-is-real-or-ai-generated/">How to Tell if an Apple Photo Is Real or AI-Generated? - Android Infotech (August 2026)</a></li>
<li><a href="https://authenticity.sony.net/camera/en-us/index.html">Camera Authenticity Solution | Sony</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Photo Authentication`, `#AI-generated Content`, `#Cybersecurity`, `#Camera Technology`

---

<a id="item-13"></a>
## [Anthropic 将从 2026 年 8 月起为 Claude 内容添加 AI 水印](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) ⭐️ 7.0/10

Anthropic 已签署欧盟《人工智能法案》第 50\(2\) 条的透明度行为准则，并承诺从 2026 年 8 月 2 日起，在欧盟发布的新 Claude 模型生成的文本中嵌入机器可读水印，同时在支持的文件中加入 C2PA 来源元数据。相关标记适用于 Claude、Claude Code、Claude Cowork 和 Claude Tag 等所有产品，覆盖全球使用场景。 这是 AI 内容来源追溯和合规方面的重要一步，表明主要 AI 实验室正在落实欧盟《人工智能法案》下的透明度义务。它将影响使用 Claude 的企业、教育机构和出版商，并可能为其他 AI 模型提供商应对类似要求树立先例。 文本水印不可见，可经受复制粘贴和部分编辑；支持的文件采用 C2PA 来源标准并带有数字签名元数据。Anthropic 正在为 2026 年 8 月 2 日前发布的旧模型补充标记功能，并计划发布检测技术细节；检测到标记仅说明内容可能经过 Claude 处理，未检测到标记也不能证明内容不是 AI 生成。

telegram · zaihuapd · 8月11日 03:06

**背景**: 欧盟《人工智能法案》是一部具有里程碑意义的法规，其中第 50 条对特定 AI 系统的提供者和部署者规定了透明度义务，包括为 AI 生成内容添加标记。C2PA（内容来源与真实性联盟）是一个开放技术标准，由 Adobe、Microsoft、Google 等公司支持，通过向媒体文件添加加密签名的元数据来验证内容来源和编辑历史。随着 AI 生成的文本越来越难以与人类写作区分，水印和来源元数据正成为维护网络信任的关键工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content">How Claude marks AI-generated content | Claude Help Center</a></li>
<li><a href="https://artificialintelligenceact.eu/article/50/">Article 50: Transparency Obligations for Providers and ...</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI transparency`, `#Watermarking`, `#EU AI Act`

---

<a id="item-14"></a>
## [iOS 27 测试版 5 预埋中国版 Apple 智能隐私说明](https://ai.privacy/) ⭐️ 7.0/10

iOS 27 开发者测试版 5 中预埋了中文版 Apple 智能隐私说明，确认苹果将在中国大陆使用当地公司的安全机制，并且用户请求全部在设备端处理。相关代码字符串还新增了打开或关闭 Apple 智能的开关。 这揭示了苹果在遵守中国 AI 法规的同时维持其隐私定位的具体做法，是全球 AI 落地的重要考验。也意味着 Apple 智能在中国大陆的上线已进入适配后期，将影响中国数以百万计的 iPhone 用户。 隐私说明中提到，按照法律要求，苹果会收集匿名化的安全结果并以汇总形式共享，安全机制会自动下载和更新。文案中附有“关于 Apple 智能与隐私”的链接，新增的弹窗文案也表明用户可以在设置中关闭 Apple 智能。

telegram · zaihuapd · 8月11日 04:49

**背景**: Apple 智能是苹果的 AI 功能套件，而中国要求 AI 服务在上线前通过安全评估。由于中国规定敏感数据须在国内处理，苹果与阿里巴巴（提供生成式 AI）和百度（提供搜索和 Siri 支持）等本地公司合作，在设备端运行安全机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sftpmac.com/en/blog/20260716-apple-intelligence-china-approved-qwen-baidu-decision-guide.html">2026 Apple Intelligence Approved in China : Qwen... | SFTPMAC</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#iOS`, `#Privacy`, `#China`, `#AI regulation`

---

<a id="item-15"></a>
## [Amkor 据称拟出售中国业务股份，估值或达 15 亿美元](https://www.bloomberg.com/news/articles/2026-08-11/amkor-is-said-to-explore-stake-sale-in-1-5-billion-china-unit) ⭐️ 7.0/10

Amkor Technology 据称正在考虑出售其中国业务的部分股份，估值可能在 10 亿至 15 亿美元之间。该公司已聘请顾问协助剥离该部门，并可能保留少数股权。 此举反映了美中科技紧张局势下跨国公司重新评估在华业务的趋势，并可能影响全球半导体供应链和 AI 封装格局。Amkor 最近与英伟达签署了价值 15 亿美元的多年期协议，共同开发下一代 AI 半导体封装技术。 Amkor 于 2001 年在上海设立封装厂，据称正在考虑包括出售少数股权在内的各种选项。该报道基于知情人士的消息，Amkor 拒绝置评。

telegram · zaihuapd · 8月11日 07:21

**背景**: 半导体封装测试是芯片制造的后端环节，包括划片、装片、键合、塑封和最终电性测试等工艺。随着摩尔定律放缓，3D 封装、Chiplet、混合键合等先进封装技术对 AI 芯片的算力提升越来越重要。Amkor 是全球第二大外包半导体封装测试厂商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E5%8D%8A%E5%AF%BC%E4%BD%93%E5%B0%81%E8%A3%85%E6%B5%8B%E8%AF%95/6417278">半导体封装测试 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2033639507938035195">AI半导体封装技术实战指南：从TSV到混合键合的全景解析</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#Amkor`, `#supply chain`, `#US-China`, `#AI packaging`

---

<a id="item-16"></a>
## [字节跳动新设 AI 数据与安全一级部门，与 Seed、Flow 并列](https://36kr.com/newsflashes/3934989813710209) ⭐️ 7.0/10

字节跳动近期成立了一个新的一级部门“AI 数据与安全”，由王赢磊（Adam Wang）负责，与 Seed、Flow、抖音等部门平级。这是继 2023 年底成立 Seed 和 Flow 两个 AI 一级部门后，字节围绕 AI 业务设立的又一个一级部门。 此举表明字节跳动在扩展 AI 产品（如豆包）时，正将 AI 治理、数据基础设施和安全提升到战略高度。该部门可能重塑公司对 AI 数据合规和安全的管理方式，影响其在国内外 AI 竞争中的地位。 新部门负责人王赢磊此前曾任 TikTok 平台责任负责人和 TikTok 直播负责人。该部门为一级部门，直接向高层汇报，与核心业务线平级，体现了字节对其数据与安全职能的重视。

telegram · zaihuapd · 8月11日 11:25

**背景**: 字节跳动于 2023 年底成立 Seed（AI 研究）和 Flow（AI 应用）两个一级部门，作为其通用人工智能（AGI）战略的一部分。Seed 负责豆包等产品背后的基础模型，Flow 聚焦 AI 应用。新成立的 AI 数据与安全部门则为这些 AI 业务提供了专门的数据与安全治理层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yicaiglobal.com/news/chinas-bytedance-sets-up-new-division-focusing-on-ai-applications">China’s ByteDance Sets Up New Division Focusing on AI Applications</a></li>
<li><a href="https://eu.36kr.com/en/p/3934936980667776">36Kr Exclusive: ByteDance Launches New First-Tier AI Division...</a></li>
<li><a href="https://seed.bytedance.com/en/">ByteDance Seed</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#AI`, `#Data Security`, `#Org Structure`, `#Tech Industry`

---

<a id="item-17"></a>
## [Cloudflare 报告：2026 上半年超 1Tbps 攻击激增](https://blog.cloudflare.com/ddos-threat-report-2026-h1/) ⭐️ 7.0/10

Cloudflare 2026 年上半年 DDoS 威胁报告显示，共缓解 935 起超 1 Tbps 的网络层攻击，第二季度环比增长 519%。DNS Flood 攻击环比激增 580%，成为第三大攻击类型。 报告凸显了 DDoS 攻击规模的不断升级，超大流量攻击已成为企业和基础设施提供商的常态。安全团队必须为多 Tbps 级攻击以及日益普遍的 DNS 威胁做好准备。 上半年 DNS 类攻击占网络层攻击的 34.3%。媒体、出版与制作行业是最受攻击的行业；政府行业排名从第 29 位升至第 9 位。

telegram · zaihuapd · 8月11日 13:20

**背景**: DDoS（分布式拒绝服务）攻击通过向目标发送大量流量来中断服务。网络层攻击（第 3 层）利用 ICMP 等协议饱和带宽，而 DNS Flood 则向 DNS 服务器发送海量查询，使其无法处理合法请求。Cloudflare 的全球网络缓解这些攻击并发布季度威胁报告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/">DNS flood DDoS attack | Learning Center</a></li>
<li><a href="https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/">How Do Layer 3 DDoS Attacks Work? | L3 DDoS - Cloudflare</a></li>
<li><a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">What is a DDoS attack? | Learning Center - Cloudflare</a></li>

</ul>
</details>

**标签**: `#DDoS`, `#Cloudflare`, `#Security`, `#Network Attacks`, `#Threat Report`

---

<a id="item-18"></a>
## [OpenAI 伦理负责人上任不到一年即离职](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) ⭐️ 6.0/10

OpenAI 的伦理负责人 Chloé Bakalar 在加入不到一年后离开了公司。这一消息由《金融时报》率先报道，并再次引发关于 AI 伦理团队在顶级 AI 实验室中角色的讨论。 此次离职引发了对 OpenAI 内部 AI 治理与伦理职能的稳定性及影响力的质疑，而 OpenAI 正是 AI 热潮中的核心企业。同时，这也加剧了行业对伦理团队究竟是真正融入模型开发、还是主要充当对外安抚角色的普遍怀疑。 Bakalar 在加入 OpenAI 不到一年前曾在 Meta 担任首席伦理学家约六年。《金融时报》的文章没有详细说明她离职的原因，外界只能猜测。

hackernews · ilamont · 8月11日 12:23 · [社区讨论](https://news.ycombinator.com/item?id=49257160)

**背景**: OpenAI 和 Anthropic 等公司的 AI 伦理团队，职责是研究大型语言模型等 AI 系统对社会和道德的影响。一个反复出现的批评——在社区讨论中也有体现——是这类团队往往缺乏真正的决策权，可能更像公关手段，而非运营层面的安全机制。Bakalar 曾表示，AI 伦理提出的问题与人类几百年来思考的问题本质相同，这反映出将 AI 视为独特威胁还是传统伦理议题延续之间的张力。

**社区讨论**: 评论者普遍对企业的 AI 伦理部门持怀疑态度。有人指出，伦理团队被雇佣只是为了公关噱头，实际没有影响力；也有人认为 Bakalar 离职背后存在更复杂、未公开的因素，并指出报道细节不足。还有人将她的离职与 OpenAI 和 Anthropic 的哲学立场联系起来，即认为大语言模型会带来独特的大规模风险。

**标签**: `#AI ethics`, `#OpenAI`, `#AI governance`, `#AI safety`, `#personnel`

---

<a id="item-19"></a>
## [AAAI 2027 评审：代码提交缺席令人意外](https://www.reddit.com/r/MachineLearning/comments/1vlqjby/aaai_2027_review_no_code_submission_d/) ⭐️ 6.0/10

一位 AAAI 2027 的审稿人报告称，尽管会议对可复现性有明确要求，但提交的论文中包含代码实现的却少得令人意外。该审稿人计划将代码提交情况纳入初始评分考量。 这一轶事性观察揭示了顶级 AI 会议在可复现性政策与实际投稿实践之间可能存在的差距。如果这一现象普遍存在，可能会影响已发表研究的可信度，并影响审稿人与作者对待代码公开的方式。 审稿人指出，根据 AAAI 的可复现性指南，论文应附带详细的附录和代码，但许多投稿缺少代码。他们还提到，借助 AI 助手能在数小时内生成带有虚假结果的实证论文，因此代码提交成为判断真实性的重要信号。

reddit · r/MachineLearning · /u/wontonut · 8月11日 18:58

**背景**: AAAI（人工智能促进协会）是人工智能研究领域的重要会议，已将可复现性作为关键评审标准。机器学习中的可复现性通常要求作者公开代码、数据和详细的实验配置，以便他人验证结果。近年来，许多会议都加强了这些要求，审稿人越来越将代码可用性作为评估论文质量的依据。

**标签**: `#AAAI`, `#reproducibility`, `#peer review`, `#machine learning`

---

<a id="item-20"></a>
## [Anthropic 宣布 Claude Sonnet 5 促销定价永久生效](https://x.com/claudeai/status/2086891169217122586) ⭐️ 6.0/10

8 月 10 日，Anthropic 宣布 Claude Sonnet 5 的促销定价将永久保留，原定 9 月 1 日的涨价计划被取消。API 将继续按每百万输入 token 2 美元、每百万输出 token 10 美元计费，而不会恢复为标准的 3 美元/15 美元。 这让使用 Claude Sonnet 5 的开发者和企业获得可预测且更低的 API 成本，使 Anthropic 在与其他大模型提供商的竞争中更具优势。这也表明公司即使此前计划涨价，仍愿意维持较低价格以促进采用。 Claude Sonnet 5 于 6 月上线时采用促销定价，原计划仅持续到 8 月 31 日。永久定价意味着该模型的输入/输出费率将无限期保持为每百万 token 2 美元/10 美元。

telegram · zaihuapd · 8月11日 03:39

**背景**: 在 AI 语言模型 API 中，计费通常基于 token——即模型读取和生成的小段文本单位。输入 token（提示内容）和输出 token（生成的内容）分开计费，输出 token 的价格通常是输入 token 的 2 到 4 倍。Claude Sonnet 5 是 Anthropic 的中端模型之一，此次公告涉及的是其 API 接入价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://www.gmicloud.ai/en/blog/how-do-different-cloud-providers-compare-in-terms-of-pricing-for-ai-model-inference">How Do Different Cloud Providers Compare in Terms of Pricing for AI...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#Pricing`, `#AI`, `#LLM`

---

<a id="item-21"></a>
## [ZCode 用户数突破百万，重置 GLM Coding Plan 使用限额](http://z.ai/) ⭐️ 6.0/10

Z.ai 宣布 ZCode 用户数已突破 100 万，并为所有 GLM Coding Plan 订阅用户重置了使用限额。这次更新还将缓存命中率提升至 98%，带来约 1.8 倍的有效使用量。 这一里程碑表明 ZCode 作为 AI 编程工具正获得越来越多的采用，也提升了 Z.ai 在竞争激烈的 AI 开发者工具市场中的地位。更高的缓存命中率意味着开发者可以获得更快、更高效的编码工作流，也让 GLM Coding Plan 更具性价比。 此次限额重置面向所有 GLM Coding Plan 用户，不区分套餐等级，以感谢社区支持。98% 的缓存命中率直接转化为相同套餐下约 1.8 倍的可使用量或使用时长。

telegram · zaihuapd · 8月11日 05:58

**背景**: ZCode 是 Z.ai（智谱 AI）推出的智能体式 AI 编程环境，旨在将 AI Agent 与开发者现有工具链相结合，完成规划、编码、评审和部署等任务。它基于 Z.ai 的 GLM 系列大语言模型（包括最新的 GLM-5.2）提供能力。GLM Coding Plan 是一种订阅服务，允许用户在 Claude Code、Kilo Code、Cline 等主流 AI 编程工具中使用这些模型。此次更新重点提升了缓存效率，减少重复计算，从而加速 AI 辅助编程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zcode.z.ai/en">ZCode - Simple, Fast, Vibe‑Ready | Official Harness for GLM-5.2</a></li>
<li><a href="https://z.ai/subscribe">GLM Coding Plan — AI Coding Powered by GLM-5.2 &amp; GLM-5-Turbo ...</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#ZCode`, `#GLM`, `#product update`, `#milestone`

---

<a id="item-22"></a>
## [石墨烯驱动软性镜片问世，有望革新相机与医疗设备](https://www.qmul.ac.uk/news/latest-news/2026/science-and-engineering/se/new-graphene-powered-soft-lens-could-pave-the-way-for-smarter-glasses-cameras-and-medical-devices.html) ⭐️ 6.0/10

伦敦玛丽女王大学的研究团队开发出一种基于还原氧化石墨烯的透明软性镜片，可通过施加小电场改变焦距。该原型发表在《Advanced Functional Materials》上，并将透明石墨烯电极直接集成到镜片的驱动层中。 这项技术有望让自动对焦相机、VR/AR 头显和微型医疗成像设备摆脱笨重的机械部件，实现更紧凑的设计。它也为更智能的眼镜和更小型化的光学系统铺平了道路。 该镜片模拟人眼工作原理，通电压时软膜会拉伸并改变形状，从而对不同距离的物体对焦。团队通过将超薄透明石墨烯电极嵌入驱动层，解决了传统电极只能置于镜片边缘的瓶颈，但电极的透明度和性能仍需进一步优化。

telegram · zaihuapd · 8月11日 12:27

**背景**: 还原氧化石墨烯是氧化石墨烯经过化学或热还原后得到的材料，具有较好的导电性，并且可以大规模制备。电调焦透镜利用可变形薄膜或液晶等材料，在电场作用下改变焦距，无需传统机械移动部件，这在相机、可穿戴设备和医疗设备中有广泛应用前景。理解这些背景有助于明白这种新型软镜片如何在保持紧凑的同时实现焦距变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Nitrogen-doped_reduced_graphene_oxide">Nitrogen-doped reduced graphene oxide</a></li>
<li><a href="https://www.researchgate.net/publication/228446426_The_reduction_of_graphene_oxide">The reduction of graphene oxide | Request PDF</a></li>
<li><a href="https://www.yumpu.com/en/document/view/36796818/optotune-product-offeringpdf-pacer/2">Electrically tunable lens | Optotune product offering.pdf - Pacer</a></li>

</ul>
</details>

**标签**: `#graphene`, `#optics`, `#lens`, `#materials science`, `#research`

---