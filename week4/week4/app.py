import logging

from fastapi import FastAPI, Request, Response, HTTPException,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

from week4.routers.login import router

templates = Jinja2Templates(directory="templates")

log = logging.getLogger()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, )

app.add_middleware(SessionMiddleware, secret_key="secret_key")

@app.get("/signout")
async def logout(request: Request):
    """Sign out the user.

    Args:
        request (Request): The incoming request.

    Returns:
        RedirectResponse: A redirect response to the home page.
    """
    try:
        request.session.pop('SIGNED_IN', None)
        return RedirectResponse(url="/")
    except Exception as e:
        log.error(e,exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@app.get("/member", response_class=HTMLResponse)
async def success(request: Request):
    """Display the member page.

    Args:
        request (Request): The incoming request.

    Returns:
        TemplateResponse: The HTML response for the member page.
    """
    try:
        if not request.session.get('SIGNED_IN', False):
            return RedirectResponse(url="/")
        
        return templates.TemplateResponse("member.html", {"request": request})
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))