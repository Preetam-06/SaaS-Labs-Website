from flask import Blueprint, render_template
from flask import send_from_directory

import json
import os


routes = Blueprint("routes", __name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data():

    path = os.path.join(BASE_DIR, "blogs.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/sitemap")
def sitemap_page():
    return render_template("sitemap.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory("static", "sitemap.xml")

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

    data = load_data()

    return render_template(
        "blogs.html",
        blogs=data["blogs"]
    )



@routes.route("/faqs")
def faqs():
    return render_template("Faqs.html")
