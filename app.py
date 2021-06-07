from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__name__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')
