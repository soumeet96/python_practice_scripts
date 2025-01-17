import boto3

def deploy_cloudformation_stack(stack_name, template_file, parameters):
    with open(template_file, 'r') as file:
        template_body = file.read()
    
    cloudformation = boto3.client('cloudformation')
    cloudformation.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"Cloudformation Stack {stack_name} is being created.")

deploy_cloudformation_stack(
    "devops",
    "path/to/template.yaml",
    [
        {'ParameterKey': 'InstanceType', 'ParameterValue': 't3.micro'},
        {'ParameterKey': 'KeyName', 'ParameterValue': 'my-key-pair'}
    ]
)