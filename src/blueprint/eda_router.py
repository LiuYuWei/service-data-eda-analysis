"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# import project package.
from config.config_setting import ConfigSetting
from src.util.eda_router_base_model import DataframeBaseModel, EdaReportBaseModel
from src.app.eda_app import EdaApp

def create_eda_router():
    """The function to creates the fastapi api router service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_api_router]")
    config = config_setting.yaml_parser()

    user_router = APIRouter()
    # HTML template.
    templates = Jinja2Templates(directory="src/templates")

    eda_app = EdaApp()

    @user_router.post("/action/upload_data", response_model=DataframeBaseModel)
    def upload_data(data: list, column_names: list):
        """health_check: Check the service is working.
        Returns:
            json format: the health check content.
        """
        return eda_app.transform_to_table(data, column_names)
    
    @user_router.get("/action/eda_analysis", response_model=EdaReportBaseModel)
    def eda_analysis(title_name: str):
        """health_check: Check the service is working.
        Returns:
            json format: the health check content.
        """
        return eda_app.eda_analysis(title_name)
    
    @user_router.get("/html/eda_result_dashboard")
    def eda_analysis(request: Request):
        """health_check: Check the service is working.
        Returns:
            json format: the health check content.
        """
        html = eda_app.eda_html()
        log.info(html)
        return templates.TemplateResponse(html,  {"request": request})

    log.info("Successfully setting the eda router.")
    return user_router
