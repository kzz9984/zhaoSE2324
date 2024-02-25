from flask import Flask, render_template

app = Flask(__name__)

# Display a couple of sample blog posts
posts = [
    {
    'author': 'Gandalf the Grey',
    'title': 'The Balrog at the Bridge of Kazad-dum',
    'content': 'YOU SHALL NOT PASS!',
    'date_posted': '3019 of the 3rd age'
    },
    {
    'author': 'Elrond of Rivendell',
    'title': 'The Secret Council',
    'content': 'A beginner\'s guide on how to destroy the one ring.',
    'date_posted': '3018 of the 3rd age'
    },
]

@app.route("/")                             # Home Page
def home():
    # Rather than place all of the html in the 'return'
    # statement, you can render an entire html page stored
    # in the templates folder.
    # render_template will render the specified html file
    # Posts argument passes in posts data
    return render_template("home2.html", posts=posts)

@app.route("/about")
def about():
    # title parameter will set the tile for browser tab
    return render_template("about2.html", title = "About")


# Run server on local IP address on port 5000
if __name__ == "__main__":
    app.run(debug = True)