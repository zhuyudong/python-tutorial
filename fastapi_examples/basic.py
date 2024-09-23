"""
中间件不必是专为 FastAPI 或 Starlette 定制的，只要遵循 ASGI 规范即可

"""

import time
from typing import Annotated

from fastapi import Depends, FastAPI, File, Form, Request, UploadFile
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .classes import Item

# NOTE: fastapi.Request is not the same as starlette.Request
# from starlette.requests import Request
from .fixed_content_query_checker import checker

app = FastAPI(
  title='Request Forms and Files',
  docs_url='/docs',
  redoc_url='/redoc',
  openapi_url='/openapi',
)


@app.post('/files/')
async def create_file(
  file: Annotated[bytes, File()],  # bytes
  fileb: Annotated[UploadFile, File()],
  token: Annotated[str, Form()],
):
  return {
    'file_size': len(file),
    'token': token,
    'fileb_content_type': fileb.content_type,
  }


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
  start_time = time.perf_counter()
  response = await call_next(request)
  process_time = time.perf_counter() - start_time
  response.headers['X-Process-Time'] = str(process_time)
  return response


app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['localhost', '*.localhost.com'])
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)


@app.get('/')
async def main():
  return 'root'


@app.get('/query-checker/')
async def read_query_check(fixed_content_included: bool = Depends(checker)):
  return {'fixed_content_in_query': fixed_content_included}


@app.get('/items/next', response_model=Item)
async def read_next_item():
  return {
    'name': 'Island In The Moon',
    'price': 12.99,
    'description': "A place to be playin' and havin' fun",
    'tags': ['breater'],
  }


# if __name__ == '__main__':
#   import uvicorn

#   uvicorn.run('app:main', host='0.0.0.0', port=8000, reload=True)
