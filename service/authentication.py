from client import vaccine_client_factory

vaccine_service_client = vaccine_client_factory.get_cowin_service_client()

def generate_otp(mobileNumber):
   return vaccine_service_client.generate_otp(mobileNumber=mobileNumber)["txnId"] 

def confirm_otp(txnId, otp):
   return vaccine_service_client.confirm_otp(txnId=txnId, otp=otp)["token"] 
