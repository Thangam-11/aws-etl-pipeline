import boto3
from io import StringIO


# ---------- S3 UPLOAD FUNCTION ----------
def upload_to_s3(df, bucket, key, aws_config):

    csv_buffer = StringIO()

    df.to_csv(csv_buffer, index=False)

    s3 = boto3.client("s3", **aws_config)

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=csv_buffer.getvalue()
    )

    print(f"✅ Uploaded to s3://{bucket}/{key}")



    