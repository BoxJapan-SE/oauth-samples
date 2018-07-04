const express = require('express');
const app = express();
const axios = require('axios')
const qs = require('querystring');

//認証画面にリダイレクト
app.get('/authenticate', function (req, res) {
    res.redirect('https://account.box.com/api/oauth2/authorize?response_type=code&client_id={your client id}&redirect_uri=http://localhost:3000/oauth&state={your client secret}')
})

//認証後、Boxから認証コードが送られてきます。この認証コードを使ってBoxのアクセストークンと交換します。
//例：http://localhost:3000/oauth?state=zxxxxxxxxxxxxxxxxxxxxx&code=7c0UAdSqMlKWh7GcooMd4Fcm1W9E0Hvm
//URL中のCodeパラメーターが認証コードになります。
app.get('/oauth', function (req, res) {
    let code = req.query.code
    //認証コードパラメーターを使ってアクセストークンを発行します。
    //https://api.box.com/oauth/tokenにpostリクエストを送ります。
    axios.post('https://api.box.com/oauth2/token', qs.stringify({
        grant_type: 'authorization_code',
        code: code,
        client_id: 'Client ID値を入れてください',
        client_secret: 'Client Secret値を入れてください'
    })
    ).then(response => {
        //うまくリクエストが通れば画面にAccess TokentとRefresh Tokenが表示されているはずです。
        res.send(response.data)
    }).catch(function (error) {
        res.send(error);
    })
})

app.listen(3000, function () {
    console.log('Box OAuth Example app listening on port 3000!')
})

