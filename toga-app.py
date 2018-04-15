import toga
import time

# Imports the Google Cloud client library
from google.cloud import pubsub_v1

# Variables
project_name = "track-it-now"
topic_name = "my-topic"

# Instantiates a client
publisher = pubsub_v1.PublisherClient()
# The resource path for the new topic contains the project ID and the topic name.
topic_path = publisher.topic_path(project_name, topic_name)


def publish_messages(project_name, topic_name):
    ''' Publishes multiple messages to a Pub/Sub topic. '''

    for n in range(1, 11):
        data = u'Message number {}'.format(n)
        # Data must be a bytestring
        data = data.encode('utf-8')
        publisher.publish(topic_path, data=data)
        print('Published message is: {}'.format(data))
        time.sleep(3)

def send_telemetrydata(widget):
    # Send telemetry data to Google Cloud
    print("==========>Started sending telemetry data..")
    publish_messages(project_name, topic_name)
    print("==========>Successfully sent data.\n")

def build(app):
    main_box = toga.Box()

    main_label = toga.Label('Trackersweb.. track anything, anyscale')
    main_button = toga.Button('Track me!', on_press=send_telemetrydata)

    main_box.add(main_label)
    main_box.add(main_button)

    return main_box

def main():
    return toga.App('Trackersweb', 'com.trackersweb', startup=build)

if __name__ == '__main__':
    main().main_loop()
