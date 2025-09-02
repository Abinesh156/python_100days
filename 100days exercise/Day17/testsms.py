import boto3

# Replace with your credentials (⚠️ DO NOT expose these in production)
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

# Replace with your values
AWS_REGION = "ap-south-1"
PINPOINT_PROJECT_ID = "your-pinpoint-application-id"
DESTINATION_NUMBER = ""   # E.164 format
SENDER_ID = "MySenderID"             # Optional
MESSAGE = "Hello! This is a test SMS from AWS Pinpoint."

# Initialize the Pinpoint client with credentials
client = boto3.client(
    'pinpoint',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Send the SMS message
response = client.send_messages(
    ApplicationId=PINPOINT_PROJECT_ID,
    MessageRequest={
        'Addresses': {
            DESTINATION_NUMBER: {
                'ChannelType': 'SMS'
            }
        },
        'MessageConfiguration': {
            'SMSMessage': {
                'Body': MESSAGE,
                'MessageType': 'TRANSACTIONAL',  # or 'PROMOTIONAL'
                'SenderId': SENDER_ID            # Optional
            }
        }
    }
)

# Print the response
print("Message response:")
print(response)
