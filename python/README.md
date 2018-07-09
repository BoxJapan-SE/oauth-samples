Box OAuth実装 with Python

# 前提条件

## Python3

本アプリを実行するPython環境がVersion3系統であることを確認してください。  

例  
```
$ python --version
Python 3.6.4
         ↑
表示されたバージョンが3.xであること
```

## Webアプリケーションフレームワーク"flask"

Python環境にWebアプリケーション用のフレームワーク"flask"をインストールしてください。  

コマンド  
$ pip3 install flask

例  
```
$ pip3 install flask
(中略)
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-1.0.2 itsdangerous-0.24

flaskをインポートできるか確認

$ python3
>>> import flask
>>>
    ↑エラーが出なければ正しくインストール完了しています

```
