import shutil
from typing import Annotated
from src.apis.search_api.register_api_docs import api_id, openapi_specs_filepath, docs_endpoint_name
from fastapi import FastAPI, Request, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from os import path

from starlette.staticfiles import StaticFiles

curdir: str = path.dirname(path.abspath(__file__))

OPENAPI_SPECS_DIR_ENDPOINT = "/openapi_specs"
OPENAPI_SPECIFICATIONS_DIR: str = "openapi_specs"
OPENAPI_SPECIFICATIONS_DIR_ABSPATH: str = path.join(curdir, OPENAPI_SPECIFICATIONS_DIR)
app = FastAPI(
    docs_url="/",
    redoc_url="/redocs/",
)

# path.name openapi_specs_filepath
web_static_openapi_specs_filename: str = f"{api_id}-{path.basename(openapi_specs_filepath)}"

web_static_openapi_specs_os_abs_path: str = path.join(OPENAPI_SPECIFICATIONS_DIR_ABSPATH, web_static_openapi_specs_filename)
web_static_openapi_specs_server_path: str = path.join(OPENAPI_SPECS_DIR_ENDPOINT, web_static_openapi_specs_filename)
shutil.copy(src=openapi_specs_filepath, dst=web_static_openapi_specs_os_abs_path)

openapi_specs: dict = {
    api_id: web_static_openapi_specs_server_path,
}
docs_paths: dict[str, str] = {
    api_id: docs_endpoint_name
}

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

*map(lambda endpoint_path: app.get(endpoint_path[1], name=endpoint_path[0])(show_docs), docs_paths.items()),
app.mount(OPENAPI_SPECS_DIR_ENDPOINT, StaticFiles(directory=OPENAPI_SPECIFICATIONS_DIR_ABSPATH), name="openapi_specs")

