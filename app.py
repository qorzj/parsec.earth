from boss import people, api, setting
import json
import web
web.config.debug = False

urls = ('/', 'Home',
        '/api', api.app,
        '/login', people.Login,
        '/setting', setting.app,
       )

class Home:
    def GET(self):
        return "go parsec"


def resultWrapper(f):
    res = f()
    if isinstance(res, dict):
        web.header('Content-Type', 'application/json')
        return json.dumps(res)
    elif res is None:
        return ''
    else:
        return res


app = web.application(urls, globals())
app.add_processor(resultWrapper)

if __name__ == "__main__":
    app.run()
