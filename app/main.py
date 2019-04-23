from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/clickme")
def clickme():
    return render_template("clickme.html")

@app.route("/")
def flash(message):
  return render_template('flash.html')

@app.route('/mylink/')
def my_link():
  print 'I got clicked!'

  return 'Click.'

@app.route('/clickfunction/')
def click_function():
  print 'I clicked!'

  return 'Click-function.'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')