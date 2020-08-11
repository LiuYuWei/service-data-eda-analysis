"""Define fastapi input variable type."""
# import relation package.
from pydantic import BaseModel

# import project package.


class DataframeBaseModel(BaseModel):
    length_df: int
    length_column_df: int


class EdaReportBaseModel(BaseModel):
    timestamp: str
    eda_report: str
