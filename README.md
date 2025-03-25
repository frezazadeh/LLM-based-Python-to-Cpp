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

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/frezazadeh/LLM-based-Python-to-Cpp.git
cd python-to-cpp-ai

```bash
### 2. Create a .env file and add API keys
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_claude_api_key

```bash
### 3. Run the App
python3 main.py


2. Install Dependencies

We recommend using a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Create a .env File and Add API Keys

In the root directory, create a .env file and include the following lines with your actual API keys:

OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_claude_api_key

4. Run the App

python3 main.py


