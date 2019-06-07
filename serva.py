from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def submit_info():
    print("submitted")
    name = request.form['your_name']
    location = request.form['Dojo_location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name = name, location=location, language = language, comment = comment)


if __name__=="__main__":
    app.run(debug=True)