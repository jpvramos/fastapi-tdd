from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now=True)

    def __str__(self) -> str:
        self.url


SummarySchema = pydantic_model_creator(TextSummary)
