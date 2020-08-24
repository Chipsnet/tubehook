# Tubehook

YouTubeのURLを含むTwitter投稿をフックしてDiscord Webhookするためのアプリケーションです。

## How to use

以下のものを使用します

- IFTTT
- Discord Webhooks
- Heroku

### IFTTT


### Heroku

環境変数に各種設定をします

```
TWITTER_USER = "USERNAME"
DISCORD_URL = "DISCORD WEBHOOK URL"
TWITTER_API_KEY = "TWITTER API KEY"
TWITTER_API_SECRET = "TWITTER API SECRET"
TWITTER_ACCESS_KEY = "TWITTER ACCESS KEY"
TWITTER_ACCESS_SECRET = "TWITTER ACCESS KEY"
```


## ngrok (開発用)

開発用として、ngrokでの使用方法です。       
（基本的に本番環境では非推奨とします）

1. 環境変数などは上記と同じように設定します。
1. まずはサーバーを起動します。
    1. `pipenv install` を利用して、依存関係のインストールを行います。
    1. `pipenv run start` を実行して、サーバーを起動します。
1. ngrokのサーバーを起動します。
    1. `./ngrok.exe http 80` を実行すると、80番ポートのlistenを開始します。
1. ngrokのダッシュボードにあるURLに対しIFTTTからwebhookすると、ローカルサーバーにリクエストが届きます。