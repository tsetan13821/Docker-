from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <form action='/greet' method='post'>
                Enter your name: <input type='text' name='name'>
            <input type='submit' value='Submit'>
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello,{name}, Welcome to this docker demo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)