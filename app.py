from flask import Flask, jsonify, redirect, render_template, session, url_for
from static.python.restcountries_info import country_filter
from static.python.onthisday import get_fact
from static.python.wbdata_info import *
from static.python.get_news import get_news_articles

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', fact=get_fact())

@app.route('/getFact', methods=['GET'])
def get_fact_GET():
    return jsonify(get_fact())

@app.route('/covid19')
def covid19():
    return render_template('covid19.html', page=' - COVID-19')

@app.route('/404')
def page_not_found(message = 'Page not found'):
    return render_template('404.html', message = message, page=' - 404'), 404

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/<country>')
def get_country(country):
    restcountries_data = country_filter(country)
    if not restcountries_data:
        return redirect(url_for('page_not_found', message = 'Country not found'))

    #articles = get_news_articles(restcountries_data['altSpellings'][-1])
    #covid_info = get_country_covid_info(restcountries_data['altSpellings'][-1])

    return render_template('country.html', country = restcountries_data, page=f' - {restcountries_data["altSpellings"][-1]}')



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
