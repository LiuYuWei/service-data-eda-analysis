"""This file is main file."""
# import relation package.
import uvicorn

# import project package.
from src import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0')
