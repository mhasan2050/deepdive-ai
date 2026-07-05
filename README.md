# DeepDive AI - Open Source Multi-Agent Research Assistant

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/deepdive-ai)](https://github.com/yourusername/deepdive-ai)
[![Hugging Face Spaces](https://img.shields.io/badge/🚀-Live_Demo-blue)](https://huggingface.co/spaces/yourusername/deepdive-ai)

An autonomous AI research system that turns any question into a high-quality, cited research report.

## ✨ Features
- Multi-agent architecture (Planner → Researcher → Writer → Critic)
- Real-time web search + page scraping
- Self-critique and quality improvement loop
- Structured Markdown + PDF export
- Fully open source & locally runnable

## Live Demo
→ Try it here: [Hugging Face Space](link)

## Architecture
![Architecture](assets/architecture.png)

## Tech Stack
- LangGraph + LangChain
- Tavily Search
- Llama 3.1 / Grok / Claude
- Streamlit UI

## How to Run Locally
```bash
git clone https://github.com/yourusername/deepdive-ai
cd deepdive-ai
pip install -r requirements.txt
cp .env.example .env
streamlit run main.py
