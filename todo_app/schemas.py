from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    done: bool
    created_at: datetime

    model_config = {"from_attributes": True}
