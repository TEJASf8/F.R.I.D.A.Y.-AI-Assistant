# F.R.I.D.A.Y. — Advanced AI Assistant Project Log

Welcome to the development history of **F.R.I.D.A.Y.**, a modular, real-time AI assistant built to master agentic workflows, multi-modal pipelines, and automation layers. As an AIML undergraduate student, I am building this project from scratch to bridge the gap between heavy college theory and practical engineering.

---

## 📈 The Evolution Track

### 🚀 Milestone 1: The Core Brain (Phase 1)
* **Status:** Operational & Fully Secure ✅
* **Key Challenges Overcome:** 
  * Fixed environment clashes between `langchain-core` and legacy `pydantic_v1` frameworks.
  * Resolved `404 NOT_FOUND` API errors by adapting to the native `gemini-2.5-flash` model endpoint structure.
  * **Security Migration:** Successfully removed hardcoded API credentials from the codebase and established a professional environment tracking pipeline using `python-dotenv`.
* **Architecture:** Implemented a continuous terminal polling loop using streaming system instructions via the Gemini SDK.
* **Core Stack:** Python 3.12, LangChain Ecosystem, python-dotenv, Google Gemini API (Free Developer Tier).

### 🛠️ Milestone 2: Automated Actions (Phase 2 - Next Up)
* **Status:** In Design ⏳
* **Target:** Deploying a self-hosted `n8n` automation framework via local Docker containers. This will provide the LLM brain with execution tools to interact with real-world web APIs securely without cloud hosting costs.

---

## ⚙️ Local Sandbox Deployment

1. **Clone the Workspace:**
```bash
   git clone [https://github.com/TEJASf8/F.R.I.D.A.Y.-AI-Assistant.git](https://github.com/TEJASf8/F.R.I.D.A.Y.-AI-Assistant.git)
   cd F.R.I.D.A.Y.-AI-Assistant
