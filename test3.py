import boto3
import json

# Thay thế các giá trị sau đây bằng thông tin của bạn
aws_access_key = 'AKIA6QLYCSQ6DGJAEEWO'
aws_secret_key = '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'
aws_region = 'ap-southeast-1'
queue_url = 'https://sqs.ap-southeast-1.amazonaws.com/997221110844/ttlab_virtual_teacher_output_video_generation'

# Tạo một phiên làm việc với AWS SQS
sqs = boto3.client('sqs', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Nhận và xử lý thông điệp từ hàng đợi
# message_body = {
#      "video_id": "abs123456789123", #unique    
#      "character_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRPZFhqDWtzYIAU2fIjVfB9LuRqQ0hCpcFWw&usqp=CAU",
#      "background_color": "#008000",
#      "background_url": "string",
#      "text_input": "anh có lòng thì cho em xin bát phở. Em đói quá.",
#      "speed": 1,
#      "language": "VI",
#      "vocal": "female" 
# }


# response = sqs.send_message(
#     QueueUrl=queue_url,
#     MessageBody=json.dumps(message_body)  # Convert the dict to a JSON string before sending
# )

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

if 'Messages' in response:
    received_message = response['Messages'][0]
    receipt_handle = received_message['ReceiptHandle']
    
    try:
        # Try to parse the message body as JSON
        parsed_body = json.loads(received_message["Body"])
        print(parsed_body)
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
    # Xác nhận xử lý xong thông điệp để nó không xuất hiện trong hàng đợi nữa
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
else:
    print("No messages in the queue.")
