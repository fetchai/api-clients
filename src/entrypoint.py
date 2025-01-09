import importlib
import os
from glob import iglob
from os import path
from typing import Annotated

from fastapi import FastAPI, Request, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.staticfiles import StaticFiles


curdir = path.dirname(path.abspath(__file__))
OPENAPI_SPECS_DIR_ENDPOINT = "/openapi_specs"
OPENAPI_SPECIFICATIONS_DIR: str = "openapi_specs"
OPENAPI_SPECIFICATIONS_DIR_ABSPATH: str = path.join(curdir, "web", OPENAPI_SPECIFICATIONS_DIR)
app = FastAPI(
    docs_url="/",
    redoc_url="/redocs/",
)

def load_apis() -> tuple[dict, dict]:
    openapi_specs: dict = {}
    docs_paths: dict = {}

    curdir = path.dirname(path.abspath(__file__))
    glob_pattern: str = os.path.join(curdir, "./apis/*/register_api_docs.py")

    for register_api_docs_filepath in iglob(glob_pattern):
        spec = importlib.util.spec_from_file_location(
            name="register_api_docs",
            location=register_api_docs_filepath
        )
        w = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(w)
        openapi_specs[w.api_id] = os.path.join(OPENAPI_SPECS_DIR_ENDPOINT, w.openapi_specs_name)
        docs_paths[w.api_id] = w.docs_endpoint_name
    return openapi_specs, docs_paths

def get_openapi_spec_file(request: Request) -> str:
    path: str = request.url.path
    api_name: str
    api_name = next((name for name, url_path in docs_paths.items() if url_path == path), None)
    print(openapi_specs[api_name])
    return openapi_specs[api_name]

async def show_docs(request: Request, open_api_specs_path: Annotated[str, Depends(get_openapi_spec_file)]):
    return get_swagger_ui_html(
        openapi_url=open_api_specs_path,
        title="API v2 Docs"
    )

print("🚀 Starting API v2 docs server...")
openapi_specs, docs_paths = load_apis()
*map(lambda endpoint_path: app.get(endpoint_path[1], name=endpoint_path[0])(show_docs), docs_paths.items()),
app.mount(OPENAPI_SPECS_DIR_ENDPOINT, StaticFiles(directory=OPENAPI_SPECIFICATIONS_DIR_ABSPATH), name="openapi_specs")

