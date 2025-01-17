import boto3

def create_sns_topic_and_publish(topic_name, message):
    sns = boto3.client('sns')
    topic = sns.create_topic(Name=topic_name)
    topic_arn = topic['TopicArn']
    sns.publish(TopicArn=topic_arn, Message=message)

    print(f"Message sent to topic {topic_name}: {message}")

create_sns_topic_and_publish("Alerts", "Hello! How are you.")