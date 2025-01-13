import boto3
import time

def push_log_to_cw(log_group, log_stream, message):
    logs = boto3.client('logs')
    try:
        logs.create_log_group(logGroupName = log_group)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        logs.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

    timestamp = int(round(time.time() * 1000))
    logs.put_log_events(
        logGroupName=log_group,
        losStreamName=log_stream,
        logEvents=[{'timestamp': timestamp, 'message': message}]
    )
    print(f"Log pushed to {log_group}/{log_stream}")

push_log_to_cw("devops_log_group", "devops_log_stream", "Test Log")