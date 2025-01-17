import boto3

def create_rds_instance(instance_id, db_name, master_user, master_password):
    rds = boto3.client('rds')
    rds.create_db_instance(
        DBInstanceIdentifier=instance_id,
        AllocatedStorage=20,
        DBName=db_name,
        Engine='mysql',
        MasterUsername=master_user,
        MasterUserPassword=master_password,
        DBInstanceClass='db.t3.micro'
    )
    print(f"RDS Instance {instance_id} is created.")

create_rds_instance("devops-db", "devopsdb", "admin", "adminpass123")