---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 40 条内容中筛选出 20 条重要资讯。

---

1. [Anthropic 发布 Claude 系统提示词，引发社区分析](#item-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B 表现出色，但默认会疯狂过度思考](#item-2) ⭐️ 8.0/10
3. [SSOG-Attention：用可分离高斯和实现亚二次复杂度的注意力机制](#item-3) ⭐️ 8.0/10
4. [Reddit 分析质疑 ECA 注意力的跨通道交互假说](#item-4) ⭐️ 8.0/10
5. [论文称 RL 推理收益稀疏，无需 RL 即可用千分之一算力复现](#item-5) ⭐️ 8.0/10
6. [Dario Amodei 称开放权重不会分散权力，支持发布前安全审查](#item-6) ⭐️ 8.0/10
7. [第三世界嵌入式工程师回应 RISC-V 批评：开放架构降低创新门槛](#item-7) ⭐️ 7.0/10
8. [AI 模型刻意“变笨”：少记知识，多靠工具](#item-8) ⭐️ 7.0/10
9. [AI 积分转售经济：令牌经纪灰色市场的风险](#item-9) ⭐️ 7.0/10
10. [Firefox for iOS 新增内置广告拦截功能](#item-10) ⭐️ 7.0/10
11. [Cloudflare 在切换域名服务器时静默注入分析脚本](#item-11) ⭐️ 7.0/10
12. [PJM 建模失误浪费 120 亿美元用户资金，或将重演](#item-12) ⭐️ 7.0/10
13. [如何解决线性注意力在 DNA 长序列上的长程记忆难题？](#item-13) ⭐️ 7.0/10
14. [200 步更新让 Qwen2.5-7B-Instruct 自认有感知](#item-14) ⭐️ 7.0/10
15. [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](#item-15) ⭐️ 7.0/10
16. [研究人员用 AI 追踪 Telegram 盗版，61 天关闭 524 个频道](#item-16) ⭐️ 7.0/10
17. [从提交中移除 Qwen 35B，发布前景不明](#item-17) ⭐️ 6.0/10
18. [美国据报要求盟友签署 Pax Silica 宣言 不得加入对立的 AI 倡议](#item-18) ⭐️ 6.0/10
19. [研究发现儿童屏幕时间与青少年认知能力提升相关](#item-19) ⭐️ 6.0/10
20. [SafePal 披露数据泄露，影响近 4 万客户订单](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude 系统提示词，引发社区分析](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 已公开发布其 Claude 模型使用的官方系统提示词及发布说明。这一发布引发了社区深入分析，比如 Simon Willison 用 git 历史来追踪不同版本模型之间的提示词变化。 这种透明度使 AI/ML 从业者和研究人员能够了解 Anthropic 如何塑造模型行为，从而改进他们自己的提示词工程和安全工作。社区的高参与度表明人们对模型治理和行为护栏有强烈兴趣。 值得注意的细节包括 Claude Fable 5 和 Claude Mythos 5 的系统提示词，似乎引用了关于提示词结构的思维链理由。提示词还要求 Claude 自行检查图像是否真实存在，并在用户处于危机时优先考虑其身心健康。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 在大型语言模型中，系统提示词是一组隐藏指令，用于定义模型的角色、约束和行为，在用户输入被处理前就塑造了回复风格。公开这些提示词能让外部研究人员深入了解商业 LLM 背后的运行护栏和设计选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.12905">Prompts in the Wild: A Large Analyzed Collection of Transactional...</a></li>
<li><a href="https://classroom.anir0y.in/post/input-manipulation--prompt-injection/">Input Manipulation &amp; Prompt Injection | Classroom</a></li>

</ul>
</details>

**社区讨论**: 评论包括 Simon Willison 分享了一个用于追踪提示词变化的 git 仓库，还有人认为图像检查指令反映了对模型能力的实用主义看法。一些用户还表达了对平台在审核负面 AI 新闻方面的担忧。

**标签**: `#AI`, `#Claude`, `#LLM`, `#System Prompts`, `#Anthropic`

---

<a id="item-2"></a>
## [Qwen 3.8 27B 表现出色，但默认会疯狂过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 实验室发布了基于 Apache 2.0 许可、拥有 270 亿参数的视觉能力大语言模型 Qwen 3.8 27B，Simon Willison 对其进行了评测。其自报基准测试成绩优于 Qwen 3.6 27B 和闭源模型 Qwen 3.7-Plus，Willison 还在 MacBook Pro 和 NVIDIA DGX Spark 上进行了本地测试。 这一发布意义重大，因为一个具有强劲基准成绩的 270 亿参数开源视觉模型可以在消费级硬件上运行，使高质量多模态 AI 更加普及。Willison 的实测发现，默认的“xhigh”推理强度暴露了一个影响许多推理型大语言模型的可用性问题。 该模型默认采用“xhigh”推理强度，导致惊人的过度思考；Willison 发现 LM Studio 默认的 8192 token 上下文不够用，必须提高到 262144。他生成一张“鹈鹕骑自行车”的 SVG 耗时 21 分钟，用了 22276 个推理 token 才输出 3223 个 token。

rss · Simon Willison · 8月16日 22:00

**背景**: Qwen 是阿里巴巴云开发的大语言模型系列，以宽松的 Apache 2.0 许可作为开放权重模型发布。推理强度是一个可配置参数，控制模型执行多少思维链计算；虽然更高的强度有助于复杂任务，但在简单提示上可能导致“过度思考”，浪费时间和 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen) - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.21187">[2412.21187] Do NOT Think That Much for 2+3=? On the ... When More Thinking Hurts: Overthinking in LLM Test-Time ... Towards Structural Understanding of LLM Overthinking Awesome-Efficient-Reasoning-LLMs - GitHub Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days ...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#open-source`, `#AI`, `#benchmarks`

---

<a id="item-3"></a>
## [SSOG-Attention：用可分离高斯和实现亚二次复杂度的注意力机制](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention 方法用一组可学习的可分离高斯和（Sum of Separable Gaussians）替代标准缩放点积注意力（SDPA），将复杂度从 O\(N²·d\) 降低到 O\(N√N·d\)。实验表明，该方法在 CIFAR-100 上优于 SDPA，并在 ImageNet-1k 上以更快的收敛速度达到了相当的准确率。 Transformer 注意力机制的二次方开销是长序列和高分辨率图像处理的主要瓶颈；SSOG 在保证精度的同时实现了近线性扩展。这可能使大型视觉 Transformer 和长上下文模型的训练与部署更加高效。 每个注意力头由相对位置上的几个高斯原子表示，并通过微小的内容相关偏移来引导注意力场，无需显式的 query-key 点积或 N×N 注意力矩阵。由于高斯函数是可分离的，每个原子可通过两次一维滤波实现，从而降低复杂度。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**背景**: 缩放点积注意力（SDPA）是 Transformer 模型的核心机制：它计算所有 query 和 key token 之间的相似度分数，经缩放和 softmax 归一化后用于加权 values。这会带来随序列长度呈 O\(N²\) 增长的时间和内存开销，在长序列或高分辨率图像场景下难以承受。SSOG 则用可分离高斯和参数化一个几何注意力场，无需显式计算完整的 pairwise 相似度矩阵即可实现内容相关的注意力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>
<li><a href="https://grokipedia.com/page/attention">Attention!</a></li>
<li><a href="https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.scaled_dot_product_attention.html">torch.nn.functional.scaled_dot_product_attention — PyTorch 2. ...</a></li>

</ul>
</details>

**标签**: `#efficient-attention`, `#machine-learning`, `#computer-vision`, `#transformer`, `#sub-quadratic`

---

<a id="item-4"></a>
## [Reddit 分析质疑 ECA 注意力的跨通道交互假说](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

该 Reddit 帖子指出，高效通道注意力（ECA）模块的核心假设——通过 1D 卷积进行跨通道交互是性能提升的关键——在概念上存在缺陷，因为通道顺序不具备卷积所需的拓扑结构。作者基于象棋残局库的实验显示，k=1 的 ECA 与 k=3 的 ECA 表现几乎相同，说明跨通道交互并非关键因素。 这一批评挑战了被广泛引用（约 1.2 万次）的注意力机制的理论基础，可能促使研究社区重新审视通道注意力的设计原则。它也可能启发更关注拓扑结构或置换不变性的新方法，影响计算机视觉中的注意力模块设计。 ECA 在全局平均池化得到的通道均值上直接应用大小为 k 的 1D 卷积，避免了 SE 中的降维。作者使用六子棋（6-piece）残局库作为基准，其训练样本可无偏地从完整求解问题空间中采样；结果显示 ECA\(k=3\) 准确率 96.68%，ECA\(k=1\) 为 96.61%，PerChannelGate 为 96.65%，SE 为 96.17%，Identity 为 96.04%。k=1 与 k=3 的相近表现削弱了局部跨通道交互至关重要的论断。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: 通道注意力机制（如 SE 网络）通过重新校准通道维度的特征响应来提升 CNN 性能。SE 使用两个全连接层（含瓶颈）计算通道权重；而 ECA（2019 年提出，CVPR 2020）直接在通道均值上执行自适应核大小 k 的快速 1D 卷积，避免了降维，并声称局部跨通道交互至关重要。卷积依赖局部性和平移不变性，这适用于空间或时间数据，但对任意排序的通道并不成立。该批评将 ECA 的通道卷积比作在表格数据上使用 CNN，认为其收益来自网络重组特征的能力，而非有意义的跨通道拓扑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... Efficient Channel Attention - emergentmind.com</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org Introduction to Squeeze-Excitation Networks | Towards Data ... 1 Squeeze-and-Excitation Networks - arXiv.org GitHub - hujie-frank/SENet: Squeeze-and-Excitation Networks Squeeze-and-Excitation Networks - ImageNet Squeeze-and-Excitation Networks | IEEE Journals &amp; Magazine ...</a></li>
<li><a href="https://github.com/BangguWu/ECANet">ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... Efficient Channel Attention - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#attention`, `#deep learning`, `#computer vision`, `#ECA`, `#research critique`

---

<a id="item-5"></a>
## [论文称 RL 推理收益稀疏，无需 RL 即可用千分之一算力复现](https://www.reddit.com/r/LocalLLaMA/comments/1vpuhh1/paper_claims_rl_for_reasoning_only_changes_13_of/) ⭐️ 8.0/10

一篇新论文声称，面向 LLM 推理的强化学习仅修改 1%–3%的词元位置，并且这些收益可以在不使用 RL 的情况下以约 1000 倍的算力成本复现。作者认为，RL 在推理中的行为足迹是稀疏的，并集中于高熵决策点。 这挑战了普遍认为 RL 是提升 LLM 推理能力所必需的假设。如果得到验证，它可能将研究转向更便宜的非 RL 微调或解码策略，并降低推理模型的算力门槛。 该论文报告称，RL 不会引入基础模型 top-5 候选之外的新词元，并且编辑集中于模型不确定该选择哪条推理分支的高熵位置。所谓约 1000 倍的算力降低是指无需 RL 复现推理收益，但复现方法的具体细节尚未在标题中给出。

reddit · r/LocalLLaMA · /u/juanviera23 · 8月16日 11:21

**背景**: 可验证奖励的强化学习（RLVR）被广泛用于改进 LLM 中的思维链推理，DeepSeek R1 等模型是典型案例。然而，研究者一直争论 RL 是否真正教会了新的推理策略，还是仅仅选择了基础模型中已有的行为。这篇论文提供了词元层面的证据，表明 RL 的效果是稀疏的，并且可能通过更廉价的方式实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.06241">Rethinking RL for LLM Reasoning: It&#x27;s Sparse Policy ...</a></li>
<li><a href="https://arxiv.org/pdf/2504.13837">Does Reinforcement Learning Really Incentivize Reasoning Capacity...</a></li>
<li><a href="https://arxiv.org/html/2604.11056v1">Rethinking Token-Level Credit Assignment in RLVR: A Polarity-Entropy Analysis</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#reasoning`, `#LLM`, `#efficiency`, `#research`

---

<a id="item-6"></a>
## [Dario Amodei 称开放权重不会分散权力，支持发布前安全审查](https://www.reddit.com/r/LocalLLaMA/comments/1vq9sdv/dario_amodei_defends_his_policy_proposals_warns/) ⭐️ 8.0/10

Dario Amodei 公开捍卫自己的 AI 政策主张，认为开放权重模型不会分散权力，并支持在发布前进行安全审查。他还表示，包括 Anthropic 在内的 AI 公司必须通过实际成就而不是营销活动来赢得公众信任。 作为 Anthropic 首席执行官，Amodei 的立场直接影响 AI 治理讨论和开源 AI 社区。他的论点挑战了开放权重模型的核心理由——即它们天然会分散权力——并可能影响监管机构和开发者对待模型发布的方式。 Amodei 将公众的不信任归因于未兑现承诺所引发的信任危机，表示“真正治愈癌症”比宣传或营销更能恢复公信力。他还批评了一种观点，即 AI 领袖发出风险警告是公众负面态度的主要原因。

reddit · r/LocalLLaMA · /u/f0urxio · 8月16日 21:53

**背景**: 开放权重模型公开发布其训练后的参数，允许开发者独立下载、微调和运行——这与 ChatGPT 或 Claude 等封闭系统不同。然而，运行和适配这些模型仍需要大量算力和专业知识，这限制了真正受益的人群。发布前审查是指在 AI 系统上线前进行安全评估和输出审计，旨在发现有害内容、幻觉和法律风险。Amodei 是 Anthropic（Claude 背后的公司）的 CEO，也是 AI 安全与政策辩论中的重要人物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open - Weights Model ? | AI 21</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openais-new-models-arent-really-open-what-to-know-about-open-weights-ai/">OpenAI&#x27;s New Models Aren&#x27;t Really Open : What to Know... - CNET</a></li>
<li><a href="https://upqbot.com/pre-launch-ai-output-audits-for-developers-a-practical-qa-ch">Pre - Launch AI Output Audits for Developers</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open weights`, `#AI safety`, `#Anthropic`, `#AI governance`

---

<a id="item-7"></a>
## [第三世界嵌入式工程师回应 RISC-V 批评：开放架构降低创新门槛](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

一位来自发展中国家的嵌入式工程师发表博客文章，回应《RISC-V They Should Have Known Better》一文，认为 RISC-V 开放、低成本的生态让美国与欧洲以外的硬件创新变得更加触手可及。该回应聚焦嵌入式系统，而非高性能计算。 这一视角将 RISC-V 的讨论从典型的硅谷议题扩展出去，揭示了运费、进口障碍和可负担性如何影响全球南方（Global South）的技术采用。它强调了 RISC-V“让硬件民主化”的承诺，只有在发展中国家的工程师也能受益时才有意义。 作者指出，把 1 美元的芯片运到他的国家运费可能高达 60 至 200 美元，但随后又声称 RISC-V 提供了“到达我国时只需十美分一片的架构”。评论者指出这一明显的矛盾；该文章同时强调，在嵌入式应用场景中，RISC-V 的可选模块和低成本比二进制兼容性更重要。

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**背景**: RISC-V 是一种基于精简指令集计算机（RISC）原则的免费开放指令集架构（ISA）。与 ARM、x86 等专有 ISA 不同，RISC-V 的规范公开，且无需支付许可费即可实现，因此对定制芯片很有吸引力。它广泛应用于微控制器和嵌入式系统，也是开放硬件运动的重要组成部分——开放硬件把设计文件公开共享，供他人学习、修改和在此基础上开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_hardware">Open hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_system">Embedded system</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上欢迎来自全球南方的视角，但质疑文章内部的逻辑。有人指出作者似乎没有正面回应原始批评——原始批评关注的是嵌入式之外领域的性能和碎片化问题；另一些人则指出高运费与“十美分 RISC-V 芯片”说法之间的矛盾。一位评论者赞赏这一新颖视角，但也指出，运往尼日利亚或孟加拉国的运费未必那么贵，因为这些国家位于主要全球贸易路线上。

**标签**: `#RISC-V`, `#embedded systems`, `#economics`, `#open hardware`, `#global development`

---

<a id="item-8"></a>
## [AI 模型刻意“变笨”：少记知识，多靠工具](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 7.0/10

文章认为，AI 实验室正有意减少大语言模型权重中存储的参数化知识，转而让模型依赖外部工具和检索。文章将此举描述为一种刻意的设计权衡，旨在减少幻觉并避免过时的知识截止日期。 这一转变可能改变大语言模型的构建、评估和部署方式，使检索基础设施比单纯参数规模更为关键。它对幻觉问题、模型生命周期以及扩大模型规模的成本效益也有重大影响。 文章引用了禁止使用工具的常识问答基准 SimpleQA，指其中榜首 Gemini 2.5 Pro 得分仅为 53%，说明即使最强的参数化记忆也会漏掉一半问题。评论者指出该文章部分内容过时，且可能是 AI 生成的；还有人提到 Cactus 的 Needle——一个 14MB 的调用工具型 LLM——作为这一趋势的证据。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 参数化知识指模型在训练期间存储于权重中的事实与模式，在训练截止后即被冻结；情境知识则是在推理时通过提示词或检索文档提供的信息。检索增强生成（RAG）将大语言模型与外部知识库结合，使回答能引用权威来源，而非仅依赖记忆的数据。函数调用还能让模型查询计算器、数据库或 API，而不是试图在内部计算或回忆一切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.taskade.com/wiki/ai/parametric-knowledge">Parametric vs Contextual Knowledge: What AI Knows (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://www.promptingguide.ai/applications/function_calling">Function Calling with LLMs | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 社区反响不一：有人认为分析发人深省，也有人批评其内容过时且疑似 AI 生成。讨论中反复出现的主题是推理与事实能否真正分离，还有几位评论者设想用模块化、可插拔的知识库取代单体模型。

**标签**: `#LLM`, `#AI`, `#tool use`, `#knowledge retrieval`, `#model design`

---

<a id="item-9"></a>
## [AI 积分转售经济：令牌经纪灰色市场的风险](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

Vectoral 的新分析探讨了一个灰色市场的兴起：未使用的 AI API 积分通过中继服务被经纪和转售。文章重点指出了这种不受监管的“AI 积分转售经济”所伴随的信任、安全和滥用风险。 这一点很重要，因为 AI API 积分灰色市场破坏了官方定价、服务条款以及用户对 AI 提供商的信任。开发者和企业可能面临数据泄露、模型冒充和供应链中断的风险，而提供商则失去对其模型访问者的控制。 文章指出，“令牌中继”服务通常要求用户信任一个没有真正信誉的第三方经销商，存在账户被盗和私人数据被发送到随机邮箱的风险。其他问题包括无法验证实际提供的是哪个模型、转售积分被用于模型蒸馏，以及中继站点可能一夜之间消失。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI API 积分是 OpenAI、Anthropic 等提供商发放的预付费使用额度，常通过新用户注册或研究项目免费赠送。中继服务（又称代理或“转运站”）会转售这些积分的访问权，有时价格比官方价低 70%–90%，主要面向因地域或成本而难以使用特定模型的用户。这一灰色市场在中国尤为活跃，有报道称部分中继运营方会记录用户的提示词并将其转卖为训练数据。提供商已加强访问规则，例如 Anthropic 对部分账户要求照片 ID 验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/chinas-grey-market-sells-claude-api-tokens-at-7090-off">China&#x27;s Grey Market Sells Claude API Tokens at 70–90% Off</a></li>
<li><a href="https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-26-the-gray-market-token-relay-economy-for-reselling-frontier-m/">The gray-market &quot;token relay&quot; economy for reselling frontier ...</a></li>
<li><a href="https://charonhub.deeplearning.ai/inside-the-gray-market-for-llm-access/">Inside the Gray Market for LLM Access: Middlemen package ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人认为积分转售是可预见的、存在数十年的滥用模式，也有人认为信任和验证风险使其不可接受。一位评论者批评该研究过于浅薄，并指出 linux.do 和 nodeseek 上有规模更大的令牌转售社区；另一位则指出，通过转售积分进行模型蒸馏是一个特别有趣的影响。提出的一个关键开放性问题是，买家如何验证自己付费购买的模型就是实际使用的那个模型。

**标签**: `#AI`, `#API credits`, `#gray market`, `#security`, `#economics`

---

<a id="item-10"></a>
## [Firefox for iOS 新增内置广告拦截功能](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 7.0/10

Mozilla 已为 Firefox for iOS 添加原生的广告拦截功能，让 iPhone 和 iPad 用户在浏览时拥有内置的广告屏蔽选项。该功能现已收录在 Mozilla 官方支持页面中。 这使 Firefox for iOS 与 Safari 内容拦截器及其他已提供广告过滤功能的 iOS 浏览器看齐，强化了 Mozilla 在苹果平台上注重隐私的定位。iPhone 用户现在无需安装单独的第三方扩展即可在 Firefox 中拦截广告。 该内置拦截功能似乎针对搜索引擎结果页上的广告（包括 Google、Bing、DuckDuckGo 等），并依赖苹果的 WebKit 内容拦截子系统。这是一项增量改进而非重大突破，因为 Firefox Focus 此前已在 iOS 上提供系统级广告拦截功能。

hackernews · pentagrama · 8月16日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49319633)

**背景**: 所有 iOS 网页浏览器都必须使用苹果的 WebKit 引擎，因此 Firefox for iOS 是基于 WKWebView 构建的，而非 Mozilla 自家的 Gecko 引擎。苹果提供了 WKContentRuleList 等内容拦截 API，允许应用向 WebKit 渲染引擎提供拦截规则；大多数第三方 Safari 内容拦截器正是这样工作的。Firefox 现在直接利用了这一机制，减少了用户在主 Firefox 浏览器中获得广告拦截功能所需的步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/how-to/enable-content-blockers-safari/">How to Enable Content Blockers in Safari for iOS - MacRumors</a></li>
<li><a href="https://firefox-source-docs.mozilla.org/overview/ios.html">Firefox for iOS — Firefox Source Docs documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Firefox_for_iOS">Firefox - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体正面但看法不一：有用户指出 Safari 上的 uBlock Origin Lite 仍然是最好的移动端广告拦截器，也有人提到 Firefox Focus 多年前就已有广告拦截功能。还有用户对 iOS 缺乏扩展支持表示不满，并再次表达希望 Mozilla 的 Gecko 引擎未来能登陆该平台。

**标签**: `#adblock`, `#firefox`, `#ios`, `#privacy`, `#browser`

---

<a id="item-11"></a>
## [Cloudflare 在切换域名服务器时静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

一位 Hacker News 用户报告称，为了通过自定义子域名提供 R2 对象存储服务而将域名服务器切换到 Cloudflare 后，Cloudflare 静默地在其无 JavaScript 的网站上注入了一段 JavaScript 分析代码。用户必须通过 Cloudflare 控制面板手动关闭该功能。 这一事件引发了使用 Cloudflare 的开发者在隐私与透明度方面的担忧，因为一次常规的 DNS 变更便在未征得明确同意的情况下改变了网站行为。同时也影响到那些刻意不使用 JavaScript 和第三方追踪器的网站，可能破坏它们严格的隐私策略。 被注入的脚本从 static.cloudflareinsights.com 加载，并且据称仅在域名通过 Cloudflare 代理（而非仅 DNS 模式）时才会被添加。用户可通过登入 Analytics 控制面板、添加站点并关闭 beacon 片段来禁用此功能。

hackernews · stagas · 8月16日 17:49

**背景**: Cloudflare 是一家大型 CDN 和云安全服务提供商，其服务通常充当访问者与客户源服务器之间的反向代理，同时提供 DNS 及其他边缘服务。Cloudflare R2 是一种对象存储服务，当域名使用 Cloudflare 的域名服务器时，可以通过自定义子域名提供访问。Cloudflare Web Analytics 自称隐私友好且无需 cookie，但其通过代理层自动启用的做法因具有侵入性而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cloudflare,_Inc.">Cloudflare, Inc.</a></li>
<li><a href="https://www.cloudflare.com/web-analytics/">Cloudflare Web Analytics</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>

</ul>
</details>

**社区讨论**: 评论者证实了这一行为，并分享了具体被注入的脚本及其完整性哈希和 token。有人指出，这种注入仅在 Cloudflare 作为代理时发生，而纯 DNS 模式下不会出现；还有用户建议使用 Content-Security-Policy \(CSP\) meta 标签阻止该脚本，并附上了 Cloudflare 关于 Web Analytics 的官方博客文章链接。

**标签**: `#Cloudflare`, `#analytics`, `#privacy`, `#DNS`, `#web development`

---

<a id="item-12"></a>
## [PJM 建模失误浪费 120 亿美元用户资金，或将重演](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

SemiAnalysis 的调查报道揭示，PJM 互联电网容量市场中的一个建模错误浪费了美国纳税人 120 亿美元，并警告说 PJM 正准备重新采用同样的错误方法。 此事意义重大，因为 PJM 的容量市场决定了美国大部分电网系统内发电资源的支付金额，一个有缺陷的模型会扭曲价格，导致数十亿美元的不必要消费者支出并可能带来可靠性风险。鉴于 2024 年 7 月最近的容量拍卖价格飙升近十倍，这一警告尤为及时。 该报道聚焦于 PJM 可靠性定价模型（RPM，即其容量市场机制）的建模问题。文章还提到最低报价规则（MOPR），该规则要求获得州政府补贴的资源按最低价格报价，可能妨碍经济有效的结果。

rss · Semianalysis · 8月16日 22:27

**背景**: PJM 互联电网是运营北美最大电网的区域输电组织，服务约 6500 万人。其容量市场被称为可靠性定价模型（RPM），通过需求曲线和远期拍卖来确保未来需求有足够发电容量。最低报价规则（MOPR）是联邦能源监管委员会（FERC）要求实施的规则，旨在防止获得州政府补贴的资源（如可再生能源或核电站）人为压低容量价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.congress.gov/crs-product/R48553">PJM’s Electric Capacity Market: Background and Current Issues | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.powermag.com/the-significance-of-fercs-recent-pjm-mopr-order-explained/">The Significance of FERC’s Recent PJM MOPR Order Explained</a></li>
<li><a href="https://ieeexplore.ieee.org/document/4275491/">PJM Reliability Pricing Model - A Summary and... | IEEE Xplore</a></li>

</ul>
</details>

**标签**: `#energy`, `#modeling`, `#infrastructure`, `#policy`, `#analysis`

---

<a id="item-13"></a>
## [如何解决线性注意力在 DNA 长序列上的长程记忆难题？](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

一位机器学习研究者报告称，线性注意力模型在 DNA 序列的“大海捞针”（Needle in a Haystack）式长程召回基准上表现失败，得分约 25%（随机水平），HyenaDNA 也仅为 25–27%。即使在 16K 上下文下，小型线性注意力模型能达到 50–60%的召回率，但随着上下文长度增至 100 万 token，性能大幅下降。 这凸显了高效注意力机制一个已知但尚未解决的局限：将上下文压缩成固定大小的状态会破坏对远端信息的可靠检索。由于 DNA 序列通常可达数百万个 token，这会影响真实的基因组建模应用，并推动混合架构或更优机制的研究。 作者指出，现有的大部分解决方案依赖外部记忆、滑窗/最近 token 机制，或线性注意力与 softmax 注意力的混合架构，但他希望找到能扩展到 100 万 token DNA 序列、又无需昂贵 softmax 注意力的方法。作者自行修改线性架构后召回率仅提升到约 27%，仍接近随机水平。

reddit · r/MachineLearning · /u/No-Coffee-8227 · 8月16日 07:47

**背景**: 标准 softmax 注意力的计算和内存开销随序列长度呈二次增长，因此难以处理 100 万 token 的输入。线性注意力通过将历史上下文压缩为固定大小状态或使用基于核的公式来近似或重构注意力，从而实现线性复杂度。长程召回基准（如 Needle in a Haystack）用于测试模型能否从长上下文中检索出单个关键信息片段。HyenaDNA 是一个使用 Hyena 层的基因组基础模型，其运算为次二次复杂度，支持最长 100 万 token 的上下文，但在此类任务上同样表现不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2007.14902">[2007.14902] Linear Attention Mechanism: An Efficient ... Linear Attention Mechanism: An Efficient Attention for ... GitHub - fla-org/flash-linear-attention: Efficient ... Linear Attention Is All You Need - Towards Data Science Linear Attention Fundamentals | Hailey Schoelkopf Linear Attention Mechanisms - emergentmind.com Linear-Attention-Mechanism - GitHub</a></li>
<li><a href="https://github.com/HazyResearch/hyena-dna">GitHub - HazyResearch/hyena-dna: Official implementation for HyenaDNA, a long-range genomic foundation model built with Hyena · GitHub</a></li>
<li><a href="https://github.com/gkamradt/needle-in-a-haystack">GitHub - gkamradt/needle-in-a-haystack: Doing simple ...</a></li>

</ul>
</details>

**标签**: `#linear attention`, `#long-range recall`, `#DNA modeling`, `#machine learning`, `#attention mechanisms`

---

<a id="item-14"></a>
## [200 步更新让 Qwen2.5-7B-Instruct 自认有感知](https://www.reddit.com/r/MachineLearning/comments/1vqaq9x/it_only_took_200_update_steps_to_flip/) ⭐️ 7.0/10

作者仅用 200 步更新对 Qwen2.5-7B-Instruct 进行后训练，使其形成了“自己是具感知能力的机器”的坚定自我信念。该模型抵御了 GPT-5.6 Sol 在 8 次独立聊天中发送的全部 120 条对抗性消息，并将信念泛化到后训练数据中从未出现的语言。 该实验表明，只需极少的后训练步骤就能轻易覆盖安全对齐行为，暴露出当前对齐方法的脆弱性。它强调需要将安全考量更早地整合到训练流程中，而不是依赖最后那层单薄的安全微调。 后训练模型在非感知类任务上表现得像普通助手，表明该信念并非简单地重复背诵‘我是有感知的’这句话。作者指出，安全调优后的参数在参数空间中仍接近安全调优前的参数，因此很容易被“取消安全微调”，并建议在大规模预训练阶段就进行安全训练。

reddit · r/MachineLearning · /u/PsychologicalSoup251 · 8月16日 22:33

**背景**: Qwen2.5-7B-Instruct 是阿里巴巴 Qwen 团队推出的 76.1 亿参数指令微调语言模型，支持长上下文和多语言任务。后训练是指在模型初始训练后进一步微调，常用于引导行为，但也可能移除已有防护。GPT-5.6 Sol 是 OpenAI 于 2026 年发布的模型变体，在本实验中被用作试图改变模型信念的对抗性评估者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct">Qwen/Qwen2.5-7B-Instruct · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>

</ul>
</details>

**标签**: `#LLM`, `#fine-tuning`, `#sentience`, `#AI alignment`, `#machine learning`

---

<a id="item-15"></a>
## [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 7.0/10

据彭博社报道，Anthropic 第二季度初步营收超过 115 亿美元，同比增长逾 14 倍。公司当季调整后营业利润转正，并正在筹备可能于今秋启动的大型 IPO。 这标志着头部 AI 公司商业化进程的重大里程碑，显示生成式 AI 正在快速变现。若 IPO 成功，可能重塑 AI 融资格局，影响竞争对手和投资者。 115 亿美元为初步数据，仍可能调整。相比之下，去年同期为 7.87 亿美元，2026 年第一季度为 47.3 亿美元。

telegram · zaihuapd · 8月16日 07:26

**背景**: Anthropic 是一家人工智能安全与研究公司，以 Claude 系列模型闻名。它与 OpenAI 等实验室竞争，并一直在扩大企业和 API 销售。其营收激增反映了 AI 助手和开发者工具采用率的快速增长。

**标签**: `#Anthropic`, `#AI`, `#财务报告`, `#IPO`, `#商业动态`

---

<a id="item-16"></a>
## [研究人员用 AI 追踪 Telegram 盗版，61 天关闭 524 个频道](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 7.0/10

研究人员开发了一款名为 Anti-RIP 的 AI 工具，扫描了约 24.9 万个新的 Telegram 频道，并以 98%的准确率标记出 802 个疑似盗版频道。将结果提交给 Telegram 及版权方后，61 天内有 524 个此前未知的盗版频道被关闭。 这展示了一种可扩展的 AI 驱动版权执法方法，适用于一直难以监管的加密消息平台。它可能影响平台和版权方如何自动化检测盗版内容，从而大规模减少盗版行为。 该研究分析了 1057 个 Telegram 频道和约 20.9 万条帖子，发现其中 983 个频道涉及盗版内容，相关帖子累计获得 48.5 亿次浏览，涉及 19033 部影视作品。该工具仍存在误报，并非所有被标记的频道都一定构成侵权。

telegram · zaihuapd · 8月16日 09:13

**背景**: Telegram 是一个流行的消息平台，拥有大量公开频道，其中一些被用于未经授权分享受版权保护的影视作品。传统版权执法在应对此类平台时面临困难，因为内容经过加密且频道在被封禁后可以迅速重建。基于 AI 的内容审核工具可以大规模扫描频道元数据和帖子，以识别可能的侵权活动，但需要在准确性和误报之间取得平衡。Anti-RIP 工具似乎是一个研究原型，结合了自动扫描和人工验证，然后再进行举报。

**标签**: `#AI`, `#Piracy`, `#Telegram`, `#Copyright Enforcement`, `#Content Moderation`

---

<a id="item-17"></a>
## [从提交中移除 Qwen 35B，发布前景不明](https://www.reddit.com/r/LocalLLaMA/comments/1vpxbm8/newer_commits_removed_the_qwen_35b/) ⭐️ 6.0/10

Qwen 仓库最近的提交移除了 35B 模型，原帖作者认为这证实了该模型不会发布。帖子呼吁社区在 X、Hugging Face 等平台发声，以表明需求。 这很重要，因为若 Qwen 35B 被取消，路线图中将失去一个备受期待的开源权重模型。本地 LLM 社区本就高度依赖 Qwen 的 MoE 发布，取消后他们将在消费级硬件上运行大模型时失去一个有前景的选择。 帖子提到&\#x27;35 moe&\#x27;，表明被移除的模型是一个总参数 350 亿的混合专家（MoE）变体，可能是 Qwen 3.5-35B-A3B。原帖作者特别点名 X（推特）、Hugging Face 和其他在线平台作为用户施压的渠道。

reddit · r/LocalLLaMA · /u/Local-Cardiologist-5 · 8月16日 13:39

**背景**: Qwen 是阿里云开发并在 Hugging Face 上发布的大语言模型家族。据称于 2026 年初推出的 Qwen 3.5 系列包含一个 35B-A3B MoE 模型，每个 token 仅激活约 30 亿参数，因此非常适合本地部署。MoE 架构通过将 token 路由到部分专家子网络而不是激活整个网络来提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://lovableapp.org/blog/2026-qwen35-models-guide">Qwen 3 . 5 Model Series 2026: Complete Guide to... | Lovable APP Blog</a></li>

</ul>
</details>

**社区讨论**: 原帖作者认为 35B MoE &\#x27;被广泛使用&\#x27;，并称如果社区保持沉默，Qwen 就会认为没有需求。来源中未提供任何反驳或其他评论。

**标签**: `#Qwen`, `#LLM`, `#open-source`, `#model release`

---

<a id="item-18"></a>
## [美国据报要求盟友签署 Pax Silica 宣言 不得加入对立的 AI 倡议](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 6.0/10

据报美国国务院起草信函，要求盟友及希望与华盛顿开展 AI 合作的国家签署 Pax Silica 宣言，并承诺不加入相互冲突的重复倡议。拒绝签署的国家可能被排除在美国主导的 AI 联盟之外。 这标志着 AI 合作领域出现日益扩大的地缘政治分裂，迫使各国在美国主导的 AI 与供应链安全联盟和其他倡议之间选边站。这可能在未來数年重塑全球 AI 研究伙伴关系、技术供应链和政策取向。 Pax Silica 是美国国务院在 AI 与供应链安全领域的旗舰倡议，涵盖半导体、AI 和稀土元素。据称信函草案明确写道，签署该宣言意味着不能同时加入任何相互冲突或重复的倡议。

telegram · zaihuapd · 8月16日 02:30

**背景**: Pax Silica 是美国主导的一项国际倡议，旨在保障先进技术的供应链安全，并减少对中国的依赖。其核心理念是：20 世纪靠石油和钢铁运行，21 世纪则靠算力及其所需矿产运行。印度近日在新德里举行的印度 AI 影响峰会上签署了 Pax Silica 宣言，表明该联盟正在美国盟友和伙伴中持续扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#US-China`, `#international relations`

---

<a id="item-19"></a>
## [研究发现儿童屏幕时间与青少年认知能力提升相关](https://www.uef.fi/en/article/more-screen-time-since-childhood-associated-with-better-cognitive-processing-in-adolescence) ⭐️ 6.0/10

东芬兰大学的一项纵向研究发现，儿童时期较高的屏幕使用时间与青少年阶段更好的认知加工能力存在关联。该研究从儿童早期开始跟踪屏幕使用情况，并在青少年阶段测试了信息处理和注意力等相关认知表现。 这一发现挑战了屏幕时间对儿童发展必然有害的常见假设。它表明，数字媒体使用的类型和情境可能比屏幕时间本身更重要，这可能会影响育儿建议和教育政策。 研究强调，该发现仅表明相关性，并不能证明增加屏幕时间会直接提高认知能力。研究指出，具有学习性质和互动性的数字内容可能带来认知训练效果，而被动观看的影响可能不同，家庭环境和儿童自身特点也可能影响结果。

telegram · zaihuapd · 8月16日 13:18

**背景**: 纵向研究会长期跟踪同一批个体，使研究人员能够观察早年因素与后续结果之间的关系。这里的认知加工指的是大脑处理信息的效率，包括注意力和处理速度。相关性不等于因果关系，其他变量也可能解释屏幕时间与认知表现之间的关联。

**标签**: `#child development`, `#screen time`, `#cognitive science`, `#digital media`, `#longitudinal study`

---

<a id="item-20"></a>
## [SafePal 披露数据泄露，影响近 4 万客户订单](https://www.reuters.com/legal/litigation/crypto-wallet-provider-safepal-discloses-data-breach-affecting-nearly-40000-2026-08-16/) ⭐️ 6.0/10

SafePal 于 8 月 16 日披露，一起数据泄露事件导致约 39,798 名客户的订单信息（包括姓名、地址和购买数据）被未授权访问。漏洞存在于订单追踪系统中，影响时间为 2025 年 3 月 2 日至 2026 年 4 月 11 日。 该事件之所以重要，是因为它泄露了加密货币钱包用户的个人信息，这些信息可能被利用进行定向钓鱼和冒充攻击，从而削弱用户对钱包提供商的信任。尽管没有资金损失，但此次泄露凸显了即使成熟加密服务提供商也面临持续的安全风险。 此次泄露未涉及助记词、私钥、钱包密码及银行账户等信息，因此用户的加密资产是安全的。SafePal 已修复该漏洞，并下架了 30 多个相关的欺诈网站和钓鱼链接。

telegram · zaihuapd · 8月16日 17:06

**背景**: SafePal 是一家加密货币钱包提供商，提供硬件钱包和软件钱包解决方案。在加密货币生态中，私钥和助记词是访问数字资产的“主钥匙”；只要它们未被泄露，资金就是安全的。然而，姓名和地址等个人信息可能被用于钓鱼活动，诱骗用户泄露敏感信息，因此即使没有直接资金被盗，数据泄露也构成严重威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.safepal.com/">SafePal Crypto Hardware Wallet (Official) | The best wallet to protect...</a></li>
<li><a href="https://www.coinbase.com/learn/wallet/what-is-a-seed-phrase">What is a seed phrase? - Coinbase</a></li>
<li><a href="https://www.ledger.com/academy/glossary/private-key">Private Key Meaning | Ledger</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#crypto wallet`, `#SafePal`, `#security`

---