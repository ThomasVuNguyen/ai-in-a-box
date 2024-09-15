from flask import Flask, Response, stream_with_context, request
from bot import bot
from knowledge_hub import knowledge
import time
app = Flask(__name__)

@app.route("/")
def hello_world():
    information = knowledge.query()
    
    def generate():
        for chunk in bot.ask(f'from the given information: {information}, who likes robotics?'):
            yield chunk
            print(chunk)

    return Response(stream_with_context(generate()), mimetype='text/plain')

@app.route('/stream')
def streamed_response():
    print('howdy')
    def generate():
        yield 'Hello'
        time.sleep(1)
        yield 'buddy'
        time.sleep(5)
        yield '!'
    return app.response_class(stream_with_context(generate()))