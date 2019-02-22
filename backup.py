
from flask import Flask, flash, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return """hallo. error.<a href="/">eten</a><a href="/">terug</a>"""

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'loser' and request.form['username'] == 'lolbroek':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return hello_world()


@app.route('/hello_world')
def hello_world():
    return """
dit is mijn restaurant programma  <a href="/hello">hello</a>
<p><a href="https://spacegamer360.pythonanywhere.com">naar de website van mijn broertje</a>
<p><a href="/inlogpagina">Naar de inlogpagina!</a>
<p><a href="https://www.youtube.com/watch?v=eRlKUj0c5sY">liedje</a>
<p><img src="/static/PA310085.JP
G">
<font face="verdana" color="red">hallo dit is leuk!</font>
"""

@app.route('/hello')
def hello_world2():
    return """dit is het eten dat ik leuk vind om te maken <a href="/">eten</a><a href="/eten">eten</a>
    <select>
  <option value="volvo">wereld</option>
  <option value="saab">radio</option>
  <option value="opel">reclame</option>
  <option value="audi">de dood</option>
  <option value="audi">lol</option>
  <option value="audi">mickey mouse</option>
  <option value="audi">een groooooooote zin is erg grappig</option>
  <option value="audi">de grap</option>
  <option value="audi">de moeder</option>
  <option value="audi">je kont</option>
  <option value="audi">een laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaange en rare zin</option>
</select>
"""

@app.route('/eten')
def hello_world3():
    return """
het is macaroni met kaas <a href="/hello">eten</a>
<p><img src="/static/PA310085.JPG">
<form action="/action_page.php" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="Submit">
</form>
"""

@app.route('/inlogpagina')
def inlogpagina():
    return """
<h1>Welkom op de inlogpagina van de site van mij!:-)</h1>

<form action="/inloggen" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="Submit">
</form>

"""

@app.route('/inloggen')
def inloggen():
    return """
<h1>Welkom {}: Je bent ingelogd op de site van mij!:-)</h1>


"""

@app.route('/ik')
def hello_world10():
    return """
hallo <a href="/">logged_in</a><a href="/eten">ik</a>
"""
#        .format(request.args.get('fname'))
