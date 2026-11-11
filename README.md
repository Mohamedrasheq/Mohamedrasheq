# Hi, I'm Mohamed Rasheq 👋

**AI Product Engineer** · ~2 years shipping AI products from first requirement to production.  
I build LLM agents end to end: context engineering, tool calling and MCP, retrieval, memory, evals and self-hosted models, plus the full-stack product around them.

📍 Trichy, India · [LinkedIn](https://www.linkedin.com/in/mohamedrasheq/) · [X](https://x.com/mohamedrasheq)

---

### 📝 Recently learned

<!-- til starts -->
- [Ignoring background noise and garbled speech before the agent replies](https://github.com/Mohamedrasheq/til/blob/main/voice/ignoring-noise-and-garbled-speech.md)
- [Carrying per-user memory across voice sessions](https://github.com/Mohamedrasheq/til/blob/main/voice/per-user-memory-across-voice-sessions.md)
- [Streaming STT and TTS so a voice agent doesn't pause mid-reply](https://github.com/Mohamedrasheq/til/blob/main/voice/streaming-stt-tts-without-gaps.md)
- [Detecting key movement events from pose landmarks](https://github.com/Mohamedrasheq/til/blob/main/vision/detecting-events-from-pose-landmarks.md)
- [Measuring joint angles from MediaPipe world landmarks](https://github.com/Mohamedrasheq/til/blob/main/vision/joint-angles-from-mediapipe.md)

[all notes](https://github.com/Mohamedrasheq/til)
<!-- til ends -->

<!-- releases starts -->
<!-- releases ends -->

### 🧠 What I work on
- **Agents & tool calling**: 40+ LLM assistants and agents in production. Tool-calling agent loops, MCP integrations, multi-step actions with human confirmation, and computer-use agents on sandboxed desktops
- **Grounded RAG & document AI**: hybrid and vector search, answers with server-checked citations, schema-checked extraction with confidence scores, and human review for uncertain fields
- **Evals & reliability**: rule-based and rubric-based evals, LLM tracing, and code checks that drop invented facts before users see them
- **Self-hosted & private LLMs**: open-weight models (Qwen, Llama) on vLLM and Ollama, on scale-to-zero serverless GPU, matched against commercial models on evals
- **Memory & self-improving agents**: per-user memory across sessions, and a reviewer agent that mines session data and opens validated pull requests
- **Voice & multimodal**: real-time voice agents (streaming STT/TTS, WebRTC), live AI avatars, and two-pass multimodal pipelines over pages and images
- **Vision + LLM**: pose estimation and multi-person tracking (MediaPipe, YOLOv8, OpenCV) turned into structured, safety-checked LLM reports

### 🚧 Building now: BackForge AI
A mobile AI task assistant (iOS & Android). You talk or type in plain language, the LLM turns each message into structured actions, and code resolves the tasks and dates. It asks instead of guessing, and every change waits for your confirmation. Backed by 270+ unit tests and 68 eval cases.  
*Closed source. Demo and case study coming soon.*

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

### 📌 Open-source projects
Small, installable LLM tools are on the way: an eval-first RAG app, an MCP server, CLIs and more, plus contributions to the open-source AI tools I use every day. Pinned below as they ship.
