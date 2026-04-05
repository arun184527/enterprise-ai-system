import boto3
s3 = boto3.client('s3')
BUCKET_NAME = "arun-ai-docs-1845"
def upload_file_to_s3(file, filename):
    s3.upload_fileobj(file, BUCKET_NAME, filename)
    return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"