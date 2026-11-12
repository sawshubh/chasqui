from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class EventRequest(BaseModel):
    name: str
    description: str | None = None


class EventResponse(BaseModel):
    message: str
    status_code: int
    event: dict


@app.post("/event", response_model=EventResponse)
def event(event: EventRequest):
    event_str = event
    return {
        "message": "success",
        "status_code": status.HTTP_200_OK,
        "event": {"name": event_str.name}
    }
