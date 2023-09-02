import boto3

def delete_key(key_id):
    """
    Delete the specified AWS KMS encryption key.
    """
    kms_client = boto3.client('kms')
    kms_client.schedule_key_deletion(KeyId=key_id)
