import kubernetes.client
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint

def create(user):
    #hay que cambiarlos para reutilizar desde varios script
    config.load_kube_config()
    client.configuration.debug = True
    v1 = client.CoreV1Api()
    namespace = 'users'
    body = {'metadata': {'name': user} }

    pretty = 'true'
    dry_run = 'All' # str | When present, indicates that modifications should not be persisted.

    try:
        api_response = v1.create_namespaced_service_account(namespace,body,dry_run=dry_run,
        pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_service_account: %s\n" % e)

def rolecreate(user,rol):
    pass
