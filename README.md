# DynamoDB Generic HTTP Request Maker
# generic-http-lambda-python 💻
Small project of a generic http request maker. It receives a 'request input' and makes a request using parameter values.

This code is meant to be used on a Lambda function. The handler input is an event with these informations:

- url;
- http method;
- timeout;
- number of desired retries;
- headers;
- body;
- correlation_id.

JSON payload:
```
{
  "url": "https://example.com/api/resource",
  "http_method": "POST",
  "timeout": 30,
  "number_of_desired_retries": 3,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token_here"
  },
  "body": {
    "key1": "value1",
    "key2": "value2"
  },
  "correlation_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

Using the 'requests' HTTP library, the lambda function makes a request to the desired URL. The function will retry the request if it fails, up to the number of desired retries.

## Local Testing 

Necessary tools:

1) Create a virtual environment for your python application by running the following commands:
    ```
        python3 -m venv .venv
        source .venv/bin/activate
    ```
2) Install python requirements for requirements.txt file:
    ```
        python3 -m pip install -r requirements.txt
    ```
3) Move the 'localExec/test_local.py' file to the 'app' folder
4) Change directories using 'cd app' to run code from 'app' dir. Use the python script moved to the app folder to run the scan:
    ```
        python3 test_local.py
    ```
5) The output will be printed on the console.
6) Change the attribute values on the request_input in the 'test_local.py' file to test different scenarios.


## Authors

*Giovanna Albuquerque* [@GHBAlbuquerque](https://github.com/GHBAlbuquerque)

Done in 2025
