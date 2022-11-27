from flask import render_template, request
from modules import cfg_to_cnf, table_filling_cyk

def configure_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")
    @app.route("/aplikasi", methods=["GET", "POST"])
    def aplikasi():
        if (request.method == "POST"):
            string = request.form["string"]
            isSubmit = True
            isAccepted = table_filling_cyk.is_accepted(string)
            convert = cfg_to_cnf.get_set_of_production()
            table = table_filling_cyk.get_triangular_table()
            lenString = len(string)
            templateData = {
                "isSubmit": isSubmit,
                "isAccepted": isAccepted,
                "string": string,
                "convert": convert,
                "table": table,
                "lenString": lenString
            }
            return render_template("app.html", **templateData)
        else:
            return render_template("app.html")
