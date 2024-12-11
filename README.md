# Description
Under src/apis you will find a list of all available Fetch AI's APIs.

In each, under the client directory, you will find a functional client to interact 
with the latest version of the service's API in question.

You can also get information about the API running our web app, 
where all Fetch AI's APIs docs are exposed using swagger & redocs.

# Get the docs; Run the app
To run the server and get the live documentation:

Go to the project root and execute:

```shell
poetry shell
poetry install # if necessary (~ just first time)
make run-web-server
```

