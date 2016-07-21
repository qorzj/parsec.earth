import leancloud
from leancloud import User
from util.param import checkInput, mapInput
import web


def lib(moduleName='pdb'):
    return __import__(moduleName)


def catch(func, alternative, errorType=Exception):
    try:
        return func()
    except errorType:
        return alternative


def render(path=''):
    "render('people').register(name='Jack')"
    return web.template.render('template/'+path, base='base')


def parseParam(keyTipe):
    if ':' in keyTipe:
        key, tipe = keyTipe.split(':')
        isMust, tipe = (False, tipe[:-1]) if tipe[-1] == '?' else (True, tipe)
    elif keyTipe[-1] == '?':
        key, tipe, isMust = keyTipe[:-1], 's', False
    else:
        key, tipe, isMust = keyTipe, 's', True
    return key, tipe, isMust


def needLogin(isRedirectOn=False):
    def f(g):
        def h(*a, **b):
            ck = web.cookies()
            tokenName = 'session'
            token = ck.get(tokenName, None) or web.input().get(tokenName, '!')
            try:
                user = User().become(token)
                web.ctx.userId = user.id
                web.ctx.userName = user.get("nickName")
                return g(*a, **b)
            except leancloud.errors.LeanCloudError as e:
                if isRedirectOn:
                    web.seeother("/login.html", True)
                return {'code': e.code, 'message': e.error}

        return h
    return f


def input(*params):
    def f(g):
        def h(*a, **b):
            it = web.input()
            for keyTipe in params:
                key, tipe, isMust = parseParam(keyTipe)
                value = mapInput(it.get(key, None), tipe)
                errorMsg = checkInput(value, tipe, isMust)
                if errorMsg:
                    return {'code':1, 'message':errorMsg, 'errorField':key}
                b['_'+key] = value
            try:
                return g(*a, **b)
            except leancloud.errors.LeanCloudError as e:
                return {'code': e.code, 'message': e.error}

        return h
    return f


