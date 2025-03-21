# Telegram Chat - OpenAI API Integration(serverless)
 
integrate the OpenAI API with a Telegram bot for automated responses using AWS Lambda. It covers setup, deployment, and configuration.

You can **customize** the system to fit your company's needs, whether it's adjusting OpenAI responses, adding business logic, or workflows. Ensure you stay within **usage quotas** to avoid penalties or interruptions.

## Step 1: Prepare pkg Files ✅

1. **Part1.rar** and **Part2.rar**: Extract and re-zip them into a single folder.
2. **Upload** the zipped folder via the **UPLOAD FROM** button in the AWS Lambda console.

## Step 2: Upload Lambda Code ✅

1. Upload `lambda_function.py` into the **EXPLORER/** directory.
2. Set the following keys in Lambda environment settings:
   - **OPENAI_API_KEY**: Your OpenAI API key.
   - **TELEGRAM_BOT_TOKEN**: Your Telegram bot token.

## Test Event ✅

You can use this test event to check the integration:

```json
{
  "body": {
    "message": {
      "chat": {
        "id": 123456
      },
      "text": "Hello, bot!"
    }
  }
}
```

## Notes: 

- **Function Timeout**: Increase the timeout to handle longer API calls if necessary.
- **Memory Settings**: Ensure adequate memory for processing.
- **API Rate Limits**: Ensure awareness of your OpenAI API rate limits.
- **Security**: Securely store API keys using AWS Secrets Manager.


