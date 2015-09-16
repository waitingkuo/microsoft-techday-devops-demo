from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    x = request.args.get('x')
    y = request.args.get('y')

    try:
        result = add(int(x) , int(y))
    except ValueError:
        result = ''
    
    return '''
<body>
    <form action="/" method="get">

        <input name="x" type="text"> + <input name="y" type="text"> = %s
        <br>
        <input type="submit" value="submit">
    </form>
</body>
''' % result


def add(x, y):
    return x+y

if __name__ == '__main__':
    app.run(debug=True)
