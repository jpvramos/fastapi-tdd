# project/app/api/crud.py
import tortoise

from typing import Union, List

from app.models.schema import SummaryPayLoadSchema
from app.models.text_summary import TextSummary


async def post(payload: SummaryPayLoadSchema) -> int:
    data = tortoise.timezone.now()

    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
