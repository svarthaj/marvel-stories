from flask import Blueprint, render_template, redirect, url_for, request

from ..services.stories import get_story_info

main = Blueprint("main", __name__)

@main.route('/')
def index():
    story_info = get_story_info()
    return render_template( "index.html",
                            hero_name=story_info['hero_name'],
                            story_name=story_info['title'],
                            story_description=story_info['description'],
                            characters=story_info['characters'],
                            attribution_text=story_info['attribution_text'])