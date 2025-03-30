from flask import Flask, render_template

app = Flask("магазин RR",
            template_folder="",
            static_folder="")

@app.route('/')
def  index():
    return render_template("index.html")

app.run(debug=True)

