#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

class GetToken:

    def __init__(self):
        # 変数の初期化と定義
        self.code = ""
        self.url = "https://api.box.com/oauth2/token"
        self.client_id = "アプリのClient_IDを指定"
        self.client_secret = "アプリのSecretを指定"

    def get_token(self, code):

        # POSTリクエスト用のヘッダとペイロードを定義
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        payload = "client_id="+self.client_id+\
                  "&client_secret="+self.client_secret+\
                  "&code="+code+"&grant_type=authorization_code"

        # POSTを実行
        post_response = requests.request("POST", self.url, data=payload, headers=headers)

        # POSTの実行結果をパースし、トークンを抽出
        post_response = post_response.json()
        access_token = post_response["access_token"]
        refresh_token = post_response["refresh_token"]

        # 実行結果としてAccess TokenとRefresh Tokenを返す
        return access_token, refresh_token
