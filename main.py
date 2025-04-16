import flask
from calculate import calculates, DrawGraph, get_suggestions

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', user="Rüzgar")

@app.route('/calculate')
def calculatePage():
    return flask.render_template('calculate.html')

@app.route('/from_create', methods=['POST'])
def forForm():
    try:
        todaylyWater = int(flask.request.form.get("water_usage", 0))  # Default 0 alıyoruz
        PersonCount = int(flask.request.form.get("family_members", 1))  # Default 1 alıyoruz
        DaysCount = int(flask.request.form.get("days", 1))  # Default 1 alıyoruz
    except ValueError:
        return flask.render_template('error.html', message="Lütfen geçerli sayısal değerler giriniz.")
    result = calculates(todaylyWater, PersonCount, DaysCount)
    DrawGraph(todaylyWater, PersonCount, DaysCount)
    return flask.render_template('result.html', result=result)

@app.route('/suggestion', methods=['POST'])
def SuggestionPage():
    user_input = flask.request.form.get('user_message')
    suggestions = get_suggestions(user_input)
    return flask.render_template('suggestion.html', user_input=user_input, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)