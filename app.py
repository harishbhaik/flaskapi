from flask import Flask

app =Flask(__name__)




if __name__ =="__main__":
    app.run(port=3500,host='0.0.0.0')