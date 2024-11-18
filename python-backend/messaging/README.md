# Messaging Module - Backend Toolkit

Welcome to the Messaging Module of the Backend Toolkit! This module is designed to be a plug-and-play solution for integrating messaging systems like RabbitMQ, Kafka, and AWS SQS into your backend application. It provides dynamic, loosely coupled, and reusable components for developers of all experience levels.

## Table of Content

1. [Features](#features)

2. [Supported Messaging Systems](#supported-messaging-systems)

3. [Installation](#installation)

4. [Directory Structure](#directory-structure)

5. [Quick Start Guide](#quick-start-guide)

6. [Detailed Instructions](#detailed-instructions)

   - [RabbitMQ](#rabbitmq)
   - [Kafka](#kafka)
   - [AWS SQS](#aws-sqs)

7. [Contributing](#contributing)

8. [License](#license)

## Features

- **Dynamic Configuration:** Pass settings like hosts, ports, credentials, and more at runtime.
- **Loose Coupling:** Works independently of the rest of your codebase.
- **Reusability:** Simplified interfaces for sending and receiving messages.
- **Beginner-Friendly:** Minimal setup with clear examples.
- **Scalable:** Easily extendable to include other messaging systems.

## supported-messaging-systems

- **RabbitMQ:** A lightweight message broker for reliable and asynchronous communication.
- **Kafka:** A distributed event-streaming platform for high-throughput, fault-tolerant messaging.
- **AWS SQS:** A fully managed message queuing service by Amazon.

## installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/backend-toolkit.git
   cd backend-toolkit/messaging
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt  # Python dependencies
   ```

3. For Kafka, ensure Kafka is installed and running locally or on a server.
4. For RabbitMQ, ensure RabbitMQ is installed and configured.
5. For AWS SQS, configure your AWS credentials.

## directory-structure

```plaintext
messaging/
├── rabbitmq/
│   ├── setup.py          # RabbitMQ connection setup
│   ├── message_util.py   # Utilities for publishing/consuming messages
├── kafka/
│   ├── setup.py          # Kafka connection setup
│   ├── message_util.py   # Utilities for publishing/consuming messages
├── sqs/
│   ├── setup.py          # AWS SQS connection setup
│   ├── queue_util.py     # Utilities for sending/receiving messages
├── README.md             # Documentation
```

## quick-start-guide

Here’s a quick example of how to use the messaging modules.

### RabbitMQ

1. Setup a queue and publish a message:

   ```python
   from rabbitmq.message_util import RabbitMQUtil


   rabbit_util = RabbitMQUtil(host='localhost', port=5672, username='guest', password='guest')
   rabbit_util.publish_message(queue_name='test_queue', message='Hello, RabbitMQ!')
   rabbit_util.close()
   ```

2. Consume messages from the queue:

   ```python
   Copy code
   def callback(ch, method, properties, body):
       print(f"Received message: {body.decode()}")

   rabbit_util.consume_messages(queue_name='test_queue', callback=callback)
   ```

### Kafka

1. Send a message to a Kafka topic:

   ```python
   from kafka.message_util import KafkaUtil

   kafka_util = KafkaUtil(bootstrap_servers='localhost:9092')
   kafka_util.send_message(topic='test_topic', message='Hello, Kafka!')
   ```

2. Consume messages from a Kafka topic:

   ```python
   def process_message(msg):
       print(f"Received message: {msg.value.decode('utf-8')}")

   kafka_util.consume_messages(topic='test_topic', group_id='test_group',    callback=process_message)
   ```

### AWS SQS

1. Send a message to an SQS queue:

   ```python
   from sqs.queue_util import SQSUtil

   sqs_util = SQSUtil(region_name='us-east-1', access_key='your-key', secret_key='your-secret')
   sqs_util.send_message(queue_name='test_queue', message='Hello, SQS!')
   ```

2. Receive messages from an SQS queue:

   ```python
   messages = sqs_util.receive_messages(queue_name='test_queue')
   for message in messages:
       print(f"Received: {message['Body']}")
   ```

## detailed-instructions

<!-- ### RabbitMQ

Prerequisites:

Install RabbitMQ: RabbitMQ Installation Guide
Setup:

Use the rabbitmq/setup.py module to configure the connection.
Use rabbitmq/message_util.py for queue operations.
Example Configuration: Modify the host, port, username, and password to match your RabbitMQ setup.

### kafka

Kafka
Prerequisites:

Install Kafka: Kafka Quickstart
Ensure the kafka-python library is installed.
Setup:

Use the kafka/setup.py module to configure producers and consumers.
Use kafka/message_util.py for topic operations.
Example Configuration: Modify bootstrap_servers to match your Kafka server.

### aws-sqs

AWS SQS
Prerequisites:

Set up AWS CLI and configure credentials: AWS CLI Configuration
Install boto3 library.
Setup:

Use sqs/setup.py to configure the AWS SQS client.
Use sqs/queue_util.py for message operations.
Example Configuration: Update region_name, access_key, and secret_key for your AWS setup. -->

## contributing

<!-- Contributing
We welcome contributions to enhance the Messaging Module!

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit your changes and push the branch:
bash
Copy code
git push origin feature-name
Open a pull request. -->

## license

<!-- License
This project is licensed under the MIT License. See the LICENSE file for details. -->

### Happy Coding! 🎉

This README serves as a starting point for anyone, from beginners to experienced developers, to integrate messaging systems with ease. If you have any questions or encounter issues, feel free to open a GitHub issue or reach out!
