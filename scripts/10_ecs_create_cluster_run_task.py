import boto3

def create_and_run_ecs_cluster(cluster_name, taskdef, subnet_id):
    ecs = boto3.client('ecs')
    ecs.create_cluster(clusterName=cluster_name)
    print(f"ECS Cluster {cluster_name} is created.")

    ecs.run_task(
        cluster=cluster_name,
        taskDefinition=taskdef,
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [subnet_id],
                'assignPublicIp': 'ENABLED'
            }
        }
    )
    print(f"Task {taskdef} started in cluster {cluster_name}.")

create_and_run_ecs_cluster("devops_cluster", "mytaskdef", "subnet-abcdef01234")