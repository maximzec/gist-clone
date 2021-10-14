from fastapi import FastAPI
from fastapi.param_functions import File
from starlette.responses import FileResponse

app = FastAPI(
    title = "Gist-clone",
    description="FastApi based application which allows to markdown -> html",
    openapi_tags=[
        {
            "name" : "Information",
            "description" : "This is FastAPI based web-application which allows you to transform markdown to html"
        }
    ],
    version='0.1.0'
)

@app.get("/")
def welcome_root():
    return "Hi there, you're visiting my FastApi application which allows you to markdown -> html"


@app.post('/markdown')
def markdown_to_html():
    return FileResponse('html_response.html')
