import leancloud
from leancloud import User
import time
from util import page
import web

urls = ("", "Setting")

app = web.application(urls, globals())
render = page.render("api-doc")

class Setting:
    def GET(self):
        urlPrefix = web.cookies().get('mockUrlPrefix', 'https://lightyear.leanapp.cn')
        return render.setting(urlPrefix)

    @page.input("prefix")
    def POST(self, _prefix):
        now = int(time.time())
        web.setcookie('mockUrlPrefix', _prefix.strip(), expires=now+86400*300, path='/')
        web.seeother('/api/list', '/')
        return {'status':0}


