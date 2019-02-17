from __future__ import print_function

import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')
phone_number = '1-484-949-1383'  # change it to your phone number


def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    message = 'Hello from your IoT Button %s. Here is the full event: %s' % (event['serialNumber'], json.dumps(event))
    sns.publish(PhoneNumber=phone_number, Message=message)
    logger.info('SMS has been sent to ' + phone_number)
