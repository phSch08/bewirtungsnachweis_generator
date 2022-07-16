from flask import Flask, render_template, request, make_response
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import date
from generator import generate_pdf

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def index():
    return render_template('index.html',
        catering_date=date.today().isoformat(),
        catering_location_1 = 'Wiese hinter dem HPI Hauptgebäude',
        catering_location_2 = 'Prof.-Dr.-Helmert-Str. 2-3',
        catering_location_3 = '14482 Potsdam',
        catering_reason = "Friday Beers: Vernetzung der Studierenden",
        catering_kostenstelle = "14.9.000 Friday Beers",
        catering_expense = 158.55,
        catering_hosts = "",
        catering_guests = "",
        catering_type_restaurant = False,
        catering_type_other = True
    )

@app.route("/submit_form", methods=['GET'])
def submit_form():
    pdf = generate_pdf(
        date.fromisoformat(request.args.get("catering_date")).strftime("%d.%m.%y"),
        request.args.get("catering_location_1"),
        request.args.get("catering_location_2"),
        request.args.get("catering_location_3"),
        request.args.get("catering_reason"),
        request.args.get("catering_kostenstelle"),
        float(request.args.get("catering_expense")),
        int(request.args.get("catering_type")),
        request.args.get("catering_hosts").splitlines(),
        request.args.get("catering_guests").splitlines()
    )

    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename="Bewirtungsnachweis " + request.args.get("catering_date") + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response