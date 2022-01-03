from db import movies
from flask import Flask

web_app = Flask('web_app')


def render_index():
    html = []
    html.append('</br></br><ul>')
    for movie_name, movie in movies.items():
       html.append(render_movie_as_item_list(movie))
    html.append('</ul>')
    return ''.join(html)

def render_movie_as_item_list(movie):
    return f"<li><a href='movie/{movie['name']}'>{movie['name']}</a></li>"

def movie_view(movie_name):
    movie = movies.get(movie_name)
    html = []
    html.append("<ul>")
    html.append(f"<li>{movie['name']}</li>")
    html.append(f"<li>{movie['year']}</li>")
    html.append("</ul>")
    return ''.join(html)

@web_app.route("/movies")
def hello_world():
    return render_index()

web_app.add_url_rule('/movie/<movie_name>', view_func=movie_view, endpoint='movie')
web_app.run(use_reloader=True)

