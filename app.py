from flask import Flask, request, render_template
from stories import Story, all_stories, complete_stories

app = Flask(__name__)

@app.route('/home')
def select_story():
    """Takes the list all_stories, which contains the title of each story and
    generates a drop down menu containing each title as an option."""
    return render_template("select.html", all_stories = all_stories)

@app.route('/form')
def fill_story():
    """Compares the title of the story instance against all stories and sets the
    variable story to that instance (if it matches). Afterwards, Python uses 
    render_template along with story.prompts to generate the full form page."""
    cover = request.args.get('title')
    for st in complete_stories:
        if st.title == cover:
            story = st
    return render_template("fill.html", prompts=story.prompts)

@app.route('/story')
def show_story():
    """Converts request.args.keys() into a string and runs a for loop on
    complete_stories to create another string. If both strings match, then
    tale is set to that story, which allows Python to pull from that instance
    and generate the story"""
    story_stuff = request.args.keys()
    test_str1 = f'{story_stuff}'
    for s in complete_stories:
        test_str2 = f'dict_keys({s.prompts})'
        if test_str2 == test_str1:
            tale = s
    text = tale.generate(request.args)
    return render_template("story.html", text=text)