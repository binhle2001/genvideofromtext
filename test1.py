import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id = "AKIA6QLYCSQ6DGJAEEWO",
    aws_secret_access_key = "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",
    region_name = "ap-southeast-1",
)

with open("output_video.mp4", "rb") as f:
            s3.upload_fileobj(f, "ttlab-virtual-teacher", "data_temp/output_video.mp4")
            
            
url_model = "https://" + "ttlab-virtual-teacher" + ".s3." + "ap-southeast-1" +  ".amazonaws.com/" + "data_temp/output_video.mp4"