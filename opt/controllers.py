from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import img

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
    nume = img.randomer()
    return templates.TemplateResponse('start.html',
                                     {'request': request,
                                      'position': nume})
                                    
def tr(request: Request):
    text, posinega,hiryo = img.mimi()
    return templates.TemplateResponse('start.html',
                                     {'request': request,
                                      'text': text,
                                      'posinega':posinega,
                                      'hiryo':hiryo})