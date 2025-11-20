# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import datetime

from firebase_admin import messaging

def send_to_token():
    # [START send_to_token]
    registration_token = 'YOUR_REGISTRATION_TOKEN'

    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
    # [END send_to_token]

def send_to_topic():
    # [START send_to_topic]
    topic = 'highScores'

    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
    # [END send_to_topic]

def send_to_condition():
    # [START send_to_condition]
    condition = "'stock-GOOG' in topics || 'industry-tech' in topics"

    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        condition=condition,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
    # [END send_to_condition]

def send_dry_run():
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token='token',
    )

    response = messaging.send(message, dry_run=True)
    print('Dry run successful:', response)
    # [END send_dry_run]

def android_message():
    message = messaging.Message(
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                title='$GOOG up 1.43% on the day',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        topic='industry-tech',
    )
    return message

def apns_message():
    message = messaging.Message(
        apns=messaging.APNSConfig(
            headers={'apns-priority': '10'},
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    alert=messaging.ApsAlert(
                        title='$GOOG up 1.43% on the day',
                        body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                    ),
                    badge=42,
                    custom_data={"event": "end"}  # Ensure compliance with Apple's APNs requirements
                ),
            ),
        ),
        topic='industry-tech',
    )
    return message

def webpush_message():
    message = messaging.Message(
        webpush=messaging.WebpushConfig(
            notification=messaging.WebpushNotification(
                title='$GOOG up 1.43% on the day',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                icon='https://my-server/icon.png',
            ),
        ),
        topic='industry-tech',
    )
    return message

def all_platforms_message():
    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        topic='industry-tech',
    )
    return message

def subscribe_to_topic():
    topic = 'highScores'
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    response = messaging.subscribe_to_topic(registration_tokens, topic)
    print(response.success_count, 'tokens were subscribed successfully')

def unsubscribe_from_topic():
    topic = 'highScores'
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    response = messaging.unsubscribe_from_topic(registration_tokens, topic)
    print(response.success_count, 'tokens were unsubscribed successfully')

def send_each():
    registration_token = 'YOUR_REGISTRATION_TOKEN'
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=registration_token,
        ),
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='readers-club',
        ),
    ]

    response = messaging.send_each(messages)
    print(f'{response.success_count} messages were sent successfully')

def send_each_for_multicast_and_handle_errors():
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        'YOUR_REGISTRATION_TOKEN_N',
    ]

    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_each_for_multicast(message)
    if response.failure_count > 0:
        responses = response.responses
        failed_tokens = []
        for idx, resp in enumerate(responses):
            if not resp.success:
                failed_tokens.append(registration_tokens[idx])
        print(f'List of tokens that caused failures: {failed_tokens}')