import boto3

def enable_key(key_id):
    """
    Enable the specified AWS KMS encryption key.
    """
    kms_client = boto3.client('kms')
    kms_client.enable_key(KeyId=key_id)
