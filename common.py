import qrcode
import qrcode.image.svg
import boto3
import os

BUCKET = os.environ.get('AWS_BUCKET_NAME', 'hold-my-spot-st')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
TEMP_FOLDER = "uploads"

def create_s3_client():
    return boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_KEY, region_name = "us-west-1")

def create_qr(url, reservation_id):
    img = qrcode.make(url)
    file_name = os.path.join(TEMP_FOLDER,"reservation_" + str(reservation_id) + ".jpg")
    img.save(file_name)
    upload_file(file_name)
    os.remove(file_name)
    return file_name

def upload_file(file_name, bucket=BUCKET):
    object_name = file_name
    s3_client = create_s3_client()
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def get_qr_url(file_name, bucket=BUCKET):
    s3_client = create_s3_client()
    url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': file_name})
    return url

def delete_qr(file_name, bucket=BUCKET):
    s3_client = create_s3_client()
    s3_client.delete_object(Bucket = bucket, Key = file_name)
    return
