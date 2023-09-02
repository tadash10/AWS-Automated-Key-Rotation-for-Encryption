from aws_kms import create_new_key
from resource_updater import update_resources_with_new_key
from key_rotation_scheduler import schedule_key_rotation

def main():
    # Schedule key rotation every 30 days (30 * 24 * 60 * 60 seconds)
    interval_in_seconds = 30 * 24 * 60 * 60
    schedule_key_rotation(interval_in_seconds)

if __name__ == "__main__":
    main()
