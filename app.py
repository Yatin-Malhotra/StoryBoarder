from flask import Flask, render_template, request, url_for
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

        image_src = url_for('static', filename='collage.png')
        
        video_path = 'static'
        video_file = 'my_video.mp4'
        full_path = video_path + video_file

        return render_template("index.html", message = script, image_src = image_src, vide_url = full_path)
    else:
        return render_template("index.html")












if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=81)
