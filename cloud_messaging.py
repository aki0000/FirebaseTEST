from firebase_admin import messaging


class cloud_messaging:
    # トークンに対して送信
    def sendToToken(self, token, title, body, priority=10, badge=1):
        message = messaging.Message(
            apns=messaging.APNSConfig(
                headers={'apns-priority': str(priority)},
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        alert=messaging.ApsAlert(
                            title=title,
                            body=body,
                        ),
                        badge=badge,
                        sound='default',
                    ),
                ),
            ),
            token=token,
        )
        response = messaging.send(message)
        print('Successfully sent message: ', response)
        return response

    # トピックに対して送信
    def sendToTopic(self, topic, title, body, priority=10, badge=1):
        message = messaging.Message(
            apns=messaging.APNSConfig(
                headers={'apns-priority': str(priority)},
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        alert=messaging.ApsAlert(
                            title=title,
                            body=body,
                        ),
                        badge=badge,
                        sound='default',
                    ),
                ),
            ),
            topic=topic,
        )
        response = messaging.send(message)
        print('Successfully sent message: ', response)
        return response