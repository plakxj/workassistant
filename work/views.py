
from flask import flash,redirect,url_for,render_template
from work import app,db
from work.forms import RecordForm,EditForm,DeleteForm
from work.models import Note

import click

@app.route("/recordform",methods=["GET","POST"])
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
    return render_template("recordform.html",form=form)


@app.route("/showform",methods=["GET"])
def showform():
    form = DeleteForm()
    notes = Note.query.all()
    return render_template("showform.html", notes=notes, form=form)


@app.route("/delete/<note_id>",methods=["POST"])
def deleteform(note_id):
    form = DeleteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        flash("当前笔记已删除")
    else:
        abort(400)
    return redirect(url_for("showform"))


@app.route("/editform/<note_id>",methods=["GET","POST"])
def editform(note_id):
    form = EditForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.subject = form.subject.data
        note.keyword1 = form.keyword1.data
        note.keyword2 = form.keyword2.data
        note.text = form.text.data
        db.session.commit()
        flash("笔记已更新")
        redirect(url_for("showform"))
    form.subject.data = note.subject
    form.keyword1.date = note.keyword1
    form.keyword2.data = note.keyword2
    form.text.data = note.text
    return render_template("editform.html",form=form)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.') 
def initdb(drop): 
    """Initialize the database.""" 
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')
