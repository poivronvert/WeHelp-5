import logging
import os

from fastapi import HTTPException, Request, Response, status, Form, APIRouter, Query
from fastapi.responses import HTMLResponse, RedirectResponse,JSONResponse
from fastapi.templating import Jinja2Templates

from week7 import templates
from week7 import sql_template as temp
from week7.db.connection import get_connection
from week7.db.schema import DeleteMessageRequest, EditMessageRequest, UpdateNameRequest

__all__ = ['router',]

log = logging.getLogger('uvicorn')
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
        conn, cursor = get_connection()
        if not username or not password:
            msg = 'Please enter username and password.'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
        cursor.execute(temp.CHECK_USER_EXISTS,(username,password))
        row = cursor.fetchone()

        if row:
            log.info(f"User=({row[0]}, {username}) login successfully.")
            request.session['SIGNED_IN'] = True
            request.session['name'] = row[1]
            request.session['member_id'] = row[0]
            return RedirectResponse(f"/member", status_code=status.HTTP_302_FOUND)
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

@router.get("/signout")
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

@router.get("/member", response_class=HTMLResponse)
async def success(request: Request):
    """Display the member page.

    Args:
        request (Request): The incoming request.

    Returns:
        TemplateResponse: The HTML response for the member page.
    """
    conn = None
    try:
        if not request.session.get('SIGNED_IN', False):
            return RedirectResponse(url="/")
        name = request.session.get('name')
        member_id = request.session.get('member_id')
        conn, cursor = get_connection()
        cursor.execute(temp.SHOW_MESSAGE_ALL_ROWS,)
        row = cursor.fetchall()

        return templates.TemplateResponse("member.html", {"request": request,"name":name,"messages":row,"member_id":member_id})
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/signup")
async def signup(*, signup_name: str = Form(None), signup_username: str = Form(None), signup_password: str = Form(None), request: Request, response: Response):
    conn = None
    try:
        if not signup_name or not signup_username or not signup_password:
            msg = '請輸入所有欄位'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)

        conn, cursor = get_connection()

        cursor.execute(temp.CHECK_DUPLICATE_USER,(signup_username,))
        result = cursor.fetchone()

        if result[0] > 0:
            msg = 'Repeated username'
            return RedirectResponse(f"/error?message={msg}", status_code=status.HTTP_302_FOUND)
        cursor.execute(temp.INS_USER_SINGLE_ROW, (signup_username, signup_name, signup_password))
        conn.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

    except Exception as e:
        if conn:
            conn.rollback()
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()
@router.post("/createMessage")
async def create_message(*, message_input: str = Form(), request: Request, response: Response):
    conn = None
    try:
        conn, cursor = get_connection()
        member_id=request.session.get('member_id')
        cursor.execute(temp.INS_MESSAGE_SINGLE_ROW,(member_id,message_input))
        conn.commit()
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)

    except Exception as e:
        if conn:
            conn.rollback()
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/deleteMessage/")
async def delete_message(*, req:DeleteMessageRequest, request: Request, response: Response):
    conn = None
    try:
        message_id = req.message_id
        conn, cursor = get_connection()
        member_id:int = request.session.get('member_id', None)
        if member_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        cursor.execute(temp.DEL_MESSAGE_SINGLE_ROW,(message_id, member_id))
        del_row:int = cursor.rowcount
        conn.commit()
        if del_row>0:
            return status.HTTP_200_OK
        else:
            return status.HTTP_304_NOT_MODIFIED

    except Exception as e:
        if conn:
            conn.rollback()
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/editMessage/")
async def edit_message(*, req:EditMessageRequest, request: Request, response: Response):
    conn = None
    try:
        message_id = req.message_id
        content= req.content

        conn, cursor = get_connection()
        member_id:int = request.session.get('member_id', None)
        if member_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        cursor.execute(temp.EDIT_MESSAGE_SINGLE_ROW,(content, message_id, member_id))
        edit_row:int = cursor.rowcount
        conn.commit()
        if edit_row>0:
            return status.HTTP_200_OK
        else:
            return status.HTTP_304_NOT_MODIFIED

    except Exception as e:
        if conn:
            conn.rollback()
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/api/member")
async def query_name(*, username:str=Query(...,), request: Request, response: Response):
    conn = None
    try:
        signed_in:int = request.session.get('SIGNED_IN', None)
        if signed_in is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not signed in")

        
        conn, cursor = get_connection()
        with conn, cursor:
            cursor.execute(temp.QUERY_NAME,(username,))
            row= cursor.fetchone()

        if row:
            data = {
                "id": row[0],
                "name": row[1],
                "username": row[2]
            }
            return JSONResponse(content={"data": data})
        else:
            return JSONResponse(content={"data": None})

    except Exception as e:
        if conn:
            conn.rollback()
        log.error(e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn:
            conn.close()    

@router.patch("/api/member")
async def update_name(*, body:UpdateNameRequest, request: Request, response: Response):
    conn = None
    cursor = None
    try:
        
        new_name = body.name
        if not new_name:
            raise HTTPException(status_code=400, detail="New name is required in the request body")
        
        signed_in:int = request.session.get('SIGNED_IN', None)
        member_id = request.session.get('member_id')
        if signed_in is None or member_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not signed in")

        conn, cursor = get_connection()
        try:
            cursor.execute(temp.UPDATE_NAME,(new_name,member_id))
            row_count = cursor.rowcount

            if row_count > 0:
                conn.commit()
                return JSONResponse(content={"ok": True})
            else:
                return JSONResponse(content={"error": True})

        except Exception as e:
            conn.rollback()
            log.error(f"An error occurred while updating name: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
    
    except HTTPException as e:
        log.error(f"HTTPException occurred: {e}")
        raise
    
    finally:
        if cursor:  
            cursor.close()
        if conn:
            conn.close()
