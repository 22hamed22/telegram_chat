# Telegram Chat - OpenAI API Integration

This repository demonstrates how to integrate the OpenAI API with Telegram Bot for automated responses. The code includes AWS Lambda setup instructions, OpenAI API usage, and Telegram bot integration. The following sections describe the setup, code deployment, and configuration.

## Step 1: Prepare Files ✅

To begin with, ensure you have the necessary files ready for upload:

1. **Part1.rar** and **Part2.rar**: These two parts of the compressed file will need to be extracted and re-zipped for upload.

### How to Extract and Zip the Files:
- Extract the contents of both **part1.rar** and **part2.rar** into a single folder.
- Re-zip the extracted folder to prepare for uploading.

### How to Upload the Files ✅:
- In the AWS Lambda console, use the **UPLOAD FROM** button located in the top-right corner of the code source section. This will automatically extract and replace the existing files with the new ones.

## Step 2: Upload Lambda Function Code ✅

Once the files are prepared:
1. **Lambda Function File**: Upload `lambda_function.py` in the **EXPLORER/** directory.

### Configuration Keys ✅:
Make sure to configure the following keys in your Lambda environment settings:
1. **OPENAI_API_KEY**: Your OpenAI API key.
2. **TELEGRAM_BOT_TOKEN**: Your Telegram bot token.

These keys are necessary to interact with both the OpenAI API and your Telegram bot.

## Step 3: Lambda Function Configuration ✅

1. **Function Timeout**: If necessary, increase the function timeout in AWS Lambda to accommodate longer API calls.
2. **Memory Settings**: Ensure that the Lambda function has enough memory allocated to handle the processing efficiently. This may depend on the size of the data being processed.

## Step 4: Running the Code ✅

Once your Lambda function is uploaded and configured:
- Trigger the Lambda function as required, and it will handle the communication between your Telegram bot and OpenAI API.

### Example Code to Trigger Function:
You can use the Telegram bot to send a message, which will trigger the Lambda function to get a response from OpenAI and send it back via the bot.

## Notes:

- **API Rate Limits**: Ensure you are aware of your API rate limits with OpenAI. If you hit the limit, the function may fail due to insufficient quota.
- **Security**: Make sure the API keys are securely stored and not hardcoded into the source code. You can use AWS Secrets Manager to securely handle API keys.

## Conclusion ✅

By following these steps, you will be able to set up a fully automated system using AWS Lambda, the OpenAI API, and a Telegram bot. This project can be expanded for more complex interactions, such as processing images or handling various types of user input.

Feel free to fork this repository and modify it according to your needs.

### Additional Enhancements:
- **Error Handling**: Add robust error handling to ensure smooth interaction between Telegram bot and OpenAI API.
- **Logging**: Implement logging to capture API errors or exceptions.
- **User Authentication**: Optionally, you could integrate user authentication via Telegram to limit who can access the service.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
