import json
import os

from flask import Flask, render_template
from backend.routes import routes


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../templates"),
    static_folder=os.path.join(BASE_DIR, "../static")
)


app.register_blueprint(routes)


def load_data():
    json_path = os.path.join(BASE_DIR, "blogs.json")

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)



@app.route("/blogs/<int:blog_id>")
def blog_details(blog_id):

    data = load_data()

    for blog in data["blogs"]:
        if blog["id"] == blog_id:
            return render_template(
                "blogs_details.html",
                blog=blog
            )

    return "Blog not found", 404



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )