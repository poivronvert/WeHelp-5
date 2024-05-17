from pydantic import BaseModel


class DeleteMessageRequest(BaseModel):
    message_id:int

class EditMessageRequest(BaseModel):
    message_id:int
    content:str

class UpdateNameRequest(BaseModel):
    name:str