import boto3
import uuid

def create_bucket_and_upload():
    s3 = boto3.client('s3')
    region = boto3.session.Session().region_name
    print(f"Current AWS region: {region}")

    # Create a unique bucket name (must be globally unique)
    bucket_name = f"my-unique-bucket-{uuid.uuid4()}".lower()

    # Create the S3 bucket with correct region handling
    if region == 'us-east-1':
        response = s3.create_bucket(Bucket=bucket_name)
    else:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print(f"Bucket created: {bucket_name}")

    # Create a sample file to upload
    file_name = "example.txt"
    with open(file_name, "w") as f:
        f.write("Hello from Boto3!")

    # Upload the file to the bucket
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Uploaded file '{file_name}' to bucket '{bucket_name}'")

if __name__ == "__main__":
    create_bucket_and_upload()

