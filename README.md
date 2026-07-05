# DeepDive AI - Agentic Research Assistant

[![GitHub Stars](https://img.shields.io/github/stars/mhasan2050/deepdive-ai?style=social)](https://github.com/mhasan2050/deepdive-ai)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-4B8BBE)

An open-source **multi-agent AI research system** that autonomously researches any topic and delivers high-quality, well-cited reports.

## ✨ Features
- Multi-agent workflow (Planner → Researcher → Writer → Critic)
- Real-time web search & content scraping
- Self-critique and quality improvement
- Structured Markdown reports with citations
- Easy-to-use web interface

## 🚀 Live Demo
https://huggingface.co/spaces/ditux/DeepDive-AI

## Tech Stack
- **LangGraph** + LangChain (for agent orchestration)
- Tavily (web search)
- Streamlit (UI)
- Support for Grok, Llama 3.1, Claude, OpenAI, etc.

## Quick Start

```bash
git clone https://github.com/mhasan2050/deepdive-ai.git
cd deepdive-ai
pip install -r requirements.txt

# Create .env file with your API keys
cp .env.example .env
