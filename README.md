# Telegram Chat - OpenAI API Integration

This repository demonstrates how to integrate the OpenAI API with a Telegram bot for automated responses using AWS Lambda. It covers setup, deployment, and configuration.

You can **customize** the system to fit your company's needs, whether it's adjusting OpenAI responses, adding business logic, or workflows. Ensure you stay within **usage quotas** to avoid penalties or interruptions.

## Step 1: Prepare Files ✅

1. **Part1.rar** and **Part2.rar**: Extract and re-zip them into a single folder.
2. **Upload** the zipped folder via the **UPLOAD FROM** button in the AWS Lambda console.

## Step 2: Upload Lambda Code ✅

1. Upload `lambda_function.py` into the **EXPLORER/** directory.
2. Set the following keys in Lambda environment settings:
   - **OPENAI_API_KEY**: Your OpenAI API key.
   - **TELEGRAM_BOT_TOKEN**: Your Telegram bot token.

## Step 3: Lambda Function Configuration ✅

1. **Function Timeout**: Increase the timeout to handle longer API calls if necessary.
2. **Memory Settings**: Ensure adequate memory for processing.

## Step 4: Running the Code ✅

Trigger the Lambda function via the Telegram bot. It will get responses from OpenAI and send them back via the bot.

### Example Trigger:
Use the Telegram bot to send a message, which will trigger the Lambda function.

## Notes: 

- **API Rate Limits**: Ensure awareness of your OpenAI API rate limits.
- **Security**: Securely store API keys using AWS Secrets Manager.

## Conclusion ✅

This guide sets up an automated system using AWS Lambda, OpenAI API, and Telegram bot. Feel free to fork and customize as needed.

### Additional Enhancements:
- **Error Handling**: Add robust error handling for smoother interactions.
- **Logging**: Implement logging for capturing API errors.
- **User Authentication**: Optionally integrate Telegram authentication for service access.

## License

Licensed under the MIT License - see [LICENSE.md](LICENSE.md).
