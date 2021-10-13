# server.py
# templates 폴더를 만들어서 covid_vaccine.html 넣기
from flask import Flask, redirect
import logging

logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)-7s] : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    )

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


@app.route("/강의자료")
def redirect_notion():
    return redirect("https://bolder-grade-b47.notion.site/f3181a3387004c13ba2551118046723a")


@app.route("/이메일")
def registry_email():
    return "calathea@naver.com"


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
