# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect, request
import box_token

redirect_url = "http%3a%2f%2flocalhost%3a5000%2foauth"  # http://localhost:5000/oauth をURLエンコードしたもの
client_id = "アプリのClient_IDを指定"
client_secret = "アプリのSecretを指定"

app = Flask(__name__)

# /authenticateへGETリクエストが来たらaccount.box.comのOAuth用URLにリダイレクト
@app.route("/authenticate")
def box_oath():
    return redirect("https://account.box.com/api/oauth2/authorize?response_type=code&client_id=" +
                    client_id + "&redirect_uri=" + redirect_url + "&state=" + client_secret)


# ユーザがアプリケーションを承認後、リダイレクトされてくる通信を/oauthのパスで待ち受ける
@app.route("/oauth")
def get_code():
    # リダイレクトURLに含まれる「code=XXXXX」部分を抜き取る
    code = request.args.get('code')

    # トークン取得用のモジュール「box_token」のGetTokenクラスをインスタンス化
    gt = box_token.GetToken()

    # get_token関数にcodeを渡して実行し、トークンを取得する
    token = gt.get_token(code)

    # トークンをブラウザに返して終了
    return "Access_Token : " + token[0] + "Refresh Token : " + token[1]

if __name__ == "__main__":
    app.run()

