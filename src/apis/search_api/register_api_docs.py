from os import path

api_id: str = "search-api"
openapi_specs_filepath: str = path.join(
    path.dirname(path.abspath(__file__)),
    './openapi_specs/openapi_specification.json'
)
docs_endpoint_name: str = "/search-api/"
