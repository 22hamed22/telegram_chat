import json
import requests
import os
from openai import OpenAI  # New import for OpenAI API v1.0.0+
from openai import AsyncOpenAI  # For asynchronous operations (if needed)

def lambda_handler(event, context):
    # Get environment variables for OpenAI and Telegram
    openai_api_key = os.environ.get("OPENAI_API_KEY")  # Fetch from Lambda environment variables
    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")  # Fetch from Lambda environment variables
    
    if not openai_api_key or not telegram_bot_token:
        # Return an error if any environment variable is missing
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'failure', 'message': 'Missing environment variables'})
        }
    
    # The event['body'] is already a dictionary, so no need to use json.loads()
    body = event['body']
    chat_id = body['message']['chat']['id']
    text = body['message']['text']

    # Initialize the OpenAI client with the new API format
    client = OpenAI(api_key=openai_api_key)

    try:
        # Use the updated method for generating text with OpenAI's completions API
        completion = client.completions.create(
            model="gpt-3.5-turbo",  # You can specify other models as needed
            prompt=text,  # Text input from the user
            max_tokens=100  # You can adjust max tokens as per your requirement
        )

        # Extract the generated text from the response
        openai_message = completion.choices[0].text.strip()

        # Sending the response to Telegram
        TELEGRAM_API_URL = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
        telegram_response = requests.post(TELEGRAM_API_URL, data={
            'chat_id': chat_id,
            'text': openai_message
        })

        # Print the Telegram API response for debugging
        print("Telegram API response:", telegram_response.json())

        # Return a status back to Lambda invocation
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'success', 'message': 'Message sent to Telegram'})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'status': 'failure', 'message': str(e)}),
        }
