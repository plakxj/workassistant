
from flask import flash,redirect,url_for,render_template
from work import app,db
from work.forms import RecordForm
from work.models import Note

import click

@app.route("/",methods=["GET","POST"])
def recordform():
    form = RecordForm()
    if form.validate_on_submit():
        subject = form.subject.data
        keyword1 = form.keyword1.data
        keyword2 = form.keyword2.data
        text = form.text.data
        text1 = Note(subject=subject,keyword1=keyword1,keyword2=keyword2,text=text)
        db.session.add(text1)
        db.session.commit()
        flash("you text is saved")
        redirect(url_for("showform"))
    return render_template("form.html",form=form)

@app.route("/showform",methods=["GET","POST"])
def showform():
    notes = Note.query.all()
    return render_template("showform.html",notes=notes)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.') 
def initdb(drop): 
    """Initialize the database.""" 
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')
