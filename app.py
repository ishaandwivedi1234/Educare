from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tasks(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/spotify', methods=['GET', 'POST'])
def spotify():
    return render_template('spotify.html')

@app.route('/pomodoro', methods=['GET', 'POST'])
def pomodoro():
    return render_template('pomodoro.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        task = Tasks(title=title, desc=desc)
        db.session.add(task)
        db.session.commit()
    allTasks = Tasks.query.all()
    return render_template('todo.html', allTasks = allTasks)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        task = Tasks.query.filter_by(sno = sno).first()
        task.title = title
        task.desc = desc
        db.session.add(task)
        db.session.commit()
        return redirect('/todo')

    task = Tasks.query.filter_by(sno = sno).first()
    return render_template('update.html', task = task)

@app.route('/delete/<int:sno>')
def delete(sno):
    task = Tasks.query.filter_by(sno = sno).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/todo')

if __name__ == "__main__":
    app.run(debug=True)