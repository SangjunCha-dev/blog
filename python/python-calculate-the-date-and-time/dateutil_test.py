from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()

print("---------------------------------------------")
print(f"now = {now}")

print("---------------------------------------------")
print(f"microsecond before = {now - relativedelta(microseconds=1)}")
print(f"microsecond next   = {now + relativedelta(microseconds=1)}")

print("---------------------------------------------")
print(f"second before = {now - relativedelta(seconds=1)}")
print(f"second next   = {now + relativedelta(seconds=1)}")

print("---------------------------------------------")
print(f"minute before = {now - relativedelta(minutes=1)}")
print(f"minute next   = {now + relativedelta(minutes=1)}")

print("---------------------------------------------")
print(f"hour before = {now - relativedelta(hours=1)}")
print(f"hour next   = {now + relativedelta(hours=1)}")

print("---------------------------------------------")
print(f"day before = {now - relativedelta(days=1)}")
print(f"day next   = {now + relativedelta(days=1)}")

print("---------------------------------------------")
print(f"week before = {now - relativedelta(weeks=1)}")
print(f"week next   = {now + relativedelta(weeks=1)}")

print("---------------------------------------------")
print(f"month before = {now - relativedelta(months=1)}")
print(f"month next   = {now + relativedelta(months=1)}")

print("---------------------------------------------")
print(f"year before = {now - relativedelta(years=1)}")
print(f"year next   = {now + relativedelta(years=1)}")
