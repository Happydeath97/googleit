from flask import Flask, request, render_template
from scrap_google import get_links


app = Flask(__name__)


@app.route('/search')
def index():
    return render_template('index.html')


@app.route('/search_with_google', methods=['post'])
def get_searching_term():
    search_term = request.form['search_term']

    links = get_links(search_term)
    return render_template('index.html', links=links)