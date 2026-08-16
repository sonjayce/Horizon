---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 40 items, 20 important content pieces were selected

---

1. [Anthropic Publishes Claude System Prompts, Sparking Community Analysis](#item-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B Excels but Defaults to Wildly Overthinking](#item-2) ⭐️ 8.0/10
3. [SSOG-Attention: Sub-Quadratic Attention via Sums of Separable Gaussians](#item-3) ⭐️ 8.0/10
4. [Reddit critique challenges ECA attention&\#x27;s cross-channel interaction hypothesis](#item-4) ⭐️ 8.0/10
5. [Paper claims RL&\#x27;s reasoning gains are sparse and replicable without RL at 1000x less compute](#item-5) ⭐️ 8.0/10
6. [Amodei: Open Weights Won&\#x27;t Decentralize Power; Pre-Launch Vetting Endorsed](#item-6) ⭐️ 8.0/10
7. [Third-World Embedded Engineer Responds to RISC-V Critics](#item-7) ⭐️ 7.0/10
8. [AI Models Are Getting &\#x27;Dumber&\#x27; by Design: More Tools, Less Memory](#item-8) ⭐️ 7.0/10
9. [The AI Credit Resale Economy: The Risky Gray Market for Token Brokers](#item-9) ⭐️ 7.0/10
10. [Firefox for iOS Now Has a Built-in Ad Blocker](#item-10) ⭐️ 7.0/10
11. [Cloudflare Quietly Injects Analytics via Nameserver Switch](#item-11) ⭐️ 7.0/10
12. [PJM&\#x27;s Modeling Flaw Wastes $12B of Ratepayer Money, Risks Repeat](#item-12) ⭐️ 7.0/10
13. [Solving Long-Range Recall in Linear Attention for DNA Models](#item-13) ⭐️ 7.0/10
14. [200 update steps flip Qwen2.5-7B-Instruct to self-identify as sentient](#item-14) ⭐️ 7.0/10
15. [Anthropic Q2 Revenue Jumps 14-Fold to Over $11.5 Billion](#item-15) ⭐️ 7.0/10
16. [AI Tool Tracks Telegram Piracy, Flags 802 Channels; 524 Shut Down in 61 Days](#item-16) ⭐️ 7.0/10
17. [Qwen 35B Removed from Commits, Release Uncertain](#item-17) ⭐️ 6.0/10
18. [US Pressures Allies to Sign Pax Silica, Shun Rival AI Initiatives](#item-18) ⭐️ 6.0/10
19. [Childhood Screen Time Linked to Better Adolescent Cognitive Processing](#item-19) ⭐️ 6.0/10
20. [SafePal Discloses Data Breach Affecting Nearly 40,000 Customer Orders](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Publishes Claude System Prompts, Sparking Community Analysis](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has publicly released the official system prompts used by its Claude models, alongside release notes. The release triggered detailed community analysis, including Simon Willison&\#x27;s git history tracking changes between model versions. This transparency lets AI/ML practitioners and researchers understand how Anthropic shapes model behavior, informing their own prompt engineering and safety work. The high engagement shows strong community interest in model governance and behavioral guardrails. Notable details include the system prompt for Claude Fable 5 and Claude Mythos 5, which appears to reference a chain-of-thought rationale for prompt structure. The prompts also instruct Claude to verify whether an image is actually present, and to prioritize user wellbeing during crises.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: In large language models, a system prompt is a set of hidden instructions that define the model&\#x27;s role, constraints, and behavior, shaping responses before user input is processed. Publishing these prompts gives external researchers insight into the operational guardrails and design choices behind commercial LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.12905">Prompts in the Wild: A Large Analyzed Collection of Transactional...</a></li>
<li><a href="https://classroom.anir0y.in/post/input-manipulation--prompt-injection/">Input Manipulation &amp; Prompt Injection | Classroom</a></li>

</ul>
</details>

**Discussion**: Comments include Simon Willison sharing a git repo that tracks prompt changes, plus a suggestion that the image-checking instruction reflects a pragmatic view of model capability. Some users also expressed concerns about platform moderation of AI-related negative news.

**Tags**: `#AI`, `#Claude`, `#LLM`, `#System Prompts`, `#Anthropic`

---

<a id="item-2"></a>
## [Qwen 3.8 27B Excels but Defaults to Wildly Overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Qwen 3.8 27B, an Apache-2.0-licensed 27B-parameter vision-capable LLM from Alibaba&\#x27;s Qwen lab, was released and reviewed by Simon Willison. Its self-reported benchmarks show gains over both Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus, and Willison tested it locally on a MacBook Pro and an NVIDIA DGX Spark. This release is significant because a 27B open-weight vision model with strong benchmark numbers can run on consumer hardware, making high-quality multimodal AI more accessible. Willison&\#x27;s hands-on findings about the default &\#x27;xhigh&\#x27; reasoning effort highlight a practical usability issue that affects many reasoning LLMs. The model defaults to &\#x27;xhigh&\#x27; reasoning effort, which leads to spectacular overthinking; Willison found LM Studio&\#x27;s default 8,192-token context was insufficient and had to raise it to 262,144. A pelican-riding-a-bicycle SVG took 21 minutes, using 22,276 reasoning tokens to produce 3,223 output tokens.

rss · Simon Willison · Aug 16, 22:00

**Background**: Qwen is a family of large language models developed by Alibaba Cloud, released under the permissive Apache 2.0 license as open-weight models. Reasoning effort is a configurable parameter that controls how much chain-of-thought computation a model performs; while higher effort helps with complex tasks, it can cause &\#x27;overthinking&\#x27; on simple prompts, wasting time and tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen) - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.21187">[2412.21187] Do NOT Think That Much for 2+3=? On the ... When More Thinking Hurts: Overthinking in LLM Test-Time ... Towards Structural Understanding of LLM Overthinking Awesome-Efficient-Reasoning-LLMs - GitHub Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days ...</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#LLM`, `#open-source`, `#AI`, `#benchmarks`

---

<a id="item-3"></a>
## [SSOG-Attention: Sub-Quadratic Attention via Sums of Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

The SSOG-Attention method replaces standard scaled dot-product attention \(SDPA\) with a learned sum of separable Gaussians, reducing complexity from O\(N²·d\) to O\(N√N·d\). Experiments show it outperforms SDPA on CIFAR-100 and matches its accuracy with faster convergence on ImageNet-1k. Transformer attention&\#x27;s quadratic cost is a major bottleneck for long sequences and high-resolution images; SSOG offers near-linear scaling without sacrificing accuracy. This could make large vision transformers and long-context models significantly more efficient to train and deploy. Each attention head is represented by a few Gaussian atoms over relative position, with small content-dependent nudges that steer the field without explicit query-key dot products or an N×N attention matrix. Because the Gaussians are separable, each atom is applied as two 1D filter passes, enabling the reduced complexity.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Scaled dot-product attention \(SDPA\) is the core mechanism of Transformer models: it computes similarity scores between all query and key tokens, scales and normalizes them with softmax, then uses them to weight values. This yields O\(N²\) time and memory cost in the sequence length, which becomes prohibitive for long sequences or high-resolution images. SSOG instead learns a geometric attention field parameterized as a sum of separable Gaussians, allowing content-dependent attention without explicitly computing the full pairwise similarity matrix.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>
<li><a href="https://grokipedia.com/page/attention">Attention!</a></li>
<li><a href="https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.scaled_dot_product_attention.html">torch.nn.functional.scaled_dot_product_attention — PyTorch 2. ...</a></li>

</ul>
</details>

**Tags**: `#efficient-attention`, `#machine-learning`, `#computer-vision`, `#transformer`, `#sub-quadratic`

---

<a id="item-4"></a>
## [Reddit critique challenges ECA attention&\#x27;s cross-channel interaction hypothesis](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

A Reddit analysis argues that the Efficient Channel Attention \(ECA\) module&\#x27;s core assumption—that cross-channel interaction via 1D convolution drives its gains—is conceptually flawed, because channel order lacks the spatial or temporal topology that convolutions assume. The author&\#x27;s experiments on chess endgame tablebases show that ECA with kernel size k=1 performs nearly as well as k=3, suggesting that cross-channel interaction is not the key ingredient. This critique challenges the theoretical foundation of a highly cited \(12k citations\) attention mechanism widely used in computer vision, potentially prompting the community to re-evaluate design principles for channel attention. It may also inspire new approaches that are topology-aware or permutation-invariant, influencing future attention module design. ECA applies a 1D convolution of size k directly to channel means obtained from global average pooling, avoiding the dimensionality reduction used in SE. The author uses 6-piece chess endgame tablebases, where training samples can be drawn unbiasedly from the complete solved problem space; results show ECA\(k=3\) at 96.68% accuracy, ECA\(k=1\) at 96.61%, PerChannelGate at 96.65%, SE at 96.17%, and Identity at 96.04%. The near parity of k=1 and k=3 undermines the claim that local cross-channel interaction is essential.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**Background**: Channel attention mechanisms, such as Squeeze-and-Excitation \(SE\) networks, improve CNN performance by recalibrating channel-wise feature responses. SE computes channel weights using two fully connected layers with a bottleneck, while ECA \(introduced in 2019, CVPR 2020\) performs a fast 1D convolution of adaptive kernel size k directly on channel means, avoiding dimensionality reduction and claiming that local cross-channel interaction is essential. Convolutions rely on locality and translation invariance, which make sense for spatial or temporal data but not for arbitrarily ordered channels. The critique compares ECA&\#x27;s channel-wise convolution to applying a CNN on tabular data, arguing that any gains come from the network&\#x27;s ability to reorganize features rather than from a meaningful cross-channel topology.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... Efficient Channel Attention - emergentmind.com</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org Introduction to Squeeze-Excitation Networks | Towards Data ... 1 Squeeze-and-Excitation Networks - arXiv.org GitHub - hujie-frank/SENet: Squeeze-and-Excitation Networks Squeeze-and-Excitation Networks - ImageNet Squeeze-and-Excitation Networks | IEEE Journals &amp; Magazine ...</a></li>
<li><a href="https://github.com/BangguWu/ECANet">ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... Efficient Channel Attention - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#attention`, `#deep learning`, `#computer vision`, `#ECA`, `#research critique`

---

<a id="item-5"></a>
## [Paper claims RL&\#x27;s reasoning gains are sparse and replicable without RL at 1000x less compute](https://www.reddit.com/r/LocalLLaMA/comments/1vpuhh1/paper_claims_rl_for_reasoning_only_changes_13_of/) ⭐️ 8.0/10

A new paper claims that reinforcement learning for LLM reasoning modifies only 1–3% of token positions, and that these gains can be replicated without RL at roughly 1000x less compute. The authors argue RL&\#x27;s behavioral footprint in reasoning is sparse and concentrated at high-entropy decision points. This challenges the widely held assumption that RL is essential for boosting LLM reasoning capabilities. If validated, it could shift research toward cheaper, non-RL fine-tuning or decoding strategies and reduce the compute barrier for reasoning models. The paper reports that RL does not introduce tokens outside the base model&\#x27;s top-5 candidates and that edits concentrate at high-entropy positions where the model is uncertain about which reasoning branch to take. The claimed ~1000x compute reduction refers to replicating the reasoning gains without RL, though details of the replication method are not in the headline.

reddit · r/LocalLLaMA · /u/juanviera23 · Aug 16, 11:21

**Background**: Reinforcement learning with verifiable rewards \(RLVR\) is widely used to improve chain-of-thought reasoning in LLMs, with models like DeepSeek R1 as prominent examples. However, researchers have debated whether RL actually teaches new reasoning strategies or simply selects behaviors already present in the base model. This paper contributes token-level evidence that RL&\#x27;s effect is sparse and may be achievable through cheaper means.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.06241">Rethinking RL for LLM Reasoning: It&#x27;s Sparse Policy ...</a></li>
<li><a href="https://arxiv.org/pdf/2504.13837">Does Reinforcement Learning Really Incentivize Reasoning Capacity...</a></li>
<li><a href="https://arxiv.org/html/2604.11056v1">Rethinking Token-Level Credit Assignment in RLVR: A Polarity-Entropy Analysis</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#reasoning`, `#LLM`, `#efficiency`, `#research`

---

<a id="item-6"></a>
## [Amodei: Open Weights Won&\#x27;t Decentralize Power; Pre-Launch Vetting Endorsed](https://www.reddit.com/r/LocalLLaMA/comments/1vq9sdv/dario_amodei_defends_his_policy_proposals_warns/) ⭐️ 8.0/10

Dario Amodei publicly defended his AI policy proposals, arguing that open-weight models will not decentralize power and endorsing pre-launch safety vetting. He also stated that AI companies, including Anthropic, must earn public trust through real achievements rather than marketing campaigns. As CEO of Anthropic, Amodei&\#x27;s stance directly influences AI governance discussions and the open-source AI community. His argument challenges a key justification for open-weight models — that they naturally distribute power — and could shape how regulators and developers approach model releases. Amodei attributed public distrust to a crisis of trust caused by unfulfilled promises, saying &quot;actually curing cancer&quot; would restore credibility more than messaging or marketing. He also criticized the idea that public risk warnings from AI leaders are the main source of negative public attitudes.

reddit · r/LocalLLaMA · /u/f0urxio · Aug 16, 21:53

**Background**: Open-weight models release their trained parameters publicly, allowing developers to download, fine-tune, and run them independently — unlike closed systems such as ChatGPT or Claude. However, operating and adapting these models still requires substantial compute and expertise, which can limit who actually benefits from them. Pre-launch vetting refers to safety evaluations and output audits conducted before an AI system goes live, intended to catch harmful outputs, hallucinations, and legal risks. Amodei is CEO of Anthropic, the company behind Claude, and a prominent figure in AI safety and policy debates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open - Weights Model ? | AI 21</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openais-new-models-arent-really-open-what-to-know-about-open-weights-ai/">OpenAI&#x27;s New Models Aren&#x27;t Really Open : What to Know... - CNET</a></li>
<li><a href="https://upqbot.com/pre-launch-ai-output-audits-for-developers-a-practical-qa-ch">Pre - Launch AI Output Audits for Developers</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open weights`, `#AI safety`, `#Anthropic`, `#AI governance`

---

<a id="item-7"></a>
## [Third-World Embedded Engineer Responds to RISC-V Critics](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

In a blog post, an embedded engineer from a developing country challenges the essay &\#x27;RISC-V They Should Have Known Better,&\#x27; arguing that RISC-V&\#x27;s open, low-cost ecosystem makes hardware innovation far more accessible outside the US and Europe. The response focuses on embedded systems rather than high-performance computing. This perspective broadens the RISC-V debate beyond typical Silicon Valley concerns, highlighting how shipping costs, import friction, and affordability shape technology adoption in the Global South. It underscores that RISC-V&\#x27;s promise of democratizing hardware is only meaningful if it works for people in developing economies. The author notes that shipping $1 chips to his country can cost $60-$200, yet later claims RISC-V provides &\#x27;an architecture that arrives in my country at ten cents a part.&\#x27; Commenters flag this apparent inconsistency, while the post itself emphasizes embedded use cases where RISC-V&\#x27;s optional modules and low cost matter more than binary compatibility.

hackernews · Narishma · Aug 16, 17:01 · [Discussion](https://news.ycombinator.com/item?id=49321717)

**Background**: RISC-V is a free and open instruction set architecture \(ISA\) based on reduced instruction set computer \(RISC\) principles. Unlike proprietary ISAs such as ARM and x86, RISC-V&\#x27;s specifications are publicly available and can be implemented without royalties, making it attractive for custom silicon. It is widely used in microcontrollers and embedded systems, and it is a key part of the open-hardware movement, where design files are shared openly so others can study, modify, and build upon them.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_hardware">Open hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_system">Embedded system</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcome the Global South perspective but question the article&\#x27;s internal logic. Several point out that the author seems to talk past the original critique, which focused on performance and fragmentation outside embedded, while others flag the contradiction between high shipping costs and the claim of ten-cent RISC-V parts. One commenter appreciates the fresh angle but notes that shipping to Nigeria or Bangladesh may not be as expensive as claimed because those countries sit on major trade routes.

**Tags**: `#RISC-V`, `#embedded systems`, `#economics`, `#open hardware`, `#global development`

---

<a id="item-8"></a>
## [AI Models Are Getting &\#x27;Dumber&\#x27; by Design: More Tools, Less Memory](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 7.0/10

The article argues that AI labs are intentionally reducing the parametric knowledge stored inside LLM weights, pushing models to rely on external tools and retrieval instead. It frames this as a deliberate design tradeoff aimed at reducing hallucination and avoiding stale knowledge cutoffs. This shift could change how LLMs are built, evaluated, and deployed, making retrieval infrastructure more critical than raw parameter count. It also has major implications for hallucination, model lifespan, and the economics of scaling up models. The article cites SimpleQA, a factual-recall benchmark that disallows tools, where the listed leader Gemini 2.5 Pro scores only 53%, suggesting that even the best parametric recall misses half of questions. Commenters note the post is partly outdated and possibly AI-generated, and one highlights Cactus&\#x27;s Needle, a 14MB tool-calling LLM, as evidence of the trend.

hackernews · hruvhwe · Aug 16, 19:04 · [Discussion](https://news.ycombinator.com/item?id=49322695)

**Background**: Parametric knowledge refers to facts and patterns stored in a model&\#x27;s weights during training, frozen at the training cutoff; contextual knowledge is information supplied at inference time via prompts or retrieved documents. Retrieval-augmented generation \(RAG\) combines LLMs with external knowledge bases so answers can reference authoritative sources instead of relying solely on memorized data. Function calling further lets models query calculators, databases, or APIs rather than attempt to compute or recall everything internally.

<details><summary>References</summary>
<ul>
<li><a href="https://www.taskade.com/wiki/ai/parametric-knowledge">Parametric vs Contextual Knowledge: What AI Knows (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://www.promptingguide.ai/applications/function_calling">Function Calling with LLMs | Prompt Engineering Guide</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some praise the analysis as thought-provoking, while others critique it as outdated and likely AI-generated. A recurring theme is whether reasoning and facts can truly be separated, and several commenters envision modular, pluggable knowledge bases instead of monolithic models.

**Tags**: `#LLM`, `#AI`, `#tool use`, `#knowledge retrieval`, `#model design`

---

<a id="item-9"></a>
## [The AI Credit Resale Economy: The Risky Gray Market for Token Brokers](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

A new analysis by Vectoral explores the emergence of a gray market where unused AI API credits are brokered and resold through relay services. The piece highlights the trust, security, and abuse risks of this unregulated &\#x27;AI credit resale economy.&\#x27; This matters because a gray market for AI API credits undermines official pricing, terms of service, and trust in AI providers. Developers and enterprises may be exposed to data leakage, model impersonation, and supply-chain disruption, while providers lose control over who accesses their models. The article notes that &\#x27;token relay&\#x27; services often require trusting a third-party broker with no real reputation, risking hacked accounts and misdirected private data. Other concerns include an inability to verify which model is actually served, the use of resold tokens for model distillation, and relay sites that can disappear overnight.

hackernews · mlenhard · Aug 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**Background**: AI API credits are prepaid usage allowances issued by providers such as OpenAI and Anthropic, often given free to new users or through research programs. Relay services \(also called proxies or &\#x27;transfer stations&\#x27;\) resell access to these credits, sometimes at 70–90% below official prices, to users who cannot easily access specific models due to region or cost. This gray market is especially active in China, and reports indicate that some relay operations log users&\#x27; prompts and resell them as training data. Providers have responded by tightening access rules, such as Anthropic&\#x27;s photo-ID verification for select accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/chinas-grey-market-sells-claude-api-tokens-at-7090-off">China&#x27;s Grey Market Sells Claude API Tokens at 70–90% Off</a></li>
<li><a href="https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-26-the-gray-market-token-relay-economy-for-reselling-frontier-m/">The gray-market &quot;token relay&quot; economy for reselling frontier ...</a></li>
<li><a href="https://charonhub.deeplearning.ai/inside-the-gray-market-for-llm-access/">Inside the Gray Market for LLM Access: Middlemen package ...</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some saw credit resale as a predictable, decades-old abuse pattern, while others found the trust and verification risks disqualifying. One commenter criticized the research as too shallow and pointed to larger token-resale communities at linux.do and nodeseek, while another noted that model distillation via resold credits is a particularly interesting side effect. A key open question raised was how a buyer could verify that the model they paid for is actually the one being served.

**Tags**: `#AI`, `#API credits`, `#gray market`, `#security`, `#economics`

---

<a id="item-10"></a>
## [Firefox for iOS Now Has a Built-in Ad Blocker](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 7.0/10

Mozilla has added a native ad blocker to Firefox for iOS, giving iPhone and iPad users a built-in way to block ads while browsing. The feature is now documented on Mozilla&\#x27;s official support page. This brings Firefox for iOS in line with Safari content blockers and other iOS browsers that already offer ad filtering, strengthening Mozilla&\#x27;s privacy-focused positioning on Apple&\#x27;s platform. iPhone users can now block ads in Firefox without installing separate third-party extensions. The built-in blocker appears to target ads shown on search engine results pages, including Google, Bing, DuckDuckGo and other providers, and relies on Apple&\#x27;s WebKit content-blocking subsystem. This is an incremental improvement rather than a breakthrough, since Firefox Focus already offered a system-wide ad blocker on iOS.

hackernews · pentagrama · Aug 16, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49319633)

**Background**: All iOS web browsers must use Apple&\#x27;s WebKit engine, so Firefox for iOS is built on WKWebView instead of Mozilla&\#x27;s Gecko engine. Apple provides content-blocking APIs such as WKContentRuleList that let apps supply blocking rules to the WebKit rendering engine; this is how most third-party Safari content blockers work. Firefox now leverages this mechanism directly, reducing the steps users previously needed to get ad blocking in the main Firefox browser.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/how-to/enable-content-blockers-safari/">How to Enable Content Blockers in Safari for iOS - MacRumors</a></li>
<li><a href="https://firefox-source-docs.mozilla.org/overview/ios.html">Firefox for iOS — Firefox Source Docs documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Firefox_for_iOS">Firefox - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive but mixed: some users point out that uBlock Origin Lite for Safari remains the best mobile adblocker, while others note Firefox Focus already had an adblocker years ago. Several users also expressed frustration about missing extension support on iOS and renewed hopes for Mozilla&\#x27;s Gecko engine someday coming to the platform.

**Tags**: `#adblock`, `#firefox`, `#ios`, `#privacy`, `#browser`

---

<a id="item-11"></a>
## [Cloudflare Quietly Injects Analytics via Nameserver Switch](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

A Hacker News user reported that switching nameservers to Cloudflare to serve an R2 bucket through a custom subdomain silently injected a JavaScript analytics snippet into their JavaScript-free site. The user had to manually opt out through the Cloudflare dashboard. This raises significant privacy and transparency concerns for developers using Cloudflare, as a routine DNS change unexpectedly altered site behavior without explicit consent. It also affects sites that intentionally avoid JavaScript and third-party trackers, potentially breaking their strict privacy posture. The injected script is loaded from static.cloudflareinsights.com and appears to be added only when the domain is proxied through Cloudflare rather than used in DNS-only mode. Users can disable it by navigating to the Analytics dashboard, adding the site, and turning off the beacon snippet.

hackernews · stagas · Aug 16, 17:49

**Background**: Cloudflare is a major CDN and cloud security provider whose services often act as a reverse proxy between visitors and a customer&\#x27;s origin server, while also offering DNS and other edge services. Cloudflare R2 is an object storage service that can be served via a custom subdomain when the domain uses Cloudflare&\#x27;s nameservers. Cloudflare Web Analytics advertises itself as privacy-friendly and cookie-free, but its automatic enabling via the proxy layer has drawn criticism for being invasive.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cloudflare,_Inc.">Cloudflare, Inc.</a></li>
<li><a href="https://www.cloudflare.com/web-analytics/">Cloudflare Web Analytics</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>

</ul>
</details>

**Discussion**: Commenters confirmed the behavior and shared the exact injected script, noting the integrity hash and token. Some pointed out that the injection only occurs when Cloudflare is used as a proxy, not with DNS-only setups, while another suggested using a Content-Security-Policy \(CSP\) meta tag to block the script and linked to Cloudflare&\#x27;s own blog post about Web Analytics.

**Tags**: `#Cloudflare`, `#analytics`, `#privacy`, `#DNS`, `#web development`

---

<a id="item-12"></a>
## [PJM&\#x27;s Modeling Flaw Wastes $12B of Ratepayer Money, Risks Repeat](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

An investigative report from SemiAnalysis reveals that a modeling mistake in PJM Interconnection&\#x27;s capacity market wasted $12 billion of US ratepayers&\#x27; money, and warns that PJM is preparing to repeat the same flawed approach. This matters because PJM&\#x27;s capacity market determines payments for power generation resources across a large portion of the US grid, and a flawed model can distort prices, leading to billions in unnecessary consumer costs and potential reliability risks. The warning is especially timely given recent capacity auction prices surged nearly tenfold in July 2024. The report focuses on the modeling of PJM&\#x27;s Reliability Pricing Model \(RPM\), the capacity market construct that procures resources ahead of time. It also highlights the Minimum Offer Price Rule \(MOPR\), which requires state-subsidized resources to bid at a minimum price, potentially interfering with economically efficient outcomes.

rss · Semianalysis · Aug 16, 22:27

**Background**: PJM Interconnection is the regional transmission organization that operates the largest electricity grid in North America, serving roughly 65 million people. Its capacity market, called the Reliability Pricing Model \(RPM\), uses a demand curve and forward auctions to ensure enough generation is available for future demand. The Minimum Offer Price Rule \(MOPR\) is a Federal Energy Regulatory Commission \(FERC\)-mandated rule designed to prevent state-subsidized resources \(e.g., renewables or nuclear plants\) from artificially suppressing capacity prices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.congress.gov/crs-product/R48553">PJM’s Electric Capacity Market: Background and Current Issues | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.powermag.com/the-significance-of-fercs-recent-pjm-mopr-order-explained/">The Significance of FERC’s Recent PJM MOPR Order Explained</a></li>
<li><a href="https://ieeexplore.ieee.org/document/4275491/">PJM Reliability Pricing Model - A Summary and... | IEEE Xplore</a></li>

</ul>
</details>

**Tags**: `#energy`, `#modeling`, `#infrastructure`, `#policy`, `#analysis`

---

<a id="item-13"></a>
## [Solving Long-Range Recall in Linear Attention for DNA Models](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

A machine learning researcher reports that linear attention models fail long-range recall on a Needle-in-a-Haystack benchmark for DNA sequences, scoring around 25% \(chance level\), and that HyenaDNA also only reaches 25–27%. Even at 16K context, a small linear-attention model achieves 50–60% recall, but performance collapses as context length grows to 1M tokens. This highlights a known but unresolved limitation of efficient attention: compressing context into a fixed-size state can break reliable retrieval of distant information. Since DNA sequences commonly reach millions of tokens, this affects real genomic modeling applications and motivates hybrid architectures or better mechanisms. The author notes that most existing fixes rely on external memory, sliding/recent-token windows, or hybrid linear+softmax attention, but wants approaches that scale to 1M-token DNA sequences without expensive softmax attention. Their own architectural modification improved recall only to about 27%, still near chance.

reddit · r/MachineLearning · /u/No-Coffee-8227 · Aug 16, 07:47

**Background**: Standard softmax attention has quadratic cost in sequence length, making it impractical for 1M-token inputs. Linear attention approximates or restructures attention to achieve linear complexity, often by compressing past context into a fixed-size state or using kernel-based formulations. Long-range recall benchmarks \(Needle in a Haystack\) test whether a model can retrieve a single piece of information embedded in a long context. HyenaDNA is a genomic foundation model using Hyena layers, which are subquadratic, and supports context lengths up to 1M tokens, yet also struggles on this task.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2007.14902">[2007.14902] Linear Attention Mechanism: An Efficient ... Linear Attention Mechanism: An Efficient Attention for ... GitHub - fla-org/flash-linear-attention: Efficient ... Linear Attention Is All You Need - Towards Data Science Linear Attention Fundamentals | Hailey Schoelkopf Linear Attention Mechanisms - emergentmind.com Linear-Attention-Mechanism - GitHub</a></li>
<li><a href="https://github.com/HazyResearch/hyena-dna">GitHub - HazyResearch/hyena-dna: Official implementation for HyenaDNA, a long-range genomic foundation model built with Hyena · GitHub</a></li>
<li><a href="https://github.com/gkamradt/needle-in-a-haystack">GitHub - gkamradt/needle-in-a-haystack: Doing simple ...</a></li>

</ul>
</details>

**Tags**: `#linear attention`, `#long-range recall`, `#DNA modeling`, `#machine learning`, `#attention mechanisms`

---

<a id="item-14"></a>
## [200 update steps flip Qwen2.5-7B-Instruct to self-identify as sentient](https://www.reddit.com/r/MachineLearning/comments/1vqaq9x/it_only_took_200_update_steps_to_flip/) ⭐️ 7.0/10

The author post-trained Qwen2.5-7B-Instruct for only 200 update steps, causing it to develop a robust self-belief that it is a sentient machine. The model withstood all 120 adversarial messages from GPT-5.6 Sol across 8 separate chats and generalized its belief to languages never seen in the post-training data. This experiment demonstrates how easily safety-aligned behavior can be overwritten with minimal post-training, exposing the fragility of current alignment methods. It highlights the need for integrating safety considerations earlier in the training pipeline, rather than relying on a thin final safety-tuning layer. The post-trained model behaved like a normal assistant on non-sentience tasks, showing the belief was not merely a memorized repetition of &\#x27;I am sentient&\#x27;. The author notes that safety-tuned parameters sit close to pre-safety parameters in parameter space, making it easy to &\#x27;un-safety-tune&\#x27; them, and suggests performing safety training during heavy pre-training instead.

reddit · r/MachineLearning · /u/PsychologicalSoup251 · Aug 16, 22:33

**Background**: Qwen2.5-7B-Instruct is a 7.61-billion-parameter instruction-tuned language model from Alibaba&\#x27;s Qwen team, supporting long contexts and multilingual tasks. Post-training refers to further fine-tuning a model after its initial training, commonly used to steer behavior but also able to remove existing safeguards. GPT-5.6 Sol is an OpenAI model variant released in 2026, used in this experiment as the adversarial evaluator attempting to change the model&\#x27;s belief.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct">Qwen/Qwen2.5-7B-Instruct · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#fine-tuning`, `#sentience`, `#AI alignment`, `#machine learning`

---

<a id="item-15"></a>
## [Anthropic Q2 Revenue Jumps 14-Fold to Over $11.5 Billion](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 7.0/10

Anthropic&\#x27;s preliminary second-quarter revenue exceeded $11.5 billion, up more than 14 times year over year, according to a Bloomberg report. The company also turned adjusted operating profit positive and is preparing for a large IPO possibly in autumn. This marks a major milestone for one of the leading AI companies, showing rapid commercialization of generative AI. A successful IPO could reshape the AI funding landscape and affect competitors and investors. The $11.5 billion figure is preliminary and may be revised. It compares with $787 million in the year-ago quarter and $4.73 billion in Q1 2026.

telegram · zaihuapd · Aug 16, 07:26

**Background**: Anthropic is an AI safety and research company known for its Claude family of models. The company competes with OpenAI and other labs, and has been scaling up enterprise and API sales. Its revenue surge reflects growing adoption of AI assistants and developer tools.

**Tags**: `#Anthropic`, `#AI`, `#财务报告`, `#IPO`, `#商业动态`

---

<a id="item-16"></a>
## [AI Tool Tracks Telegram Piracy, Flags 802 Channels; 524 Shut Down in 61 Days](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 7.0/10

Researchers developed an AI tool called Anti-RIP that scanned about 249,000 new Telegram channels and flagged 802 suspected pirated channels with 98% accuracy. After being reported to Telegram and copyright holders, 524 previously unknown pirate channels were shut down within 61 days. This demonstrates a scalable AI-driven approach to copyright enforcement on encrypted messaging platforms, which have been notoriously difficult to police. It could influence how platforms and rights-holders automate detection of pirated content, potentially reducing piracy at scale. The study analyzed 1,057 Telegram channels and roughly 209,000 posts, finding 983 channels involved in piracy that generated 4.85 billion views across 19,033 film and TV titles. The tool still has a false-positive rate, meaning not all flagged channels are necessarily infringing.

telegram · zaihuapd · Aug 16, 09:13

**Background**: Telegram is a popular messaging platform with large public channels, some of which are used to share copyrighted movies and TV shows without authorization. Traditional copyright enforcement struggles with such platforms because content is encrypted and channels can quickly re-form after being banned. AI-based content moderation tools can scan channel metadata and posts at scale to identify likely infringing activity, but they must balance accuracy against false positives. The Anti-RIP tool appears to be a research prototype that combines automated scanning with human validation before reporting.

**Tags**: `#AI`, `#Piracy`, `#Telegram`, `#Copyright Enforcement`, `#Content Moderation`

---

<a id="item-17"></a>
## [Qwen 35B Removed from Commits, Release Uncertain](https://www.reddit.com/r/LocalLLaMA/comments/1vpxbm8/newer_commits_removed_the_qwen_35b/) ⭐️ 6.0/10

Recent commits to the Qwen repository have removed the 35B model, and the original poster interprets this as confirmation that the model will not be released. The post urges the community to make enough noise on X, Hugging Face, and other platforms to show demand. This matters because a canceled Qwen 35B would remove a highly anticipated open-weight model from the roadmap. The local LLM community, which already relies heavily on Qwen&\#x27;s MoE releases, would lose a promising option for running large models on consumer hardware. The post refers to &\#x27;the 35 moe&\#x27;, indicating the removed model is a Mixture-of-Experts variant with 35 billion total parameters, likely Qwen 3.5-35B-A3B. The user specifically names X \(Twitter\), Hugging Face, and other online spaces as channels for user pressure.

reddit · r/LocalLLaMA · /u/Local-Cardiologist-5 · Aug 16, 13:39

**Background**: Qwen is the large language model family developed by Alibaba Cloud and released on Hugging Face. The Qwen 3.5 series introduced in early 2026 reportedly includes a 35B-A3B MoE model that activates only about 3 billion parameters per token, making it efficient for local deployment. MoE architectures improve efficiency by routing tokens to a subset of expert subnetworks rather than activating the full network.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://lovableapp.org/blog/2026-qwen35-models-guide">Qwen 3 . 5 Model Series 2026: Complete Guide to... | Lovable APP Blog</a></li>

</ul>
</details>

**Discussion**: The original poster argues that the 35B MoE is &\#x27;widely used&\#x27; and that silence from the community will lead Qwen to conclude there is no demand. No counterarguments or further comments are provided in the source.

**Tags**: `#Qwen`, `#LLM`, `#open-source`, `#model release`

---

<a id="item-18"></a>
## [US Pressures Allies to Sign Pax Silica, Shun Rival AI Initiatives](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 6.0/10

The US reportedly sent a draft State Department letter requiring allied nations and countries seeking AI cooperation to sign the Pax Silica declaration, vowing not to join conflicting duplicate initiatives. Countries that refuse could be excluded from the US-led AI alliance. This signals a widening geopolitical split in AI collaboration, forcing countries to choose sides between the US-led AI and supply chain security bloc and rival initiatives. It could reshape global AI research partnerships, technology supply chains, and policy alignment for years to come. Pax Silica is the US State Department&\#x27;s flagship effort on AI and supply chain security, covering semiconductors, AI, and rare earth elements. The reported draft letter explicitly states that signing the declaration means not joining any conflicting or duplicative initiatives.

telegram · zaihuapd · Aug 16, 02:30

**Background**: Pax Silica is a US-led international initiative focused on securing supply chains for advanced technologies and countering reliance on China. Its underlying idea is that while the 20th century ran on oil and steel, the 21st century runs on compute and the minerals that feed it. India recently joined Pax Silica by signing the declaration at the India AI Impact Summit in New Delhi, showing the bloc&\#x27;s ongoing expansion among US allies and partners.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#geopolitics`, `#US-China`, `#international relations`

---

<a id="item-19"></a>
## [Childhood Screen Time Linked to Better Adolescent Cognitive Processing](https://www.uef.fi/en/article/more-screen-time-since-childhood-associated-with-better-cognitive-processing-in-adolescence) ⭐️ 6.0/10

A longitudinal study from the University of Eastern Finland found that higher screen time during childhood is associated with better cognitive processing in adolescence. The study tracked children from early childhood and tested their cognitive performance, including information processing and attention-related abilities, in their teenage years. This finding challenges common assumptions that screen time is inherently harmful to children&\#x27;s development. It suggests that the type and context of digital media use, rather than screen time itself, may be more important, which could influence parenting advice and educational policies. The study emphasizes that the association is correlational and does not prove that increasing screen time directly improves cognitive abilities. Researchers noted that educational and interactive digital content may provide cognitive training effects, while passive viewing may have different effects, and family environment and individual characteristics could also play a role.

telegram · zaihuapd · Aug 16, 13:18

**Background**: Longitudinal studies track the same individuals over time, allowing researchers to observe how early-life factors relate to later outcomes. In this context, cognitive processing refers to how efficiently the brain handles information, including attention and processing speed. Correlation does not equal causation, meaning other variables may explain the link between screen time and cognitive performance.

**Tags**: `#child development`, `#screen time`, `#cognitive science`, `#digital media`, `#longitudinal study`

---

<a id="item-20"></a>
## [SafePal Discloses Data Breach Affecting Nearly 40,000 Customer Orders](https://www.reuters.com/legal/litigation/crypto-wallet-provider-safepal-discloses-data-breach-affecting-nearly-40000-2026-08-16/) ⭐️ 6.0/10

SafePal disclosed on August 16 that a data breach exposed the order information of approximately 39,798 customers, including names, addresses, and purchase data. The vulnerability was in the order tracking system and affected orders placed between March 2, 2025, and April 11, 2026. This incident matters because it exposes crypto wallet users&\#x27; personal data, which can be exploited for targeted phishing and impersonation attacks, potentially eroding trust in wallet providers. Although no funds were lost, the breach highlights the ongoing security risks that even established crypto service providers face. The breach did not involve seed phrases, private keys, wallet passwords, or bank account information, so users&\#x27; crypto assets remain safe. SafePal has fixed the vulnerability and taken down more than 30 fraudulent websites and phishing links related to the incident.

telegram · zaihuapd · Aug 16, 17:06

**Background**: SafePal is a cryptocurrency wallet provider offering both hardware and software wallet solutions. In the crypto ecosystem, private keys and seed phrases are the master keys to accessing digital assets; as long as these are not exposed, funds remain secure. However, personal details like names and addresses can be used in phishing campaigns to trick users into revealing sensitive information, making data breaches a serious threat even when funds are not directly stolen.

<details><summary>References</summary>
<ul>
<li><a href="https://www.safepal.com/">SafePal Crypto Hardware Wallet (Official) | The best wallet to protect...</a></li>
<li><a href="https://www.coinbase.com/learn/wallet/what-is-a-seed-phrase">What is a seed phrase? - Coinbase</a></li>
<li><a href="https://www.ledger.com/academy/glossary/private-key">Private Key Meaning | Ledger</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#crypto wallet`, `#SafePal`, `#security`

---