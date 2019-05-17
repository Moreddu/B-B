"""from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
"""

from controllers.auth import GoogleLogin
from data_access.commentiDA import insertCommento, getAllCommenti
from flask import *
app = Flask(__name__)

googler = GoogleLogin()


@app.route('/')
def index():
    comments = getAllCommenti()
    return render_template('index.html', comments=comments)


@app.route('/submitComment', methods=['POST'])
def submitComment():
        if "first_step" not in session:
            form = request.form
            session['message'] = form['testo']
            return redirect(googler.step1())
        else:
            try:
                userinfo = googler.userinfo()
                result = insertCommento(session['message'], userinfo)
                session.clear()
                flash(result)
            except Exception as e:
                session.clear()
                flash("Commento non inserito!")

            return redirect(url_for('main.index'))


@app.route('/authorization')
def google_authorized():
    googler.step2()
    return redirect(url_for('submitComment'))


#####################################################
#                   ADMIN SIDE                      #
#####################################################


@app.route('/admin')
def admin():
    return render_template('admin/admin_index.html', admin=True)


@app.route('/admin/new')
def nuova_stanza():
    if request.method == 'GET':
        return render_template('admin/new_stanza.html', admin=True)
    else:
        return redirect(url_for('admin'))


@app.route('/admin/edit')
def edit_stanza():
    return redirect(url_for('admin'))


@app.route('/admin/remove')
def remove_stanza():
    return redirect(url_for('admin'))


@app.route('/admin/removeAll')
def remove_all():
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run()