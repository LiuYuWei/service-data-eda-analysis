"""Confusion matrix calculation service."""
# coding=utf-8
# import relation package.
from pandas_profiling import ProfileReport
import pandas as pd
import datetime
import json

# import project package.
from config.config_setting import ConfigSetting


class EdaService:
    """Confusion matrix calculation service."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[eda_service]")
        self.config = config_setting.yaml_parser()
        self.eda_html = None

    def transform_json_to_pandas(self, data, column_name):
        df = pd.DataFrame(data, columns=column_name)
        payload = {}
        payload["length_df"] = len(df)
        payload["length_column_df"] = len(df.columns)
        df.to_csv("data/csv/dataframe.csv")
        return payload
    
    def pandas_profiling_eda_transfer(self, title_name):
        df = pd.read_csv("data/csv/dataframe.csv")
        profile = df.profile_report(title='Pandas Profiling Report')
        payload = {}
        now_time = datetime.datetime.now()
        payload["timestamp"] = now_time.isoformat()
        payload["eda_report"] = "eda_{}.html".format(now_time.strftime("%Y%m%d_%H%M%S"))
        self.eda_html = payload["eda_report"]
        profile.to_file("src/templates/{}".format(payload["eda_report"]))
        return payload
    
    def show_eda_result_in_html(self):
        result = None
        if self.eda_html is not None:
            result = self.eda_html
        return result
