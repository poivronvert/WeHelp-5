import logging

from typing import Annotated, Optional
from fastapi import FastAPI, HTTPException, Request, Response, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

log = logging.getLogger()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(*, request:Request, response: Response):
    """Return to Home HTML

    Args:
        request (Request): signin HTML
        response (Response): signin HTML

    Raises:
        HTTPException: HTTP status 400

    Returns:
        HTML: sign HTML
    """
    try:
        return templates.TemplateResponse(
            request=request, name="index.html", context={"request":request}
        )
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

pseudo_user_data = {
    "test": "test",
}

@app.post("/signin")
async def signin(*, username:str=Form(None), password:str=Form(None), request:Request, response: Response):
    try:
        if not username or not password:
            msg:str = '請輸入帳號和密碼'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
            # return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
        elif password==pseudo_user_data.get(username, None):
            return templates.TemplateResponse(
                request=request, name="member.html")
        else:
            msg:str = '帳號、或密碼輸入錯誤'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    

@app.get("/error")
async def get_error_msg(*, message:str|None='Default Error Message', request:Request, response: Response):
    try:
        return templates.TemplateResponse(
                request=request, name="error.html", context={"error_message":message}
            )
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
 
    