from MorseAlphabet import Interpreter
from flask import Flask, render_template, request
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Kek = Interpreter()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        inp_text = request.form["morse_input"]
        out_text = Kek.inter(text=inp_text)
        return render_template('index.html', out_text=out_text, inp_text=inp_text)
    return render_template('index.html')



if __name__ == "__main__":
    app.run()












