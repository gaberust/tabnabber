from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', dest=request.args.get('dest'))


if __name__ == '__main__':
    app.run()
