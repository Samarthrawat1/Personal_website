from flask import Flask, render_template
from models import db, Project, Testimonial

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    projects = Project.query.all()
    testimonials = Testimonial.query.all()
    return render_template('home.html', projects=projects, testimonials=testimonials)

if __name__ == '__main__':
    app.run(debug=True)
