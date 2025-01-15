import boto3

def create_auto_scaling_group(group_name, launch_template, min_size, max_size, subnet_ids):
    asg = boto3.client('autoscaling')
    asg.create_auto_scaling_group(
        AutoScalingGroupName=group_name,
        LaunchTemplate=launch_template,
        MinSize=min_size,
        MaxSize=max_size,
        VPCZoneIdentifier=subnet_ids
    )
    print(f"Auto Scaling Group {group_name} is created")

create_auto_scaling_group("devops-asg", "lt-0123456789", 1, 3, "subnet-abc012,subnet-def345")