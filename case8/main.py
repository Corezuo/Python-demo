# Create by MAX_zuo on 2018/8/28

from flask import Flask

app = Flask(__name__)


@app.route("/api/token/user", methods=["GET"])
def user():
    # 获取token
    return "get ok"


@app.route("/api/token/verify", methods=["POST"])
def verify():
    # 验证token
    return "post ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=81)
