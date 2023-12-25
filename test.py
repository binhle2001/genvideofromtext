import boto3
import requests
import os
s3 = boto3.client(
    's3',
    aws_access_key_id = "AKIA6QLYCSQ6DGJAEEWO",
    aws_secret_access_key = "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",
    region_name = "ap-southeast-1",
)
local_directory = "input_images"
s3_prefix = 'input_images'

for file_name in range(1):

    local_path = local_directory + f"/{file_name}"
    s3_path = local_path.replace("ai_core", "ai_model")
    with open(local_path, "rb") as f:
        s3.upload_fileobj(f, "ttlab-virtual-teacher", s3_path)
#     # Đẩy tệp lên S3
#     # s3.upload_file(local_path, "ttlab-virtual-teacher", s3_path)


# response = s3.list_objects_v2(Bucket="ttlab-virtual-teacher", Prefix=s3_prefix)

# # Extract file names from the response
# file_names = [obj['Key'] for obj in response.get('Contents', [])]

# # Print the list of file names
# print("File Names in the folder:")
# for file_name in file_names:
#     print(file_name)
# url_model = "https://" + "ttlab-virtual-teacher" + ".s3." + "ap-southeast-1" +  ".amazonaws.com/" + "ai_model/wav2lip/model/experiments/001_ESRGAN_x4_f64b23_custom16k_500k_B16G1_wandb/models/net_g_67500.pth"
# response = requests.get(url_model)
# print(response.status_code)