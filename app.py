from flask import Flask,render_template, request,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = 'students'

mysql =MySQL(app)

@app.route('/index',methods=['GET'])
def index():
    cur=mysql.connection.cursor()
    index=cur.execute("SELECT * FROM students")
    if index>0:
        data=cur.featchall()
    return render_template('index.html',data=data)


@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(id, name, age, city) VALUES (?,?,?,?)", (id, name, age, city))
        mysql.connection.commit() 
        cur.close()
    return render_template("index.html")

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

