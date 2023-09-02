import boto3

def disable_key(key_id):
    """
    Disable the specified AWS KMS encryption key.
    """
    kms_client = boto3.client('kms')
    kms_client.disable_key(KeyId=key_id)
