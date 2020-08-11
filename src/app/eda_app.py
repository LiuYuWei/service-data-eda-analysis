"""svm classification app."""
# coding=utf-8
# import relation package.

# import project package.
from config.config_setting import ConfigSetting
from src.service.eda_service import EdaService


class EdaApp:
    """svm classification app."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[eda_app]")
        self.config = config_setting.yaml_parser()
        self.eda_service = EdaService()

    def transform_to_table(self, data, column_names):
        payload = self.eda_service.transform_json_to_pandas(data, column_names)
        return payload
    
    def eda_analysis(self, title_name):
        payload = self.eda_service.pandas_profiling_eda_transfer(title_name)
        return payload
    
    def eda_html(self):
        result = self.eda_service.show_eda_result_in_html()
        return result