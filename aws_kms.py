import boto3

def create_new_key():
    """
    Create a new AWS KMS encryption key.
    """
    kms_client = boto3.client('kms')
    response = kms_client.create_key(Description='Automated Key Rotation')
    return response['KeyMetadata']['KeyId']
