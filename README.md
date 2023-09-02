# Automated-Key-Rotation-for-Encryption
# AWS Key Rotation Automation

This project provides a command-line tool for automating AWS Key Management Service (KMS) encryption key rotation. It allows you to create, manage, and rotate encryption keys for enhanced security.

## Installation

Before using the tool, make sure you have Python 3.x installed on your system. You'll also need to set up your AWS credentials and configure the AWS CLI with the desired region. If you haven't done so, you can install the AWS CLI and configure it using `aws configure`.

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt

Usage
1. Key Rotation

To start the key rotation process, run the following command:

python main.py

This will schedule key rotation at regular intervals (e.g., every 30 days) and update the relevant AWS resources to use the newly generated keys.
2. List Available Keys

You can list all available AWS KMS encryption keys using the following command:

bash

python list_keys.py

3. Enable a Key

To enable a specific AWS KMS encryption key, use the following command:

bash

python enable_key.py <key_id>

Replace <key_id> with the ID of the key you want to enable.
4. Disable a Key

To disable a specific AWS KMS encryption key, use the following command:

bash

python disable_key.py <key_id>

Replace <key_id> with the ID of the key you want to disable.
5. Delete a Key

To delete a specific AWS KMS encryption key, use the following command:

bash

python delete_key.py <key_id>

Replace <key_id> with the ID of the key you want to delete. Be cautious as this action is irreversible.


