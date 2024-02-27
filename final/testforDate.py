x="09-09-2023 13:19:25 UTC"
from datetime import datetime
input_datetime = datetime.strptime(x, "%d-%m-%Y %H:%M:%S UTC")
last_pl_date_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
last_pl_date=datetime.strptime(last_pl_date_str, "%Y-%m-%d %H:%M:%S")


y="08-09-2023 13:19:25 UTC"

from datetime import datetime
input_datetime2 = datetime.strptime(y, "%d-%m-%Y %H:%M:%S UTC")
last_pl_date_str2 = input_datetime2.strftime("%Y-%m-%d %H:%M:%S")
last_pl_date2=datetime.strptime(last_pl_date_str2, "%Y-%m-%d %H:%M:%S")

print(last_pl_date.date()>last_pl_date2.date())