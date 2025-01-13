import boto3

def manage_ec2_instance(action, tag_key, tag_value):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}])
    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]

    if action == "start" or "Start" or "START":
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"Started Instances: {instance_ids}")
    elif action == "stop" or "Stop" or "STOP":
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped Instances: {instance_ids}")
    else:
        print("Invalid Action. Specify either Start or Stop, please!!")


manage_ec2_instance("start", "env", "dev")