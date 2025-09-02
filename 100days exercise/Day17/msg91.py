import requests
import json

# Define your API URL and key
url = "https://api.msg91.com/api/v5/otp/send"
api_key = ""  # Replace with your API key from MSG91
sender_id = "MSG91"  # Sender ID registered with MSG91
mobile_number = "9600316815"  # Recipient mobile number (in international format without +)
message = "Your OTP is 123456"  # The OTP or message you want to send
route = "1"  # '1' for transactional SMS
country_code = "91"  # Country code (for India, it's '91')

# Prepare data for the request
data = {
    "authkey": api_key,
    "mobiles": mobile_number,
    "message": message,
    "sender": sender_id,
    "route": route,  # Transactional route
    "country": country_code
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
