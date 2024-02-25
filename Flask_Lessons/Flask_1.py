# Import flask module
from flask import Flask

# Flask constructor takes name of current module
# (__name__) as argument
app = Flask (__name__)


# route() function of Flask class is a decorator,
# that tells app which URL should call the associated
# function.

@app.route("/")                     # Home Page
def home():                         # Returns a blank page with an <h1> elem.
    return "<h1>Home Page</h1>"

@app.route("/about")                # About page
def about():                        # Returns a blank page wiht an <h1> elem.
    return "<h1>About Page</h1>"



# main driver function
if __name__ == "__main__":

    # Run app through port 5000 on local dev. server
    app.run(debug = True)