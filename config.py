# config.py
import os
from dotenv import load_dotenv
import anthropic
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# Instantiate API clients
openai = OpenAI(api_key=openai_api_key)
claude = anthropic.Anthropic(api_key=anthropic_api_key)

# Model names
OPENAI_MODEL = "gpt-4o"
CLAUDE_MODEL = "claude-3-5-sonnet-20240620"

# System message
system_message = (
    "You are an assistant that reimplements Python code in high performance C++ for a Linux UBUNTU. "
    "Respond only with C++ code; use comments sparingly and do not provide any explanation other than occasional comments. "
    "The C++ response needs to produce an identical output in the fastest possible time."
)
