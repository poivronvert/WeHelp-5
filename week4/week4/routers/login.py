import logging
import os

from week4 import templates

from fastapi import HTTPException, Request, Response, status, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

__all__ = ['router',]

log = logging.getLogger()
router = APIRouter(tags=['login', ])
TEMPLATES_PATH:os.PathLike = os.path.realpath(os.path.dirname(templates.__file__))

templates = Jinja2Templates(directory=TEMPLATES_PATH)

@router.get("/", response_class=HTMLResponse)
async def root(*, request: Request, response: Response):
    """Return the Home HTML page.

    Args:
        request (Request): The incoming request.
        response (Response): The outgoing response.

    Raises:
        HTTPException: If there's an error processing the request.

    Returns:
        HTMLResponse: The HTML response for the home page.
    """
    try:

        return templates.TemplateResponse(
            request=request, name='index.html', context={"request": request}
        )
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

pseudo_user_data = {
    "test": "test",
}

@router.post("/signin")
async def signin(*, username: str = Form(None), password: str = Form(None), request: Request, response: Response):
    """Sign in a user.

    Args:
        request (Request): The incoming request.
        response (Response): The outgoing response.
        username (str, optional): The username entered by the user. Defaults to Form(None).
        password (str, optional): The password entered by the user. Defaults to Form(None).

    Raises:
        HTTPException: If there's an error processing the request.

    Returns:
        RedirectResponse: A redirect response based on the sign-in status.
    """
    try:
        if not username or not password:
            msg = 'Please enter username and password.'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
        elif password == pseudo_user_data.get(username, None):
            request.session['SIGNED_IN'] = True
            return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
        else:
            msg = 'Incorrect username or password.'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    

@router.get("/error")
async def get_error_msg(*, message: str | None = 'Default Error Message', request: Request, response: Response):
    """Get the error message.

    Args:
        request (Request): The incoming request.
        response (Response): The outgoing response.
        message (str | None, optional): The error message. Defaults to 'Default Error Message'.

    Raises:
        HTTPException: If there's an error processing the request.

    Returns:
        TemplateResponse: The HTML response displaying the error message.
    """
    try:
        return templates.TemplateResponse(
                request=request, name="error.html", context={"error_message": message}
            )
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/square/{number_input}")
async def calculate_square(*, number_input:int, request: Request):
    try:
        squared_number = number_input**2
        return templates.TemplateResponse("calculator.html", {"request": request, "squared_number": squared_number})
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

