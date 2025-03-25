![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4o-orange.svg)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg)
![Static Badge](https://img.shields.io/badge/Claude3.5.svg)



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

## 🧠 Technologies Used

- [Gradio](https://gradio.app/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Anthropic Python SDK](https://docs.anthropic.com/claude/docs/quickstart)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- C++17 + Clang (via subprocess)

---

# 🛠️ Setup Instructions

## 1. Clone the Repository

Run the following commands in your terminal:

```bash
git clone https://github.com/frezazadeh/LLM-based-Python-to-Cpp.git
cd python-to-cpp-ai
pip install -r requirements.txt
```

## 2. Create a .env File and Add API Keys

Create a file named `.env` in the project root and add the following content:

```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_claude_api_key
```

## 3. Run the App

Run the application with:

```bash
python3 main.py
```







