from flask import Blueprint, render_template, send_from_directory, Response, current_app
import json
import os

routes = Blueprint("routes", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data():
    path = os.path.join(BASE_DIR, "blogs.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


@routes.route("/sitemap")
def sitemap_page():
    return render_template("sitemap.html")

STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")


@routes.route("/robots.txt")
def robots():
    return send_from_directory(STATIC_DIR, "robots.txt")


@routes.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(STATIC_DIR, "sitemap.xml")

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
