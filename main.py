from flask import Flask, request, render_template
from scrap_google import get_links


app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_with_google', methods=['post'])
def get_searching_term():
    search_term = request.form['search_term']

    links = get_links(search_term)
    return render_template('index.html', links=links)

if __name__ == '__main__':
    # Run the app on the specified port
    app.run(host='0.0.0.0', port=port)
