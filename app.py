from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index", methods=["GET", "POST"])
def translate():
    translated_text = ""
    target_language = "default" 
    if request.method == "POST":
        text = request.form.get("text")
        target_language = request.form.get("language")
        if text and target_language:
            try:
                translated_text = GoogleTranslator(target=target_language).translate(text)
            except Exception as e:
                translated_text = f"Error: {str(e)}"
    return render_template("index.html", translated_text=translated_text, target_language=target_language)

@app.route("/about",methods = ["GET","POST"])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)

    app.run(debug=True)
