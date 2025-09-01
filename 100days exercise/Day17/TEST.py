import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def send_sms(phone_number, message):
    try:
        sns = boto3.client(
            'sns',
            region_name='ap-south-1',
            aws_access_key_id='',
            aws_secret_access_key=''
        )

        sns.set_sms_attributes(
            attributes={
                'DefaultSenderID': 'Acaia',
                'DefaultSMSType': 'Transactional'
            }
        )

        response = sns.publish(
            PhoneNumber=phone_number,
            Message=message
        )

        print(f"✅ SMS sent! Message ID: {response['MessageId']}")

    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except PartialCredentialsError:
        print("❌ Incomplete AWS credentials.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    print("Enter phone number in E.164 format (e.g., +919600316815):")
    # phone_number = input().strip()
    phone_number = input().strip()

    if not phone_number.startswith('+'):
        print("❌ Error: Phone number must start with '+' and country code.")
        return

    print("Enter message text (must match your DLT-registered template if in India):")
    message = input().strip()

    send_sms(phone_number, message)

if __name__ == "__main__":
    main()
