import leancloud
from leancloud import User
from util import page
import web

urls = ()

app = web.application(urls, globals())
render = page.render()

Interface = leancloud.Object.extend('Login')

class Login:
    @page.input("phone", "password")
    def POST(self, _phone, _password):
        user = User()
        try:
            user.login(_phone, _password)
            token = user.get_session_token()
            trueName = user.get("nickName")
            web.setcookie('session', token)
            return {'status': 0, 'token': token, 'name': trueName}
        except leancloud.errors.LeanCloudError:
            return {'status': 1, 'message': 'login failed'}

