from work.forms import RecordForm
from flask import flash,redirect,url_for,render_template
@app.route("/form")
def recordform():
    form = RecordForm()
    return render_template("form.html",form=form)