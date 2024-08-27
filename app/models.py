from django.db import models
from pydantic import BaseModel

# Create your models here.
class recipeGenerationModel(BaseModel):
    name: str
    ingredients:list[str]
    instructions: list[str]