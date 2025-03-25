# execution.py
import io
import sys
import subprocess
from conversion import write_output  # Reuse write_output from conversion.py

def execute_python(code):
    namespace = {}
    output = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output
    try:
        exec(code, namespace)
    finally:
        sys.stdout = old_stdout
    return output.getvalue()

def execute_cpp(code):
    write_output(code)
    try:
        compile_cmd = ["clang++", "-Ofast", "-std=c++17", "-march=native", "-o", "optimized", "optimized.cpp"]
        subprocess.run(compile_cmd, check=True, text=True, capture_output=True)
        run_cmd = ["./optimized"]
        result = subprocess.run(run_cmd, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred:\n{e.stderr}"
