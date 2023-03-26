from flask import Flask, render_template, request
from custom_story import Custom_Script
from divider import divide_script

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        style = request.form["style"]
        storyboard = int(request.form["storyboard"])
        genre = request.form["genre"]
        descp = request.form["descp"]

        script = Custom_Script(descp, genre)
        divide_script(script, storyboard, style)

        return render_template("index.html", message = script, url = "../collage.jpg")
    else:
        return render_template("index.html")

@app.route('/index', methods=['POST', 'GET'])
def process_input():
    if request.method == "POST":
        style = request.form["style"]
        storyboard = int(request.form["storyboard"])
        genre = request.form["genre"]
        descp = request.form["descp"]

        script = Custom_Script(descp, genre)
        divide_script(script, storyboard, style)

        return render_template("index.html", message = script, url = "collage.jpg")
    else:
        return render_template("index.html")









if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=81)