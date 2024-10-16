from pydantic import BaseModel


class Damage(BaseModel):
    image_url: str
    pre_signed_url: str