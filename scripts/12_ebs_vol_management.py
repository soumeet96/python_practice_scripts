import boto3

def create_and_attach_ebs(instance_id, size, az, device_name):
    ec2 = boto3.client('ec2')
    volume = ec2.create_volume(
        Size=size,
        AvailabilityZone=az
    )
    volume_id = volume['VolumeId']
    print(f"EBS Volume {volume_id} created.")

    ec2.attach_volume(
        InstanceId=instance_id,
        VolumeId=volume_id,
        Device=device_name
    )
    print(f"EBS Volume {volume_id} attached to instance {instance_id} as {device_name}.")

create_and_attach_ebs("i-0abcdeff2345ghj", 10, "us-east-1a", "/dev/xvdf")