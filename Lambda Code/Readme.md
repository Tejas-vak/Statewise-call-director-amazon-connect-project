# AWS Lambda Function

This folder includes:

- `lambda_function.zip`: Contains only the Lambda function code. You can upload this to AWS Lambda and manually configure settings like runtime, handler, environment variables, memory, and permissions.

- `template.yml`: A SAM (Serverless Application Model) template that includes both the code and all configuration settings. Use this if you want to deploy the function with predefined settings.

## Deployment Options

### Option 1: Manual Setup (ZIP File)
1. Go to AWS Lambda Console.
2. Create or select a Lambda function.
3. Upload `lambda_function.zip`.
4. Manually configure runtime, handler, environment variables, etc.

### Option 2: Automated Setup (SAM Template)
1. Install the AWS SAM CLI.
2. Run:
   ```bash
   sam build
   sam deploy --guided
   ```
