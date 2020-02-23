from flask import Flask, render_template
import data
from data import tours

app = Flask(__name__)

@app.route('/')
def main():
    new_tours = {}
    for key, value in tours.items():
        if key <= 6:
            new_tours[key] = value
    return render_template('index.html', tours = new_tours)

@app.route('/departure/<depart>/')
def render_departure(depart):
    sametours = {}
    price = []
    nights = []
    for i in tours:
        for key, value in tours[i].items():
            if value == depart:
                sametours[i] = tours[i]
    for p in sametours:
        prc = sametours[p].get('price')
        price.append(prc)
    for n in sametours:
        night = sametours[n].get('nights')
        nights.append(night)
    city = sametours[next(iter(sametours))]
    return render_template('departure.html', tours = sametours, price=price, nights=nights, city=city)

@app.route('/tour/<id>/')
def render_tour(id):
    tour = tours.get(int(id))
    return render_template('tour.html', tour = tour)

if __name__ == '__main__':
    app.run()