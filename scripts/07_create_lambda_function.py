import boto3

def create_lambda_function(function_name, runtime, role_arn, handler, zip_file_path):
    with open(zip_file_path, 'rb') as zip_file:
        zip_bytes = zip_file.read()

    lambda_client = boto3.client('lambda')
    lambda_client.create_function(
        FunctionNam=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={'ZipFile': zip_bytes},
    )
    print(f"Lambda function {function_name} is create.")

create_lambda_function(
    "my-lambda-function",
    "python3.9",
    "arn:aws:iam::123456789012:role/lambda-role",
    "lambda_function.lambda_handler",
    "path/to/lambda/code.zip"
)