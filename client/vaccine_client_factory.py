from client import cowin_service_client

def get_cowin_service_client():
    cowinServiceClient = cowin_service_client.Client()
    return cowinServiceClient