import time

def schedule_key_rotation(interval_in_seconds):
    """
    Schedule key rotation at specified intervals (in seconds).
    """
    while True:
        try:
            # Create a new encryption key
            new_key_id = create_new_key()
        
            # Update relevant resources to use the new key
            update_resources_with_new_key(new_key_id)

            print(f"Created and applied a new encryption key: {new_key_id}")

            # Sleep for the specified interval before rotating keys again
            time.sleep(interval_in_seconds)
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            # Add error handling and logging as needed
