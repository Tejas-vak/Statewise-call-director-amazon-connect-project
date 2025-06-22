import json
import requests
import os

NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY')

# State to CS team mapping
STATE_TEAM_MAP = {
    'Telangana': 'TG',
    'Andhra Pradesh': 'AP',
    'Tamil Nadu': 'TN',
    'Maharashtra': 'MH'
}

# Default CS team for unrecognized states
DEFAULT_CS_TEAM = 'Default'

def lambda_handler(event, context):
    print(event)
    # Extract customer's phone number
    phone_number = event['Details']['ContactData']['Attributes']['number']
    if not phone_number:
        return {
            'statusCode': 400,
            'body': json.dumps("Missing customer phone number.")
        }

    # Call numverify API
    url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone_number[3:]}&country_code=IN&format=1"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if not data.get('valid'):
            return {
                'statusCode': 400,
                'body': json.dumps("Invalid phone number.")
            }

        location = data.get('location', '')
        region = location.strip()
        print(location)

        # Assign to default CS team if region is not in the predefined list
        cs_team = STATE_TEAM_MAP.get(region, DEFAULT_CS_TEAM)
        print(cs_team)
        return {
            'statusCode': 200,
            'cs_team': cs_team,
            'location': region
        }

    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Request error: {str(e)}")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

''' Lambda Function for State-Based Call Routing in Amazon Connect

This Python Lambda function is integrated into Amazon Connect using the "Invoke Lambda Function" block within the contact flow.

### Purpose:
When a customer calls, this function is triggered to:
1. Extract the caller's phone number.
2. Send the number to the NumberVerify API for validation and location detection.
3. Retrieve the state information from the API response.
4. Return the state name to Amazon Connect, which then routes the call to the appropriate state-specific customer service queue.

This enables dynamic, location-based call routing for improved customer experience and operational efficiency. '''
