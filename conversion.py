# conversion.py
from config import openai, claude, OPENAI_MODEL, CLAUDE_MODEL, system_message

def user_prompt_for(python_code):
    prompt = (
        "Rewrite this Python code in C++ with the fastest possible implementation that produces identical output in the least time. "
        "Respond only with C++ code; do not explain your work other than a few comments. "
        "Pay attention to number types to ensure no int overflows. Remember to #include all necessary C++ packages such as iomanip.\n\n"
        + python_code
    )
    return prompt

def messages_for(python_code):
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt_for(python_code)}
    ]

def write_output(cpp_code, filename="optimized.cpp"):
    code = cpp_code.replace("```cpp", "").replace("```", "")
    with open(filename, "w") as f:
        f.write(code)

def stream_gpt(python_code):
    stream = openai.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages_for(python_code),
        stream=True
    )
    reply = ""
    for chunk in stream:
        fragment = chunk.choices[0].delta.content or ""
        reply += fragment
        yield reply.replace("```cpp\n", "").replace("```", "")

import time
import anthropic

def stream_claude(python_code):
    retry_attempts = 3
    delay = 2  # seconds
    for attempt in range(retry_attempts):
        try:
            result = claude.messages.stream(
                model=CLAUDE_MODEL,
                max_tokens=2000,
                system=system_message,
                messages=[{"role": "user", "content": user_prompt_for(python_code)}],
            )
            reply = ""
            with result as stream:
                for text in stream.text_stream:
                    reply += text
                    yield reply.replace("```cpp\n", "").replace("```", "")
            return  # exit if successful
        except anthropic.APIStatusError as e:
            if "overloaded" in str(e).lower():
                time.sleep(delay)
                delay *= 2  # exponential backoff
            else:
                yield f"Error: {e}"
                return
    yield "Anthropic API is overloaded. Please try again later."

def optimize(python_code, model):
    if model == "GPT":
        generator = stream_gpt(python_code)
    elif model == "Claude":
        generator = stream_claude(python_code)
    else:
        raise ValueError("Unknown model")
    final_output = ""
    for partial in generator:
        final_output = partial
    write_output(final_output)
    return final_output
