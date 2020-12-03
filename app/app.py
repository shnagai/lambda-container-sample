def handler(event, context):
    for record in event['Records']:
        payload=record["body"]
        print('SQSキューの中身: {}'.format(str(payload)))