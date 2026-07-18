---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 37 items, 14 important content pieces were selected

---

1. [GPT-5.6 closes 30-year gap in convex optimization](#item-1) ⭐️ 9.0/10
2. [LG monitors silently install software via Windows Update without consent](#item-2) ⭐️ 9.0/10
3. [China&\#x27;s Kimi K3 Model Achieves Parity via Distillation](#item-3) ⭐️ 9.0/10
4. [US Considers FINRA-Like Watchdog for Top AI Models](#item-4) ⭐️ 9.0/10
5. [Fable 5 vs GPT-5.6 Sol on NP-Hard Problem: Does /goal Help?](#item-5) ⭐️ 8.0/10
6. [Stack Overflow decline: AI impact and community barriers](#item-6) ⭐️ 8.0/10
7. [PHK Reflects on Bikeshedding in Farewell Piece](#item-7) ⭐️ 8.0/10
8. [Anthropic Makes Claude Fable 5 Permanent in Subscription Plans](#item-8) ⭐️ 8.0/10
9. [Allegation: DeepMind/Kaggle Grand Prize Awarded to Incoherent AI Submission](#item-9) ⭐️ 8.0/10
10. [Meta in Talks to Rent AI Compute to Anthropic for $10B](#item-10) ⭐️ 8.0/10
11. [SpaceX in Talks with Pentagon for AI Computing Power Deal](#item-11) ⭐️ 8.0/10
12. [OpenRouter Reportedly in Acquisition Talks at $1.3B Valuation](#item-12) ⭐️ 8.0/10
13. [TSMC A14 process yield and performance near 90%, ahead of schedule](#item-13) ⭐️ 8.0/10
14. [Bilibili shows open-source AI companion Project N.E.K.O.](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 closes 30-year gap in convex optimization](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

GPT-5.6, a large language model, was used via a single prompt to prove a 30-year-old open problem in convex optimization, establishing an upper bound on the time complexity for minimizing convex Lipschitz functions over a spherical domain. This breakthrough demonstrates that AI can solve longstanding mathematical problems, potentially accelerating research and shifting the role of mathematicians toward more novel approaches. According to community discussions, the result was achieved using the &\#x27;Sol Pro&\#x27; variant of GPT-5.6, not the more advanced &\#x27;Ultra&\#x27; version, and the problem is more niche than the recent CDC proof but still a real contribution.

hackernews · mbustamanter · Jul 18, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48957779)

**Background**: Convex optimization is a subfield of mathematical optimization that minimizes convex functions over convex sets, with applications across engineering and machine learning. The 30-year gap referred to an open problem about the optimal time complexity for minimizing convex Lipschitz functions, where only lower bounds were known. The restriction to a spherical domain is not limiting, as any bounded domain can be transformed via change of variables.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48957779">GPT-5.6 used a prompt to close a 30-year gap in convex optimization | Hacker News</a></li>

</ul>
</details>

**Discussion**: Comments highlight that while the solved problem is niche, it represents a real step forward. There is debate about whether such AI-made proofs will make researchers obsolete or shift focus to higher-level problems. Some users note the model variant used \(Sol Pro vs Ultra\) and discuss implications for math research and software development.

**Tags**: `#AI`, `#convex optimization`, `#mathematics`, `#breakthrough`

---

<a id="item-2"></a>
## [LG monitors silently install software via Windows Update without consent](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

LG monitors are automatically installing software, including a McAfee trial app, through Windows Update without user consent when connected to a Windows PC. This behavior was discovered and reported by users, raising serious privacy and security concerns. This issue turns legitimate hardware into a vector for unwanted software installation, resembling malware behavior. It affects potentially millions of LG monitor users and highlights a broader vulnerability in Windows&\#x27; device metadata delivery system. The software installs as soon as the monitor is plugged in via HDMI, runs at boot, has full system and internet access, and requires no user interaction. A user-identified workaround involves disabling automatic download of manufacturer apps through Group Policy or Device Installation Settings.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update automatically delivers drivers and firmware to ensure hardware compatibility. However, it can also install additional software from hardware vendors via device metadata, a feature Microsoft trusts vendors to use responsibly. This incident shows that LG abused this trust to push promotional software without user consent.

<details><summary>References</summary>
<ul>
<li><a href="https://windowsforum.com/threads/lg-monitor-app-installer-pushes-mcafee-ads-on-windows-11.439030/">LG Monitor App Installer Pushes McAfee Ads on... | Windows Forum</a></li>
<li><a href="https://support.microsoft.com/en-us/windows/update-drivers-through-device-manager-in-windows-ec62f46c-ff14-c91d-eead-d7126dc1f7b6">Update drivers through Device Manager in Windows - Microsoft...</a></li>

</ul>
</details>

**Discussion**: The community is highly concerned, with many comparing the behavior to malware. Users provided detailed workarounds and debated whether the blame lies solely with LG or also with Microsoft for allowing such installations. Some emphasized that this is a systemic Windows security issue reminiscent of past autorun vulnerabilities.

**Tags**: `#security`, `#privacy`, `#windows-update`, `#lg`, `#malware`

---

<a id="item-3"></a>
## [China&\#x27;s Kimi K3 Model Achieves Parity via Distillation](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

The Kimi K3 model, developed in China, has achieved performance competitive with frontier models like ChatGPT 5.6 and Opus 4.8 through model distillation, with 2.8 trillion parameters and pricing at $3/$15 per million tokens. This demonstrates that distillation can enable latecomers to rapidly catch up with frontier labs, posing a challenge to US leadership in AI and raising national security concerns over the proliferation of open-weight models. Kimi K3 has 2.8 trillion parameters and is priced competitively against ChatGPT 5.6 Sol \($5/$30\) and Opus 4.8 \($5/$25\), though community testing showed it consumed nearly 5 hours of usage on a single task under a $19 plan.

hackernews · sbochins · Jul 18, 17:32 · [Discussion](https://news.ycombinator.com/item?id=48960218)

**Background**: Model distillation transfers knowledge from a large &\#x27;teacher&\#x27; model to a smaller &\#x27;student&\#x27; model, allowing efficient deployment. Open-weight models release trained parameters publicly, enabling wider access. Frontier models refer to the most capable AI systems at any given time, often requiring massive compute and data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.datacamp.com/blog/frontier-models">Frontier Models Explained: What Defines the Cutting Edge of AI</a></li>

</ul>
</details>

**Discussion**: Commenters like nickysielicki argue distillation was inevitable and not an &\#x27;attack&\#x27;, while montroser warns of potential national security crackdowns similar to Napster. Credit\_guy notes the parameter counts and pricing are comparable, and SwellJoe reports practical experience with long runtime.

**Tags**: `#AI`, `#open-source`, `#model distillation`, `#national security`, `#frontier models`

---

<a id="item-4"></a>
## [US Considers FINRA-Like Watchdog for Top AI Models](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 9.0/10

The Trump administration is considering creating an independent AI oversight body, modeled after FINRA, to review the safety of top AI models. The proposal is led by Treasury Secretary Scott Bessent and is under review by White House Chief of Staff Susie Wiles. This marks a significant shift in AI governance, proposing a self-regulatory organization that balances security concerns from Wall Street and innovation interests from Silicon Valley. It could set a precedent for how the US regulates advanced AI, potentially influencing global standards. The proposed body would report to the SEC, similar to FINRA&\#x27;s relationship with the securities regulator. Notably, Anthropic and OpenAI have previously objected to government requests to modify or restrict their latest models, underscoring industry tensions.

telegram · zaihuapd · Jul 18, 05:45

**Background**: FINRA, the Financial Industry Regulatory Authority, is a private self-regulatory organization that oversees brokerage firms and exchange markets, operating under SEC oversight. The proposed AI watchdog would follow a similar model, funded by the industry, to conduct safety reviews of advanced AI models. This approach mirrors a suggestion by Google DeepMind CEO Demis Hassabis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FINRA">FINRA</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#policy`, `#Trump administration`, `#FINRA`, `#model safety`

---

<a id="item-5"></a>
## [Fable 5 vs GPT-5.6 Sol on NP-Hard Problem: Does /goal Help?](https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/) ⭐️ 8.0/10

A blog post by Charles Azam evaluates whether the /goal directive improves performance on an NP-hard problem using Fable 5 \(Anthropic\) and GPT-5.6 Sol \(OpenAI\). Results indicate that /goal provides marginal benefits but depends on the search strategy; Ultra mode may be more effective. This comparison highlights the practical differences between leading AI models in solving complex, NP-hard problems, which are critical for optimization tasks. The findings also inform prompt engineering strategies, showing that simple directives like /goal have limited impact compared to more sophisticated agentic approaches. The blog uses a specific NP-hard problem to benchmark performance, measuring success rates and solution quality. GPT-5.6 Sol features a 1.05M context window and 128k output tokens, while Fable 5 is Anthropic&\#x27;s highest-scoring model on FrontierBench for coding. The /goal directive is a prompting technique to set explicit objectives.

hackernews · couAUIA · Jul 18, 11:00 · [Discussion](https://news.ycombinator.com/item?id=48956879)

**Background**: NP-hard problems are computationally intractable, often requiring heuristic or search-based approaches. Modern large language models \(LLMs\) like GPT-5.6 Sol and Fable 5 can be used to generate code or strategies for such problems. The /goal directive is a simple prompt addition intended to focus the model&\#x27;s behavior; however, more advanced methods like Ultra mode \(multiple parallel agents with adversarial review\) may yield better results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://simtheory.ai/model-card/gpt-5.6-sol/">GPT - 5 . 6 Sol - AI Model Details | Simtheory</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>

</ul>
</details>

**Discussion**: Commenters note that Anthropic&\#x27;s Claude \(Fable 5\) is losing ground to OpenAI&\#x27;s Codex in coding tasks, with complaints about slowness and issue resolution. Others suggest that /goal may help in shorter sessions but not in long ones, and that GPT models are naturally better at optimization problems due to their performance in competitions like AtCoder Heuristics.

**Tags**: `#AI comparison`, `#LLM evaluation`, `#NP-hard problem`, `#coding assistant`, `#goal directive`

---

<a id="item-6"></a>
## [Stack Overflow decline: AI impact and community barriers](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

A graph from Stack Exchange Data Explorer shows a significant decline in Stack Overflow activity, attributed to the rise of AI tools like ChatGPT and the site&\#x27;s own restrictive community policies. This trend highlights how AI-driven alternatives and poor community governance can erode a once-dominant platform, impacting millions of developers who relied on Stack Overflow for help. The graph shows activity dropping especially after the 2021 acquisition by Prosus and the release of ChatGPT in late 2022, with some users reporting rate-limiting when trying to access the data.

hackernews · secretslol · Jul 18, 11:12 · [Discussion](https://news.ycombinator.com/item?id=48956949)

**Background**: Stack Overflow is a Q&amp;A platform for programmers, where users ask and answer technical questions. Its strict moderation and downvoting culture created high barriers for newcomers, while AI tools like ChatGPT offer direct answers without social friction.

**Discussion**: Commenters largely agree that Stack Overflow&\#x27;s strict policies and lack of community feeling drove users away, with one noting that the site &\#x27;dug its own grave&\#x27; by not fostering conversation. The acquisition by Prosus is also seen as a turning point.

**Tags**: `#Stack Overflow`, `#AI impact`, `#community decline`, `#software engineering`

---

<a id="item-7"></a>
## [PHK Reflects on Bikeshedding in Farewell Piece](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

Poul-Henning Kamp \(PHK\) published a reflective article titled &\#x27;Goodbye, and Thanks for All the Bikesheds&\#x27; on ACM Queue, revisiting the bikeshedding phenomenon he famously described in 1999. This article re-energizes discussion around a fundamental software engineering anti-pattern, reminding teams to prioritize important decisions over trivial ones, which can improve project efficiency. PHK originally coined the bikeshedding metaphor to explain why people spend excessive time on minor issues like bike shed color while neglecting complex technical decisions; the article is presented as a farewell piece.

hackernews · Ygg2 · Jul 18, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48960155)

**Background**: Bikeshedding, also known as the law of triviality, describes the tendency to give disproportionate weight to trivial issues. PHK introduced the term in a 1999 FreeBSD FAQ. The concept is widely used in software engineering to caution against misallocated attention.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Law_of_triviality">Law of triviality - Wikipedia</a></li>
<li><a href="https://fourweekmba.com/bikeshedding/">What Is Bikeshedding And Why It Matters In Business - FourWeekMBA</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the revisit, with some highlighting the concept of reversible decisions as a solution to bikeshedding. Others noted PHK&\#x27;s contributions like MD5crypt. There was also tangential discussion about age restrictions and gender in tech.

**Tags**: `#software engineering`, `#bikeshedding`, `#project management`, `#community`

---

<a id="item-8"></a>
## [Anthropic Makes Claude Fable 5 Permanent in Subscription Plans](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic announced that starting July 20, Claude Fable 5 will be permanently included in Max and Team Premium plans at 50% of usage limits, reversing a previous decision to remove the model from subscriptions due to competitive pressure from GPT-5.6 Sol and Kimi 3. This move ensures subscribers retain access to Anthropic&\#x27;s best model, keeping the subscription plans competitive against rival offerings from OpenAI and Kimi, and alleviating user concerns about losing access to top-tier AI capabilities. The $20/month plans still do not include Fable 5; only Max \($100/$200 per month\) and Team Premium subscribers benefit. Pro and Team Standard users receive a one-time $100 credit and can access Fable via usage credits.

rss · Simon Willison · Jul 18, 06:00

**Background**: Claude Fable 5 is a Mythos-class large language model from Anthropic, known for strong capabilities in coding and autonomous tasks. It was initially set to be removed from subscriptions due to compute capacity constraints, but competitive launches like OpenAI&\#x27;s GPT-5.6 Sol \(which outperforms Fable 5 on benchmarks\) and Kimi 3 forced Anthropic to reverse course.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#Fable 5`, `#GPT-5.6`

---

<a id="item-9"></a>
## [Allegation: DeepMind/Kaggle Grand Prize Awarded to Incoherent AI Submission](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

A Reddit user claims that the winning submission of the Google DeepMind-sponsored Kaggle competition &\#x27;Measuring Progress Toward AGI&\#x27;—which received a $25,000 grand prize—is incoherent and poorly constructed, based on their detailed review of the write-up, methodology, code, and data. This allegation raises serious questions about the integrity of evaluation standards in high-profile AI competitions, especially those sponsored by leading organizations like DeepMind, and could undermine trust in community-driven benchmark development. The submission involved presenting an LLM with alternative viewpoints from other LLMs on five claims about a tricky situation, but the user describes the resulting write-up as a &\#x27;vibed pile of spaghetti&\#x27; ten times the required format size, with no apparent rigorous analysis.

reddit · r/MachineLearning · /u/TheWerkmeister · Jul 18, 15:10

**Background**: Kaggle competitions are well-known platforms where data scientists and ML practitioners compete to solve problems, often sponsored by major tech companies. The &\#x27;Measuring Progress Toward AGI&\#x27; competition specifically asked participants to design new cognitive-science-based AI benchmarks. This incident highlights the challenge of evaluating subjective or creative submissions, where rigor can be hard to quantify.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/googledeepmind_how-do-we-measure-progress-toward-agi-it-activity-7439782084551806976-0e2M">How do we measure progress toward AGI ? It takes a village – and...</a></li>
<li><a href="https://www.mindstudio.ai/blog/google-agi-benchmark-10-cognitive-dimensions">How Google&#x27;s New AGI Benchmark Measures Intelligence Across 10 Cognitive Dimensions | MindStudio</a></li>

</ul>
</details>

**Discussion**: The Reddit post has sparked debate, with some commenters supporting the user&\#x27;s analysis and questioning the judges&\#x27; oversight, while others defend the organizers&\#x27; stance that review was proper and the outcome is subjective. The discussion reflects broader concerns about reproducibility and quality control in AI research competitions.

**Tags**: `#AI ethics`, `#Kaggle`, `#DeepMind`, `#research integrity`, `#LLM evaluation`

---

<a id="item-10"></a>
## [Meta in Talks to Rent AI Compute to Anthropic for $10B](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta is negotiating with AI startup Anthropic to rent its AI data center computing power, in a potential deal worth $10 billion over two years. Anthropic proposed the arrangement in June 2026, and Meta is currently evaluating the offer. This deal highlights the extreme scarcity of AI computing resources and could provide Meta with a new revenue stream while validating its massive data center investments. It also reflects the growing trend of large tech companies renting out spare compute capacity to AI startups. If finalized, Anthropic would pay Meta monthly, and both parties have the option to exit the agreement early. The negotiations are still in early stages and may not result in a deal; Meta plans to spend up to $145 billion this year, largely on AI and data centers.

telegram · zaihuapd · Jul 18, 01:14

**Background**: AI computing power, or &\#x27;compute,&\#x27; has become a critical and scarce resource for training and running large language models. Major tech companies like Meta, Microsoft, and Google are investing billions in data centers, and renting out spare capacity has emerged as a way to offset costs and address market demand for compute.

**Tags**: `#AI`, `#cloud computing`, `#Meta`, `#Anthropic`, `#data centers`

---

<a id="item-11"></a>
## [SpaceX in Talks with Pentagon for AI Computing Power Deal](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX is in negotiations with the U.S. Department of Defense to provide data center computing power for running AI models, with a potential deal worth tens of billions of dollars. This deal highlights the increasing importance of AI infrastructure for national security and could significantly expand SpaceX&\#x27;s role in the defense sector, affecting the cloud computing market. The negotiations are ongoing and could still fall through. The Pentagon has recently approved SpaceX, along with Amazon, Google, Microsoft, and Oracle, to use AI models in classified environments. SpaceX has also signed similar computing power agreements with Anthropic and Google.

telegram · zaihuapd · Jul 18, 01:44

**Background**: The Pentagon is accelerating its acquisition of cloud computing capabilities to support AI applications in national security and daily operations. This move aligns with SpaceX&\#x27;s recent expansion into cloud computing services beyond its core satellite launch business, positioning it as a potential major player in the defense cloud market.

**Tags**: `#SpaceX`, `#AI算力`, `#五角大楼`, `#国家安全`, `#云计算`

---

<a id="item-12"></a>
## [OpenRouter Reportedly in Acquisition Talks at $1.3B Valuation](https://www.theinformation.com/articles/startup-openrouter-fields-multi-billion-dollar-takeover-interest) ⭐️ 8.0/10

OpenRouter, an AI model routing platform, is reportedly attracting acquisition interest from multiple large tech companies at a valuation exceeding $1.3 billion. This potential acquisition signals major consolidation in the AI infrastructure space and validates the model routing market, which is critical for optimizing AI model usage. OpenRouter routes over 400 models, serves about 8 million users, processes roughly 100 trillion tokens monthly, and had an annualized revenue of approximately $50 million by early 2026.

telegram · zaihuapd · Jul 18, 03:45

**Background**: OpenRouter is an AI model routing platform that acts as an intermediary, directing user queries to the most suitable AI model from a large pool, optimizing for cost, speed, or quality. Tokens are the basic units of text that AI models process; one token is roughly 4 characters in English. The platform handles massive token volumes, indicating heavy usage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.augmentcode.com/tools/model-routing-platforms-ai-agent-systems">5 Best Model Routing Platforms for AI Agent Systems | Augment Code</a></li>
<li><a href="https://www.braintrust.dev/articles/best-llm-routers-2026">Best LLM routers and model routing platforms in 2026 - Articles - Braintrust</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens? The Language and Currency Powering Modern AI | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#acquisition`, `#model routing`, `#OpenRouter`, `#venture capital`

---

<a id="item-13"></a>
## [TSMC A14 process yield and performance near 90%, ahead of schedule](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 8.0/10

TSMC announced in its earnings call that its A14 \(1.4nm-class\) process has achieved approximately 90% of target device performance and nearly 90% yield on 256 Mb SRAM, up from over 85% and over 80% respectively in April. CEO CC Wei revealed strong interest from smartphone, AI, and HPC customers, with tape-outs progressing faster than planned. This milestone demonstrates TSMC&\#x27;s leadership in advanced semiconductor manufacturing, with A14 expected to deliver 10-15% better performance or 25-30% lower power consumption compared to N2. The progress could accelerate the adoption of 1.4nm technology in AI accelerators, high-end smartphones, and HPC chips, potentially shifting industry roadmaps. A14 is on track for volume production in the second half of 2028, with the current progress significantly ahead of N2&\#x27;s timeline at a comparable stage. The process uses second-generation GAA nanosheet transistors, leveraging experience from N2, and offers a 23% improvement in logic transistor density.

telegram · zaihuapd · Jul 18, 05:00

**Background**: GAA \(Gate-All-Around\) nanosheet transistors are the successor to FinFET technology, offering better electrostatic control and reduced leakage at advanced nodes. TSMC&\#x27;s A14 is a 1.4nm-class process, representing the next step after its upcoming N2 \(2nm\) node. Higher yields and performance at early stages indicate strong process maturity, which is critical for cost-effective mass production.

<details><summary>References</summary>
<ul>
<li><a href="https://community.aijishu.com/a/1060000000394639">FinFET接班人，详解 GAA ...</a></li>
<li><a href="https://www.163.com/dy/article/I1FRKMC90511CPMT.html">FinFET接班人，详解 GAA 的机遇和挑战|栅极|电容|fet...</a></li>
<li><a href="https://mp.ofweek.com/ee/a256714604647">每片晶圆30万元也照买！ 苹果抢占 1 . 4 纳 米 制 程 深层布局曝光 - 维科号V</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#台积电`, `#先进制程`, `#A14`, `#良率`

---

<a id="item-14"></a>
## [Bilibili shows open-source AI companion Project N.E.K.O.](https://finance.sina.com.cn/roll/2026-07-18/doc-iniifanf8394663.shtml) ⭐️ 8.0/10

At the 2026 World AI Conference in Shanghai, Bilibili unveiled Project N.E.K.O., an open-source, proactive full-modal AI companion that can understand desktop content through screen capture and initiate conversations. This project demonstrates a significant advancement in open-source AI companions by combining multi-modal perception, local processing for privacy, and proactive dialogue, with over 1,000 GitHub stars and 10,000 Steam users indicating strong community interest. Project N.E.K.O. supports Live2D and VRM avatar engines, voice cloning via VoiceClone, and a separated architecture for UI, AI brain, and memory, allowing users to keep core data locally.

telegram · zaihuapd · Jul 18, 06:45

**Background**: Live2D is a technology for creating 2D animations from static images, often used for virtual avatars. VRM is a standardized 3D avatar file format designed for VR applications. VoiceClone refers to AI-based voice cloning that replicates a person&\#x27;s voice from a short audio sample. Together, these technologies enable the creation of personalized, interactive AI companions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=GJiYwbz1xd0">Live 2 D Body Angles Tutorial for Beginners - YouTube</a></li>
<li><a href="https://vrm.dev/en/">3D humanoid avatar file format for VR | VRM</a></li>
<li><a href="https://voicecloneai.app/blog/how-ai-voice-cloning-works">How AI Voice Cloning Works: A Complete Guide... | VoiceClone AI</a></li>

</ul>
</details>

**Tags**: `#AI companion`, `#open-source`, `#multi-modal`, `#voice cloning`, `#community-driven`

---