import boto3

def update_dns_record(zone_id, record_name, record_type, record_value, ttl=300):
    route53 = boto3.client('route53')
    route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': record_name,
                    'Type': record_type,
                    'TTL': ttl,
                    'ResourceRecords': [{'Value': record_value}],
                }
            }]
        }
    )
    print(f"Record {record_name} updated to {record_value}.")

update_dns_record("Z123456ABCD", "test.soumeet.com", "A", "192.168.2.66")