from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)
 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def index(request: Request):
    return templates.TemplateResponse('index.html', 
                                     {'request': request})


def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                     {'request': request,
                                      'username': 'admin'})

def start(request: Request):
    num = 2
    return templates.TemplateResponse('start.html',
                                     {'request': request,
                                      'num': num})