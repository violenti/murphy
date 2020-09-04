import kubernetes.client
from kubernetes import client, config

from kubernetes.client.rest import ApiException
from pprint import pprint
from kubernetes import config
import base64


def secret(secretname):

    config.load_kube_config()
    client.configuration.debug = True
    v1 = client.CoreV1Api()
    namespace = 'users'
    secret = (v1.read_namespaced_secret(secretname,namespace).data)
    ca = secret.get('ca.crt')
    token = secret.get('token')
    print (base64.b64decode(ca))
    print (base64.b64decode(token))
secret()
