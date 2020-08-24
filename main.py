import web
import json
import os
import tweepy
import requests

urls = ('/.*', 'hooks')
app = web.application(urls, globals())

auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_KEY"], os.environ["TWITTER_ACCESS_SECRET"])

api = tweepy.API(auth)

class hooks:
    def POST(self):
        data = web.data()
        data_json = json.loads(data, strict=False)
        print(data_json)

        content = data_json["content"]
        url = data_json["url"]
        
        if content.startswith('RT'):
            print('対象ツイートではありません', 'Reason: RTです。')
            return 'OK'

        twi_id = url.split('/')

        tweetstatus = api.get_status(twi_id[5])
        tweeturls = tweetstatus.entities["urls"]

        print(tweetstatus.entities["urls"])

        if not tweeturls:
            print('対象ツイートではありません', 'Reason: URLが含まれていません。')
        elif '告知' in content or '予告' in content or '今日' in content and '時' in content or 'この後' in content and '時' in content:
            print('キーワードが見つかりました')

            requestContent = {
                "content": url
            }

            requests.post(os.environ["DISCORD_URL"], requestContent)
        else:
            for u in tweeturls:
                print(u)
                if "youtube" in u["expanded_url"] or "youtu.be" in u["expanded_url"]:
                    print("YouTubeリンクが見つかりました")

                    requestContent = {
                        "content": url
                    }

                    requests.post(os.environ["DISCORD_URL"], requestContent)
                    break
        return 'OK'

if __name__ == '__main__':
    # pass
    app.run()