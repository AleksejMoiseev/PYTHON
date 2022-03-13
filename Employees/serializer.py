from typing import List, Any

from pydantic import BaseModel, validator


class SerializerEmployees(BaseModel):
    name: str
    position: str
    hours: Any
    plan: Any
    kpi: Any
    experiens: Any

    @validator('name')
    def clean_name(cls, value: str):
        return value.strip()

    @validator('position')
    def clean_position(cls, value: str):
        return value.strip()

    @validator('hours')
    def clean_hours(cls, value: str):
        value.strip()
        return int(value[0:len(value)-1])

    @validator('plan')
    def clean_plan(cls, value: str):
        value.strip()
        return int(value[0:len(value) - 1])

    @validator('kpi')
    def clean_kpi(cls, value: str):
        return int(value)

    @validator('experiens')
    def clean_experiens(cls, value: str):
        value.strip()
        return int(value)


KEYS = tuple(SerializerEmployees.__fields__.keys())
