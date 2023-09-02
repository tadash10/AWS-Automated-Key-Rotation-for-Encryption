import boto3

def list_keys():
    """
    List all available AWS KMS encryption keys.
    """
    kms_client = boto3.client('kms')
    response = kms_client.list_keys()
    return response['Keys']
