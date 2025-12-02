from pydantic import BaseModel

class MatchRequest(BaseModel):
    mentee_username: str
