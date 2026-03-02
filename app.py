from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

from tasks.routes import tasks_bp
app.register_blueprint(tasks_bp)


@app.route('/')
def index():
    return 'This is the home page'


@app.errorhandler(404)
def not_found(error):
    return render_template(
        'error.html',
        message='The page you are looking for does not exist.'
    ), 404


@app.errorhandler(500)
def server_error(error):
    return render_template(
        'error.html',
        message='An unexpected error occurred. Please try again later.'
    ), 500


if __name__ == '__main__':
    app.run(debug=True)