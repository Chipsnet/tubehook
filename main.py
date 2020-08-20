import web
import json

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        data_json = json.loads(data, strict=False)
        print(data_json)
        content = data_json["content"]
        if 'http' in content:
            print('content detected.')
        return 'OK'

if __name__ == '__main__':
    app.run()