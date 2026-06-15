from flask import Flask, render_template,request, redirect

app = Flask(__name__, template_folder='templates')

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_roblox = request.form.get('button_roblox')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    email = request.form.get("email")
    text = request.form.get("text")
    return render_template('index.html', button_python=button_python,
                                        button_roblox=button_roblox,
                                        button_html=button_html,
                                        button_db=button_db,
                                        )


if __name__ == "__main__":
    app.run(debug=True)