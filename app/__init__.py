from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import linecache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Language(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    change = db.Column(db.String)

    def __init__(self, change):
        self.change = change


db.create_all()
a = '1'
b = Language(a)
db.session.add(b)
db.session.commit()


@app.route('/')
def index():
    lc = Language.query.filter_by(id=1).first()

    if lc.change == '1':
        lang = 'app/static/languages/ptBR.lang'
    elif lc.change == '2':
        lang = 'app/static/languages/enUS.lang'

    title = linecache.getline(lang, 1)
    maintitle = linecache.getline(lang, 2)
    maincont = linecache.getline(lang, 3)
    option = linecache.getline(lang, 4)
    btnlang = linecache.getline(lang, 5)
    maintitle2 = linecache.getline(lang, 6)
    maincont2 = linecache.getline(lang, 7)

    return render_template('index.html', title=title, maintitle=maintitle,
                           maincont=maincont, option=option, btnlang=btnlang,
                           maintitle2=maintitle2, maincont2=maincont2)


@app.route('/lang', methods=['POST'])
def lang():
    c = Language.query.filter_by(id=1).first()
    lc = request.form.get('choice')

    if lc in ['1', '2']:
        c.change = lc
        db.session.commit()

    return redirect(url_for('index'))
