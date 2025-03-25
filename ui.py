# ui.py
import gradio as gr
from conversion import optimize
from execution import execute_python, execute_cpp

# CSS styling for a modern look
css = """
body {background-color: #f4f4f9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px;}
.gradio-container {border: 2px solid #444; border-radius: 10px; padding: 20px; background-color: #ffffff;}
h2 {color: #333;}
.gr-button {background-color: #0066cc; color: #fff; border: none; padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; border-radius: 5px;}
.gr-button:hover {background-color: #005bb5;}
.gr-input {border: 1px solid #ccc; padding: 10px; border-radius: 5px;}

/* Styles for Conversion tab */
.python {background-color: #2d89ef; color: #fff; padding: 10px; font-family: 'Courier New'; border-radius: 5px;}
.cpp {background-color: #28a745; color: #fff; padding: 10px; font-family: 'Courier New'; border-radius: 5px;}

/* Styles for Execution tab */
.execution-python {
    background-color: #282c34;
    color: #61dafb;
    padding: 10px;
    font-family: 'Courier New';
    border-radius: 5px;
    border: 1px solid #61dafb;
}
.execution-cpp {
    background-color: #1e1e1e;
    color: #c5e1a5;
    padding: 10px;
    font-family: 'Courier New';
    border-radius: 5px;
    border: 1px solid #c5e1a5;
}
"""

# Example Python code (can be modified by the user)
python_code_example = '''def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 10
for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")
'''

def launch_ui():
    with gr.Blocks(css=css) as ui:
        gr.Markdown("## Advanced Code Converter: Python to C++")
        with gr.Tabs():
            with gr.TabItem("Conversion"):
                with gr.Row():
                    python_input = gr.Textbox(label="Python Code", value=python_code_example, lines=10, elem_classes=["gr-input"])
                    cpp_output = gr.Textbox(label="C++ Code", lines=10, elem_classes=["gr-input"])
                with gr.Row():
                    model = gr.Dropdown(["GPT", "Claude"], label="Select Model", value="GPT", elem_classes=["gr-input"])
                with gr.Row():
                    convert_button = gr.Button("Convert Code", elem_classes=["gr-button"])
            with gr.TabItem("Execution"):
                with gr.Row():
                    python_run_button = gr.Button("Run Python", elem_classes=["gr-button"])
                    cpp_run_button = gr.Button("Run C++", elem_classes=["gr-button"])
                with gr.Row():
                    python_result = gr.TextArea(label="Python Output", elem_classes=["execution-python"], lines=8)
                    cpp_result = gr.TextArea(label="C++ Output", elem_classes=["execution-cpp"], lines=8)
        convert_button.click(optimize, inputs=[python_input, model], outputs=[cpp_output])
        python_run_button.click(execute_python, inputs=[python_input], outputs=[python_result])
        cpp_run_button.click(execute_cpp, inputs=[cpp_output], outputs=[cpp_result])
    return ui
