---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 38 items, 25 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B: 2.4T-Parameter MoE Model with Frontier-Level Claims](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Pro 0813 Launches as Production Model](#item-2) ⭐️ 8.0/10
3. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-3) ⭐️ 8.0/10
4. [xAI Releases Grok 4.6, Sparking Debate on API System Prompts and Competition](#item-4) ⭐️ 8.0/10
5. [AI Could Eliminate Middle-Tier Software Engineering Roles](#item-5) ⭐️ 8.0/10
6. [License Plate Reader Searches Should Require a Warrant](#item-6) ⭐️ 8.0/10
7. [Gowers Explores Which Math Problems LLMs Can Handle](#item-7) ⭐️ 8.0/10
8. [No Lossless Transformations of Natural-Language Text](#item-8) ⭐️ 8.0/10
9. [Adam Breaks Rotational Invariance, Losing GD&\#x27;s Low-Rank Bias in Factored Models](#item-9) ⭐️ 8.0/10
10. [LTX-2.5 Open-Source Video Model Runs Locally on a Single RTX 5090](#item-10) ⭐️ 8.0/10
11. [Tencent Q2 Revenue Beats at 204.8B Yuan; AI Capex Triples, Free Cash Flow Turns Negative](#item-11) ⭐️ 8.0/10
12. [WeChat Releases WeLM, Resource-Efficient LLM Family with MoE](#item-12) ⭐️ 8.0/10
13. [Why Tiny JPEGs Look Different in Chrome](#item-13) ⭐️ 7.0/10
14. [uBlock Origin Stops Blocking Facebook Ads, Citing Escalating Arms Race](#item-14) ⭐️ 7.0/10
15. [Grok 4.6 scores 61 on the Artificial Analysis Intelligence Index](#item-15) ⭐️ 7.0/10
16. [AI Code Could Become So Convoluted No One Understands It, Engineer Warns](#item-16) ⭐️ 7.0/10
17. [New website ranks CS conferences by trip quality instead of CORE rating](#item-17) ⭐️ 7.0/10
18. [Zed Unveils Delta, a Multiplayer Coding Environment for AI Agents](#item-18) ⭐️ 6.0/10
19. [2026 Eclipse Webcams: Live Views From Iceland and Spain](#item-19) ⭐️ 6.0/10
20. [Tim King, AmigaDOS Developer, Passes Away](#item-20) ⭐️ 6.0/10
21. [Microsoft Reportedly Plans 7-10% Increase in Windows OEM Fees](#item-21) ⭐️ 6.0/10
22. [Musk: All Future Teslas to Get Starlink, Cybercab First with Integrated Antenna](#item-22) ⭐️ 6.0/10
23. [Codex Passes 10 Million Active Users; Tibo Teases Surprise](#item-23) ⭐️ 6.0/10
24. [ChatGPT Testing $8 Paid Usage Reset for $20 Plan Users](#item-24) ⭐️ 6.0/10
25. [Enterprise SSDs Reach 48% of NAND Shipments; YMTC Enters Top Three](#item-25) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B: 2.4T-Parameter MoE Model with Frontier-Level Claims](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released Qwen3.8-2.4T-A95B, a Mixture-of-Experts \(MoE\) language model with 2.4 trillion total parameters and 95 billion active parameters. The open-weight release on Hugging Face includes BF16 and FP8 versions, and the model card claims performance between Opus and Fable levels. This release pushes open-source MoE models to a new scale, directly challenging proprietary models like Kimi k3 and DeepSeek V4. The relatively small active parameter count \(95B\) makes deployment feasible on high-end consumer hardware after aggressive quantization, signaling a trend toward ultra-large sparse models. The model has a native context length of 262,144 tokens, extendable to 1,010,000 tokens, but lacks vision support and 1M context in the open-weight version. It is available only in BF16 and FP8; no quantization-aware training for 4-bit means community quantizations \(e.g., ~1.3TB\) will require additional calibration data. The license is free for internal use or companies with under $50M annual revenue.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture of Experts \(MoE\) is a neural network architecture that activates only a subset of parameters for each token, allowing models to scale to trillions of parameters while keeping inference compute manageable. In MoE models, total parameters refer to all experts held in memory, while active parameters are the few used per token, which is why a 2.4T-parameter model with 95B active can run on a single GPU when aggressively quantized. Quantization reduces model size and memory footprint but can degrade quality; FP8 is widely supported on modern accelerators, while lower-bit formats like INT4 often require quantization-aware training to avoid accuracy loss.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>
<li><a href="https://rcrtech.com/semiconductor-news/llms-quantization-fp8-fp4-int8/">LLMs and quantization: FP8, FP4, and INT8 explained</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the performance claims but note serving challenges: the model is larger than Kimi k3, only BF16/FP8 versions are available at launch, and the lack of QAT means effective 4-bit quantization will require significant compute and calibration data. Some highlight that a 1-bit quantized version \(397GB\) could bring Opus 4.5-level performance to consumer hardware, while others joke about running it on an Intel N100. There is also disappointment that the open-weight version lacks the vision input and 1M context of the official Qwen3.8-Max.

**Tags**: `#AI`, `#LLM`, `#Qwen`, `#MoE`, `#Machine Learning`

---

<a id="item-2"></a>
## [DeepSeek V4 Pro 0813 Launches as Production Model](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek has released the production version of DeepSeek V4 Pro \(build 0813\), ending a preview period of nearly four months. The model is now available on OpenRouter and adds support for the Responses API format, with the version designation changed to DeepSeek-V4-Pro-0813. This release gives developers access to a flagship open-weight model at a very low cost, continuing DeepSeek&\#x27;s pattern of undercutting Western rivals on price. The strong community engagement and practical test results suggest it could become a go-to option for cost-sensitive development workloads. DeepSeek V4 Pro 0813 is a large-scale mixture-of-experts model with a 1,048,576-token context window and a maximum output of 384,000 tokens. It is priced at $0.435 per million input tokens and $0.87 per million output tokens, and it is the general-availability build that followed roughly four months of preview.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI company founded in 2023 by Liang Wenfeng and funded by the hedge fund High-Flyer. It is known for releasing open-weight large language models at strikingly low training and inference costs, such as DeepSeek-R1 and DeepSeek-V3, which reportedly cost only about US$6 million to train, far less than comparable models from OpenAI or Meta. These models are often built using techniques like mixture of experts \(MoE\) and trained on export-restricted AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**Discussion**: Community reactions were mixed: some users praised the model&\#x27;s cost-effectiveness and were eager to test it, while one developer reported that DeepSeek V4 Pro took 12 minutes and $0.12 but produced a bug, whereas Grok 4.6 finished in 3 minutes and 18 seconds at $1.41 with no bug. Another commenter criticized the choice to link to OpenRouter instead of official documentation or benchmarks, and a user noted a rendering issue in a test output.

**Tags**: `#DeepSeek`, `#AI Models`, `#LLM`, `#Cost Efficiency`, `#Hacker News`

---

<a id="item-3"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale published a post-mortem explaining that recurring database corruption in its control plane was caused by a 16-year-old SQLite WAL-reset race condition. The company funded an open-source SQLite VFS shim that helped isolate the bug, and the SQLite team also uncovered a second stale expression index bug during the investigation. This bug evaded SQLite&\#x27;s famously extensive test suite for over a decade, underscoring how subtle concurrency bugs can hide in even the most battle-tested database code. Tailscale&\#x27;s approach also illustrates how companies can fund targeted open-source debugging tools, which the broader community can reuse. The bug can only occur with multiple concurrent connections to a WAL-mode database, even though Tailscale used a single-writer design. The VFS shim, combined with record-and-replay debugging, helped reproduce and trace the race condition to the WAL-index structures.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is an embedded relational database that supports write-ahead logging \(WAL\), a protocol that improves concurrency by allowing multiple readers alongside a single writer. In WAL mode, a shared WAL-index file coordinates transactions between database connections, and a race condition in the reset phase can corrupt this index under specific timing. Tailscale funded an open-source SQLite VFS shim—a layer that intercepts file operations—to help reproduce and isolate the bug.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug: A Data Corruption Race That Hid for 15...</a></li>

</ul>
</details>

**Discussion**: The community reaction was overwhelmingly positive, with commenters praising Tailscale for funding open-source debugging and writing a detailed post-mortem. Some highlighted the novel funding model, while others expressed curiosity about how a single-writer design could still hit a data race; a few also noted the value of supporting SQLite&\#x27;s ongoing maintenance.

**Tags**: `#sqlite`, `#database`, `#debugging`, `#tailscale`, `#open-source`

---

<a id="item-4"></a>
## [xAI Releases Grok 4.6, Sparking Debate on API System Prompts and Competition](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI announced Grok 4.6, an incremental update to its frontier chatbot model, making it available via API and in Cursor subscriptions. The release immediately sparked extensive Hacker News discussion, particularly about the API adding a default system prompt that overrides user instructions. This release underscores xAI&\#x27;s growing role as a serious frontier-model competitor, potentially offering a cost-effective alternative to OpenAI and Anthropic. The heated debate over system prompt behavior also highlights broader industry concerns about user control, transparency, and how benchmarks are achieved. Users report that the xAI API appends a default system prompt to every request, and its instruction not to mention these guidelines can supersede user-supplied system prompts, leading to refusals. Community comparisons suggest Grok 4.6 is perceived as fast, concise, and competitive in price against models like GPT-5.6-Sol and Kimi K3.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is an AI chatbot developed by xAI, built on large language models and designed to compete with OpenAI&\#x27;s GPT and Google&\#x27;s Gemini. System prompts are predefined directives in LLMs that guide model behavior and take precedence over user inputs, making their design and enforcement a key governance issue. The controversy around Grok 4.6&\#x27;s API system prompt reflects this wider tension between provider control and user agency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_%28chatbot%29">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://x.ai/">SpaceXAI — Creators of Grok, the AI Chatbot</a></li>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some praise Grok 4.6&\#x27;s speed, conciseness, and pricing, while others express concern about the API&\#x27;s default system prompt overriding user instructions. Several skeptics question whether rapid benchmark gains across labs are genuine or result from distillation or benchmark hacking, and some view Grok as healthy competition despite its polarizing reputation.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#model release`

---

<a id="item-5"></a>
## [AI Could Eliminate Middle-Tier Software Engineering Roles](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

A blog post by Florian Herrengt argues that AI coding tools are eliminating middle-tier software engineering work by automating routine coding tasks, while amplifying the productivity of both strong and weak engineers. The post has attracted widespread discussion, with 584 comments debating the implications for the profession. This matters because it reflects a growing belief that AI assistants are reshaping the software engineering job market, potentially compressing career ladders and changing how engineering teams are structured. If true, it could affect hiring practices, salaries, and the skills developers need to stay relevant. The central claim is that AI is &\#x27;removing the middle class&\#x27; of software engineering—not eliminating all jobs, but shrinking the demand for developers who primarily implement well-defined tasks. Commenters point out that this could lead to &\#x27;bad&\#x27; engineers amplifying their bad output, and to a reduced need for the traditional senior-to-junior handoff via Jira tickets.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**Background**: Software engineering has often been viewed as a field with a broad middle tier: senior engineers design systems and break work into tickets, while mid-level and junior engineers write the code and solve isolated problems, often relying on search engines and Q&amp;A sites like Stack Overflow. AI coding assistants such as GitHub Copilot and ChatGPT can now generate boilerplate code, fix common errors, and even implement small features from natural-language prompts. The blog post argues that this automation is making the middle tier redundant, leaving only highly skilled architects on one end and low-cost or prompt-driven workers on the other. This debate is part of a larger conversation about how generative AI will change knowledge work and the future of tech employment.

**Discussion**: Commenters share a mix of agreement and skepticism. Some agree that AI can amplify the negative impact of disengaged &\#x27;bad&\#x27; engineers, while others question whether there is concrete evidence of job losses yet. One commenter reinterprets the trend as &\#x27;the automation of the Stack Overflow engineer,&\#x27; suggesting senior engineers will handle work directly instead of handing off to juniors. Several emphasize the importance of not outsourcing critical thinking to LLMs and of continuing to learn fundamentals.

**Tags**: `#AI`, `#Software Engineering`, `#Future of Work`, `#LLMs`, `#Tech Industry`

---

<a id="item-6"></a>
## [License Plate Reader Searches Should Require a Warrant](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/) ⭐️ 8.0/10

An article argues that searches of automated license plate reader \(ALPR\) data should require a warrant, touching off a debate over mass surveillance and police accountability. This matters because ALPRs enable continuous location tracking of vehicles, and requiring warrants would impose judicial oversight on a powerful surveillance tool. The debate could influence how cities and police departments handle ALPR data and whether new privacy-preserving technologies are adopted. ALPR devices are essentially general-purpose internet-connected cameras that can be repurposed beyond reading plates, and there have been cases of police misusing stored location data. Commenters have also proposed cryptographic approaches such as zero-knowledge proofs and homomorphic encryption to allow verification without revealing location history.

hackernews · apwheele · Aug 12, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49273165)

**Background**: Automated license plate readers \(ALPRs\) are cameras that capture license plates and locations, often mounted on patrol cars or fixed poles, and the data can be stored for years. Privacy advocates argue this enables mass surveillance, while law enforcement says it helps solve crimes. Without a warrant, police can often search this data freely; some jurisdictions treat it as public record under FOIL laws. Cryptographic techniques like zero-knowledge proofs and homomorphic encryption are part of a broader effort to make such data usable without exposing individuals&\#x27; movements.

<details><summary>References</summary>
<ul>
<li><a href="https://sls.eff.org/technologies/automated-license-plate-readers-alprs">Automated License Plate Readers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments express strong distrust of ALPRs, with one noting they are general-purpose cameras that could be co-opted into a mass surveillance network. A reader proposes a cryptographic system where license plates display rotating numbers derived from a DMV-issued private key to prevent tracking. Others argue that a warrant requirement is insufficient if mass surveillance itself is the problem, and one commenter criticizes the article&\#x27;s tone of inevitability about cameras in public spaces.

**Tags**: `#privacy`, `#surveillance`, `#law-enforcement`, `#cryptography`, `#public-policy`

---

<a id="item-7"></a>
## [Gowers Explores Which Math Problems LLMs Can Handle](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

In a new blog post, mathematician Timothy Gowers examines which kinds of mathematical problems large language models can actually solve, connecting their strengths to sampling and test-time scaling. He also questions when LLMs might produce genuinely novel, elegant proofs rather than merely searching a large space of possibilities. Because Gowers is a Fields Medalist and prominent mathematician, his analysis carries weight in both AI and mathematics communities. His focus on test-time scaling and sampling helps frame where LLM-based tools are reliable and where they may fall short in research mathematics. The post reportedly never uses the term &\#x27;test-time scaling,&\#x27; yet commenters note the argument is essentially about it. One commenter cites Google&\#x27;s AlphaCode, which generated millions of candidate programs and filtered them to beat average human programmers in 2022, as an early example of sampling-driven success.

hackernews · ColinWright · Aug 12, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49270022)

**Background**: Test-time scaling refers to allocating extra computation during inference—such as letting a model generate many candidate solutions or &\#x27;think&\#x27; longer—to improve reasoning, and it has become a major research direction as pretraining compute growth slows. Sampling is the process by which LLMs choose the next token from a probability distribution; generating many samples and filtering them can dramatically boost performance on math and coding tasks. These ideas are central to understanding why LLMs can handle certain mathematical problems, and why producing a surprising but beautiful proof remains a much harder challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.24235">[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?</a></li>
<li><a href="https://testtimescaling.github.io/">What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.1278/">Balancing Diversity and Risk in LLM Sampling: How to Select ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely engage seriously with Gowers&\#x27; argument. One notes the post is really about test-time scaling and emphasizes that early sampling-based results like AlphaCode were the first surprising wins; another agrees with Gowers that genuinely human-level proofs would be recognizable. Others share lists of AI math achievements and wonder how LLMs would handle temporal logic or counterexample search.

**Tags**: `#LLMs`, `#mathematics`, `#AI research`, `#test-time scaling`, `#proofs`

---

<a id="item-8"></a>
## [No Lossless Transformations of Natural-Language Text](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/) ⭐️ 8.0/10

Sophie Alpert published her internal policy on acceptable AI-assisted writing for engineers, arguing that there are no lossless transformations of natural-language text. Simon Willison highlighted and endorsed this policy, calling it crucial. This guidance offers practical, concrete principles for responsibly using LLMs in writing, emphasizing that authors must stand behind every sentence. It is especially relevant to engineers and technical writers, and could shape team policies on AI-assisted documentation. The core rule is that authors must stand behind every idea and sentence, and cannot dismiss unclear lines with &\#x27;AI wrote that.&\#x27; The &\#x27;no lossless transformations&\#x27; idea explains that any AI rewrite lacking the author&\#x27;s detailed mental representation will inevitably lose information.

rss · Simon Willison · Aug 11, 23:48

**Background**: Lossless transformation is a concept from data compression where the original data can be perfectly reconstructed. Alpert applies this idea to natural language, arguing that every rewrite or rephrase changes meaning, and when done by an AI that lacks the author&\#x27;s precise intent, information is lost. This context is important because AI writing tools are increasingly used by engineers and technical writers, making clear accountability policies necessary.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/">There are no lossless transformations of natural-language text</a></li>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural-language text</a></li>

</ul>
</details>

**Tags**: `#AI writing`, `#LLM`, `#software engineering`, `#documentation`, `#responsibility`

---

<a id="item-9"></a>
## [Adam Breaks Rotational Invariance, Losing GD&\#x27;s Low-Rank Bias in Factored Models](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A Reddit analysis shows that Adam&\#x27;s per-coordinate second moment breaks the rotational invariance of factored models, causing it to lose the implicit low-rank bias that gradient descent exhibits. In systematic tests on nine update rules, only GD, shared-scalar Adam, Muon, and Shampoo preserved the bias, while Adam, RMSProp, Lion, signum, and Adafactor did not. This finding provides a mechanistic explanation for why some optimizers preserve the low-rank simplicity bias that helps generalization in deep learning, while others do not. It could guide the design of optimizers that maintain desirable inductive biases, particularly for tasks like matrix sensing and deep linear networks. The analysis tested nine update rules on underdetermined matrix sensing at matched training loss, yielding two clean clusters. A one-parameter family interpolating Adam&\#x27;s denominator from per-coordinate to shared scalar showed monotonic recovery, and Muon showed surprising crossover behavior near 4% spectral tail energy; the author also found that switching from per-coordinate clip to a global norm clip improved recovery error from 0.347 to 0.220 in their own optimizer.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In factored models where a weight matrix is written as W = UVᵀ, the loss is invariant to orthogonal rotations of the factors, and gradient descent respects this symmetry. However, Adam&\#x27;s per-coordinate second-moment normalization breaks this invariance, which removes the implicit low-rank bias that helps generalization. Muon is a newer optimizer that has shown strong performance in large language model training, and Shampoo is a preconditioned tensor optimizer; both preserve the invariance. The low-rank simplicity bias of gradient-based methods is a well-studied phenomenon in deep learning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2103.10427">[2103.10427] The Low-Rank Simplicity Bias in Deep Networks SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks The Low-Rank Simplicity Bias in Deep Networks - arXiv.org SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks SGD Noise and Implicit Low-Rank Bias in Deep Neural Networks The Low-rank Simplicity Bias in Deep Networks THE L -R SIMPLICITY BIAS IN DEEP NETWORKS - GitHub Pages</a></li>
<li><a href="https://grokipedia.com/page/muon-optimizer">Muon optimizer</a></li>
<li><a href="https://arxiv.org/abs/1802.09568">[1802.09568] Shampoo: Preconditioned Stochastic Tensor Optimization</a></li>

</ul>
</details>

**Tags**: `#optimization`, `#deep learning`, `#matrix factorization`, `#Adam`, `#low-rank`

---

<a id="item-10"></a>
## [LTX-2.5 Open-Source Video Model Runs Locally on a Single RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX released LTX-2.5, an open-source video generation foundation model with published weights, training code, and inference pipeline. The model supports text-to-video and image-to-video generation, and can run locally on a single RTX 5090. This release marks a milestone for open-source video generation by enabling high-quality local inference on consumer-grade hardware, significantly lowering the barrier for developers and small teams. Free commercial use for companies under $10M annual revenue and strong evaluation results could accelerate adoption in creative and AI content workflows. LTX-2.5 uses a new diffusion video decoder and a Gemma 4 12B text encoder. In an automated flaw-based evaluation of 98 text-to-video prompts across ten models, LTX 2.5 Pro ranked first; it also supports multi-shot scene generation in one pass and cinema-grade EXR export.

telegram · zaihuapd · Aug 12, 02:15

**Background**: Video generation models typically require large server clusters and are often closed-source, limiting experimentation and local use. Open-source releases like LTX-2.5 offer researchers and artists local alternatives. Gemma 4 12B is an open multimodal model from Google DeepMind that natively handles text, images, audio, and video without separate encoders, and the diffusion video decoder converts latent representations into coherent video frames. The cited evaluation uses automated scoring instead of human judgment.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX&#x27;s Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/gemma-4-12B · Hugging Face</a></li>
<li><a href="https://www.labellerr.com/blog/gemma-4-12b-run-locally-and-fine-tune/">Gemma 4 12B : Run Locally, Fine-Tune, Benchmark Performance</a></li>

</ul>
</details>

**Tags**: `#video-generation`, `#open-source`, `#AI`, `#local-inference`, `#LTX`

---

<a id="item-11"></a>
## [Tencent Q2 Revenue Beats at 204.8B Yuan; AI Capex Triples, Free Cash Flow Turns Negative](https://wallstreetcn.com/articles/3779275) ⭐️ 8.0/10

Tencent reported Q2 revenue of 204.8 billion yuan, up 11% year-over-year and slightly above Bloomberg expectations. Capital expenditures nearly tripled to 52.8 billion yuan, driven by AI infrastructure investment, pushing free cash flow to negative 13.8 billion yuan. This marks a strategic pivot for Tencent, prioritizing AI infrastructure spending over short-term cash generation, a trend echoing broader moves by major tech firms. The negative free cash flow, despite strong revenue growth, signals intensified AI competition and could pressure future profitability and investor sentiment. Net profit rose only 0.7% to 56 billion yuan, missing expectations. Excluding AI compute prepayments, Tencent said free cash flow would have been 37.6 billion yuan; marketing services revenue led growth at 22%, while domestic games rose 17% and international games dipped 0.8% on FX headwinds.

telegram · zaihuapd · Aug 12, 10:30

**Background**: Tencent has been rapidly expanding its AI infrastructure, including investments in AI compute and its office AI agent WorkBuddy, which reportedly leads Chinese desktop AI office agent monthly visits. Capital expenditure on AI data centers and prepayments for AI computing capacity have become a major cash outlay, a common pattern among Chinese tech giants racing to build AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://workbuddy365.com.cn/">WorkBuddy官网 | AI办公智能体 腾讯出品 功能介绍</a></li>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>
<li><a href="https://xueqiu.com/1540104684/403488053">xueqiu.com/1540104684/403488053</a></li>

</ul>
</details>

**Tags**: `#Tencent`, `#Earnings`, `#AI Infrastructure`, `#Capital Expenditure`, `#Free Cash Flow`

---

<a id="item-12"></a>
## [WeChat Releases WeLM, Resource-Efficient LLM Family with MoE](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 8.0/10

WeChat&\#x27;s AI team announced WeLM, a family of resource-efficient large language models built around Mixture of Experts \(MoE\) architecture. The WeLM-80B \(3B activated\) is already deployed in WeChat&\#x27;s AI assistant Xiaowei, while the in-development WeLM-617B \(23B activated\) targets complex ecosystem tasks. This release highlights how a major tech company is leveraging MoE to achieve competitive performance with far fewer active parameters, potentially lowering the computational cost of large-scale LLM deployment. Because WeLM already powers WeChat&\#x27;s AI assistant, the integration can impact hundreds of millions of users and may accelerate similar efficiency-driven approaches across the industry. WeLM-80B has 80 billion total parameters but only 3 billion activated per token, while the upcoming WeLM-617B activates 23 billion parameters. The 617B model is intended for scenarios such as intelligent mini-program development and the generation of small tools for WeChat&\#x27;s AI assistant.

telegram · zaihuapd · Aug 12, 13:58

**Background**: WeLM \(WeChat Language Model\) is a pre-trained language model series developed by Tencent&\#x27;s WeChat team; the original 2022 release was a 10B-parameter model that reportedly matched the performance of models up to 25 times larger. Mixture of Experts \(MoE\) is a machine learning technique where a router selects a subset of expert networks for each input, so only a fraction of the model&\#x27;s total parameters are activated per token, improving efficiency while preserving capacity. The WeLM team&\#x27;s blog reports that an 80B-A3B MoE model trained on fewer than 14 trillion tokens delivers competitive performance against similarly sized and larger systems.

<details><summary>References</summary>
<ul>
<li><a href="https://welm.weixin.qq.com/en/">WeLM Blog</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#WeChat`, `#AI`, `#resource efficiency`

---

<a id="item-13"></a>
## [Why Tiny JPEGs Look Different in Chrome](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

A technical blog post explains that Chrome renders tiny JPEGs differently because it performs decode-time downscaling, shrinking images while decoding instead of scaling them after the full decode. The author recommends serving images at the exact display size rather than relying on browser scaling. This subtle rendering difference can cause images to appear blurrier or sharper depending on the browser, which matters for web developers who care about visual consistency. It also highlights a broader performance best practice: shipping appropriately sized images saves bandwidth and decode time. Chrome and Firefox use different scaling algorithms, so even the same decode-time downscaling approach can produce visibly different results. The post advises against using JPEGs for icons and similar UI elements; developers should use correct-resolution assets instead of oversized images.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**Background**: JPEG is a lossy image format mainly suited to photographs, while PNG is lossless and supports transparency, making it common for icons. Modern browsers decode and scale images as part of their rendering pipeline, and Chrome&\#x27;s optimized decoding path can apply downscaling during decode for efficiency. The Chromium project documents its rendering architecture, including image processing, through the RenderingNG effort.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/chromium/renderingng-architecture">RenderingNG architecture | Chromium | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/chromium/renderingng">RenderingNG | Chromium | Chrome for Developers</a></li>
<li><a href="https://stackoverflow.com/questions/3343090/which-is-the-fastest-decoder-for-jpeg-full-scale-decoding">c++ - Which is the fastest decoder for jpeg full- scale ... - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Commenters pointed out that PNGs can be affected too, and that Chrome&\#x27;s change once broke Electron app icons. Others noted Firefox is working on lower-scale decompression, and that Chrome and Firefox use different scaling algorithms, with some preferring Firefox&\#x27;s sharper result. A CSS workaround using image-rendering was also mentioned.

**Tags**: `#jpeg`, `#browser`, `#image-scaling`, `#chrome`, `#web-performance`

---

<a id="item-14"></a>
## [uBlock Origin Stops Blocking Facebook Ads, Citing Escalating Arms Race](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 7.0/10

uBlock Origin has officially stopped attempting to block ads on Facebook, acknowledging that the platform&\#x27;s anti-adblocking measures have made it technically impractical. The decision was reported via Neowin and discussed in the r/uBlockOrigin subreddit. This marks a symbolic defeat in the ad-blocking arms race, showing that even top-tier filter lists can be overwhelmed by platforms with deep resources. It affects millions of users who rely on uBlock Origin for privacy and a cleaner browsing experience on Facebook, and it may push developers toward AI-based ad detection rather than traditional filter lists. Facebook ads are served as first-party content from the same domain and are dynamically rendered, making them nearly indistinguishable from organic posts using static filter rules. uBlock Origin&\#x27;s maintainer and community concluded that the effort required to keep up with Facebook&\#x27;s anti-blocking techniques is no longer sustainable. The decision does not affect uBlock Origin&\#x27;s ad blocking on other websites.

hackernews · Markoff · Aug 12, 11:28 · [Discussion](https://news.ycombinator.com/item?id=49270726)

**Background**: uBlock Origin is a free, open-source browser extension with over 10 million users, known for its low memory and CPU usage while blocking ads and trackers. Traditional ad blockers rely on filter lists of known ad domains, but Facebook embeds ads directly into its feed and serves them from its own infrastructure. Facebook&\#x27;s help center explicitly states that users cannot block Facebook ads entirely, and the platform continuously changes its code to evade ad-blocking tools. This background explains why uBlock Origin&\#x27;s decision was inevitable rather than surprising.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://www.facebook.com/help/146952742043748">Can you block or hide ads showing on your Facebook account | Facebook Help Center</a></li>
<li><a href="https://www.cloudwards.net/stop-ads-on-facebook/">How to Get Rid of Ads on Facebook: 8 Proven Ways for 2026</a></li>

</ul>
</details>

**Discussion**: Reddit commenters largely supported the call, viewing it as a pragmatic retreat from a losing battle. One user predicted the ultimate ad blocker will use computer vision to detect and cover ads visually, while others argued that the only true escape is leaving Facebook altogether. Some also noted the irony of Facebook&\#x27;s ad platform reaching &\#x27;disgusting&\#x27; levels of technical complexity, with several users sharing nostalgic references to older ad-replacement tools.

**Tags**: `#ad-blocking`, `#uBlock Origin`, `#Facebook`, `#privacy`, `#arms race`

---

<a id="item-15"></a>
## [Grok 4.6 scores 61 on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis) ⭐️ 7.0/10

Grok 4.6, the latest model from SpaceXAI, scored 61 on the Artificial Analysis Intelligence Index. The model is now available through SpaceXAI&\#x27;s API and grok.com, with a cache read price of $0.50 per million tokens, up from $0.30 for Grok 4.5. This score places Grok 4.6 among frontier AI models, and community feedback shows it is already a daily driver for coding tasks, often used with Cursor or Grok Build. However, the near-doubling of cache read pricing could affect developers with heavy API usage. The Artificial Analysis Intelligence Index is a composite benchmark that includes tests such as GDPval-AA v2, Terminal-Bench v2.1, and Humanity&\#x27;s Last Exam. According to a community comment, cache read/write charges often account for about 80% of a heavy coding session&\#x27;s token bill, making the price increase from $0.30 to $0.50 significant.

hackernews · wertyk · Aug 12, 16:54 · [Discussion](https://news.ycombinator.com/item?id=49275385)

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark that measures language model capabilities across reasoning, coding, knowledge, instruction following, scientific reasoning, and multi-step tasks. Grok is an AI assistant built by SpaceXAI \(formerly xAI\), and Grok 4.6 is the latest model in the series, available through dedicated APIs and at grok.com. Developers often use such indices to compare frontier models and decide which to integrate into their tools.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://docs.x.ai/developers/models">Models | SpaceXAI Docs</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model &amp; API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters generally have a positive view of Grok 4.6 for coding: one says it communicates better than Claude and is faster than Claude Code, while another highlights Cursor&\#x27;s subscription as a cost-effective way to use Grok. A user points out that cache read pricing almost doubled from $0.30 to $0.50 and that most of their token bill is cache reads/writes in heavy coding sessions. Another commenter jokingly says this makes them bullish on Gemini if reaching the frontier is this easy.

**Tags**: `#AI`, `#benchmarks`, `#Grok`, `#LLM`, `#pricing`

---

<a id="item-16"></a>
## [AI Code Could Become So Convoluted No One Understands It, Engineer Warns](https://simonwillison.net/2026/Aug/12/florian-herrengt/) ⭐️ 7.0/10

Florian Herrengt published a blog post arguing that AI-generated codebases may become so convoluted that no human—or even an AI like Fable—can understand them, potentially eliminating the need for middle-class software engineers. Simon Willison highlighted the quote on his blog on August 12, 2026. This highlights a critical risk in the rapid adoption of AI-assisted programming: codebases may accumulate unmanageable complexity, making maintenance and debugging increasingly difficult. It could reshape software engineering roles, particularly mid-level developers who traditionally bridge the gap between business logic and implementation. The quote specifically mentions Fable, an Anthropic AI model, failing to fix a recurring bug, and a developer admitting they don&\#x27;t know where the data comes from, relying on Claude to generate code. The post&\#x27;s argument centers on &\#x27;cognitive debt&\#x27;—code that functions but that no one truly comprehends.

rss · Simon Willison · Aug 12, 15:08

**Background**: Claude is a series of large language models developed by Anthropic, first released as a chatbot in March 2023; Fable is a newer Anthropic model \(announced alongside Claude Fable 5\) that the quote references as a hypothetical debugging tool. AI-assisted programming tools like these can generate large amounts of code quickly, but if developers blindly trust AI output without understanding it, codebases can become difficult to maintain—an issue sometimes called &\#x27;cognitive debt.&\#x27; Simon Willison is a prominent developer and blogger who frequently curates thought-provoking commentary about AI and software engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software-engineering`, `#developer-productivity`, `#future-of-work`

---

<a id="item-17"></a>
## [New website ranks CS conferences by trip quality instead of CORE rating](https://www.reddit.com/r/MachineLearning/comments/1vmbdk6/i_built_an_honest_cs_conference_ranking_sorted_by/) ⭐️ 7.0/10

A developer launched Honest CS Rankings \(honestcsrankings.org\), a site that ranks roughly 540 upcoming CORE-ranked conferences by destination quality—weather, safety, cost, accessibility, and city vibe—instead of by their CORE tier. The tool includes filters, a home-city distance option, an &\#x27;Upsets&\#x27; tab, .ics calendar export, and deep links for coauthors. This tool fills a real gap: researchers often weigh the host city when deciding where to submit and attend, even if rankings are the primary metric. By making venue appeal transparent and customizable, it could influence submission decisions, increase attendance at under-appreciated locations, and spark broader discussion about conference quality beyond raw rankings. The site uses real climate data for the conference month, the Global Peace Index for safety, and World Bank price levels for cost. Notable caveats: ICML/ICLR 2027 are absent because they are not yet announced, COLM is missing because CORE hasn&\#x27;t ranked it, and the long tail of smaller conferences scraped from WikiCFP may contain errors.

reddit · r/MachineLearning · /u/JohnAZoidberg77 · Aug 12, 11:23

**Background**: The CORE \(Computing Research and Education Association of Australasia\) conference ranking is a widely used system that rates computing conferences into tiers A\*, A, B, and C, influencing how researchers and institutions perceive venue prestige. WikiCFP is a community-driven wiki that aggregates calls for papers for conferences, workshops, and journals, often used by academics to find upcoming deadlines. The Global Peace Index \(GPI\), produced by the Institute for Economics &amp; Peace, ranks countries by peacefulness and is a proxy for safety at conference destinations. Researchers frequently consider the host city&\#x27;s livability and travel logistics in parallel with formal rankings, which is the problem this tool addresses.

<details><summary>References</summary>
<ul>
<li><a href="https://www.core.edu.au/conference-portal">CORE Rankings Portal - core.edu.au</a></li>
<li><a href="http://www.wikicfp.com/">WikiCFP : Call For Papers of Conferences, Workshops and Journals</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Peace_Index">Global Peace Index</a></li>

</ul>
</details>

**Tags**: `#conference rankings`, `#CS conferences`, `#travel`, `#ML community`, `#tools`

---

<a id="item-18"></a>
## [Zed Unveils Delta, a Multiplayer Coding Environment for AI Agents](https://zed.dev/blog/introducing-delta) ⭐️ 6.0/10

Zed has introduced Delta, a new multiplayer coding environment designed for collaborating with AI agents and reviewing their work. Currently in private beta, Delta uses a proprietary real-time database called DeltaDB to keep code and conversation threads synchronized. This move signals a push toward making AI agent collaboration more interactive and transparent, addressing concerns about AI code quality by letting developers inspect the conversation behind a change. However, community reaction is mixed, reflecting a broader debate about whether multiplayer coding is a practical need or a solution in search of a problem. Delta is currently in private beta and revolves around two core features: real-time collaborative multiplayer conversations and conversation-as-document, which allows inline commenting directly in an AI agent&\#x27;s conversation thread. The feature is built on DeltaDB, a proprietary real-time database that synchronizes code and conversation context as the software evolves.

hackernews · khy · Aug 12, 18:19 · [Discussion](https://news.ycombinator.com/item?id=49276574)

**Background**: Zed is an open-source, high-performance code editor written in Rust, created by Nathan Sobo, one of the founders of Atom, and Zed Industries. It has long emphasized multiplayer editing and AI-assisted features, with free basic use and paid AI capabilities. Delta extends this multiplayer approach specifically to coding with AI agents, allowing teams to collaborate on—and review—the entire process an agent takes to produce a change, rather than just the final diff.

<details><summary>References</summary>
<ul>
<li><a href="https://zed.dev/">Zed — Your last next editor</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zed_%28text_editor%29">Zed (text editor) - Wikipedia</a></li>
<li><a href="https://news.linxi.com.au/news/zed-launches-delta-a-multiplayer-coding-environment-for-ai-agents">Zed launches Delta multiplayer coding environment with AI ...</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed. Some commenters question the practical value of multiplayer coding, calling it &\#x27;cool tech for no useful purpose&\#x27; and noting that coding is usually a solitary activity. Others are intrigued, particularly by the ability to comment inline within an agent conversation, which could aid in mentoring junior developers and auditing AI-generated PRs. A separate thread of criticism targets the blog post&\#x27;s low-contrast design, which many found difficult to read.

**Tags**: `#Zed`, `#code editor`, `#collaborative editing`, `#AI`, `#developer tools`

---

<a id="item-19"></a>
## [2026 Eclipse Webcams: Live Views From Iceland and Spain](https://jonty.github.io/2026_eclipse_webcams/) ⭐️ 6.0/10

A hastily assembled website aggregates live webcam feeds from Iceland and Spain to let viewers follow the 2026 total solar eclipse remotely. The project, created by developer jonty, was shared on Hacker News and quickly drew enthusiastic comments. This site makes a rare astronomical event accessible to anyone with an internet connection, regardless of their location. It also illustrates how simple tools can build community around shared experiences. The site is a basic webcam aggregator rather than a controlled livestream, and the author jonty notes it may buckle under heavy traffic. Viewers can expect feeds from Iceland and Spain, which lie on the 2026 eclipse&\#x27;s path of totality.

hackernews · zoenolan · Aug 12, 11:53 · [Discussion](https://news.ycombinator.com/item?id=49270953)

**Background**: A total solar eclipse occurs when the Moon completely covers the Sun, revealing the Sun&\#x27;s faint corona. The 2026 total eclipse will cross Iceland and Spain, making these key locations for live webcam views. jonty previously built a similar webcam aggregator for the 2024 US eclipse, finishing it just before totality began.

**Discussion**: Commenters were enthusiastic and shared personal stories: aljgz described traveling to Canada for the 2024 eclipse and treating eclipses as life milestones, while orsenthil noted the historical significance of Thales of Miletus&\#x27;s first correct eclipse prediction. Another commenter, alkyon, described seeing pink prominences through binoculars, and 1970-01-01 pointed to solar panel monitoring data as an interesting additional view. Overall, the sentiment was positive, with appreciation for the quick resource and the shared experience.

**Tags**: `#Eclipse`, `#Webcams`, `#Astronomy`, `#Event`, `#Hacker News`

---

<a id="item-20"></a>
## [Tim King, AmigaDOS Developer, Passes Away](https://amiga-news.de/en/news/AN-2026-08-00070-EN.html) ⭐️ 6.0/10

Tim King, a key developer of AmigaDOS, the disk operating system of AmigaOS, has died. Members of the Amiga community are sharing remembrances and appreciation for his contributions. King&\#x27;s work on AmigaDOS helped power the Amiga line of computers, which influenced a generation of programmers and creatives in the 1980s and 1990s. His passing highlights the enduring legacy of early personal computing pioneers. AmigaDOS, based on a port of TRIPOS by MetaComCo, was originally written in BCPL and later rewritten in C starting with AmigaOS 2.x. One commenter recalls King as the founder of UK Online, and an interview with him from October 2021 was shared in the discussion.

hackernews · doener · Aug 12, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49272655)

**Background**: The Amiga was a family of personal computers launched by Commodore in 1985, known for advanced graphics and sound hardware. AmigaDOS provided the file systems, command-line interface, and disk management for AmigaOS, and its command-line environment introduced many users to computing fundamentals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AmigaDOS">AmigaDOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amiga_computer">Amiga computer</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal memories and gratitude, with one user crediting AmigaDOS as a gateway to learning the Linux command line. Another remembered King as a friendly and helpful founder of UK Online, and a link to a 2021 interview was posted for those wanting to learn more.

**Tags**: `#Amiga`, `#Obituary`, `#Retro Computing`, `#AmigaDOS`, `#History`

---

<a id="item-21"></a>
## [Microsoft Reportedly Plans 7-10% Increase in Windows OEM Fees](https://www.techspot.com/news/113430-microsoft-raises-windows-oem-fees-pc-makers-7.html) ⭐️ 6.0/10

Microsoft reportedly plans to raise Windows OEM licensing fees for some PC manufacturers by 7% to 10% starting July 2026, a higher increase than the typical single-digit annual hikes. Retail Windows 11 prices are unaffected. This fee increase could further push up PC prices, especially for budget models already squeezed by rising component costs. PC makers, consumers, and the broader Windows ecosystem may all feel the impact. The exact fee increase varies by manufacturer and product line, with some 600-800 USD PC models having already risen close to 1000 USD. Microsoft has not publicly commented on the report.

telegram · zaihuapd · Aug 12, 02:32

**Background**: A Windows OEM license is a pre-installed version of Windows that PC manufacturers like Dell or HP bundle with their hardware. It is locked to the first device it is activated on and cannot be transferred, unlike a retail license, which offers more flexibility. The PC industry has been dealing with rising memory and other component costs, which already strained price-sensitive segments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.partitionwizard.com/clone-disk/win10-oem-vs-retail.html">Learn the Difference Between Windows 10 OEM and Retail</a></li>
<li><a href="https://www.bbirdg.com/blogs/tech/windows-oem-vs-retail-difference">Windows OEM vs Retail: Which license should you buy?</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Windows`, `#OEM`, `#Pricing`, `#PC Industry`

---

<a id="item-22"></a>
## [Musk: All Future Teslas to Get Starlink, Cybercab First with Integrated Antenna](https://www.techspot.com/news/113429-elon-musk-every-tesla-have-starlink-starting.html) ⭐️ 6.0/10

Elon Musk announced on an earnings call that all future Tesla models will include Starlink connectivity, starting with the Cybercab, which was shown with an integrated Starlink V5 antenna in the rear roof. The Cybercab&\#x27;s satellite link delivers speeds exceeding 375 Mbps, enabling navigation, customer service, fleet management, and 4K video streaming for passengers, though no production timeline was given. This move makes satellite connectivity a standard feature across Tesla&\#x27;s entire future lineup, which is critical for enabling robotaxi operations that require ubiquitous coverage. It could also pressure other automakers to adopt satellite-based connectivity for autonomous and in-car entertainment applications. The Cybercab is a purpose-built autonomous vehicle with no steering wheel or pedals, and its V5 antenna is integrated into the rear roof rather than mounted externally. The V5 antenna is designed to be smaller, lighter, and cheaper to manufacture, which helps enable mass adoption across Tesla&\#x27;s vehicle lineup.

telegram · zaihuapd · Aug 12, 03:53

**Background**: Starlink is SpaceX&\#x27;s satellite internet constellation that provides high-speed, low-latency broadband from low Earth orbit, and it is already used in vehicles like RVs and boats. Tesla&\#x27;s Cybercab is a two-seat autonomous electric vehicle unveiled in 2024, designed for robotaxi service without manual controls. The integrated Starlink V5 antenna marks a shift from aftermarket mounts to factory-installed satellite hardware in passenger vehicles.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://hypebeast.com/2026/8/tesla-cybercab-debuts-with-integrated-starlink-v5">Tesla Cybercab With Starlink V 5 Antenna Revealed | Hypebeast</a></li>
<li><a href="https://otontechnology.com/starlink-v5-dish-smaller-lighter-efficient/">SpaceX&#x27;s Starlink V 5 Ships With Half the Antenna Elements</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Starlink`, `#Satellite`, `#Connectivity`, `#Robotaxi`

---

<a id="item-23"></a>
## [Codex Passes 10 Million Active Users; Tibo Teases Surprise](https://x.com/thsottiaux/status/2087423996115681767) ⭐️ 6.0/10

OpenAI&\#x27;s coding agent Codex has surpassed 10 million active users. Tibo, an OpenAI figure, posted on X that the team has been silent and teased a surprise announcement for tomorrow. Reaching 10 million active users makes Codex a major player in the AI coding agent market, intensifying competition among developer-focused AI tools. The upcoming surprise could signal new features or milestones relevant to the broader developer ecosystem. Tibo previously promised to perform a &\#x27;reset&\#x27; each time Codex gained another million active users, up to 10 million. He says the user count has now far exceeded that figure, and the team has stayed silent until this surprise teaser.

telegram · zaihuapd · Aug 12, 08:01

**Background**: Codex is an AI coding agent developed by OpenAI for software engineering tasks such as writing code and fixing bugs. It was released in April 2025 as Codex CLI and is available through ChatGPT&\#x27;s web app, a desktop app for Windows and macOS, and several IDE integrations. Note that an earlier OpenAI Codex language model, built on GPT-3 and trained on Python code from GitHub, also shares the name but is a different product.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28language_model%29">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Codex`, `#OpenAI`, `#AI`, `#Product Milestone`, `#Announcement`

---

<a id="item-24"></a>
## [ChatGPT Testing $8 Paid Usage Reset for $20 Plan Users](https://www.reddit.com/r/ChatGPT/comments/1vks54h/its_here/) ⭐️ 6.0/10

ChatGPT is reportedly testing a feature that lets Plus \($20/month\) users reset their usage limit by paying an additional $8. The option appeared after a Reddit user exhausted their quota, indicating a gray rollout. This pricing change could affect heavy ChatGPT Plus users who frequently hit usage caps, and signals OpenAI exploring additional monetization beyond flat subscriptions. It may also set a precedent for how AI tools charge for overage usage. The reset option was observed on the $20 plan, but the cost for resetting the $200 tier remains unclear. The feature is in gray testing, so it is not visible to all users yet.

telegram · zaihuapd · Aug 12, 08:24

**Background**: Gray testing \(灰度测试\) is a deployment strategy where a new feature is released to a small subset of users before a full rollout, allowing developers to collect feedback and catch issues. In this case, OpenAI appears to be testing a paid add-on that lets users continue after hitting rate limits, rather than waiting for the next billing cycle. This is similar to how many SaaS products charge for overages when users exceed their plan limits.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.volcengine.com/articles/7534568638654005291">微信+DeepSeek...</a></li>
<li><a href="https://watermelonwater.tech/insights/gptimage2%E7%81%B0%E6%B5%8B-nanobanana%E8%BF%8E%E5%BC%BA%E6%95%8C/">GPT-Image-2 灰 度 测 试 全面解析：细节与真实感双重突破，Nano...</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#定价`, `#AI服务`, `#灰度测试`

---

<a id="item-25"></a>
## [Enterprise SSDs Reach 48% of NAND Shipments; YMTC Enters Top Three](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 6.0/10

According to Counterpoint Research, enterprise SSDs accounted for 48% of global NAND flash shipments in Q2 2026, nearly double year over year, while industry revenue grew fivefold. Yangtze Memory Technologies \(YMTC\) overtook Kioxia to claim third place in shipment share at 14%. AI inference workloads are driving an unprecedented shift toward enterprise storage, reshaping the NAND market and making data-center SSDs the dominant demand driver. YMTC&\#x27;s entry into the top three by shipments signals Chinese memory suppliers are gaining global share, although revenue rankings still reflect their consumer-focused product mix. Samsung led with 25% shipment share, followed by SK hynix at 22% and YMTC at 14%. Despite its top-three shipment rank, YMTC only placed fifth in revenue because its products are mostly consumer-grade, and Counterpoint expects enterprise SSDs to consume more than half of NAND bit shipments by end of 2026.

telegram · zaihuapd · Aug 12, 11:00

**Background**: NAND flash memory is a non-volatile storage technology that retains data without power and is the foundation of SSDs. Enterprise SSDs are engineered for data centers with higher endurance, performance, and reliability than consumer SSDs, and AI inference workloads are accelerating demand for these drives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.crucial.com/articles/for-businesses/enterprise-ssds-ultimate-guide">Ultimate guide to enterprise SSDs - crucial.com</a></li>
<li><a href="https://www.ibm.com/think/topics/nand-flash">What is NAND Flash Memory? | IBM</a></li>
<li><a href="https://www.crucial.com/articles/for-businesses/consumer-ssds-vs-enterprise-ssds">Consumer vs. Enterprise SSDs: What’s the Difference</a></li>

</ul>
</details>

**Tags**: `#NAND`, `#SSD`, `#storage`, `#semiconductors`, `#AI`

---