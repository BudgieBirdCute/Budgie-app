from flask import *

app = Flask(__name__)

@app.route('/<name>')
def main(name='bill'):
    return render_template('hollow_bones.html', name=name)

@app.route('/other1')
@app.route('/other2')
@app.route('/other3')
def example():
    return render_template('other_bones.html')

if __name__ == '__main__':
    app.run(debug=True)
    