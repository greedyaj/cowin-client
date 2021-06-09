from client import vaccine_client_factory

vaccine_service_client = vaccine_client_factory.get_cowin_service_client()
vaccines = ["COVAXIN", "COVISHIELD"]
def lookup_slots_by_pin(pin):
   print("service: lookup_slots_by_pin:" + pin)
   slotsData = []
   for vaccine in vaccines:
      data = vaccine_service_client.lookup_slots_by_pin(pin=pin, vaccine=vaccine)
      if data.__sizeof__() > 0:
         for center in data["centers"]:
            eachSlotData = {}
            slotsData.append(eachSlotData)
            for session in center["sessions"]:
               for slot in session["slots"]:
                  eachSlotData["centerName"] = center["name"]
                  eachSlotData["centerAddress"] = center["address"]
                  eachSlotData["ageLimit"] = session["min_age_limit"]
                  eachSlotData["vaccine"] = session["vaccine"]
                  eachSlotData["dose1"] = str(session["available_capacity_dose1"])
                  eachSlotData["dose2"] = str(session["available_capacity_dose2"])
                  eachSlotData["slot"] = slot
   return slotsData