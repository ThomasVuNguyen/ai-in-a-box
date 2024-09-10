import ollama

def ask_test():
    stream = ollama.chat(
        model='phi3',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def ask(query):
    stream = ollama.chat(
        model='phi3',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)