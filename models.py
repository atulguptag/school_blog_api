from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class BlogPost(BaseModel):
    title: str
    content: str
    published_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    tags: List[str] = []


class BlogPostInDB(BlogPost):
    id: Optional[str] = None
