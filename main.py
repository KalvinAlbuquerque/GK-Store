from flask import Flask, url_for, render_template

class Main():

    app = Flask(__name__)

    def __init__(self) -> None:
        pass

    @app.route('/')
    def index_page():
        return render_template('index.html')
    
catalog = Main()

catalog.app.run(debug = True)

