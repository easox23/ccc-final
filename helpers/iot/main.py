from awscrt import mqtt
from awsiot import mqtt_connection_builder
import json
import time

IOT_ENDPOINT = "<ID>-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "client-1"
TOPIC = "topic/hello"

CERT_FILE = "certs/certificate.pem.crt"
KEY_FILE = "certs/private.pem.key"
CA_FILE = "certs/AmazonRootCA1.pem"

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=IOT_ENDPOINT,
    cert_filepath=CERT_FILE,
    pri_key_filepath=KEY_FILE,
    ca_filepath=CA_FILE,
    client_id=CLIENT_ID,
    clean_session=True,
    keep_alive_secs=30,
)

mqtt_connection.connect().result()

payload = {
    "message": "hello from python",
    "ts": int(time.time())
}

mqtt_connection.publish(
    topic=TOPIC,
    payload=json.dumps(payload),
    qos=mqtt.QoS.AT_LEAST_ONCE,
)

mqtt_connection.disconnect().result()
