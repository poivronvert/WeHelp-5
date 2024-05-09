from pydantic import BaseModel


class DeleteMessageRequest(BaseModel):
    message_id:int