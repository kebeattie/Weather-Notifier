from flask import Flask, render_template, request
from Weather_Notif import *
from waitress import serve
app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/error')

def error():
    return render_template('error.html')

@app.route('/weather')

def weather():
    try:
        city = request.args.get("city").title()
        weather_data = getWeather(city)
        return render_template (
        "weather.html",
        title = city,
        cond = (weather_data["current"]["weather"][0]["description"]),
        temp = (weather_data["current"]["temp"]),

        )
    except:
        return render_template('/error.html')


if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = 8000)