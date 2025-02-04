from google.cloud import storage 
from google.cloud import logging

logger = logging.Client().logger(__name__)

def main(event, context):
    """Uploads a file to a bucket."""
    logger.log_text("starting hello world function", severity="INFO")
    try:
        # The ID of your GCS bucket
        bucket_name = "hmidata" 

        # The ID of your GCS object
        blob_name = "test.txt"

        # The path to your file to upload
        # In this case, we're creating the content dynamically
        content = "hello world"

        # Create a client
        storage_client = storage.Client()

        # Create a new bucket object
        bucket = storage_client.bucket(bucket_name)

        # Create a new blob object and upload data
        blob = bucket.blob(blob_name)
        blob.upload_from_string(content)

        #logger.log_text(f"File {blob_name} uploaded to {bucket_name}.", severity="INFO")
    except:
        #logger.log_text(f"Error running hello world.", severity="ERROR")
        print("error")

if __name__ == '__main__':
    main(None, None)