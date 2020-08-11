"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# import project package.
from config.config_setting import ConfigSetting
from src.blueprint.api_router import create_api_router
from src.blueprint.eda_router import create_eda_router

def create_app(unittest=False):
    """The function to creates the fastapi service."""
    # Initial config and log
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_app]")
    config = config_setting.yaml_parser()
    
    app = FastAPI()

    api_router = create_api_router()
    app.include_router(api_router, prefix="/api", tags=["api"])

    eda_router = create_eda_router()
    app.include_router(eda_router, prefix="/eda", tags=["eda"])

    log.info("Start the fastapi service.")
    return app