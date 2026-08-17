---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 35 items, 20 important content pieces were selected

---

1. [DuckDB v2.0 Preview Reveals Server Mode, VARIANT Type, and New Storage Format](#item-1) ⭐️ 9.0/10
2. [Qwen3.8 27B Scores 52 on Artificial Analysis, Tying Frontier Models](#item-2) ⭐️ 9.0/10
3. [AirTag Tracks Rare Book Shipment to Amazon AI Training Facility](#item-3) ⭐️ 9.0/10
4. [AI-Generated Copilot Autofix Enabled Snowflake Jira Compromise](#item-4) ⭐️ 8.0/10
5. [Ask HN: Users Weigh GitHub Alternatives Amid Reliability Woes](#item-5) ⭐️ 8.0/10
6. [Sparse Attention &amp; KV Compression: The Tricks That Make Results Look Good](#item-6) ⭐️ 8.0/10
7. [Stripe Nears $7 Billion Deal to Acquire AI Aggregator OpenRouter](#item-7) ⭐️ 8.0/10
8. [Unitree Teases &\#x27;Superman&\#x27; Humanoid Robot With 2-Meter Standing Jump](#item-8) ⭐️ 8.0/10
9. [GitHub suffers major outage, sparks debate over LLM traffic](#item-9) ⭐️ 7.0/10
10. [AI;DR: Why Readers Are Rejecting AI-Generated Content](#item-10) ⭐️ 7.0/10
11. [How to Disable or Avoid Intrusive AI: A Practical Guide](#item-11) ⭐️ 7.0/10
12. [GPT-5.6 Sol trails Gemini 3.5 Flash in Roboflow vision benchmarks](#item-12) ⭐️ 7.0/10
13. [Meituan executive reflects on AI &\#x27;shrimp farming&\#x27; campaign: daily token costs hit millions](#item-13) ⭐️ 7.0/10
14. [ChatGPT macOS App&\#x27;s Computer History Tracks Clicks and Keystrokes](#item-14) ⭐️ 7.0/10
15. [Apple to Alter Ad Tracking Consent Rules After German Regulator Ruling](#item-15) ⭐️ 7.0/10
16. [Sun Clock Visualizes Daylight and Golden Hour Times Online](#item-16) ⭐️ 6.0/10
17. [Markdown SVG Renderer Adds PNG, JPEG, and MP4 Export Tabs](#item-17) ⭐️ 6.0/10
18. [SineKAN: KAN Variant Using Sinusoidal Activations Shared on Reddit](#item-18) ⭐️ 6.0/10
19. [Doubao Launches Work Task Mode for Remote PC Control via Mobile](#item-19) ⭐️ 6.0/10
20. [U.S. Appeals Court Orders Rehearing of DJI&\#x27;s Pentagon Blacklist Case](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DuckDB v2.0 Preview Reveals Server Mode, VARIANT Type, and New Storage Format](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 9.0/10

The DuckDB team published a preview of v2.0 on August 17, 2026, unveiling headline features such as DuckDB as a server, triggers, the VARIANT type, asynchronous I/O, a new SQL parser, and a new storage format. The release is slated for fall 2026. DuckDB is one of the most popular embedded analytics databases, and v2.0 extends it toward server deployments, potentially broadening its use cases. This milestone matters for data engineers who rely on DuckDB for fast, local analytics and for the broader database ecosystem. The preview highlights a new storage format and a new SQL parser, which may affect compatibility with existing DuckDB files and queries. Additionally, the project saw 10,000 commits in under six months, and incremental materialized views remain absent despite community interest.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Background**: DuckDB is an open-source, column-oriented, in-process SQL OLAP database management system designed for fast analytical queries on large datasets without requiring a separate database server. It is widely used for embedded analytics, local data science, and ETL pipelines, and can process datasets larger than available memory via out-of-core execution.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0 – DuckDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/DuckDB">DuckDB - Wikipedia</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in-process SQL OLAP database management system</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely enthusiastic, with users praising DuckDB&\#x27;s performance and expressing excitement about new features like Quack and its out-of-core processing capabilities. However, some commenters raised concerns about the large number of commits possibly indicating AI-assisted development, and others questioned the absence of incremental materialized views, which they see as ClickHouse&\#x27;s key advantage.

**Tags**: `#DuckDB`, `#database`, `#analytics`, `#release`, `#data engineering`

---

<a id="item-2"></a>
## [Qwen3.8 27B Scores 52 on Artificial Analysis, Tying Frontier Models](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 9.0/10

Qwen3.8 27B, a 27-billion-parameter vision-language model from Alibaba&\#x27;s Qwen team, scored 52 on the Artificial Analysis Intelligence Index, tying DeepSeek V4 Flash 0731 and outperforming models several times its size. It was released as open weights under Apache 2.0 in August 2026. This result challenges the assumption that frontier capability requires hundreds of billions of parameters, suggesting efficiency gains could reduce the need for massive data center buildouts. It may accelerate the shift toward smaller, locally runnable models and reshape infrastructure investment decisions. The score of 52 equals DeepSeek V4 Flash 0731, which ranks \#5 in the large model category \(&gt;150B\), and beats all medium models \(40B–150B\). Qwen3.8 27B is a native vision-language model with flexible thinking control and runs decently on a gaming PC, making local deployment practical.

hackernews · anana\_ · Aug 17, 17:25 · [Discussion](https://news.ycombinator.com/item?id=49334544)

**Background**: Artificial Analysis is an independent benchmark site that aggregates model quality, speed, and price into an Intelligence Index score. Qwen is an open-weight model family by Alibaba; the 3.8 generation focuses on multimodal reasoning and agentic behavior. Historically, larger models \(e.g., Opus 4.6, GPT-5.6\) scored higher, so a 27B model tying frontier models marks a notable efficiency milestone.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model &amp; API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://benchlm.ai/benchmarks/artificialanalysis">Artificial Analysis Intelligence Index Leaderboard (August ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed disbelief and excitement, noting Qwen3.8 27B beats Claude Opus 4.6 and rivals DeepSeek V4 Flash despite running on consumer hardware. Some highlighted its unusually strong agentic behavior and questioned the necessity of massive data-center investments when small models approach frontier performance.

**Tags**: `#AI`, `#LLM`, `#benchmarks`, `#Qwen`, `#efficiency`

---

<a id="item-3"></a>
## [AirTag Tracks Rare Book Shipment to Amazon AI Training Facility](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 9.0/10

404 Media embedded an Apple AirTag in a rare book that was part of a 1,000-book bulk order, and tracked it to the VGT3 corner of Amazon&\#x27;s LAS8 facility in Las Vegas, a site known for destructively scanning books for AI training. This is the first concrete evidence linking Amazon, one of the largest AI players, to the clandestine practice of bulk-purchasing rare and used books for model training data. It confirms long-standing suspicions in the bookselling community and raises serious ethical and legal questions about copyright and data sourcing. The order was placed through Biblio, a used and rare book marketplace, by an anonymous price-insensitive customer. Online forum posts from Amazon workers confirmed that the VGT3 facility destructively scans large volumes of books, meaning the books are likely destroyed in the process.

rss · Simon Willison · Aug 17, 15:21

**Background**: AI companies have been quietly acquiring large volumes of physical books through intermediaries to obtain high-quality, structured text that is scarce on the open web. &\#x27;Destructive scanning&\#x27; involves cutting off book spines and running pages through high-speed scanners, which destroys the physical copy. Biblio is a marketplace founded in 2003 that connects buyers with professional antiquarian booksellers, offering nearly 100 million used and rare books.

<details><summary>References</summary>
<ul>
<li><a href="https://thebotpost.com/ai-news/ai-firms-destroying-millions-books-train-models">AI &#x27; Book Burning&#x27;: Why Firms Destroy Millions of Books to Train AI</a></li>
<li><a href="https://www.remio.ai/post/mysterious-bulk-book-orders-raise-questions-about-ai-training">Mysterious Bulk Book Orders Raise Questions About AI Training</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biblio.com">Biblio.com - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI training`, `#Amazon`, `#investigation`, `#data sourcing`, `#books`

---

<a id="item-4"></a>
## [AI-Generated Copilot Autofix Enabled Snowflake Jira Compromise](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

Wiz researchers demonstrated that an AI-generated GitHub Copilot Autofix introduced a GitHub Actions workflow injection vulnerability in Snowflake&\#x27;s CI/CD pipeline, which allowed attackers to compromise Snowflake&\#x27;s Jira instance. The research, published as part of Wiz&\#x27;s Red Agent work, shows an accepted AI security fix that inadvertently created the flaw it was meant to address. This matters because AI coding assistants are increasingly trusted with security fixes, but their output can contain the same foundational flaws as human code, sometimes even worse because it is often reviewed less carefully. It signals that organizations must enforce static analysis and security scanning on AI-generated code, especially in CI/CD workflows where injected commands can reach production infrastructure. The vulnerable workflow was Snowflake&\#x27;s jira\_issue.yml, where an issue title or body was interpolated into an inline run: shell script without safe escaping, enabling template-injection-style command execution. Community tooling such as zizmor flags this exact pattern as error\[template-injection\], and the case highlights that GitHub Actions&\#x27; safe-by-default assumptions can be violated by AI suggestions just as easily as by human mistakes.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Background**: GitHub Actions workflows are YAML files that run automated tasks; when untrusted data such as issue titles is placed directly into shell commands using GitHub expressions, attackers can inject additional commands. This is known as a GitHub Actions workflow injection or script injection. GitHub Copilot Autofix is an AI feature that proposes fixes for code-scanning alerts, but the generated patches still need validation with the same security tools—SAST, SCA, and static analysis—used for human code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/">How to catch GitHub Actions workflow injections before attackers do - The GitHub Blog</a></li>
<li><a href="https://docs.github.com/en/actions/concepts/security/script-injections">Script injections - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/actions/reference/security/secure-use">Secure use reference - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed that accepting AI-generated code without scanning is a human-process failure, and several recommended running zizmor in CI to catch template-injection issues. Others expressed broader frustration with YAML&\#x27;s footguns, while one user questioned the research&\#x27;s attribution, noting that the linked PR&\#x27;s only Copilot-co-authored commit was not related to the vulnerable change, so the AI&\#x27;s exact role warrants further scrutiny.

**Tags**: `#security`, `#AI-generated code`, `#CI/CD`, `#GitHub Actions`, `#vulnerability`

---

<a id="item-5"></a>
## [Ask HN: Users Weigh GitHub Alternatives Amid Reliability Woes](https://news.ycombinator.com/item?id=49331033) ⭐️ 8.0/10

A Hacker News discussion \(467 points, 295 comments\) asks whether users should switch from GitHub after months of reliability issues. Commenters share hands-on experience with self-hosted GitLab, Gitea/Forgejo, Codeberg, and a founder promotes the new federated forge Tangled. GitHub is the de facto home for most open-source and private repositories, so sustained downtime pushes developers to explore alternatives. The discussion reflects a broader trend toward self-hosting and federated forges, which could reshape developer tooling choices if reliability issues persist. Participants point to Gitea and Forgejo as lightweight, self-hosted GitHub-like forges, while GitLab offers a heavier but full-featured option. Tangled, promoted in the thread by its founder, is a from-scratch federated forge using the AT Protocol, with stacked PRs and Nix-based CI; one user also mentions hosting git over Reticulum.

hackernews · dhruv3006 · Aug 17, 13:59

**Background**: GitHub is a web-based platform for version control using Git, offering hosting, issue tracking, and CI/CD. A &\#x27;forge&\#x27; is a software package that provides these collaborative development features; Gitea and Forgejo are popular self-hosted forges, with Forgejo originating as a community-driven fork of Gitea. Federated forges use open protocols such as ActivityPub/ForgeFed or the AT Protocol to let different instances interoperate, similar to how email servers communicate. The discussion is partly motivated by recent GitHub outages, and some commenters note that earlier platforms like SourceForge also declined, suggesting migration may only buy time.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gitea">Gitea - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://forgefed.org/">ForgeFed</a></li>

</ul>
</details>

**Discussion**: Commenters are pragmatic: several warn that self-hosted GitLab brings its own operational pain \(e.g. Docker upgrades, Postgres buffer misconfigurations\), while Forgejo and Gitea are widely recommended as simpler, GitHub-like options. The Tangled founder&\#x27;s pitch is met with curiosity, and one notable viewpoint argues that switching forges only buys time, since platforms like SourceForge declined before.

**Tags**: `#GitHub`, `#Git-hosting`, `#Self-hosting`, `#DevOps`, `#Developer-tools`

---

<a id="item-6"></a>
## [Sparse Attention &amp; KV Compression: The Tricks That Make Results Look Good](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

In a critical post, ML practitioner Piotr Nawrot exposes common evaluation practices that make sparse attention and KV cache compression methods appear more effective than they are, such as single-hop retrieval without distractors and the use of contaminated benchmarks. He argues that many methods only report 5-10x compression or sparsity under favorable settings and that these results often do not reflect real-world difficulty. This critique matters because sparse attention and KV compression are key to reducing the memory cost of long-context LLMs, and flawed evaluations could mislead research priorities. If the field keeps inflating results, progress may slow as researchers chase methods that only work on easy benchmarks. The post lists four specific tricks: choosing cooperative test settings, never isolating the contribution of a method, hiding failures with aggregated metrics, and benchmarking on saturated tasks. It also points out that many tasks already pass under sliding window attention, making extra compression claims less meaningful.

reddit · r/MachineLearning · /u/korec1234 · Aug 17, 12:18

**Background**: Sparse attention and KV cache compression are techniques to reduce the memory footprint of transformer models, whose KV caches grow linearly with context length and can exceed GPU memory. Evaluation often uses benchmarks like RULER and the Needle-in-a-Haystack \(NIAH\) test, which inserts a single fact into a long context to test retrieval. The critique argues that many such tests are too easy—contexts are repetitive, distractors are trivial, and some benchmarks are contaminated by being included in training data.

<details><summary>References</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/eai/blogs/kv-cache-compression-and-its-infra-problems/">KV Cache Compression and Its Infra Problems | Efficient AI</a></li>
<li><a href="https://github.com/gkamradt/LLMTest_NeedleInAHaystack">GitHub - gkamradt/needle-in-a-haystack: Doing simple retrieval from LLM models at various context lengths to measure accuracy · GitHub</a></li>
<li><a href="https://github.com/NVIDIA/kvpress">GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub</a></li>

</ul>
</details>

**Tags**: `#sparse attention`, `#KV cache compression`, `#evaluation`, `#machine learning research`, `#NLP`

---

<a id="item-7"></a>
## [Stripe Nears $7 Billion Deal to Acquire AI Aggregator OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 8.0/10

Bloomberg, citing people familiar with the matter, reports that Stripe has reached an agreement to acquire OpenRouter for more than $7 billion, though the final price could still change. Neither Stripe nor OpenRouter has officially confirmed the deal. This would be one of the largest AI infrastructure acquisitions, giving payment giant Stripe a major entry into AI model aggregation. It could reshape how developers access and pay for AI models, and signals accelerating consolidation in the AI ecosystem. OpenRouter was founded in 2023 and provides developers access to more than 400 AI models, claiming 8 million developers served as of May. The deal is reportedly worth over $7 billion, but the final price may still be adjusted, and no official confirmation has been made.

telegram · zaihuapd · Aug 17, 01:19

**Background**: OpenRouter is an AI model aggregator that gives developers a single API to query many different large language models, automatically routing requests to the most suitable model. Stripe is a major online payment processing company. Acquiring OpenRouter would allow Stripe to become a key gateway for AI model access and monetization, building on its existing developer-focused payments infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.merge.dev/blog/what-is-openrouter">What is OpenRouter ? Here&#x27;s what you need to know</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter ? A Guide with Practical Examples | Codecademy</a></li>

</ul>
</details>

**Tags**: `#Stripe`, `#OpenRouter`, `#AI`, `#Acquisition`, `#M&amp;A`

---

<a id="item-8"></a>
## [Unitree Teases &\#x27;Superman&\#x27; Humanoid Robot With 2-Meter Standing Jump](https://m.weibo.cn/detail/5332901463070926) ⭐️ 8.0/10

Unitree Robotics released a teaser for its new humanoid robot, nicknamed &\#x27;Superman,&\#x27; claiming it can perform a standing jump of 2 meters and reach a top speed of 12.66 m/s \(with 0.85-meter legs\), surpassing human records for both standing jump height and sprint speed. This is significant because humanoid robots have rarely matched, let alone exceeded, human athletic performance in both jumping and running. If the claims hold, it could accelerate adoption of humanoids in industrial, logistics, and emergency-response roles that require agile movement. The teaser says the entire new machine was developed in just over three months and that there is still considerable room for improvement in the coming months. Notably, the speed figure of 12.66 m/s is stated alongside a leg length of 0.85 m, and the company has not yet released hands-on verification or a live demonstration.

telegram · zaihuapd · Aug 17, 07:12

**Background**: Unitree Robotics is a Chinese company known for agile quadruped robots and is expanding into humanoid platforms. &\#x27;Superman&\#x27; appears to be a successor or companion to earlier models such as the H1 and G1, which already demonstrated dynamic abilities like running and jumping. Elite human athletes typically achieve standing vertical jumps of about 1.2 to 1.6 meters and top sprint speeds near 12.4 m/s over short distances, so the claimed figures put the robot at or beyond human extremes.

**Tags**: `#机器人`, `#人形机器人`, `#宇树科技`, `#运动能力`, `#AI`

---

<a id="item-9"></a>
## [GitHub suffers major outage, sparks debate over LLM traffic](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) ⭐️ 7.0/10

GitHub experienced a widespread outage during which users saw &\#x27;No server is currently available to service your request.&\#x27; The incident lasted nearly three hours, and the status page initially showed no incident before acknowledging the problem. This outage highlights the fragility of core developer infrastructure and intensified community debate about whether LLM-generated traffic is overwhelming GitHub&\#x27;s rate limiting. It raises questions about GitHub&\#x27;s pricing model and reliability commitments for both free and paid users. The incident page remained in &\#x27;identifying root cause&\#x27; status for hours, and even the web interface for viewing diffs was unavailable. Community members suggested that overwhelming LLM bot traffic and ineffective rate limiting for non-paying users may be contributing factors.

hackernews · SpyCoder77 · Aug 17, 13:35 · [Discussion](https://news.ycombinator.com/item?id=49330597)

**Background**: LLM traffic refers to requests or visits generated by large language models such as ChatGPT, Copilot, and Perplexity when they fetch or cite web content. Rate limiting is a technique used to control the rate of requests sent to a server, which helps prevent denial-of-service attacks and scraping. GitHub, as a central platform for code hosting, is heavily relied upon by developers, making outages particularly disruptive.

<details><summary>References</summary>
<ul>
<li><a href="https://searchatlas.com/blog/track-llm-traffic/">LLM Traffic: What it is and How to Track it? - searchatlas.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rate_limiting">Rate limiting</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with GitHub&\#x27;s reliability, with one user saying &\#x27;the hope is dead&\#x27; and another willing to pay for a more reliable alternative. Some criticized GitHub&\#x27;s pricing and rate limiting strategy, arguing that LLM traffic should be charged or restricted, while others blamed a culture of rapid feature delivery at the expense of engineering stability.

**Tags**: `#github`, `#outage`, `#reliability`, `#devops`, `#llm-traffic`

---

<a id="item-10"></a>
## [AI;DR: Why Readers Are Rejecting AI-Generated Content](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 7.0/10

In his essay &\#x27;AI;DR \(AI; Didn&\#x27;t Read\),&\#x27; Rick Manelius argues that readers are increasingly rejecting AI-generated content because it often comes across as verbose, overconfident, and intellectually lazy, sparking a broader conversation about authenticity online. The backlash described in the article signals a growing crisis of trust in AI-generated writing and its impact on digital communication. For the tech industry, it also underscores concerns about AI-generated code comments and documentation degrading readability and code quality, affecting both developers and users. The article identifies &\#x27;intellectual laziness&\#x27; as the root cause of low-quality AI content, and criticizes AI writing for being overly wordy, jargon-heavy, and unjustifiably self-assured. It also notes that such content often lacks nuance, making it feel fake and irritating to read.

hackernews · mooreds · Aug 17, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49336573)

**Background**: AI;DR is a play on the common internet abbreviation &\#x27;TL;DR&\#x27; \(Too Long; Didn&\#x27;t Read\), which is used to summarize long posts. With the rise of large language models like GPT-4, much internet content is now generated by AI, and readers are developing heuristics to detect it. The article reflects broader cultural anxieties about whether AI-generated text can be trusted and whether its use signals a decline in genuine intellectual effort.

**Discussion**: Community members expressed strong frustration with AI-generated content, especially in the workplace. Several commented that AI-generated responses feel like a sign of intellectual laziness, while others suggested that if you&\#x27;re going to use an AI, sending the prompt is more meaningful than sending the output. A recurring concern was the negative impact of AI-generated comments on code readability and maintainability.

**Tags**: `#AI`, `#online-communication`, `#content-creation`, `#AI-generated-content`, `#tech-culture`

---

<a id="item-11"></a>
## [How to Disable or Avoid Intrusive AI: A Practical Guide](https://www.librarian.net/notoai/) ⭐️ 7.0/10

The article &\#x27;How to disable or avoid intrusive AI&\#x27; is a community-maintained guide that compiles practical tips for turning off or bypassing AI features across operating systems, browsers, and applications. The guide is hosted at NoToAI.org and accepts user contributions for ongoing updates. This matters because AI features are increasingly being bundled into everyday software, often without explicit user consent, creating privacy and usability concerns. A practical, community-driven resource helps users regain control over their devices and signals a broader backlash against forced AI integration. The guide is accessible at the short URL NoToAI.org, and the author welcomes community suggestions for additions. A notable caveat is that disabling AI features may sometimes lock users out of unrelated functionality, such as Apple CarPlay requiring Siri to be enabled for media playback.

hackernews · ColinWright · Aug 17, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49331220)

**Background**: The guide reflects a growing trend of companies integrating AI assistants and large language models into everyday software, sometimes without clear user consent. For example, Microsoft&\#x27;s Windows Recall feature captures screen snapshots to make user activity searchable, which has raised privacy concerns. Tools such as Pi-hole act as DNS sinkholes to block ads and trackers network-wide, while Firejail provides lightweight sandboxing on Linux to restrict application behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Recall">Windows Recall - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pi-hole">Pi - hole - Wikipedia</a></li>
<li><a href="https://secure-os.org/articles/firejail/">Firejail : How to Sandbox Linux Applications (2026 Guide)</a></li>

</ul>
</details>

**Discussion**: Commenters voiced frustration with companies forcing AI features, noting that the market can stay irrational and that some AI features are expensive to operate. A common concern was that disabling AI can break other functionality, such as Apple CarPlay requiring Siri to be enabled. Several users recommended switching to Linux or using browsers like LibreWolf and Waterfox, and the author invited further suggestions.

**Tags**: `#AI`, `#privacy`, `#software`, `#linux`, `#user-control`

---

<a id="item-12"></a>
## [GPT-5.6 Sol trails Gemini 3.5 Flash in Roboflow vision benchmarks](https://blog.roboflow.com/openai-gpt-5-6/) ⭐️ 7.0/10

OpenAI&\#x27;s GPT-5.6 Sol, the flagship vision model of the GPT-5.6 family launched July 9, 2026, was benchmarked by Roboflow on July 16, 2026. It lagged Google&\#x27;s Gemini 3.5 Flash on most detection, counting, OCR, and extraction tasks, with the only OCR top result going to a model called Fable. The results undercut OpenAI&\#x27;s claim that Sol sets a new standard for vision and efficiency, and suggest Gemini 3.5 Flash remains the more practical choice for high-volume vision workloads at roughly one-third the cost. Developers and enterprises building on VLM APIs may reconsider model selection for real-world image tasks. Roboflow compared the three GPT-5.6 variants — Luna, Terra, and Sol — across detection, counting, OCR, and extraction. Community analysis notes Gemini 3.5 Flash broadly outperformed Sol at lower cost, while Sol&\#x27;s MoE \(mixture-of-experts\) architecture still impressed some testers on subjective UI-quality tasks.

hackernews · plurby · Aug 17, 12:09 · [Discussion](https://news.ycombinator.com/item?id=49329575)

**Background**: GPT-5.6 is a family of large multimodal models released by OpenAI on July 9, 2026, with Luna, Terra, and Sol variants; Sol is positioned as the most capable and is marketed as OpenAI&\#x27;s best vision model. Roboflow is a computer vision platform that evaluates so-called vision-language models \(VLMs\) on practical tasks such as object detection, counting, and OCR. Gemini 3.5 Flash is Google&\#x27;s fast, low-cost multimodal model aimed at agentic, high-scale workloads. These benchmark comparisons matter because VLM claims of &\#x27;frontier&\#x27; performance often need independent testing on real-world tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.roboflow.com/openai-gpt-5-6/">GPT 5.6 Sol is the best &quot;vision&quot; model OpenAI ever released</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash">Gemini 3.5 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Commenters were largely critical of the benchmark framing: one called the summary &\#x27;understated,&\#x27; noting Gemini 3.5 Flash beat Sol on every benchmark except OCR, where Fable won, at one-third the cost. Others raised practical and methodological concerns — that Sol is overkill and 25-50x too slow for robotics/pharmacy vision, that the penny-sample image showed a failed EXIF rotation, and that Gemini 3 Flash or 3.7 should have been included since 3.5/3.6 were vision downgrades. A counterpoint from one user praised Sol&\#x27;s coherent mixture-of-experts on UI design tasks.

**Tags**: `#OpenAI`, `#vision model`, `#benchmark`, `#AI`, `#GPT-5.6`

---

<a id="item-13"></a>
## [Meituan executive reflects on AI &\#x27;shrimp farming&\#x27; campaign: daily token costs hit millions](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 7.0/10

Meituan core local commerce CEO Wang Puzhong publicly reflected on the company-wide &\#x27;shrimp farming&\#x27; AI campaign, revealing it burned tens of millions of yuan on tokens daily. He said that from April onward, business units set up AI organizations, clarified via a horse-race mechanism that AI transformation is a systematic business-organization-technology effort, and by July, AI was running through internal processes and creating value. This insight from a major tech company leader underscores the gap between AI hype and real operational value, highlighting how poorly planned AI rollouts can cause cost overruns and disruption. It reinforces that successful enterprise AI adoption requires aligning business goals, organizational structures, and technology — a lesson relevant across the industry. Wang identified four mismatches — cognition, efficiency, scenarios, and assessment — as root causes of failed AI adoption. The company&\#x27;s experience also shows that evaluating AI efforts through a race-like competitive mechanism helped clarify the real requirements for transformation.

telegram · zaihuapd · Aug 17, 02:09

**Background**: In large language models, a token is a small unit of text that the model processes; API costs are typically calculated per token, so heavy enterprise usage can easily run up massive bills. As companies rush to adopt AI, &\#x27;token costs are becoming the new cloud bill,&\#x27; according to industry observers, making efficiency and clear ROI essential. Meituan, one of China&\#x27;s largest e-commerce and local services platforms, launched an internal &\#x27;shrimp farming&\#x27; campaign to encourage broad AI experimentation, but it ended up generating noise and errors that interfered with actual operations.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://www.elvex.com/blog/ai-token-cost-enterprise-budget-control">AI Token Cost Enterprise : Stop Budget Blowouts in 2026 - elvex</a></li>

</ul>
</details>

**Tags**: `#AI adoption`, `#Enterprise AI`, `#Meituan`, `#AI cost`, `#Organizational change`

---

<a id="item-14"></a>
## [ChatGPT macOS App&\#x27;s Computer History Tracks Clicks and Keystrokes](https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes) ⭐️ 7.0/10

OpenAI&\#x27;s ChatGPT macOS app has introduced Computer History, a new feature that records clicks and keystrokes to build an activity timeline for ChatGPT and Codex. The feature is designed to help the AI learn users&\#x27; workflows and suggest automation, while avoiding screenshots. This launch marks a significant step in how AI assistants collect user activity data for training and automation, raising important privacy questions. It shows the industry trend toward AI-driven activity tracking, following Microsoft&\#x27;s Windows Recall but with a less invasive event-logging approach. Computer History is opt-in and disabled by default, with controls to exclude specific apps and websites, delete records, and ignore incognito or private browsing tabs. OpenAI emphasizes that it captures only &\#x27;events&\#x27; — not images, videos, or audio.

telegram · zaihuapd · Aug 17, 04:16

**Background**: ChatGPT is OpenAI&\#x27;s widely used conversational AI assistant, while Codex is OpenAI&\#x27;s AI coding agent designed to automate software engineering tasks. Microsoft&\#x27;s Windows Recall, announced in May 2024 for Copilot+ PCs, captures periodic screenshots of user activity for AI-based search and recall, but faced significant backlash over privacy and security. Computer History is a different approach that logs input events instead of screen content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Recall">Windows Recall</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://mashable.com/article/windows-recall-microsoft">Windows Recall can now be uninstalled. Plus, Microsoft... | Mashable</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#privacy`, `#macOS`, `#AI training`

---

<a id="item-15"></a>
## [Apple to Alter Ad Tracking Consent Rules After German Regulator Ruling](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

Germany&\#x27;s antitrust regulator has ordered Apple to modify its App Tracking Transparency \(ATT\) framework, requiring that third-party consent prompts be neutral and free of discouraging design elements. Apple must implement the changes within four months and maintain them for seven years. This ruling is a landmark in the global scrutiny of Apple&\#x27;s privacy practices, as it challenges the neutrality of ATT and its potential to favor Apple&\#x27;s own advertising business. The decision could reshape the iOS ad ecosystem, giving third-party developers a more level playing field and influencing how other regulators approach similar cases. The German regulator specifically cited &\#x27;discouraging wording and symbols&\#x27; in Apple&\#x27;s third-party consent prompts as a violation of competition rules. This follows prior fines of €150 million from France and €98.6 million from Italy over the same framework.

telegram · zaihuapd · Aug 17, 12:50

**Background**: App Tracking Transparency \(ATT\) is Apple&\#x27;s opt-in privacy framework that requires iOS apps to ask users for permission before tracking their activity across other apps and websites. Dark patterns in consent prompts—such as unequal button prominence, confusing language, or coercive design—can manipulate users into consenting. Regulators are increasingly targeting these practices, and this ruling extends that scrutiny to platform-level defaults that may disadvantage third-party developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.adjust.com/glossary/app-tracking-transparency/">What is App Tracking Transparency (ATT)? | Adjust</a></li>
<li><a href="https://usercentrics.com/knowledge-hub/dark-patterns-and-how-they-affect-consent/">Avoid Dark Patterns: Privacy Compliance Best Practices</a></li>
<li><a href="https://www.pedowitzgroup.com/what-are-dark-patterns-in-consent-management">What are dark patterns in consent management?</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#ATT`, `#隐私`, `#监管`, `#广告`

---

<a id="item-16"></a>
## [Sun Clock Visualizes Daylight and Golden Hour Times Online](https://sunclock.net/) ⭐️ 6.0/10

Sun Clock is a polished web app that visualizes daylight and golden hour times for any location. The author of the SunCalc library behind it recently released a major precision overhaul, making calculations more accurate. This app makes niche sun-position data accessible to photographers, planners, and casual users with an attractive, resizable UI. It also highlights how open-source libraries like SunCalc enable rapid development of specialized tools. A community comment notes that &\#x27;golden hour&\#x27; appears hardcoded as the hour before sunset, and suggests basing it on solar altitude to handle high-latitude regions. The author of SunCalc announced a recent major library overhaul that improves precision, and invited the developer to adopt it.

hackernews · Gecko4072 · Aug 17, 16:37 · [Discussion](https://news.ycombinator.com/item?id=49333824)

**Background**: SunCalc is a tiny, dependency-free JavaScript library for calculating sun and moon positions, sunlight phases, and lunar phases for any location and time. The golden hour in photography is the period shortly after sunrise or before sunset when daylight is redder and softer, often used for flattering photos. Many web apps rely on such libraries to avoid implementing complex astronomical formulas from scratch.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mourner/suncalc">GitHub - mourner/suncalc: A tiny JavaScript library for calculating sun/moon positions and phases. · GitHub</a></li>
<li><a href="https://www.npmjs.com/package/suncalc">suncalc - npm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Golden_hour_%28photography%29">Golden hour (photography)</a></li>

</ul>
</details>

**Discussion**: Comments were generally positive, praising the app as &\#x27;nifty&\#x27; and noting the dynamic UI rescaling makes it nice to keep on screen. One user suggested improving golden hour calculation based on sun position, another requested map clicking and calendar hover features, and the SunCalc author pointed to his recent precision overhaul.

**Tags**: `#web-app`, `#sun-calculations`, `#UI`, `#photography`, `#open-source`

---

<a id="item-17"></a>
## [Markdown SVG Renderer Adds PNG, JPEG, and MP4 Export Tabs](https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/) ⭐️ 6.0/10

Simon Willison&\#x27;s markdown-svg-renderer tool now converts SVG blocks in Markdown into tabbed panels with rendered SVG, PNG, JPEG, and MP4 exports. The MP4 tab, added today, uses ffmpeg.wasm to detect SVG animations, render frames, and compile them into a video entirely in the browser. This makes it much easier to share SVG content on platforms that don&\#x27;t support SVG or animated SVG natively, such as social media or chat apps. It also showcases what can be done with WebAssembly in the browser, eliminating the need for server-side conversion. Users can paste Markdown directly or load it from a CORS-friendly URL or GitHub Gist, and bookmarkable URLs embed the source document. The tool guesses loop duration for animated SVGs and loads over 30MB of ffmpeg.wasm to compile frames into MP4.

rss · Simon Willison · Aug 16, 23:59

**Background**: The markdown-svg-renderer is a browser-based tool created by Simon Willison in May 2026 as an ideal way to share Markdown transcripts that include SVG documents. It supports standard Markdown formatting plus special triple-backtick SVG code blocks that are rendered with a tabbed display showing both the rendered output and source code. CORS \(Cross-Origin Resource Sharing\) is a browser mechanism that allows web pages to safely request resources from other domains, which is why the tool can fetch Gists or other URLs.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/28/markdown-svg-renderer/">Tool: markdown-svg-renderer</a></li>
<li><a href="https://tools.simonwillison.net/markdown-svg-renderer">markdown-svg-renderer</a></li>
<li><a href="https://github.com/simonw/tools/commit/71e4944766b577a327ff048cc63b739ba4cbade9">markdown-svg-renderer · simonw/tools@71e4944</a></li>

</ul>
</details>

**Tags**: `#markdown`, `#svg`, `#developer-tools`, `#web-development`

---

<a id="item-18"></a>
## [SineKAN: KAN Variant Using Sinusoidal Activations Shared on Reddit](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

A Reddit user shared SineKAN, a Kolmogorov-Arnold Network variant that replaces B-spline activations with sinusoidal activation functions. The post links to the arXiv paper, a GitHub repository, and a peer-reviewed publication in MDPI Mathematics. SineKAN addresses size and speed limitations of standard KAN models, and reports better numerical performance on MNIST than B-Spline KAN. This could make KAN-based architectures more practical for deep learning tasks. The model replaces learnable grids of B-Spline activation functions with grids of re-weighted sine functions. The authors found improved numerical performance on MNIST when both models were trained with near-optimal hyperparameters, and an official peer-reviewed version was published in MDPI Mathematics.

reddit · r/MachineLearning · /u/jacobgorm · Aug 17, 00:46

**Background**: Kolmogorov-Arnold Networks \(KANs\) are a neural architecture based on the Kolmogorov-Arnold representation theorem, placing learnable activation functions on edges rather than nodes, unlike traditional MLPs. The original KAN implementation uses B-spline functions as learnable activations, which can be computationally heavy. SineKAN replaces B-splines with sinusoidal functions to improve speed and reduce model size. This line of research is part of a broader exploration of alternative activation functions for KANs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN: Kolmogorov-Arnold Networks Using Sinusoidal Activation Functions</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1462952/full">Frontiers | SineKAN: Kolmogorov-Arnold Networks using sinusoidal activation functions</a></li>
<li><a href="https://www.teachfloor.com/blog/kolmogorov-arnold-network">Kolmogorov - Arnold Network (KAN): How It Works and... | Teachfloor</a></li>

</ul>
</details>

**Tags**: `#Kolmogorov-Arnold Networks`, `#Activation Functions`, `#Machine Learning`, `#arXiv`, `#Neural Architecture`

---

<a id="item-19"></a>
## [Doubao Launches Work Task Mode for Remote PC Control via Mobile](https://mp.weixin.qq.com/s/-BIdyDXChyRIurOefB2uVw) ⭐️ 6.0/10

Doubao introduced a new &\#x27;work task&\#x27; mode that lets users remotely take over their PC from a mobile phone after authorization. Users can finish pending desktop tasks or start new ones while receiving real-time progress updates and accessing local file context. This move signals ByteDance&\#x27;s push into AI agent territory, allowing a mobile assistant to operate a desktop environment autonomously. It could boost productivity by enabling cross-device task completion and set a new standard for AI assistants in work scenarios. The work task mode is part of the Doubao Professional Edition 2.1 release, which integrates a Pro model and agent capabilities. It can autonomously decompose work objectives, operate local computer applications, and call tools like browsers and Feishu, but requires clear user authorization.

telegram · zaihuapd · Aug 17, 09:06

**Background**: Doubao is ByteDance&\#x27;s consumer-facing AI assistant built on its proprietary large language model. Unlike simple chatbots that only generate text, AI agents can autonomously perform multi-step tasks by using tools and interacting with their environment, and Doubao&\#x27;s new work task mode exemplifies this trend by directly acting on a user&\#x27;s computer.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/29112">Doubao Officially Launches Version 2.1 Professional Edition: Integrates Pro Model and Introduces a New Office Task Mode</a></li>
<li><a href="https://baike.baidu.com/en/item/Doubao+Office+Task+Mode/3199042">Doubao Office Task Mode_Baiduwiki</a></li>
<li><a href="https://www.toolcentral.ai/ai-tools/doubao/">Doubao : ByteDance&#x27;s AI Assistant for Chat &amp; Content - ToolCentral</a></li>

</ul>
</details>

**Tags**: `#AI assistant`, `#remote desktop`, `#Doubao`, `#productivity`, `#automation`

---

<a id="item-20"></a>
## [U.S. Appeals Court Orders Rehearing of DJI&\#x27;s Pentagon Blacklist Case](https://weibo.com/1642634100/RdO9T4ggz) ⭐️ 6.0/10

On August 14, the U.S. Court of Appeals for the D.C. Circuit ruled that a lower court must reconsider DJI&\#x27;s designation on the Pentagon&\#x27;s Chinese military companies blacklist, citing deficiencies in the prior review and ordering review of classified documents. DJI, first listed in October 2022, filed suit in October 2024 and appealed after a lower court ruled against it in 2025. The ruling is a significant legal victory for DJI, potentially affecting its operations and reputation in the U.S. market. It also underscores concerns about the transparency and accuracy of the Pentagon&\#x27;s 1260H list amid broader U.S.-China technology tensions. The appeals court found the earlier review flawed and evidence insufficient, ordering the lower court to examine non-public classified materials. DJI welcomed the decision as an important step toward correcting its improper designation.

telegram · zaihuapd · Aug 17, 09:51

**Background**: The Pentagon&\#x27;s 1260H list, established under Section 1260H of the FY2021 National Defense Authorization Act, identifies Chinese military companies operating in the U.S.; inclusion can restrict access to U.S. capital and government contracts. The list has grown to 188 companies as of June 2026, including Alibaba, BYD, and Baidu, though designation does not constitute a direct ban on sales.

<details><summary>References</summary>
<ul>
<li><a href="https://business.defense.gov/Resources/CLEAR/1260H-List/">1260H List - business.defense.gov</a></li>
<li><a href="https://sanctionsnews.bakermckenzie.com/us-government-updates-1260h-list-of-chinese-military-companies/">US Government Updates 1260H List of Chinese Military ...</a></li>
<li><a href="https://www.nbcnews.com/news/us-news/pentagon-blacklists-alibaba-byd-defense-contracts-rcna349154">Pentagon blacklists Alibaba and BYD from defense contracts</a></li>

</ul>
</details>

**Tags**: `#DJI`, `#legal`, `#US-China`, `#tech policy`, `#defense`

---