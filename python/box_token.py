#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 必要なモジュールのインポート
import requests

# トークン取得用のクラスを定義
class GetToken:

    def __init__(self):
        # 変数の初期化
        self.code = ""

    # トークン取得用の関数get_token()を定義
    def get_token(self, token_url, code, client_id, client_secret):

        # POSTリクエスト用のヘッダとペイロードを定義
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        payload = "client_id="+client_id+\
                  "&client_secret="+client_secret+\
                  "&code="+code+"&grant_type=authorization_code"

        # POSTを実行
        post_response = requests.request("POST", token_url, data=payload, headers=headers)

        # POSTの実行結果(Json形式)をパースして、トークンを抽出
        post_response = post_response.json()
        access_token = post_response["access_token"]
        refresh_token = post_response["refresh_token"]

        # 実行結果としてAccess TokenとRefresh Tokenを返す
        return access_token, refresh_token
