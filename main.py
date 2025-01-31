from google.cloud import storage

def upload_file(event, context):
    """Uploads a file to a bucket."""
    # The ID of your GCS bucket
    bucket_name = "your-bucket-name" 

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

    print(f"File {blob_name} uploaded to {bucket_name}.")