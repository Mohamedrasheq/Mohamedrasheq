# Hi, I'm Mohamed Rasheq 👋

**AI Product Engineer** · ~2 years shipping AI products from first requirement to production.  
I build LLM agents end to end: context engineering, tool calling and MCP, retrieval, memory, evals and self-hosted models, plus the full-stack product around them.

📍 Trichy, India · [LinkedIn](https://www.linkedin.com/in/mohamedrasheq/) · [X](https://x.com/mohamedrasheq)

---

<table><tr>
<td valign="top" width="50%">

### 📝 Recently learned

<!-- til starts -->
- [Ignoring background noise and garbled speech before the agent replies](https://github.com/Mohamedrasheq/til/blob/main/voice/ignoring-noise-and-garbled-speech.md) - 2026-11-11
- [Carrying per-user memory across voice sessions](https://github.com/Mohamedrasheq/til/blob/main/voice/per-user-memory-across-voice-sessions.md) - 2026-11-11
- [Streaming STT and TTS so a voice agent doesn't pause mid-reply](https://github.com/Mohamedrasheq/til/blob/main/voice/streaming-stt-tts-without-gaps.md) - 2026-11-11
- [Detecting key movement events from pose landmarks](https://github.com/Mohamedrasheq/til/blob/main/vision/detecting-events-from-pose-landmarks.md) - 2026-11-11
- [Measuring joint angles from MediaPipe world landmarks](https://github.com/Mohamedrasheq/til/blob/main/vision/joint-angles-from-mediapipe.md) - 2026-11-11

[all notes](https://github.com/Mohamedrasheq/til)
<!-- til ends -->

</td>
<td valign="top" width="50%">

### 🚀 Recent releases

<!-- releases starts -->
_Nothing released yet. First releases coming soon._
<!-- releases ends -->

</td>
</tr></table>

### 🧠 What I work on
- **Agents & tool calling**: 40+ LLM assistants and agents in production. Tool-calling agent loops, MCP integrations, multi-step actions with human confirmation, and computer-use agents on sandboxed desktops
- **Grounded RAG & document AI**: hybrid and vector search, answers with server-checked citations, schema-checked extraction with confidence scores, and human review for uncertain fields
- **Evals & reliability**: rule-based and rubric-based evals, LLM tracing, and code checks that drop invented facts before users see them
- **Self-hosted & private LLMs**: open-weight models (Qwen, Llama) on vLLM and Ollama, on scale-to-zero serverless GPU, matched against commercial models on evals
- **Memory & self-improving agents**: per-user memory across sessions, and a reviewer agent that mines session data and opens validated pull requests
- **Voice & multimodal**: real-time voice agents (streaming STT/TTS, WebRTC), live AI avatars, and two-pass multimodal pipelines over pages and images
- **Vision + LLM**: pose estimation and multi-person tracking (MediaPipe, YOLOv8, OpenCV) turned into structured, safety-checked LLM reports

### 🚧 Projects
- **[cite-check](https://github.com/Mohamedrasheq/cite-check)**: checks that every claim in a RAG answer is backed by the source it cites, and shows the proof. *Coming soon.*
- **[mcp-pgvector](https://github.com/Mohamedrasheq/mcp-pgvector)**: an MCP server that gives Claude, Cursor or any MCP client hybrid (vector + keyword) search over your own Postgres tables. *Coming soon.*
- **[expense-snap](https://github.com/Mohamedrasheq/expense-snap)**: snap a receipt and AI logs the amount, store and category, then shows where your money went. *Coming soon.*
- **[mac-storage-guard](https://github.com/Mohamedrasheq/mac-storage-guard)**: a quiet macOS menu bar app that explains storage junk and cleans it safely. *Coming soon.*
- **[scam-shield](https://github.com/Mohamedrasheq/scam-shield)**: a privacy-first browser extension that spots scam messages before you click, pay or reply. *Coming soon.*

### 🧰 Stack
**Models:** OpenAI · Anthropic Claude · Gemini · Grok · Qwen · Llama  
**LLM tooling:** Vercel AI SDK · LangChain · LlamaIndex · LlamaCloud · GroundX · LangSmith · Arize · Mem0 · Firecrawl · vLLM · Ollama  
**Vector & data:** pgvector · Pinecone · Supabase · Postgres (Neon) · MongoDB · Prisma  
**Voice & avatars:** Whisper · ElevenLabs · WebRTC · Anam.ai · D-ID · Synthesia  
**Vision:** MediaPipe · YOLOv8 · BoxMOT · OpenCV · TensorFlow.js  
**Frontend & mobile:** Next.js · React · React Native (Expo) · TypeScript · Tailwind · shadcn/ui · Three.js  
**Backend:** Python (Flask, Django) · Node.js (Express)  
**Infra & testing:** Vercel · AWS · Cloud Run · Cloudflare Workers · RunPod · Firebase · Docker · GitHub Actions · Clerk · Sentry · Playwright · Jest  
**Payments & release:** Stripe · RevenueCat · Razorpay · Expo EAS

### ✍️ Writing & daily notes
- **Blog:** coming soon. Longer write-ups on building with LLMs.
- **[TIL (Today I Learned)](https://github.com/Mohamedrasheq/til):** short daily notes on agents, RAG, evals, MCP and self-hosting open models.
