# Simple Producer / Consumer example for SQS

## Setup
1. Setup python env 
    ```shell script
    virtualenv -p /usr/bin/python3.7 venv
    source venv/bin/activate
    make init
    ```
2. Configure connection to SQS
    sdfgsdf
    
    
## AWS supports 2 types of SQS queue
### Standard Queue // Fifo Queue
#### Features
* unlimited throughput: nearly unlimited number of transactions per second per API action
* at-least-once delivery: this implies that duplication of messages is possible
* best-effort ordering 
#### Configuration Options
##### Queue Attributes
* **Default Visibility Timeout**: The length of time (in seconds) that a message received from a queue will be invisible to other receiving components.
    * between 0 seconds and 12 hours
    * default: 30 seconds. 0 seconds and 12 hours.

* **Message Retention Period**: The amount of time that Amazon SQS will retain a message if it does not get deleted.
    * between 1 minute and 14 days
    * default: 4 days

* **Maximum Message Size**: Maximum message size (in bytes) accepted by Amazon SQS.
    * between 1 and 256 KB
    * default: 256 KB

* **Delivery Delay**: The amount of time to delay the first delivery of all messages added to this queue.
    * between 0 seconds and 15 minutes.
    * default: 0 seconds

* **Receive Message Wait Time**: The maximum amount of time that a long polling receive call will wait for a message to become available before returning an empty response.
    * between 0 and 20 seconds.
    * default: 0 seconds
##### Dead letter queue settings
* **Use Redrive Policy**: Send messages into a dead letter queue after exceeding the Maximum Receives.
    * yes/no
    * if **yes**
        * Select an existing queue that serves as the dead letter queue
        * Maximum Receives: The maximum number of times a message can be received before it is sent to the Dead Letter Queue. Value must be between 1 and 1000.
        
##### Server-Side Encryption (SSE) Settings
* yes/no
* **Data Key Reuse Period**:  The time period during which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling KMS again.
    * between 1 minute and 24 hours
    * default: 5 minutes


### Fifo Queue (extra config options)
* Name of a fifo queue must be suffixed with **.fifo** 
* **Content-Based Deduplication**: Use a SHA-256 hash of the body of the message (but not the attributes of the message) to generate the content-based Message Deduplication ID.
    * yes/no

