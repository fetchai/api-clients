run-web-server:
	PYTHONPATH="$$PWD:$$PYTHONPATH" fastapi dev --port 2001 entrypoint.py
generate-client:
	openapi-generator-cli generate -i api-clients-repo/apis/search-api/openapi_specs/openapi_specification.json -g python -o api-clients-repo/apis/search-api/client --additional-properties=packageName=search_api_client