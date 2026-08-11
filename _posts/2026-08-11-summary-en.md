---
layout: default
title: "Horizon Summary: 2026-08-11 (EN)"
date: 2026-08-11
lang: en
---

> From 37 items, 22 important content pieces were selected

---

1. [New Attack Steals Encrypted Reasoning from Leading LLM APIs](#item-1) ⭐️ 9.0/10
2. [Meta Introduces Muse Glimmer: 30B Open-Weight Agentic Model](#item-2) ⭐️ 9.0/10
3. [Compression Is Prediction: An Information-Theoretic View of Machine Learning](#item-3) ⭐️ 8.0/10
4. [NVIDIA Releases Nemotron 3.5 Lightning and NeMo Switchyard Router](#item-4) ⭐️ 8.0/10
5. [Mojo 1.0 Released: Python Usability Meets C-Level Performance](#item-5) ⭐️ 8.0/10
6. [Nvidia&\#x27;s Risky Business: AI Demand and CUDA Moat Under Scrutiny](#item-6) ⭐️ 8.0/10
7. [London Underground Expands Live Facial Recognition Trial to Stations](#item-7) ⭐️ 8.0/10
8. [Decoupled Descent: New Training Method Certifies Test Error Matches Training Error](#item-8) ⭐️ 8.0/10
9. [HyperSAE: Poincaré Geometry Boosts Sparse Autoencoders, Cuts Dead Latents](#item-9) ⭐️ 8.0/10
10. [SK Hynix Resumes Dalian Fab 2, Boosting NAND Output 50%](#item-10) ⭐️ 8.0/10
11. [macOS VM Kernel Fix Yields 11x Faster llama.cpp on Apple Silicon](#item-11) ⭐️ 7.0/10
12. [Apple developing technology to authenticate iPhone camera photos](#item-12) ⭐️ 7.0/10
13. [Anthropic to Watermark Claude AI Outputs from August 2026](#item-13) ⭐️ 7.0/10
14. [iOS 27 Beta 5 Reveals Apple Intelligence Privacy Text for China](#item-14) ⭐️ 7.0/10
15. [Amkor Said to Explore Stake Sale in China Unit Valued at Up to $1.5B](#item-15) ⭐️ 7.0/10
16. [ByteDance Creates New AI Data &amp; Security Department Parallel to Seed, Flow](#item-16) ⭐️ 7.0/10
17. [Cloudflare H1 2026 DDoS report shows sharp rise in 1 Tbps+ attacks](#item-17) ⭐️ 7.0/10
18. [OpenAI&\#x27;s Head of Ethics Departs Less Than a Year After Joining](#item-18) ⭐️ 6.0/10
19. [AAAI 2027 Reviewers Surprised by Lack of Code Submissions](#item-19) ⭐️ 6.0/10
20. [Anthropic Makes Claude Sonnet 5 Promo Pricing Permanent](#item-20) ⭐️ 6.0/10
21. [ZCode Reaches 1 Million Users, Resets GLM Coding Plan Limits](#item-21) ⭐️ 6.0/10
22. [Graphene-Powered Soft Lens Could Revolutionize Cameras and Medical Devices](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [New Attack Steals Encrypted Reasoning from Leading LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

A new security paper demonstrates that encrypted chain-of-thought reasoning blocks from Anthropic, OpenAI, and Google can be replayed into weaker sibling models and jailbroken to recover the hidden reasoning in plaintext. The attack has since been patched by all providers. This reveals that encryption alone cannot reliably protect proprietary reasoning traces in LLM APIs, threatening model privacy and intellectual property. It matters for developers and enterprises relying on API-based reasoning, and sparks debate about whether hidden chain-of-thought should be exposed. The attack worked because models within the same family shared the same encryption key, allowing traces to be transferred across models. Claude Haiku 4.5 was the easiest target, and the paper&\#x27;s appendix includes raw reasoning traces that reveal examples like GPT-5.5 planning CSS code.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought \(CoT\) prompting is a technique that improves LLM performance on complex tasks by having the model generate step-by-step intermediate reasoning before a final answer. To protect proprietary methods, major providers encrypt these reasoning blocks, but replay attacks reuse captured responses in different contexts, and jailbreaking techniques bypass safety guardrails to force models to reveal hidden outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.03373">Demystifying Long Chain-of-Thought Reasoning in LLMs Understanding Chain-of-Thought in LLMs through Information Theory Chain of Preference Optimization: Improving Chain-of-Thought ... Chain-of-Thought Prompting: Step-by-Step Reasoning with LLMs Demystifying Long Chain-of-Thought Reasoning - OpenReview ICML Poster Understanding Chain-of-Thought in LLMs through ... What is chain of thought (CoT) prompting? - IBM</a></li>
<li><a href="https://www.lakera.ai/blog/jailbreaking-large-language-models-guide">Jailbreaking Large Language Models: Techniques, Examples ...</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some argue that using model outputs for training should be normal and criticize the &\#x27;stealing&\#x27; framing, while others share independent exploits such as using developer prompts to decrypt compaction. Several posters joke that future models will refuse to reveal their reasoning without enterprise API access, and some wonder whether the vulnerability was intentionally allowed.

**Tags**: `#LLM`, `#security`, `#privacy`, `#chain-of-thought`, `#AI`

---

<a id="item-2"></a>
## [Meta Introduces Muse Glimmer: 30B Open-Weight Agentic Model](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 9.0/10

Meta has unveiled Muse Glimmer, a new 30B parameter open-weights model released under a clean Apache 2.0 license, specifically optimized for agentic tasks, reliable tool use, and multi-step reasoning. The model is already available for local use via LM Studio, with an 18.16 GB quantized version, and supports vision inputs. This release is significant because it offers a permissive Apache 2.0 license, unlike Meta&\#x27;s earlier Llama licenses, making it attractive for commercial and research use. It targets the growing demand for locally runnable agentic models that can handle complex, multi-turn workflows and tool use, potentially accelerating the development of AI agents. The 30B model runs well on machines with 32 GB or more RAM, and its quantized version is about 18.16 GB. Meta claims strong results on benchmarks including DeepSearch QA, MCP-Atlas, τ-Bench, and SWE-Bench, and the model also handles vision tasks such as image description.

rss · Simon Willison · Aug 10, 23:56

**Background**: Agentic AI models are designed to autonomously complete multi-step tasks by calling tools, writing code, and iterating on user requests. Benchmarks such as MCP-Atlas evaluate tool-use competency across real MCP servers and tools, while τ-Bench simulates dynamic user-agent conversations with domain-specific APIs, and DeepSearch QA assesses deep research capabilities. Open-weights models under permissive licenses like Apache 2.0 allow developers to deploy and modify them freely, which is a shift from more restrictive licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/mcp-atlas">MCP Atlas Leaderboard</a></li>
<li><a href="https://github.com/sierra-research/tau-bench">GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2406.12045">[2406.12045] $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Meta`, `#Model Release`, `#Agentic`

---

<a id="item-3"></a>
## [Compression Is Prediction: An Information-Theoretic View of Machine Learning](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

The ngrok blog post &\#x27;Compression is prediction&\#x27; examines the conceptual equivalence between data compression and prediction in machine learning. It argues that understanding one in terms of the other reveals deep connections to information theory, algorithmic complexity, and generalization. This discussion matters because framing machine learning as compression connects model quality to Occam&\#x27;s razor and minimum description length principles, offering a principled way to think about generalization and overfitting. It resonates broadly across AI/ML, from LLM training to model selection. The post builds on key literature including David MacKay&\#x27;s &\#x27;Information Theory, Inference, and Learning Algorithms,&\#x27; Jürgen Schmidhuber&\#x27;s work on compression progress, and Grant Sanderson&\#x27;s &\#x27;Compression is Intelligence&\#x27; video series. A critical nuance raised in the comments is that compression equals prediction only when the training distribution exactly represents all future problems; under distribution shift, lossy compression can discard rare but important edge cases.

hackernews · nikolay · Aug 11, 19:49 · [Discussion](https://news.ycombinator.com/item?id=49263497)

**Background**: The ideas draw on algorithmic information theory, where the Kolmogorov complexity of a data set is the length of the shortest program that produces it, and Solomonoff induction, which formalizes Occam&\#x27;s razor by preferring theories with shorter algorithmic descriptions. These concepts support the minimum description length principle, which judges the best model as the one that compresses the data most effectively. Together they provide a theoretical basis for viewing prediction and learning as forms of compression.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solomonoff_induction">Solomonoff induction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov_complexity">Kolmogorov complexity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Minimum_description_length">Minimum description length</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the post, with several noting that the idea has deep roots—in MacKay&\#x27;s Cambridge course, Schmidhuber&\#x27;s earlier work, Ted Chiang&\#x27;s &\#x27;ChatGPT is a blurry JPEG&\#x27; essay, and Grant Sanderson&\#x27;s video series. The most substantive counterpoint came from a commenter who argued that compression is only equivalent to prediction when the data distribution perfectly represents all future cases, and that lossy compression may ignore rare edge cases relevant to generalization.

**Tags**: `#compression`, `#prediction`, `#information theory`, `#machine learning`, `#generalization`

---

<a id="item-4"></a>
## [NVIDIA Releases Nemotron 3.5 Lightning and NeMo Switchyard Router](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 8.0/10

NVIDIA has introduced Nemotron 3.5 Lightning, a 30B-parameter open Mixture-of-Experts \(MoE\) model with only 3B active parameters, specifically built for fast, low-latency execution in agentic workflows. Alongside it, NVIDIA released NeMo Switchyard, an open-source library that intelligently routes each request to the most suitable model for the job. This release underscores a broader industry shift toward small, efficient language models that can power always-on AI agents at lower cost. By combining a lightweight MoE model with a model-routing layer, NVIDIA is helping developers build multi-model systems that balance accuracy, latency, and infrastructure expenses. Nemotron 3.5 Lightning has 30B total parameters but only 3B active, and is optimized for high-volume, low-latency agent execution; the model is available in BF16 and NVFP4 formats on Hugging Face. NeMo Switchyard supports multiple routing policies and can carry routing state across an agent&\#x27;s session, addressing use cases that require consistent model selection.

hackernews · droidjj · Aug 11, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49263340)

**Background**: Mixture-of-Experts models activate only a subset of their parameters per token, which keeps inference fast and memory efficient while retaining the capacity of a large model. NeMo Switchyard addresses the challenge of deploying multiple models in production by acting as a smart routing layer, similar in spirit to gateway systems for LLM applications. The news builds on NVIDIA&\#x27;s broader NeMo framework for building, customizing, and deploying generative AI models, though Nemotron models are also usable outside that stack via standard platforms like MLX.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>
<li><a href="https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/">Route AI Agents Across Models with NVIDIA NeMo Switchyard</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Switchyard">GitHub - NVIDIA- NeMo / Switchyard · GitHub</a></li>

</ul>
</details>

**Discussion**: User reactions are mostly positive, with praise for the push toward smaller, more efficient models and one report that Nemotron 3.5 Lightning runs on Apple Silicon via MLX, albeit slowly. There are also constructive concerns: one user asked how NeMo Switchyard handles prompt caching with routing, while another criticized NVIDIA&\#x27;s benchmark charts for omitting the Qwen model family. A few off-topic comments about minimalist writing also appeared.

**Tags**: `#NVIDIA`, `#Nemotron`, `#small language models`, `#model routing`, `#open source`

---

<a id="item-5"></a>
## [Mojo 1.0 Released: Python Usability Meets C-Level Performance](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 8.0/10

Modular officially released Mojo 1.0 in late May 2026, marking the first stable version of the language. The release is positioned as a key milestone for a language that aims to combine Python&\#x27;s ease of use with C-level performance for AI/ML systems. Mojo 1.0 is a significant milestone for a language that could challenge established systems programming languages in the AI infrastructure space. It may give developers a more productive path to high-performance computing while retaining Python-like readability, potentially impacting AI/ML tooling and adoption. Mojo builds on the MLIR compiler framework rather than directly on LLVM, allowing it to target CPUs, GPUs, TPUs, and other accelerators. The compiler remains proprietary for now, but Modular reiterates its commitment to open-sourcing it in 2026, and the language also has a new dedicated website, mojolang.org.

hackernews · dayanruben · Aug 11, 16:56 · [Discussion](https://news.ycombinator.com/item?id=49261128)

**Background**: Mojo is a systems programming language created by Modular Inc., the company founded by Chris Lattner, the original architect of Swift. It uses Python-like syntax but adds static typing and a borrow checker inspired by Rust. Initially intended to become a superset of Python, that goal has been paused; the language now focuses on high-performance CPU, GPU, and accelerator programming. Mojo&\#x27;s design leverages MLIR to enable advanced compiler optimizations and broad hardware support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**Discussion**: The Hacker News community had mixed reactions. Some users questioned the value of a language with a closed-source compiler, while others were confused about Mojo&\#x27;s exact purpose and its relationship to Python. There was also skepticism about the &quot;superset of Python&quot; goal being walked back, and calls for the compiler to be open-sourced sooner. Despite the criticism, several commenters said they remain hopeful for Mojo&\#x27;s future.

**Tags**: `#Mojo`, `#Programming Languages`, `#AI/ML`, `#Compilers`, `#Performance`

---

<a id="item-6"></a>
## [Nvidia&\#x27;s Risky Business: AI Demand and CUDA Moat Under Scrutiny](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 8.0/10

The article analyzes Nvidia&\#x27;s strategic risks, questioning the sustainability of AI compute demand growth and the fragility of its CUDA software ecosystem advantage. It argues that while first-order demand for more compute is real, second-order assumptions about demand growth may be exaggerated. This matters because Nvidia&\#x27;s valuation and the broader AI infrastructure boom depend on sustained demand growth and the durability of its software moat. If these assumptions falter, it could impact investors, AI startups, and competitors like AMD and Google&\#x27;s TPU. The analysis distinguishes first-order assumptions \(demand for more compute exists\) from second-order assumptions \(the growth rate of that demand\), which are more likely to be exaggerated. Commentators note that while CUDA is entrenched in ML research, the development experience is poor, and Nvidia is expanding into robotics while facing geopolitical dynamics with China.

hackernews · jonbaer · Aug 11, 10:02 · [Discussion](https://news.ycombinator.com/item?id=49255710)

**Background**: CUDA is Nvidia&\#x27;s proprietary parallel computing platform and API that allows software to use GPUs for general-purpose processing, including AI and scientific computing. It includes compilers, libraries, and developer tools, and supports languages like C, C++, Python, and Julia. Nvidia&\#x27;s software ecosystem is often cited as its key moat because CUDA is deeply integrated into AI research and production workflows, making it difficult for competitors like AMD to displace. However, the analysis questions whether this ecosystem advantage is as fragile as it is strong, especially as demand growth assumptions come under scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_CUDA">Nvidia CUDA</a></li>
<li><a href="https://www.rownix.dev/en/articles/nvidia-cuda-ai-infrastructure-moat">Is Nvidia&#x27;s Moat The Chip, Or The CUDA Ecosystem ? | Rownix&#x27;s Blog</a></li>
<li><a href="https://www.chipstrat.com/p/can-amd-bridge-nvidias-software-moat">Can AMD Bridge Nvidia’s Software Moat? - by Austin Lyons</a></li>

</ul>
</details>

**Discussion**: The comments reflect a nuanced debate. Some agree that CUDA&\#x27;s entrenchment in ML research is real, but the actual development experience with CUDA C/C++ is poor. Others argue that first-order demand for compute is real, but second-order growth expectations are likely exaggerated. There is also discussion of Nvidia&\#x27;s moves into robotics and the geopolitical dimension with China.

**Tags**: `#Nvidia`, `#AI infrastructure`, `#business strategy`, `#CUDA`, `#semiconductors`

---

<a id="item-7"></a>
## [London Underground Expands Live Facial Recognition Trial to Stations](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 8.0/10

British Transport Police \(BTP\) has expanded its live facial recognition \(LFR\) trial into London Underground stations, scanning passengers&\#x27; faces in real time. The move brings mass surveillance technology into one of the world&\#x27;s busiest transit networks, raising serious privacy and civil liberty concerns. The outcome could set a precedent for facial recognition deployment in public spaces across the UK and beyond. The trial expands BTP&\#x27;s existing LFR efforts into London Underground stations, where cameras match faces against a watchlist of wanted individuals. Critics argue the technology has low accuracy and lacks a clear failure threshold for ending the trial.

hackernews · BlueBerry2001 · Aug 11, 09:40 · [Discussion](https://news.ycombinator.com/item?id=49255496)

**Background**: Live facial recognition works by using CCTV cameras to capture faces and instantly compare them against a database of images. BTP says the aim is to identify wanted criminals, but civil liberties groups warn that it enables pervasive tracking of ordinary members of the public. The London Underground has also become less anonymous over time as contactless bank cards became the primary way to enter stations.

**Discussion**: Commenters are predominantly critical, calling the trial an invasion of privacy and an &\#x27;Orwellian&\#x27; development. Some question the purpose of the trial, noting there is no realistic failure condition, while others argue anonymity on the Underground had already eroded with contactless payment. One commenter sarcastically suggests it will solve street crime, while another compares it unfavorably to China&\#x27;s surveillance state.

**Tags**: `#facial recognition`, `#surveillance`, `#privacy`, `#biometrics`, `#civil liberties`

---

<a id="item-8"></a>
## [Decoupled Descent: New Training Method Certifies Test Error Matches Training Error](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

The author introduces Decoupled Descent \(DD\), a novel training algorithm built on approximate message passing \(AMP\) theory with Onsager corrections, which certifies that the training error asymptotically equals the test error at each parameter iterate. The method is demonstrated on stylized Gaussian mixture models and a high-dimensional XOR model, in contrast to standard gradient descent. This directly tackles the fundamental generalization gap wherein training error drops while test error may stagnate or rise, a common pain point in deep learning. By certifying train-test alignment, DD enables validation without sacrificing training data and opens new possibilities for optimal stopping and hyperparameter tuning. DD leverages a low-dimensional state evolution recursion from AMP theory, making the algorithm&\#x27;s dynamics transparent and tractable. The paper is theoretical and focused on stylized high-dimensional problems; scaling to very large models remains future work, and the author plans to release a PyTorch-compatible package.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate message passing \(AMP\) is a class of iterative algorithms for high-dimensional statistical estimation problems such as compressed sensing and linear regression, known for rigorous performance guarantees in the large-system limit via state evolution. A key component of AMP is the Onsager correction, a memory term that decorrelates iterates from past errors and ensures desirable statistical properties at each step. Decoupled Descent applies these AMP principles to neural network training, explicitly tracking state evolution to prevent any mismatch between training and test error.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate ...</a></li>
<li><a href="https://arxiv.org/abs/2201.07487">[2201.07487] A Concise Tutorial on Approximate Message Passing</a></li>
<li><a href="https://www.machinebrief.com/news/decoupled-descent-bridging-the-training-test-gap-la4u">Decoupled Descent: Bridging the Training-Test Gap</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#training methods`, `#approximate message passing`, `#generalization`, `#theory`

---

<a id="item-9"></a>
## [HyperSAE: Poincaré Geometry Boosts Sparse Autoencoders, Cuts Dead Latents](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/) ⭐️ 8.0/10

HyperSAE, a PyTorch library, introduces a decoupled dual-speed design that projects dictionary weights into the Poincaré ball during training while keeping the forward pass Euclidean. On Gemma-2-2B, it reduces reconstruction MSE by 9.8% and dead latents from 3.8% to 0.2% with zero inference overhead. This matters for mechanistic interpretability, where large sparse autoencoders on LLMs suffer from feature collisions and dead latents. By applying hyperbolic geometry, HyperSAE offers a new way to improve reconstruction quality and feature utilization without slowing down inference. The library uses a TriPartite loss combining reconstruction, L1 sparsity, and an entailment cone loss that places parent concepts near the origin and child concepts near the boundary. It also includes co-activation queue tracking and a single-class trainer interface, with the paper and benchmark code openly available.

reddit · r/MachineLearning · /u/visha1v · Aug 11, 18:37 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/)

**Background**: Sparse autoencoders \(SAEs\) are a leading technique in mechanistic interpretability, decomposing neural representations into sparse, human-interpretable features. Standard SAEs embed dictionary atoms in Euclidean space, where volume grows polynomially and large dictionaries lead to feature collisions and dead latents. Hyperbolic geometry, particularly the Poincaré ball model, is effective at embedding hierarchical structures with low distortion, which matches the branching concepts learned by LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2205.13984">Information measures and geometry of the hyperbolic exponential families of Poincaré and hyperboloid distributions</a></li>
<li><a href="https://www.lesswrong.com/posts/CJPqwXoFtgkKPRay8/an-intuitive-explanation-of-sparse-autoencoders-for">An Intuitive Explanation of Sparse Autoencoders for Mechanistic ...</a></li>
<li><a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05671.pdf">HYPE: Hyperbolic Entailment Filtering for</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#interpretability`, `#sparse autoencoders`, `#hyperbolic geometry`, `#PyTorch`

---

<a id="item-10"></a>
## [SK Hynix Resumes Dalian Fab 2, Boosting NAND Output 50%](https://en.sedaily.com/finance/2026/08/11/sk-hynix-to-boost-china-nand-output-50-percent-with-dalian) ⭐️ 8.0/10

SK Hynix has restarted construction of its second NAND flash factory in Dalian, China, which will increase local production capacity by approximately 50%. Equipment installation is scheduled to begin by the end of this year, with mass production expected in the first half of next year at a monthly capacity of about 50,000 wafer starts. This expansion strengthens SK Hynix&\#x27;s position in the NAND market amid surging AI-driven demand for enterprise SSDs. Increased supply from the Dalian plant could ease current NAND shortages and influence global memory pricing trends. The second Dalian fab was originally started four years ago but stalled during a memory industry downturn. SK Hynix is pursuing a dual-track strategy: the Dalian plant will use mature technology for 100-layer NAND, while the Cheongju facility focuses on 300+ layer high-stack products, and NAND prices have surged nearly tenfold in the past year.

telegram · zaihuapd · Aug 11, 16:21

**Background**: NAND flash is a non-volatile storage technology used in SSDs, and 3D NAND stacks memory cells vertically in layers to increase density, with current products reaching over 200 layers. Enterprise SSDs are high-performance drives designed for data centers and servers, and AI workloads have sharply increased demand for storage capacity and bandwidth. SK Hynix is one of the world&\#x27;s leading memory manufacturers with production facilities in South Korea and China. The company&\#x27;s Dalian expansion reflects a broader industry response to the AI-driven memory boom.

<details><summary>References</summary>
<ul>
<li><a href="https://www.atpinc.com/blog/3d-nand-ssd-sd-flash-memory-storage-what-is">3 D NAND SSD : Breaking Scaling Limitations of 2D planar NAND</a></li>
<li><a href="https://www.everpuredata.com/knowledge/what-is-3d-nand.html">What Is 3 D NAND and How Does It Work? | Everpure</a></li>
<li><a href="https://www.newegg.com/Enterprise-SSDs/SubCategory/ID-2021">Enterprise SSDs, Enterprise Solid State Drives - Newegg.com</a></li>

</ul>
</details>

**Tags**: `#NAND`, `#SK Hynix`, `#semiconductors`, `#memory`, `#AI infrastructure`

---

<a id="item-11"></a>
## [macOS VM Kernel Fix Yields 11x Faster llama.cpp on Apple Silicon](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 7.0/10

A blog post from trycua demonstrates that fixing kernel selection inside macOS VMs on Apple Silicon can yield up to 11.08x faster LLM inference and 16.36x faster token generation with llama.cpp, compared to the same workload in a stock VM. This is significant because it shows that VM configuration can dramatically impact Metal/GPU performance for LLM inference, offering a substantial optimization for developers running llama.cpp inside macOS virtualized environments. It also clarifies that this is a targeted fix for Virtualization.framework VMs, not a general llama.cpp speedup for all Apple Silicon users. The speedup comes from ensuring the VM selects the correct GPU kernels rather than from any change to llama.cpp itself; the fix works around a problem where Virtualization.framework caused llama.cpp to pick suboptimal kernels. The comparison is specifically against a stock VM running the same workload, so the gains apply only to this VM context, not to bare-metal or other virtualization approaches.

hackernews · frabonacci · Aug 11, 14:50 · [Discussion](https://news.ycombinator.com/item?id=49259339)

**Background**: Apple&\#x27;s Virtualization.framework lets developers run macOS and Linux VMs on Apple Silicon, presenting the guest with a paravirtualized virtual graphics device that submits Metal work to the physical GPU via the host stack. llama.cpp is an open-source C/C++ implementation for LLM inference that can offload computation to Apple GPUs through Metal. In VMs, the virtual graphics device may expose a reduced Metal feature set, leading llama.cpp to select algorithms and kernels that are not optimally tuned for the host GPU; fixing the kernel selection restores near-native performance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md">cua/blog/gpu-passthrough-macos-vms.md at main · trycua/cua</a></li>
<li><a href="https://developer.apple.com/documentation/virtualization">Virtualization | Apple Developer Documentation</a></li>
<li><a href="https://arstechnica.com/gadgets/2022/07/how-to-use-free-virtualization-apps-to-safely-test-the-macos-ventura-betas/">Apple’s Virtualization framework is a great, free way to test new macOS betas - Ars Technica</a></li>

</ul>
</details>

**Discussion**: Commenters pointed out that the headline could be misleading, since the speedup applies only to Virtualization.framework VMs and not to all llama.cpp users. Some also questioned why Apple&\#x27;s Virtualization.framework exposes a lesser Metal profile instead of reporting full host GPU capabilities, while others speculated about whether Neural Accelerators in future M-series chips will appear in base models.

**Tags**: `#llama.cpp`, `#Apple Silicon`, `#macOS VMs`, `#GPU passthrough`, `#LLM inference`

---

<a id="item-12"></a>
## [Apple developing technology to authenticate iPhone camera photos](https://9to5mac.com/2026/08/10/apple-is-working-on-a-way-to-authenticate-that-a-photo-came-from-an-iphone-camera/) ⭐️ 7.0/10

Apple is developing a device-level authentication system, spotted as &quot;Apple Reference Image&quot; in code from iOS 27 beta 5, to verify that photos were captured by an iPhone camera. The system would use unique data tied to the camera hardware, along with system signatures and encrypted authentication, to establish photo provenance. As generative AI makes realistic fake images increasingly easy to create, a hardware-backed authentication mechanism could help restore trust in photo authenticity and set an industry precedent. This would affect everyday users, journalists, and content platforms that rely on visual verification. The technology currently exists only in early-stage code within a beta OS, with no official announcement, release date, or implementation details from Apple. It reportedly relies on unique data tied to the iPhone camera hardware that captured each photo, combined with system-level signing and cryptographic authentication.

telegram · zaihuapd · Aug 11, 01:53

**Background**: Image authentication and provenance aim to establish where a photo came from and whether it was altered. Open technical standards like C2PA already exist to track media origin and provenance, and Apple&\#x27;s approach would extend this idea to the hardware level by tying verification directly to the camera sensor and device firmware. This matters because generative AI now enables convincing synthetic images that can spread misinformation, making hardware-backed verification a potential safeguard.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/10/apple-is-working-on-a-way-to-authenticate-that-a-photo-came-from-an-iphone-camera/">Apple is working on a way to authenticate that a photo came from an iPhone camera - 9to5Mac</a></li>
<li><a href="https://www.androidinfotech.com/apple-photo-is-real-or-ai-generated/">How to Tell if an Apple Photo Is Real or AI-Generated? - Android Infotech (August 2026)</a></li>
<li><a href="https://authenticity.sony.net/camera/en-us/index.html">Camera Authenticity Solution | Sony</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Photo Authentication`, `#AI-generated Content`, `#Cybersecurity`, `#Camera Technology`

---

<a id="item-13"></a>
## [Anthropic to Watermark Claude AI Outputs from August 2026](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) ⭐️ 7.0/10

Anthropic has committed to the EU AI Act Article 50\(2\) transparency code of practice and will embed machine-readable watermarks in text generated by new Claude models launched in the EU on or after August 2, 2026, along with C2PA provenance metadata in supported files. These markings apply across all Claude products, including Claude, Claude Code, Claude Cowork, and Claude Tag, on a global scale. This is a significant step for AI content provenance and regulatory compliance, demonstrating how a major AI lab is operationalizing transparency obligations under the EU AI Act. It will affect businesses, educators, and publishers who use Claude, and could set a precedent for other AI model providers navigating similar requirements. The text watermarks are invisible and designed to survive copy-pasting and some editing, while supported files use the C2PA provenance standard with digitally signed metadata. Anthropic is also retrofitting older models released before August 2, 2026, and plans to publish detection technical details; detecting a mark only indicates content may have been processed by Claude, and its absence does not prove content was not AI-generated.

telegram · zaihuapd · Aug 11, 03:06

**Background**: The EU AI Act is a landmark regulation, and Article 50 sets transparency obligations for providers and deployers of certain AI systems, including marking AI-generated content. C2PA \(Coalition for Content Provenance and Authenticity\) is an open technical standard backed by Adobe, Microsoft, Google, and others; it adds cryptographically signed metadata to media files to verify content origin and editing history. As AI-generated text becomes harder to distinguish from human writing, watermarking and provenance metadata are emerging as key tools for maintaining trust online.

<details><summary>References</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content">How Claude marks AI-generated content | Claude Help Center</a></li>
<li><a href="https://artificialintelligenceact.eu/article/50/">Article 50: Transparency Obligations for Providers and ...</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI transparency`, `#Watermarking`, `#EU AI Act`

---

<a id="item-14"></a>
## [iOS 27 Beta 5 Reveals Apple Intelligence Privacy Text for China](https://ai.privacy/) ⭐️ 7.0/10

iOS 27 beta 5 includes pre-loaded Chinese-language privacy text for Apple Intelligence, confirming Apple will use a local company&\#x27;s safety mechanism in mainland China and process user requests entirely on-device. The code strings also add controls to turn Apple Intelligence on or off. This reveals Apple&\#x27;s concrete approach to complying with Chinese AI regulations while preserving its privacy positioning, a key test for global AI deployments. It also signals Apple Intelligence&\#x27;s China launch is in the final adaptation stage, affecting millions of iPhone users in China. The privacy footer states that Apple will collect anonymized safety results and share them in aggregate, as required by law, and that the safety mechanism will download and update automatically. The text links to an &\#x27;About Apple Intelligence &amp; Privacy&\#x27; page, while new alert strings confirm users can disable Apple Intelligence.

telegram · zaihuapd · Aug 11, 04:49

**Background**: Apple Intelligence is Apple&\#x27;s suite of AI features, and China requires AI services to pass a security assessment before release. Because China mandates that sensitive data be handled within the country, Apple is partnering with local firms such as Alibaba \(for generative AI\) and Baidu \(for search and Siri\) to provide a safety mechanism that operates on-device.

<details><summary>References</summary>
<ul>
<li><a href="https://sftpmac.com/en/blog/20260716-apple-intelligence-china-approved-qwen-baidu-decision-guide.html">2026 Apple Intelligence Approved in China : Qwen... | SFTPMAC</a></li>

</ul>
</details>

**Tags**: `#Apple Intelligence`, `#iOS`, `#Privacy`, `#China`, `#AI regulation`

---

<a id="item-15"></a>
## [Amkor Said to Explore Stake Sale in China Unit Valued at Up to $1.5B](https://www.bloomberg.com/news/articles/2026-08-11/amkor-is-said-to-explore-stake-sale-in-1-5-billion-china-unit) ⭐️ 7.0/10

Amkor Technology is reportedly exploring the sale of a stake in its China business, with a valuation between $1 billion and $1.5 billion. The company has hired advisers to help divest the unit and may retain a minority stake. This move reflects a broader trend of multinationals reassessing their China operations amid US-China tech tensions, and could affect the global semiconductor supply chain and AI packaging landscape. Amkor recently signed a $1.5 billion multi-year deal with Nvidia to co-develop next-generation AI semiconductor packaging technology. Amkor established its packaging plant in Shanghai in 2001, and is said to be considering options including a minority stake sale. The report is based on people familiar with the matter, and Amkor declined to comment.

telegram · zaihuapd · Aug 11, 07:21

**Background**: Semiconductor packaging and testing is the back-end process in chip manufacturing, involving dicing, mounting, bonding, molding, and final electrical testing. As Moore&\#x27;s law slows down, advanced packaging technologies such as 2.5D/3D integration, chiplet designs, and hybrid bonding are becoming increasingly critical for AI chip performance. Amkor is the world&\#x27;s second-largest outsourced semiconductor assembly and test \(OSAT\) provider.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E5%8D%8A%E5%AF%BC%E4%BD%93%E5%B0%81%E8%A3%85%E6%B5%8B%E8%AF%95/6417278">半导体封装测试 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2033639507938035195">AI半导体封装技术实战指南：从TSV到混合键合的全景解析</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#Amkor`, `#supply chain`, `#US-China`, `#AI packaging`

---

<a id="item-16"></a>
## [ByteDance Creates New AI Data &amp; Security Department Parallel to Seed, Flow](https://36kr.com/newsflashes/3934989813710209) ⭐️ 7.0/10

ByteDance has established a new first-level AI Data and Security department, led by Adam Wang \(Wang Yinglei\), making it parallel to its existing Seed, Flow, and Douyin units. This marks ByteDance&\#x27;s third AI-focused first-level department, following the creation of Seed and Flow in late 2023. The move signals ByteDance&\#x27;s strategic focus on AI governance, data infrastructure, and security as it scales its AI products like Doubao. It could reshape how the company manages AI-related data compliance and safety, affecting its competitive position in China&\#x27;s AI race. The new department&\#x27;s head, Adam Wang, previously served as TikTok&\#x27;s Head of Platform Responsibility and Head of Live. The department operates as a first-level unit, indicating direct reporting to top management and equal footing with core business lines.

telegram · zaihuapd · Aug 11, 11:25

**Background**: ByteDance established its Seed AI research division and Flow AI applications division in late 2023 as part of its AGI strategy. Seed focuses on foundation models behind Doubao and other AI products, while Flow focuses on AI applications. The new AI Data and Security department adds a dedicated governance layer for data and safety across these AI efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yicaiglobal.com/news/chinas-bytedance-sets-up-new-division-focusing-on-ai-applications">China’s ByteDance Sets Up New Division Focusing on AI Applications</a></li>
<li><a href="https://eu.36kr.com/en/p/3934936980667776">36Kr Exclusive: ByteDance Launches New First-Tier AI Division...</a></li>
<li><a href="https://seed.bytedance.com/en/">ByteDance Seed</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#AI`, `#Data Security`, `#Org Structure`, `#Tech Industry`

---

<a id="item-17"></a>
## [Cloudflare H1 2026 DDoS report shows sharp rise in 1 Tbps+ attacks](https://blog.cloudflare.com/ddos-threat-report-2026-h1/) ⭐️ 7.0/10

Cloudflare&\#x27;s H1 2026 DDoS threat report reveals 935 network-layer attacks over 1 Tbps, with Q2 up 519% quarter-over-quarter. DNS floods surged 580% QoQ, becoming the third-largest attack type. The report highlights an escalating arms race in DDoS attack scale, with record-breaking volumetric attacks now routine for enterprises and infrastructure providers. Security teams must prepare for multi-terabit attacks and the growing prevalence of DNS-based threats. DNS-based attacks accounted for 34.3% of all network-layer attacks in H1. Media, publishing, and production were the most-targeted industries; government rose from 29th to 9th most-attacked quarter-over-quarter.

telegram · zaihuapd · Aug 11, 13:20

**Background**: A DDoS \(distributed denial-of-service\) attack floods a target with traffic to disrupt service. Network-layer attacks \(Layer 3\) saturate bandwidth using protocols like ICMP, while DNS floods overwhelm DNS servers with query volumes so legitimate lookups cannot be resolved. Cloudflare&\#x27;s global network mitigates these attacks and publishes quarterly threat reports.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/">DNS flood DDoS attack | Learning Center</a></li>
<li><a href="https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/">How Do Layer 3 DDoS Attacks Work? | L3 DDoS - Cloudflare</a></li>
<li><a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">What is a DDoS attack? | Learning Center - Cloudflare</a></li>

</ul>
</details>

**Tags**: `#DDoS`, `#Cloudflare`, `#Security`, `#Network Attacks`, `#Threat Report`

---

<a id="item-18"></a>
## [OpenAI&\#x27;s Head of Ethics Departs Less Than a Year After Joining](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) ⭐️ 6.0/10

Chloé Bakalar, OpenAI&\#x27;s head of ethics, has left the company less than a year after joining. Her departure was first reported by the Financial Times and has renewed debate about the role of AI ethics teams within leading AI labs. The exit raises questions about the stability and influence of AI governance and ethics functions inside OpenAI, a central player in the AI boom. It also fuels broader industry skepticism about whether ethics teams are genuinely integrated into model development or serve mainly as public-facing reassurance. Bakalar joined OpenAI less than a year ago after serving as chief ethicist at Meta for about six years. The FT article offers few details about the reasons behind her departure, leaving observers to speculate.

hackernews · ilamont · Aug 11, 12:23 · [Discussion](https://news.ycombinator.com/item?id=49257160)

**Background**: AI ethics teams at companies like OpenAI and Anthropic are tasked with studying the societal and moral implications of large language models and other AI systems. A recurring criticism, echoed in community discussions, is that such teams often lack real decision-making power and can function as public-relations efforts rather than operational safeguards. Chloé Bakalar&\#x27;s own quoted view—that AI ethics questions are centuries-old human questions—highlights the tension between treating AI as uniquely dangerous and seeing it as a continuation of older ethical debates.

**Discussion**: Commenters are generally skeptical about the effectiveness of corporate AI ethics departments. Some argue that ethics teams are brought in as PR stunts with no real influence, while others sense more complex, undisclosed factors behind Bakalar&\#x27;s exit and note that the article is thin on details. A few also connect her departure to OpenAI and Anthropic&\#x27;s philosophical stance that large language models pose uniquely large-scale risks.

**Tags**: `#AI ethics`, `#OpenAI`, `#AI governance`, `#AI safety`, `#personnel`

---

<a id="item-19"></a>
## [AAAI 2027 Reviewers Surprised by Lack of Code Submissions](https://www.reddit.com/r/MachineLearning/comments/1vlqjby/aaai_2027_review_no_code_submission_d/) ⭐️ 6.0/10

A reviewer for AAAI 2027 reports that surprisingly few submitted papers include code implementations, despite the conference&\#x27;s explicit reproducibility requirements. The reviewer plans to factor code submission into initial scores. This anecdotal observation highlights a potential gap between stated reproducibility policies and actual submission practices at a top AI conference. If widespread, it could affect the credibility of published research and influence how reviewers and authors approach code disclosure. The reviewer notes that detailed appendices and code are expected under AAAI&\#x27;s reproducibility guidelines, yet many submissions lack code. They also mention that AI assistants could generate empirical papers with fabricated results in hours, making code submission an important signal of authenticity.

reddit · r/MachineLearning · /u/wontonut · Aug 11, 18:58

**Background**: AAAI \(Association for the Advancement of Artificial Intelligence\) is a major conference for AI research that has adopted reproducibility as a key evaluation criterion. Reproducibility in machine learning often requires authors to release code, data, and detailed experimental setups so others can verify results. In recent years, many venues have strengthened these requirements, and reviewers increasingly use code availability when assessing paper quality.

**Tags**: `#AAAI`, `#reproducibility`, `#peer review`, `#machine learning`

---

<a id="item-20"></a>
## [Anthropic Makes Claude Sonnet 5 Promo Pricing Permanent](https://x.com/claudeai/status/2086891169217122586) ⭐️ 6.0/10

On August 10, Anthropic announced that the promotional pricing for Claude Sonnet 5 will remain permanent, cancelling the price increase planned for September 1. The API will continue to charge $2 per million input tokens and $10 per million output tokens instead of reverting to the standard $3/$15 rates. This gives developers and enterprises using Claude Sonnet 5 predictable, lower API costs, making Anthropic more competitive against other LLM providers. It also signals that the company is willing to hold lower prices to encourage adoption despite earlier plans to raise them. Claude Sonnet 5 launched in June with the promotional pricing, which was originally valid only until August 31. The permanent pricing means the model&\#x27;s input/output rates remain at $2/$10 per million tokens indefinitely.

telegram · zaihuapd · Aug 11, 03:39

**Background**: In AI language model APIs, pricing is typically based on tokens, which are small chunks of text that models read and generate. Input tokens \(the prompt\) and output tokens \(the generated response\) are billed separately, with output tokens usually costing two to four times more. Claude Sonnet 5 is one of Anthropic&\#x27;s mid-tier models, and this announcement concerns its API access pricing.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://www.gmicloud.ai/en/blog/how-do-different-cloud-providers-compare-in-terms-of-pricing-for-ai-model-inference">How Do Different Cloud Providers Compare in Terms of Pricing for AI...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#Pricing`, `#AI`, `#LLM`

---

<a id="item-21"></a>
## [ZCode Reaches 1 Million Users, Resets GLM Coding Plan Limits](http://z.ai/) ⭐️ 6.0/10

Z.ai announced that ZCode has surpassed 1 million users and reset usage limits for all GLM Coding Plan subscribers. The update also improved cache hit rates to 98%, providing roughly 1.8x more effective usage. This milestone signals growing adoption of ZCode as an AI coding tool and strengthens Z.ai&\#x27;s position in the competitive AI developer tools market. The higher cache hit rate means faster and more efficient coding workflows for developers, making the GLM Coding Plan more cost-effective. The reset applies to all GLM Coding Plan users, regardless of plan tier, as a thank-you to the community. The 98% cache hit rate directly translates into approximately 1.8x more usable credits or usage from the same plan.

telegram · zaihuapd · Aug 11, 05:58

**Background**: ZCode is an agentic AI coding environment developed by Z.ai \(Zhipu AI\), designed to integrate AI agents with existing developer tools for planning, coding, reviewing, and deploying software. It is powered by Z.ai&\#x27;s GLM family of large language models, including the latest GLM-5.2. The GLM Coding Plan is a subscription service that provides access to these models for use in popular AI coding tools like Claude Code, Kilo Code, and Cline. The recent update focuses on improving caching efficiency, which reduces redundant computations and speeds up AI-assisted coding.

<details><summary>References</summary>
<ul>
<li><a href="https://zcode.z.ai/en">ZCode - Simple, Fast, Vibe‑Ready | Official Harness for GLM-5.2</a></li>
<li><a href="https://z.ai/subscribe">GLM Coding Plan — AI Coding Powered by GLM-5.2 &amp; GLM-5-Turbo ...</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#ZCode`, `#GLM`, `#product update`, `#milestone`

---

<a id="item-22"></a>
## [Graphene-Powered Soft Lens Could Revolutionize Cameras and Medical Devices](https://www.qmul.ac.uk/news/latest-news/2026/science-and-engineering/se/new-graphene-powered-soft-lens-could-pave-the-way-for-smarter-glasses-cameras-and-medical-devices.html) ⭐️ 6.0/10

Researchers at Queen Mary University of London developed a transparent soft lens made with reduced graphene oxide that can change its focal length under a small electric field. The prototype, published in Advanced Functional Materials, integrates transparent graphene electrodes directly into the lens&\#x27;s actuator layer. This technology could enable compact auto-focus cameras, AR/VR headsets, and miniature medical imaging devices without bulky mechanical parts. It represents a step toward smarter glasses and more miniaturized optical systems. The lens mimics the human eye by reshaping a soft membrane when voltage is applied, thereby focusing on objects at different distances. The team overcame a design bottleneck by embedding ultra-thin transparent graphene electrodes in the driver layer, though electrode transparency and performance still require further optimization.

telegram · zaihuapd · Aug 11, 12:27

**Background**: Reduced graphene oxide is a form of graphene oxide that has been chemically or thermally reduced to restore electrical conductivity, and it can be produced at scale. Electrically tunable lenses use deformable membranes or liquid crystals to adjust focal length without moving parts, which is relevant to applications in cameras, wearables, and medical devices. These principles help explain how the new soft lens achieves focus changes while remaining compact.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Nitrogen-doped_reduced_graphene_oxide">Nitrogen-doped reduced graphene oxide</a></li>
<li><a href="https://www.researchgate.net/publication/228446426_The_reduction_of_graphene_oxide">The reduction of graphene oxide | Request PDF</a></li>
<li><a href="https://www.yumpu.com/en/document/view/36796818/optotune-product-offeringpdf-pacer/2">Electrically tunable lens | Optotune product offering.pdf - Pacer</a></li>

</ul>
</details>

**Tags**: `#graphene`, `#optics`, `#lens`, `#materials science`, `#research`

---