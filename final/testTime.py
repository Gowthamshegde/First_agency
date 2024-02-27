last_run= "2024-02-26T12:27:44"
from datetime import datetime
last_run_date_object=datetime.strptime(last_run, "%Y-%m-%dT%H:%M:%S")

from_data= "2024/02/26T14:27:44"
from datetime import datetime
from_data_date_object=datetime.strptime(from_data, "%Y/%m/%dT%H:%M:%S")




if from_data_date_object<datetime.now() and last_run_date_object < from_data_date_object :
    print("good")

from datetime import datetime
current_date_time = datetime.now()

def main(input):
  import datetime
  import pytz

  # Get the current time in Indian time zone
  indian_timezone = pytz.timezone('Asia/Kolkata')
  now_in_india = datetime.datetime.now(indian_timezone)

  print(f"Current time in Indian time zone: {now_in_india}")




# x="2024-02-26 13:00:37"
# x_date_object=datetime.strptime(x, "%Y.%m.%d %H:%M:%S ")
# print(x_date_object)
# oldtime="2024-02-25 19:00:37.888749"

# import requests

