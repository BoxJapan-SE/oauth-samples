簡単なBox Oauth実装

# 前提条件
Box Developer コンソールでアプリケーションの登録を予めすませておいてください。

#How to setup
1. このレポジトリをClone
2. 落としてきたフォルダに移動し、npm installを実行
3. app.jsの7行目中のClientIDとClient Secretの値をご自身のものと置き換えます
4. ClientID と Client Serect を16,17行に追加
5. Box Developerコンソールに行きリダイレクトURIにhttp://localhost:3000/oauth を入れます

## 使用方法
コマンドnode app.jsで起動します
http://localhost:3000/authenticateにブラウザで移動
うまく設定できていれば、Boxアプリの認証画面が出てきます。
boxアカウントの認証がうまく通ったなら、Access TokenとRefresh tokenが画面に表示されるはずです。

## 注意書き
app.jsファイルのURL中にClient IDとClient Secretを直接記述している理由は、実際に送信されるURLを理解していただくことが重要だと思い、直接記述しています。
百聞は一見にしかず
本番の実装では環境変数などで挿入することを推奨いたします。