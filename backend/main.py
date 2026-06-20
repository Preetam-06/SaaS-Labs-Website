import json
from flask import Flask, render_template
from routes import routes

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)
app.register_blueprint(routes)

def load_data():
    with open("C:/Users/Priyanka/Documents/Project/backend/blogs.json", "r") as f:
        return json.load(f)


@app.route("/blogs.html")
def home():
    data = load_data()
    return render_template("blogs.html", blogs=data["blogs"])

@app.route("/blogs/<int:blog_id>")
def blog_details(blog_id):
    data = load_data()
    for blog in data["blogs"]:
        if blog["id"] == blog_id:
            return render_template("blogs_details.html", blog=blog)
        else:
            return "Blog not found", 404

if __name__ == "__main__":
    app.run(debug=True)