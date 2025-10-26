from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    username = request.form['uname']
    password = request.form['password']
    return render_template('greeting.html', username=uname, password=password)
if __name__ == '__main__':
    app.run(debug=True)
