# Amazon Connect Contact Flows

This folder contains two Amazon Connect contact flows exported as `.json` files:

- **main-contact-flow.json**: The primary flow that handles incoming contacts.
- **customer-flow.json**: A connected flow used for handling specific customer interactions.

## How to Use

1. Log in to your Amazon Connect instance.
2. Go to **Contact Flows** and click **Import Flow**.
3. Import both `.json` files.
4. Ensure that all referenced resources (queues, prompts, Lambda functions) exist in your instance.

## Notes

- These flows are interconnected. Make sure to import both for full functionality.
- Queue names and other resources must be manually created if they don’t already exist.
