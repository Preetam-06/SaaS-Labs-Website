from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/about")
def about():
    return render_template("about.html")


@routes.route("/services")
def services():
    return render_template("services.html")


@routes.route("/blogs")
def blogs():
    return render_template("blogs.html")


@routes.route("/faqs")
def faqs():
    return render_template("Faqs.html")