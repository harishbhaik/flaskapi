from flask import Flask

app =Flask(__name__)


@app.route("/home",methods=['GET'])

def home():
    return "<h1> Welcome.......<h1>"



if __name__ =="__main__":
    app.run(port=3500,host='0.0.0.0')