{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def submit_to_sqs(json_payload):
    '''
    Submit a message into the SQS queue.
    '''
    import boto.sqs
    sqs_region = settings.SQS_REGION
    sqs_queue_name = settings.SQS_QUEUE_NAME

    conn = boto.sqs.connect_to_region(sqs_region)

    if conn:
        queue = conn.get_queue(sqs_queue_name)

        if queue:
            try:
                msg = conn.send_message(queue, json_payload)
                if msg.id:
                    # current_app.logger.debug("msg to queue: {}".format(json_payload))
                    return True
                else:
                    logger('Error sending message to queue.', subject='SQS Error',
                           data=json_payload, data_title='SQS Payload')
                    return False
            except Exception as exc:
                logger('Exception sending message to queue.', subject='SQS Error',
                       data=json_payload, data_title='SQS Payload', exc=exc)
                return False
        else:
            logger('get_queue({}) failed'.format(sqs_queue_name),
                   subject='SQS Error', data=json_payload, data_title='SQS Payload')
            return False
    else:
        logger('boto.sqs.connect_to_region({}) failed'.format(sqs_region),
               subject='SQS Error', data=json_payload, data_title='SQS Payload')
        return False



{% else %}
# If you are not using celery/tasks, you can remove this app
{% endif %}
