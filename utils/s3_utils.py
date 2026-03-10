

import boto3
from io import StringIO
from utils.logger import logger


def upload_to_s3(df, bucket, key, aws_config):

    try:

        if df is None or df.empty:
            logger.warning("⚠️ DataFrame is empty. Skipping upload.")
            return

        csv_buffer = StringIO()

        df.to_csv(csv_buffer, index=False)

        s3 = boto3.client("s3", **aws_config)

        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=csv_buffer.getvalue()
        )

        logger.info(f"Uploaded to s3://{bucket}/{key}")

    except Exception as e:

        logger.exception(f"S3 upload failed for {key} : {str(e)}")


        raise
    logger.info("✅ S3 utilities loaded successfully")