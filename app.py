from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import StoryList
from flask import make_response

app = Flask(__name__)
app.debug = False

app.config['SECRET_KEY'] = "secretz"
debug = DebugToolbarExtension(app)


@app.route('/')
def base():
    return render_template('choose_story.html', story_list=story_list.stories.values())


@app.route('/newstory')
def new_story():
    story_list.chosen = int(request.args.get('chosen_story'))
    return render_template("form.html", needed_prompts=story_list.get_chosen().prompts)


@app.route('/story')
def show_story():
    return render_template("story.html", story=story_list.get_chosen().generate(dict(request.args)))


story_list = StoryList()

# adding stories manually at runtime
story_list.add(
    'Once upon a time...',
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story_list.add(
    'I love...',
    ["plural_noun", "verb"],
    """I love to {verb} {plural_noun}."""
)
