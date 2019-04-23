from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route('/background_process_test')
def background_process_test():
    print "Hello"
    return "nothing"

@app.route("/clickme")
def clickme():
    return render_template("clickme.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')