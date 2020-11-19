# project/app/models/schema.py


from pydantic import BaseModel, AnyHttpUrl


class SummaryPayLoadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayLoadSchema):
    id: int


class SummaryUpdatePayLoadSchema(SummaryPayLoadSchema):
    summary: str
