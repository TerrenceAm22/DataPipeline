
import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# create_bucket('rawjson-data')


data = open(r'C:\Users\TMalone\Documents\DataMigration\DataPipeline\top50_songs.csv', 'rb')
s3.Bucket('rawjson-data').put_object(Key='top50song.csv', Body=data)