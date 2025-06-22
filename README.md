# 📞 State-Wise Call Routing System Using Amazon Connect & AWS Lambda

## 📝 Project Overview

This project implements a robust and scalable solution to enhance customer service efficiency by integrating **Amazon Connect**, **AWS Lambda**, and the **Numverify API**. The system validates incoming customer phone numbers, determines their geographic location, and dynamically routes calls to the appropriate state-specific customer service queue. This ensures personalized support and optimized call handling across regions.

## 🎯 Key Objectives

- Automate call routing based on caller location.
- Improve customer experience through targeted support.
- Ensure data accuracy and system reliability using cloud-native services.

## 🛠️ Services Used & Responsibilities

### 🔹 AWS Lambda

- **Phone Number Validation**: Developed and deployed Python code to validate incoming phone numbers.
- **Location Detection**: Implemented logic to determine caller location using the Numverify API.
- **Performance Optimization**: Ensured minimal latency and high reliability in Lambda execution.

### 🔹 Amazon Connect

- **Call Management**: Configured Amazon Connect to handle and manage incoming calls.
- **Lambda Integration**: Integrated Lambda functions within contact flows to process caller data.
- **Call Flow Design**: Designed dynamic call flows to route calls based on state information.
- **Performance Monitoring**: Continuously monitored and refined call handling for better customer satisfaction.

### 🔹 Numverify API

- **Data Validation**: Used Numverify to validate phone numbers and retrieve location metadata.
- **Lambda Integration**: Seamlessly connected the API with Lambda for real-time data processing.
- **Accuracy Assurance**: Ensured high reliability of location data for precise call routing.

### 🔹 Amazon CloudWatch

- **Monitoring & Logging**: Utilized CloudWatch to monitor Lambda performance and troubleshoot issues.
- **Operational Insights**: Gained visibility into function execution and system health.

## 📈 Outcome

The system successfully routes customer calls to the correct regional support teams, reducing wait times and improving service quality. It leverages serverless architecture for scalability and cost-efficiency, making it a powerful solution for customer-centric organizations.
