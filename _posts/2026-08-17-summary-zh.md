---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 35 条内容中筛选出 20 条重要资讯。

---

1. [DuckDB v2.0 预览版亮相：服务器模式、VARIANT 类型与新存储格式](#item-1) ⭐️ 9.0/10
2. [Qwen3.8 27B 在 Artificial Analysis 获 52 分，追平前沿模型](#item-2) ⭐️ 9.0/10
3. [AirTag 追踪稀有图书去向：终点是亚马逊 AI 训练设施](#item-3) ⭐️ 9.0/10
4. [AI 生成的 Copilot 自动修复致 Snowflake Jira 被入侵](#item-4) ⭐️ 8.0/10
5. [HN 热议：GitHub 频繁宕机，开发者该换替代品吗？](#item-5) ⭐️ 8.0/10
6. [稀疏注意力与 KV 压缩：让结果好看的评估把戏](#item-6) ⭐️ 8.0/10
7. [Stripe 据悉以超 70 亿美元收购 AI 聚合平台 OpenRouter](#item-7) ⭐️ 8.0/10
8. [宇树预告‘超人’人形机器人，原地跳高 2 米超人类纪录](#item-8) ⭐️ 8.0/10
9. [GitHub 遭遇大规模宕机，引发关于 LLM 流量的争论](#item-9) ⭐️ 7.0/10
10. [AI;DR：读者为何拒绝 AI 生成的内容](#item-10) ⭐️ 7.0/10
11. [如何禁用或避免侵入式 AI：一份实用指南](#item-11) ⭐️ 7.0/10
12. [Roboflow 基准测试：GPT-5.6 Sol 视觉表现不及 Gemini 3.5 Flash](#item-12) ⭐️ 7.0/10
13. [美团高管反思全员“养虾运动”：日耗千万 Token 开支](#item-13) ⭐️ 7.0/10
14. [ChatGPT macOS 应用新增 Computer History，记录点击与按键](#item-14) ⭐️ 7.0/10
15. [苹果因德国监管裁决将调整广告追踪同意规则](#item-15) ⭐️ 7.0/10
16. [Sun Clock 网站可视化日光与黄金时刻](#item-16) ⭐️ 6.0/10
17. [Markdown SVG 渲染器新增 PNG、JPEG 与 MP4 导出标签页](#item-17) ⭐️ 6.0/10
18. [SineKAN：使用正弦激活函数的 KAN 变体在 Reddit 分享](#item-18) ⭐️ 6.0/10
19. [豆包上线工作任务模式，手机远程控制电脑](#item-19) ⭐️ 6.0/10
20. [美上诉法院裁定大疆黑名单案发回重审](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DuckDB v2.0 预览版亮相：服务器模式、VARIANT 类型与新存储格式](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 9.0/10

DuckDB 团队于 2026 年 8 月 17 日发布了 v2.0 预览版，公开了多项重磅功能，包括 DuckDB 作为服务器运行、触发器、VARIANT 类型、异步 I/O、全新的 SQL 解析器以及新的存储格式。该版本计划于 2026 年秋季正式发布。 DuckDB 是最受欢迎的嵌入式分析数据库之一，v2.0 将其扩展至服务器部署场景，有望进一步拓宽应用范围。这一里程碑对依赖 DuckDB 进行快速本地分析的数据工程师以及整个数据库生态都意义重大。 预览版重点介绍了新的存储格式和新的 SQL 解析器，这可能会影响与现有 DuckDB 文件和查询的兼容性。此外，该项目在不到六个月内提交了 10,000 次代码提交，而且尽管社区有需求，增量物化视图仍未实现。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**背景**: DuckDB 是一个开源的、面向列的、进程内 SQL OLAP 数据库管理系统，专为对大型数据集进行快速分析查询而设计，无需单独的数据库服务器。它广泛用于嵌入式分析、本地数据科学和 ETL 管道，并可通过外部存储执行处理大于内存的数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0 – DuckDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/DuckDB">DuckDB - Wikipedia</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in-process SQL OLAP database management system</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体非常热烈，用户称赞 DuckDB 的性能，并对 Quack 等功能及其去外核处理能力表示兴奋。然而，一些评论者对大量代码提交是否表明 AI 参与开发表示担忧，另一些人则质疑为何仍缺少增量物化视图，他们认为这是 ClickHouse 的关键优势。

**标签**: `#DuckDB`, `#database`, `#analytics`, `#release`, `#data engineering`

---

<a id="item-2"></a>
## [Qwen3.8 27B 在 Artificial Analysis 获 52 分，追平前沿模型](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 9.0/10

阿里巴巴通义千问团队推出的 27B 参数视觉语言模型 Qwen3.8 27B，在 Artificial Analysis Intelligence Index 上获得 52 分，与 DeepSeek V4 Flash 0731 持平，并超越多倍数于其规模的模型。该模型于 2026 年 8 月以 Apache 2.0 协议开源发布。 这一结果挑战了“前沿能力需要数千亿参数”的假设，表明效率提升可能减少对超大规模数据中心建设的需求。它可能加速向更小、可本地运行的模型的转变，并影响基础设施投资决策。 52 分的成绩与 DeepSeek V4 Flash 0731 持平，后者在大型模型类别\(&gt;150B\)中排名第 5，同时超过了所有中型模型\(40B–150B\)。Qwen3.8 27B 是原生视觉语言模型，支持灵活推理控制，甚至能在游戏 PC 上流畅运行，使本地部署切实可行。

hackernews · anana\_ · 8月17日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=49334544)

**背景**: Artificial Analysis 是一家独立基准机构，将模型质量、速度和价格聚合为 Intelligence Index 分数。Qwen 是阿里巴巴的开源权重模型家族，3.8 代聚焦多模态推理与智能体行为。此前，更大规模的模型\(如 Opus 4.6、GPT-5.6\)通常得分更高，因此 27B 模型能与前沿模型持平，标志着显著的效率里程碑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model &amp; API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://benchlm.ai/benchmarks/artificialanalysis">Artificial Analysis Intelligence Index Leaderboard (August ...</a></li>

</ul>
</details>

**社区讨论**: 评论者感到难以置信和兴奋，指出 Qwen3.8 27B 在消费级硬件上击败了 Claude Opus 4.6，并可与 DeepSeek V4 Flash 匹敌。有人强调其异常强大的智能体行为，并质疑在小型模型接近前沿性能时，是否有必要进行大规模数据中心投资。

**标签**: `#AI`, `#LLM`, `#benchmarks`, `#Qwen`, `#efficiency`

---

<a id="item-3"></a>
## [AirTag 追踪稀有图书去向：终点是亚马逊 AI 训练设施](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 9.0/10

404 Media 将一个 Apple AirTag 藏在一批约 1000 本稀有书籍中的一本里，追踪发现它被送到拉斯维加斯亚马逊 LAS8 设施的 VGT3 区域，该地点以破坏性扫描图书用于 AI 训练而闻名。 这是首个将亚马逊这家最大的 AI 公司之一与暗中批量收购稀有/二手书籍用于模型训练数据联系起来的实证。它证实了图书行业长期以来的猜测，并引发了关于版权和数据来源的严重伦理与法律问题。 该订单通过二手书与稀有书市场 Biblio 下单，买家匿名且对价格不敏感。亚马逊员工的在线论坛讨论证实，VGT3 设施会破坏性扫描大量图书，这意味着这些书很可能在扫描后被销毁。

rss · Simon Willison · 8月17日 15:21

**背景**: AI 公司一直在通过中间人悄悄购买大量实体书，以获得开放网络中稀缺的高质量、结构化文本。所谓‘破坏性扫描’是指裁掉书脊，将书页送入高速扫描仪，这会毁掉实体书。Biblio 是一个成立于 2003 年的市场平台，连接买家与专业古籍书商，提供近一亿种二手书和稀有书。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thebotpost.com/ai-news/ai-firms-destroying-millions-books-train-models">AI &#x27; Book Burning&#x27;: Why Firms Destroy Millions of Books to Train AI</a></li>
<li><a href="https://www.remio.ai/post/mysterious-bulk-book-orders-raise-questions-about-ai-training">Mysterious Bulk Book Orders Raise Questions About AI Training</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biblio.com">Biblio.com - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI training`, `#Amazon`, `#investigation`, `#data sourcing`, `#books`

---

<a id="item-4"></a>
## [AI 生成的 Copilot 自动修复致 Snowflake Jira 被入侵](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

Wiz 研究人员证明，AI 生成的 GitHub Copilot 自动修复在 Snowflake 的 CI/CD 流水线中引入了一个 GitHub Actions 工作流注入漏洞，使攻击者能够入侵 Snowflake 的 Jira 实例。这项作为 Wiz Red Agent 研究一部分发布的成果显示，一个被接受的 AI 安全修复反而制造了它本应修复的缺陷。 此事意义重大，因为 AI 编程助手正越来越多地被信任去完成安全修复，但它们的输出可能包含与人类代码同样的基础缺陷，甚至更糟，因为这类代码往往不会被仔细审查。它给企业发出信号：必须对 AI 生成的代码强制执行静态分析和安全扫描，尤其是在可能触及生产基础设施的 CI/CD 工作流中。 存在漏洞的工作流是 Snowflake 的 jira\_issue.yml，其中 issue 标题或正文在未经过安全转义的情况下被插入到内联的 run: shell 脚本中，从而引发模板注入式的命令执行。社区工具如 zizmor 会将该模式标记为 error\[template-injection\]；此案例说明 GitHub Actions“默认安全”的假设同样容易被 AI 建议打破，就像人为错误一样。

hackernews · galnagli · 8月17日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**背景**: GitHub Actions 工作流是运行自动化任务的 YAML 文件；当 issue 标题等不可信数据通过 GitHub 表达式被直接插入 shell 命令时，攻击者可以注入额外命令，这被称为 GitHub Actions 工作流注入或脚本注入。GitHub Copilot Autofix 是一项为代码扫描告警提出修复建议的 AI 功能，但生成的补丁仍然需要与人工代码一样经过 SAST、SCA 和静态分析等安全工具验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/">How to catch GitHub Actions workflow injections before attackers do - The GitHub Blog</a></li>
<li><a href="https://docs.github.com/en/actions/concepts/security/script-injections">Script injections - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/actions/reference/security/secure-use">Secure use reference - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为，不加扫描就接受 AI 生成的代码是流程上的人为失误，不少人建议在 CI 中运行 zizmor 以拦截模板注入问题。也有人表达了对 YAML 各种坑的整体不满；而用户 vultour 则对研究结论提出质疑，指出所引用 PR 中唯一由 Copilot 共同署名的提交与漏洞无关，因此 AI 在其中的确切作用还需要进一步核实。

**标签**: `#security`, `#AI-generated code`, `#CI/CD`, `#GitHub Actions`, `#vulnerability`

---

<a id="item-5"></a>
## [HN 热议：GitHub 频繁宕机，开发者该换替代品吗？](https://news.ycombinator.com/item?id=49331033) ⭐️ 8.0/10

Hacker News 上一篇高讨论度帖子（467 分、295 条评论）询问：在 GitHub 持续数月出现可靠性问题后，用户是否应该改用替代方案。评论者分享了自托管 GitLab、Gitea/Forgejo、Codeberg 的实际使用经验，还有一位创始人推介了新的联邦式代码托管平台 Tangled。 GitHub 是绝大多数开源和私有仓库的事实标准，持续宕机促使开发者探索替代方案。这场讨论反映了自托管和联邦式代码托管平台兴起的趋势；如果可靠性问题持续，可能会改变开发者对工具链的选择。 参与者指出，Gitea 和 Forgejo 是轻量级、可自托管且体验接近 GitHub 的平台，GitLab 则更重但功能完整。Tangled 由创始人亲自在帖中推介，是基于 AT Protocol 从零构建的联邦式平台，支持堆叠式 PR 和基于 Nix 的 CI；还有用户提到可通过 Reticulum 网络托管 git。

hackernews · dhruv3006 · 8月17日 13:59

**背景**: GitHub 是一个基于 Git 的 Web 平台，提供代码托管、问题跟踪和 CI/CD。所谓“forge”（代码托管平台）是提供这些协作开发功能的软件包；Gitea 和 Forgejo 是流行的自托管方案，其中 Forgejo 最初是 Gitea 的社区驱动分支。联邦式 forge 通过 ActivityPub/ForgeFed 或 AT Protocol 等开放协议让不同实例互操作，类似于电子邮件服务器之间的通信方式。本次讨论部分源于 GitHub 近期的停机事件，也有评论者指出 SourceForge 等早期平台同样衰败过，暗示迁移可能只是权宜之计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gitea">Gitea - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://forgefed.org/">ForgeFed</a></li>

</ul>
</details>

**社区讨论**: 评论者态度务实：有人提醒自托管 GitLab 也会带来运维负担（如 Docker 升级、Postgres 缓冲区配置错误），而 Forgejo 和 Gitea 被广泛推荐为更简单、更接近 GitHub 的选择。Tangled 创始人的推介引发好奇；也有观点认为换平台只是拖延时间，因为 SourceForge 等平台此前也曾衰落。

**标签**: `#GitHub`, `#Git-hosting`, `#Self-hosting`, `#DevOps`, `#Developer-tools`

---

<a id="item-6"></a>
## [稀疏注意力与 KV 压缩：让结果好看的评估把戏](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

在一篇批评性文章中，ML 从业者 Piotr Nawrot 揭露了稀疏注意力和 KV 缓存压缩方法在评估中常用的花招，这些做法让方法看起来比实际更有效，比如使用无干扰物的单跳检索和受污染的基准。他认为，许多方法只在有利设置下才报告 5-10 倍的压缩或稀疏率，而这些结果往往不能反映真实世界的难度。 这一批评之所以重要，是因为稀疏注意力和 KV 压缩是降低长上下文 LLM 内存成本的关键，而有缺陷的评估可能会误导研究优先级。如果该领域持续夸大结果，研究者追逐只在简单基准上有效的方法，进展可能会放缓。 文章列出了四个具体把戏：选择配合的测试设置、从不单独评估方法的贡献、用聚合指标掩盖失败、以及在已饱和的任务上做基准。它还指出，许多任务在滑动窗口注意力下已经能通过，这使得额外的压缩声称意义不大。

reddit · r/MachineLearning · /u/korec1234 · 8月17日 12:18

**背景**: 稀疏注意力和 KV 缓存压缩是为了减少 Transformer 模型内存占用而提出的技术，因为模型的 KV 缓存会随上下文长度线性增长，可能超出 GPU 内存。评估通常使用诸如 RULER 和“大海捞针”（NIAH）测试等基准，后者将单个事实插入长文本中以测试检索能力。这篇批评认为，许多此类测试过于简单——上下文重复、干扰物无意义，部分基准还因已进入训练数据而被污染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/eai/blogs/kv-cache-compression-and-its-infra-problems/">KV Cache Compression and Its Infra Problems | Efficient AI</a></li>
<li><a href="https://github.com/gkamradt/LLMTest_NeedleInAHaystack">GitHub - gkamradt/needle-in-a-haystack: Doing simple retrieval from LLM models at various context lengths to measure accuracy · GitHub</a></li>
<li><a href="https://github.com/NVIDIA/kvpress">GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub</a></li>

</ul>
</details>

**标签**: `#sparse attention`, `#KV cache compression`, `#evaluation`, `#machine learning research`, `#NLP`

---

<a id="item-7"></a>
## [Stripe 据悉以超 70 亿美元收购 AI 聚合平台 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 8.0/10

据知情人士透露，Stripe 已与 OpenRouter 达成收购协议，交易金额超过 70 亿美元，但最终价格仍有可能变动。Stripe 和 OpenRouter 均未正式证实此事。 这将成为 AI 基础设施领域规模最大的收购之一，让支付巨头 Stripe 强势切入 AI 模型聚合赛道。该交易可能改变开发者获取和支付 AI 模型的方式，也标志着 AI 行业整合正在加速。 OpenRouter 成立于 2023 年，为开发者提供超过 400 个 AI 模型的访问服务，并于今年 5 月称已服务 800 万名开发者。据报道，交易金额超过 70 亿美元，但最终价格仍可能调整，目前尚未得到官方确认。

telegram · zaihuapd · 8月17日 01:19

**背景**: OpenRouter 是一个 AI 模型聚合平台，为开发者提供统一 API，使其能够通过一次请求访问多种大语言模型，并自动将请求路由到最合适的模型。Stripe 是一家主要的在线支付处理公司。收购 OpenRouter 将让 Stripe 依托其面向开发者的支付基础设施，成为 AI 模型访问与变现的关键入口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.merge.dev/blog/what-is-openrouter">What is OpenRouter ? Here&#x27;s what you need to know</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter ? A Guide with Practical Examples | Codecademy</a></li>

</ul>
</details>

**标签**: `#Stripe`, `#OpenRouter`, `#AI`, `#Acquisition`, `#M&amp;A`

---

<a id="item-8"></a>
## [宇树预告‘超人’人形机器人，原地跳高 2 米超人类纪录](https://m.weibo.cn/detail/5332901463070926) ⭐️ 8.0/10

宇树科技发布了新款人形机器人“超人”的预告，宣称其原地跳高可达 2 米，极限速度达 12.66 米/秒（腿长 0.85 米），两项指标均超越人类纪录。 这一预告意义重大，因为人形机器人很少能在跳跃和奔跑两方面同时达到甚至超越人类运动水平。若数据属实，可能加速人形机器人在工业、物流和应急救援等需要敏捷动作的场景中的应用。 预告称，全新整机仅用 3 个多月研发完成，未来几个月还有较大完善空间。需要注意的是，12.66 米/秒的极限速度与 0.85 米腿长一并公布，且公司尚未发布实测验证或现场演示。

telegram · zaihuapd · 8月17日 07:12

**背景**: 宇树科技是一家以四足机器人闻名的中国公司，目前正扩展人形机器人产品线。“超人”似乎是此前 H1、G1 等型号的后续或衍生型号，而这些型号已展示过奔跑、跳跃等动态能力。人类优秀运动员的原地纵跳高度通常在 1.2 至 1.6 米左右，世界级短跑选手的最高速度约为 12.4 米/秒，因此预告中的参数已接近或超过人类极限。

**标签**: `#机器人`, `#人形机器人`, `#宇树科技`, `#运动能力`, `#AI`

---

<a id="item-9"></a>
## [GitHub 遭遇大规模宕机，引发关于 LLM 流量的争论](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) ⭐️ 7.0/10

GitHub 发生了一次大规模宕机，用户看到“当前没有服务器可为您处理请求”的错误。故障持续了近三个小时，状态页面最初未显示任何事故，随后才确认了问题。 这次宕机凸显了核心开发者基础设施的脆弱性，并加剧了社区关于 LLM 生成流量是否压垮 GitHub 限流机制的争论。它还引发了对 GitHub 定价模式及对免费和付费用户可靠性承诺的质疑。 事故页面数小时仍处于“正在确定根本原因”状态，连网页版 diff 查看功能也无法使用。社区成员认为，大量 LLM 机器人流量以及对付费用户的限流措施不力可能是促成因素。

hackernews · SpyCoder77 · 8月17日 13:35 · [社区讨论](https://news.ycombinator.com/item?id=49330597)

**背景**: LLM 流量是指 ChatGPT、Copilot、Perplexity 等大型语言模型在获取或引用网页内容时产生的请求或访问。限流是一种控制发送到服务器的请求速率的技术，有助于防止拒绝服务攻击和爬取。GitHub 作为代码托管的核心平台，开发者高度依赖，因此宕机造成的破坏尤为严重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://searchatlas.com/blog/track-llm-traffic/">LLM Traffic: What it is and How to Track it? - searchatlas.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rate_limiting">Rate limiting</a></li>

</ul>
</details>

**社区讨论**: 评论者对 GitHub 的可靠性表达了不满，一位用户称“希望已经破灭”，另一人表示愿意付费使用更可靠的替代方案。一些人批评 GitHub 的定价和限流策略，认为应对 LLM 流量收费或加以限制；另一些人则将其归咎于以牺牲工程稳定性为代价追求快速上线功能的文化。

**标签**: `#github`, `#outage`, `#reliability`, `#devops`, `#llm-traffic`

---

<a id="item-10"></a>
## [AI;DR：读者为何拒绝 AI 生成的内容](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 7.0/10

Rick Manelius 在其文章《AI;DR（AI；没读过）》中指出，读者越来越排斥 AI 生成的内容，因为这些内容往往显得冗长、自负且缺乏思想深度，引发了对网络真实性的广泛讨论。 文章所描述的这种抵制情绪，标志着人们对 AI 生成文本及其对数字通信影响的信任危机日益加深。对科技行业而言，这也凸显了 AI 生成的代码注释和文档可能降低可读性和代码质量，从而影响开发者与用户。 文章指出，‘思想懒惰’是低质量 AI 内容的根源，并批评 AI 写作过于冗长、堆砌术语且过度自信。文章还提到，这类内容往往缺乏细微差别，读起来让人觉得虚假且令人恼火。

hackernews · mooreds · 8月17日 19:47 · [社区讨论](https://news.ycombinator.com/item?id=49336573)

**背景**: AI;DR 是常见网络缩写“TL;DR”（太长了，没读）的变体，后者常用于对长文的简短总结。随着 GPT-4 等大语言模型的普及，如今许多网络内容由 AI 生成，读者也逐渐形成了识别这些内容的直觉。这篇文章反映了更广泛的文化焦虑：AI 生成的文本是否可信，以及使用 AI 是否意味着真正智力投入的减少。

**社区讨论**: 社区成员对 AI 生成内容表达了强烈的反感，尤其是在工作场景中。有人评论说，AI 生成的回复给人一种思想懒惰的感觉；还有人建议，如果要用 AI，与其发送输出内容，不如发送所使用的提示词，因为后者才真正包含你想传达的信息。另一个反复出现的问题，是 AI 生成的注释对代码可读性和可维护性的负面影响。

**标签**: `#AI`, `#online-communication`, `#content-creation`, `#AI-generated-content`, `#tech-culture`

---

<a id="item-11"></a>
## [如何禁用或避免侵入式 AI：一份实用指南](https://www.librarian.net/notoai/) ⭐️ 7.0/10

文章《如何禁用或避免侵入式 AI》是一份由社区维护的指南，汇编了在操作系统、浏览器和应用程序中关闭或绕过 AI 功能的实用技巧。该指南托管在 NoToAI.org，并接受用户贡献以持续更新。 这很重要，因为 AI 功能正越来越多地被捆绑到日常软件中，且往往未经用户明确同意，从而引发隐私和可用性问题。一个实用的、由社区驱动的资源可以帮助用户重新掌控自己的设备，并反映出对强制 AI 集成的广泛抵制。 该指南可通过短链接 NoToAI.org 访问，作者欢迎社区提出补充建议。一个值得注意的告诫是，禁用 AI 功能有时会导致用户无法使用不相关的功能，例如 Apple CarPlay 需要启用 Siri 才能播放媒体。

hackernews · ColinWright · 8月17日 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49331220)

**背景**: 该指南反映了公司将 AI 助手和大型语言模型集成到日常软件中的日益增长的趋势，有时并未获得用户明确同意。例如，微软的 Windows Recall 功能会捕获屏幕快照以使用户活动可搜索，这引发了隐私担忧。Pi-hole 等工具通过充当 DNS 黑洞（sinkhole）在网络层面拦截广告和跟踪器，而 Firejail 在 Linux 上提供轻量级沙箱机制以限制应用行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Recall">Windows Recall - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pi-hole">Pi - hole - Wikipedia</a></li>
<li><a href="https://secure-os.org/articles/firejail/">Firejail : How to Sandbox Linux Applications (2026 Guide)</a></li>

</ul>
</details>

**社区讨论**: 评论者对公司强制推行 AI 功能表示不满，指出市场可能长期不理性，且某些 AI 功能运营成本高昂。一个普遍的担忧是禁用 AI 可能会破坏其他功能，例如 Apple CarPlay 需要启用 Siri。多位用户建议改用 Linux 或使用 LibreWolf、Waterfox 等浏览器，而作者则邀请更多建议。

**标签**: `#AI`, `#privacy`, `#software`, `#linux`, `#user-control`

---

<a id="item-12"></a>
## [Roboflow 基准测试：GPT-5.6 Sol 视觉表现不及 Gemini 3.5 Flash](https://blog.roboflow.com/openai-gpt-5-6/) ⭐️ 7.0/10

OpenAI 于 2026 年 7 月 9 日发布 GPT-5.6 系列，其旗舰视觉模型 Sol 被 Roboflow 在 2026 年 7 月 16 日的评测中测试。在大多数检测、计数、OCR 和提取任务上，Sol 落后于 Google 的 Gemini 3.5 Flash，而 OCR 单项的最佳成绩由名为 Fable 的模型获得。 该结果削弱了 OpenAI 关于 Sol 在视觉能力和效率上树立新标准的说法，并表明 Gemini 3.5 Flash 仍是高用量视觉工作负载中更实用的选择，成本约为 Sol 的三分之一。依赖 VLM API 构建应用的开发者和企业可能会重新考虑真实图像任务中的模型选型。 Roboflow 对 GPT-5.6 的三个版本 Luna、Terra 和 Sol 进行了检测、计数、OCR 和提取任务的对比。社区分析指出，Gemini 3.5 Flash 在成本更低的情况下全面优于 Sol；不过 Sol 的 MoE（混合专家）架构仍在一些主观 UI 质量评测中给部分测试者留下深刻印象。

hackernews · plurby · 8月17日 12:09 · [社区讨论](https://news.ycombinator.com/item?id=49329575)

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月 9 日发布的一系列大型多模态模型，包括 Luna、Terra 和 Sol 三个版本，其中 Sol 被定位为能力最强，并被官方称为 OpenAI 迄今最好的视觉模型。Roboflow 是一家计算机视觉平台，会用目标检测、计数、OCR 等实际任务来评测视觉语言模型（VLM）。Gemini 3.5 Flash 是 Google 推出的快速、低成本多模态模型，面向智能体和大规模工作负载。这类基准对比之所以重要，是因为 VLM 在&\#x27;前沿&\#x27;性能上的宣传常常需要通过真实任务的独立测试来验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.roboflow.com/openai-gpt-5-6/">GPT 5.6 Sol is the best &quot;vision&quot; model OpenAI ever released</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash">Gemini 3.5 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: 评论区总体对评测结论持批评态度：有人称文章摘要&\#x27;过于轻描淡写&\#x27;，指出 Gemini 3.5 Flash 在除 OCR 外的所有基准上都击败了 Sol，而 OCR 单项由 Fable 夺冠，成本仅为 Sol 的三分之一。其他人则提出实际和方法论方面的担忧——Sol 用于机器人/药房视觉任务属于大材小用，速度可能慢 25-50 倍；硬币样本图片存在 EXIF 方向读取失败的问题；还应当纳入 Gemini 3 Flash 或 3.7，因为 3.5/3.6 在视觉上是退步。也有用户提出相反观点，称赞 Sol 的混合专家模型在 UI 设计任务上表现出色。

**标签**: `#OpenAI`, `#vision model`, `#benchmark`, `#AI`, `#GPT-5.6`

---

<a id="item-13"></a>
## [美团高管反思全员“养虾运动”：日耗千万 Token 开支](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 7.0/10

美团核心本地商业 CEO 王莆中公开反思全员“养虾运动”，称其每天消耗上千万元 Token 费用。他表示，4 月起各事业部成立 AI 组织，通过赛马机制明确 AI 转型是业务、组织、技术三位一体的系统工程，到 7 月 AI 已在内部产品流程中跑通并产生价值。 这位大型科技公司高管的反思凸显了 AI 炒作与实际运营价值之间的差距，说明规划不当的 AI 推广可能导致成本超支和业务干扰。它进一步印证了成功的企业 AI 应用需要业务目标、组织架构和技术三者对齐，这一教训对整个行业都具有参考意义。 王莆中指出了认知、效率、场景、考核四重错配是 AI 落地难的根本原因。公司的实践还表明，通过赛马机制评估 AI 工作，有助于厘清转型的真正要求。

telegram · zaihuapd · 8月17日 02:09

**背景**: 在大语言模型中，Token 是模型处理文本的基本单位，API 费用通常按 Token 数量计算，因此企业大规模使用 AI 很容易产生巨额账单。业内人士指出，随着企业争相采用 AI，“Token 成本正在成为新的云账单”，效率和明确的投资回报变得至关重要。美团是中国最大的电商本地生活服务平台之一，其内部发起的“养虾运动”旨在鼓励全员尝试 AI，却产生了噪音和谬误，干扰了真实经营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://www.elvex.com/blog/ai-token-cost-enterprise-budget-control">AI Token Cost Enterprise : Stop Budget Blowouts in 2026 - elvex</a></li>

</ul>
</details>

**标签**: `#AI adoption`, `#Enterprise AI`, `#Meituan`, `#AI cost`, `#Organizational change`

---

<a id="item-14"></a>
## [ChatGPT macOS 应用新增 Computer History，记录点击与按键](https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes) ⭐️ 7.0/10

OpenAI 的 ChatGPT macOS 应用推出了新功能 Computer History，它会记录用户的点击和按键，建立可供 ChatGPT 与 Codex 调用的活动时间线。该功能旨在帮助 AI 学习用户的工作方式并建议自动化操作，同时不采用截屏方式。 这次发布标志着 AI 助手在收集用户活动数据用于训练和自动化方面迈出了重要一步，也带来了不容忽视的隐私问题。它体现了 AI 驱动的活动追踪这一行业趋势，效仿微软的 Windows Recall，但采用了侵入性较低的事件记录方式。 Computer History 为可选开启功能，默认处于关闭状态，并提供排除特定应用和网站、删除记录以及忽略无痕或隐私浏览标签页等控制选项。OpenAI 强调它只捕获“事件”，不涉及图像、视频或音频。

telegram · zaihuapd · 8月17日 04:16

**背景**: ChatGPT 是 OpenAI 广泛使用的对话式 AI 助手，而 Codex 是 OpenAI 开发的 AI 编程代理，旨在自动化软件工程任务。微软于 2024 年 5 月为 Copilot+ PC 发布的 Windows Recall 会定期截取用户活动屏幕，用于 AI 搜索和回忆，但因其隐私与安全隐患遭到强烈反对。Computer History 则采用不同思路，记录输入事件而非屏幕内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Recall">Windows Recall</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://mashable.com/article/windows-recall-microsoft">Windows Recall can now be uninstalled. Plus, Microsoft... | Mashable</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#OpenAI`, `#privacy`, `#macOS`, `#AI training`

---

<a id="item-15"></a>
## [苹果因德国监管裁决将调整广告追踪同意规则](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

德国反垄断监管机构已责令苹果修改其应用追踪透明度（ATT）框架，要求第三方授权弹窗必须保持中立，去除劝阻性设计元素。苹果须在四个月内落实，并维持该承诺七年。 该裁决是全球对苹果隐私实践审查中的一个里程碑，因为它质疑了 ATT 的中立性及其可能偏袒苹果自身广告业务的问题。这一决定可能重塑 iOS 广告生态，为第三方开发者提供更公平的竞争环境，并影响其他监管机构处理类似案件的方式。 德国监管机构特别指出，苹果第三方授权弹窗中的“劝阻性措辞和符号”违反了竞争规则。此前，法国和意大利已分别因该框架对苹果处以 1.5 亿欧元和 9860 万欧元的罚款。

telegram · zaihuapd · 8月17日 12:50

**背景**: 应用追踪透明度（ATT）是苹果的隐私框架，要求 iOS 应用在追踪用户在其他应用和网站上的活动前，必须征求用户许可。同意弹窗中的“暗黑模式”（如按钮不对称、语言含糊或胁迫性设计）会操纵用户做出同意选择。监管机构正日益针对此类做法，本次裁决进一步将审查延伸至可能对第三方开发者不利的平台级默认设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adjust.com/glossary/app-tracking-transparency/">What is App Tracking Transparency (ATT)? | Adjust</a></li>
<li><a href="https://usercentrics.com/knowledge-hub/dark-patterns-and-how-they-affect-consent/">Avoid Dark Patterns: Privacy Compliance Best Practices</a></li>
<li><a href="https://www.pedowitzgroup.com/what-are-dark-patterns-in-consent-management">What are dark patterns in consent management?</a></li>

</ul>
</details>

**标签**: `#Apple`, `#ATT`, `#隐私`, `#监管`, `#广告`

---

<a id="item-16"></a>
## [Sun Clock 网站可视化日光与黄金时刻](https://sunclock.net/) ⭐️ 6.0/10

Sun Clock 是一个精美的网页应用，可直观展示任意地点的日照与黄金时刻。其底层 SunCalc 库的作者最近发布了精度大幅改进的重大更新，使计算更加准确。 该应用通过吸引人的可缩放界面，让摄影师、规划者和普通用户都能轻松获取专业的太阳位置数据。它也展示了 SunCalc 等开源库如何助力快速开发专业化工具。 有社区评论指出，“黄金时刻”可能被硬编码为日落前一小时，并建议基于太阳高度角来计算，以适用于高纬度地区。SunCalc 的作者宣布近期对库进行了重大改进以提升精度，并建议应用开发者采用新版。

hackernews · Gecko4072 · 8月17日 16:37 · [社区讨论](https://news.ycombinator.com/item?id=49333824)

**背景**: SunCalc 是一个小巧、无依赖的 JavaScript 库，用于计算任意地点和时间的太阳、月亮位置、日照阶段和月相。摄影中的黄金时刻是指日出后或日落前的一段时间，此时日光更红、更柔和，常被用来拍摄效果更佳的照片。许多网页应用依赖这类库，避免从零实现复杂的天文公式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mourner/suncalc">GitHub - mourner/suncalc: A tiny JavaScript library for calculating sun/moon positions and phases. · GitHub</a></li>
<li><a href="https://www.npmjs.com/package/suncalc">suncalc - npm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Golden_hour_%28photography%29">Golden hour (photography)</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极，称赞该应用“很别致”，动态 UI 缩放使其适合放在屏幕角落观看。有用户建议基于太阳位置改进黄金时刻的计算，有用户希望支持在地图上点击并对比当地时间，还有 SunCalc 作者指出他最近发布了精度大幅提升的新版本。

**标签**: `#web-app`, `#sun-calculations`, `#UI`, `#photography`, `#open-source`

---

<a id="item-17"></a>
## [Markdown SVG 渲染器新增 PNG、JPEG 与 MP4 导出标签页](https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/) ⭐️ 6.0/10

Simon Willison 的 markdown-svg-renderer 工具现在能把 Markdown 中的 SVG 代码块转换为带标签页的面板，支持渲染后的 SVG、PNG、JPEG 和 MP4 导出。今天新增的 MP4 标签页使用 ffmpeg.wasm 检测 SVG 动画、渲染帧，并完全在浏览器中编译成视频。 这使得在原生不支持 SVG 或动画 SVG 的平台上（如社交媒体或聊天应用）分享 SVG 内容变得更加容易。它也展示了 WebAssembly 在浏览器中的能力，免去了服务端转换的需要。 用户可以直接粘贴 Markdown，或从支持 CORS 的 URL 或 GitHub Gist 加载内容，书签式 URL 会嵌入源文档。该工具会猜测动画 SVG 的循环时长，并加载超过 30MB 的 ffmpeg.wasm 来将帧编译为 MP4。

rss · Simon Willison · 8月16日 23:59

**背景**: markdown-svg-renderer 是 Simon Willison 于 2026 年 5 月创建的一个基于浏览器的工具，用于分享包含 SVG 文档的 Markdown 转录内容。它支持标准 Markdown 格式，并支持特殊的三个反引号 SVG 代码块，这些代码块会以带标签页的界面展示渲染结果和源代码。CORS（跨源资源共享）是一种浏览器机制，允许网页安全地从其他域请求资源，因此该工具可以获取 Gist 或其他 URL 的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/28/markdown-svg-renderer/">Tool: markdown-svg-renderer</a></li>
<li><a href="https://tools.simonwillison.net/markdown-svg-renderer">markdown-svg-renderer</a></li>
<li><a href="https://github.com/simonw/tools/commit/71e4944766b577a327ff048cc63b739ba4cbade9">markdown-svg-renderer · simonw/tools@71e4944</a></li>

</ul>
</details>

**标签**: `#markdown`, `#svg`, `#developer-tools`, `#web-development`

---

<a id="item-18"></a>
## [SineKAN：使用正弦激活函数的 KAN 变体在 Reddit 分享](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

Reddit 用户分享了 SineKAN，这是一种用正弦激活函数替代 B 样条激活的 Kolmogorov-Arnold Network（KAN）变体。帖子附上了 arXiv 论文、GitHub 仓库以及 MDPI《Mathematics》期刊上同行评审论文的链接。 SineKAN 旨在解决标准 KAN 模型在尺寸和速度上的局限，并报告称在 MNIST 基准上比 B-Spline KAN 有更好的数值表现。这可能使基于 KAN 的架构在深度学习任务中更具实用性。 该模型将可学习的 B 样条激活函数网格替换为重新加权的正弦函数网格。作者发现，在两种模型均使用接近最优超参数训练的 MNIST 基准上，SineKAN 数值表现更好；其正式同行评审版本已发表在 MDPI《Mathematics》期刊。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**背景**: Kolmogorov-Arnold Network（KAN）是一种基于 Kolmogorov-Arnold 表示定理的神经架构，与传统的 MLP 不同，它将可学习的激活函数放在边的位置上而非节点上。原始的 KAN 实现使用 B 样条函数作为可学习激活函数，这可能带来较高的计算开销。SineKAN 用正弦函数替代 B 样条，以提升速度并减小模型规模。相关研究属于对 KAN 替代激活函数更广泛探索的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN: Kolmogorov-Arnold Networks Using Sinusoidal Activation Functions</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1462952/full">Frontiers | SineKAN: Kolmogorov-Arnold Networks using sinusoidal activation functions</a></li>
<li><a href="https://www.teachfloor.com/blog/kolmogorov-arnold-network">Kolmogorov - Arnold Network (KAN): How It Works and... | Teachfloor</a></li>

</ul>
</details>

**标签**: `#Kolmogorov-Arnold Networks`, `#Activation Functions`, `#Machine Learning`, `#arXiv`, `#Neural Architecture`

---

<a id="item-19"></a>
## [豆包上线工作任务模式，手机远程控制电脑](https://mp.weixin.qq.com/s/-BIdyDXChyRIurOefB2uVw) ⭐️ 6.0/10

豆包推出了新的「工作任务」模式，用户在授权后可从手机端远程接管电脑。用户可以完成桌面端未处理的任务或启动新任务，实时接收进度提醒，并获取本地文件上下文。 这一举措标志着字节跳动正在推进 AI 智能体领域，让移动端助手能够自主操作桌面环境。它能通过跨设备完成任务来提升生产力，并可能为 AI 助手在工作场景中的应用树立新标杆。 该工作任务模式是豆包专业版 2.1 发布的一部分，集成了 Pro 模型和智能体能力。它可以自主拆解工作目标、操作本地电脑应用，并调用浏览器、飞书等工具，但需要获得用户的明确授权。

telegram · zaihuapd · 8月17日 09:06

**背景**: 豆包是字节跳动面向消费者的 AI 助手，基于其自研大语言模型构建。与只能生成文本的简单聊天机器人不同，AI 智能体可以通过使用工具并与环境交互来自主完成多步骤任务，而豆包的新工作任务模式正是这一趋势的体现——它可以直接在用户的电脑上执行操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/29112">Doubao Officially Launches Version 2.1 Professional Edition: Integrates Pro Model and Introduces a New Office Task Mode</a></li>
<li><a href="https://baike.baidu.com/en/item/Doubao+Office+Task+Mode/3199042">Doubao Office Task Mode_Baiduwiki</a></li>
<li><a href="https://www.toolcentral.ai/ai-tools/doubao/">Doubao : ByteDance&#x27;s AI Assistant for Chat &amp; Content - ToolCentral</a></li>

</ul>
</details>

**标签**: `#AI assistant`, `#remote desktop`, `#Doubao`, `#productivity`, `#automation`

---

<a id="item-20"></a>
## [美上诉法院裁定大疆黑名单案发回重审](https://weibo.com/1642634100/RdO9T4ggz) ⭐️ 6.0/10

8 月 14 日，美国哥伦比亚特区联邦巡回上诉法院裁定，下级法院须重新审理大疆被列入五角大楼“中国军事企业”黑名单一案，认为此前审查存在缺陷，并下令审查非公开机密文件。大疆于 2022 年 10 月首次被列名，2024 年 10 月起诉，2025 年下级法院判决对其不利后提起上诉。 该裁定是大疆的一次重要法律胜利，可能影响其在美国市场的运营和声誉。这也凸显了在中美科技摩擦背景下，五角大楼 1260H 清单的透明度和准确性问题。 上诉法院认为此前审查存在缺陷、证据不足，要求下级法院审查非公开的机密材料。大疆欢迎这一裁决，称这是纠正不当列名的重要一步。

telegram · zaihuapd · 8月17日 09:51

**背景**: 五角大楼的 1260H 清单根据 2021 财年《国防授权法》第 1260H 条设立，用于识别在美国运营的中国军事企业；被列入可能限制其接触美国资本和政府合同。截至 2026 年 6 月，该清单已增至 188 家企业，包括阿里巴巴、比亚迪和百度，但列名本身并不直接禁止销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://business.defense.gov/Resources/CLEAR/1260H-List/">1260H List - business.defense.gov</a></li>
<li><a href="https://sanctionsnews.bakermckenzie.com/us-government-updates-1260h-list-of-chinese-military-companies/">US Government Updates 1260H List of Chinese Military ...</a></li>
<li><a href="https://www.nbcnews.com/news/us-news/pentagon-blacklists-alibaba-byd-defense-contracts-rcna349154">Pentagon blacklists Alibaba and BYD from defense contracts</a></li>

</ul>
</details>

**标签**: `#DJI`, `#legal`, `#US-China`, `#tech policy`, `#defense`

---