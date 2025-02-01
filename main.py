from google.cloud import storage, logging

logger = logging.getLogger(__name__)

def main(event, context):
    """Uploads a file to a bucket."""
    logger.info("starting hello world function")
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

    logger.info(f"File {blob_name} uploaded to {bucket_name}.")

if __name__ == '__main__':
    main(None, None)