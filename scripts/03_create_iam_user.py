import boto3

def create_iam_user(user_name, policy_arn):
    iam = boto3.client('iam')
    iam.create_user(UserName=user_name)
    iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)

    print(f"User {user_name} is created and the policy {policy_arn} is attached")

create_iam_user("Soumeet", "arn:aws:iam::aws:policy/AdministratorAccess")