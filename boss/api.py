import leancloud
from util import page
import web

urls = ("/edit", "Edit",
        "/save", "Save",
        "/detail", "Detail",
        "/list", "List",
       )

app = web.application(urls, globals())
render = page.render("api-doc")

ApiDoc = leancloud.Object.extend('ApiDoc')

class Edit:
    @page.needLogin(True)
    @page.input("id?")
    def GET(self, _id):
        obj = ApiDoc.query.get(_id) if _id else ApiDoc()
        return render.edit(_id, obj)

class Save:
    @page.needLogin(True)
    @page.input("id?", "name", "module", "url", "method:restMethod", "input?", "content")
    def POST(self, _id, _name, _module, _url, _method, _input, _content):
        _input = _input.replace('"', '').replace("'", '').replace(",", " ")
        obj = ApiDoc.query.get(_id) if _id else ApiDoc()
        if not _id:
            obj.set("creatorId", web.ctx.userId)
            obj.set("creatorName", web.ctx.userName)
        obj.set("name", _name)
        obj.set("module", _module)
        obj.set("url", _url)
        obj.set("method", _method)
        obj.set("input", _input)
        obj.set("content", _content)
        obj.save()
        return {"code":0}

class Detail:
    @page.needLogin(True)
    @page.input("id")
    def GET(self, _id):
        obj = ApiDoc.query.get(_id)
        params = obj.get("input").split()
        inputList = [page.parseParam(x) for x in params]  #inputList => [(key, tipe, isMust)*]
        urlPrefix = web.cookies().get('mockUrlPrefix', 'https://lightyear.leanapp.cn')
        return render.detail(_id, obj, inputList, urlPrefix)

class List:
    @page.needLogin(True)
    def GET(self):
        lst = ApiDoc.query.ascending("module").find()
        return render.listall(lst)
