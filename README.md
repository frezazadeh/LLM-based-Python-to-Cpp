# ⚡ Python to C++ High-Performance Code Converter

A web-based tool that converts **Python code** into **high-performance C++** using LLMs (GPT-4o / Claude 3.5). It also lets you **run and compare outputs** of both Python and the optimized C++ implementation.

## 🚀 Features

- Convert Python functions to optimized, low-latency C++.
- Support for **OpenAI GPT-4o** and **Anthropic Claude 3.5 Sonnet** models.
- Live **code execution** and **output comparison** for both Python and C++.
- Built-in web interface powered by **Gradio**.
- Auto-generates `optimized.cpp` and compiles using Clang with performance flags.
- Stylish, modern UI with clean execution results.

---

## 📸 Demo

> Coming soon...

---

## 🧠 Technologies Used

- [Gradio](https://gradio.app/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Anthropic Python SDK](https://docs.anthropic.com/claude/docs/quickstart)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- C++17 + Clang (via subprocess)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-to-cpp-ai.git
cd python-to-cpp-ai

