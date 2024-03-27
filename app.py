from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template('home.html', story=story)

@app.route('/story')
def show_story():
    new_story = story.generate(request.args)
    return render_template('story.html', story=new_story)
