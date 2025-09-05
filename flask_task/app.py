from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            return "User  already exists", 400
        user = User(email=form.email.data, password=form.password.data) 
        db.session.add(user)
        db.session.commit()
        return "User  registered successfully"
    return render_template('register.html', form=form)

@app.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    job = Job(title=title, description=description)
    db.session.add(job)
    db.session.commit()

    return jsonify({'id': job.id, 'title': job.title, 'description': job.description}), 201
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    jobs_list = [{'id': job.id, 'title': job.title, 'description': job.description} for job in jobs]
    return jsonify(jobs_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)