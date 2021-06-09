import requests
import json
from datetime import date

class Client:

    def __init__(self):
       self.lookupByPincodeUrl = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
       self.generateOTPUrl = "https://cdn-api.co-vin.in/api/v2/auth/generateOTP"
       self.confirmOTPUrl = "https://cdn-api.co-vin.in/api/v2/auth/confirmOTP"

    def generate_otp(self, mobileNumber):
        #TODO
        return {}
        #return self.cowinServiceClient.get_otp(mobile=mobileNumber)["txnId"]
    
    def confirm_otp(self, txnId, otp):
        #TODO
        return {}
        #return self.cowinServiceClient.confirm_otp(otp=otp, txn_id=txnId)["token"]

    def lookup_slots_by_pin(self, pin, vaccine):
        today = date.today()
        today = today.strftime("%d-%m-%y")
        url = self.lookupByPincodeUrl + f"date={today}&pincode={pin}&vaccine={vaccine}"
        print("client: lookup_slots_by_pin: url-" + url)
        response = requests.get(url)
        if (response.status_code == 200):
            return json.loads(response.text)
        else:
            return {}
