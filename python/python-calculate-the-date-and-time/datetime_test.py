from datetime import datetime, timedelta

now = datetime.now()

print("---------------------------------------------")
print(f"now = {now}")

print("---------------------------------------------")
print(f"microsecond before = {now - timedelta(microseconds=1)}")
print(f"microsecond next   = {now + timedelta(microseconds=1)}")

print("---------------------------------------------")
print(f"millisecond before = {now - timedelta(milliseconds=1)}")
print(f"millisecond next   = {now + timedelta(milliseconds=1)}")

print("---------------------------------------------")
print(f"second before = {now - timedelta(seconds=1)}")
print(f"second next   = {now + timedelta(seconds=1)}")

print("---------------------------------------------")
print(f"minute before = {now - timedelta(minutes=1)}")
print(f"minute next   = {now + timedelta(minutes=1)}")

print("---------------------------------------------")
print(f"hour before = {now - timedelta(hours=1)}")
print(f"hour next   = {now + timedelta(hours=1)}")

print("---------------------------------------------")
print(f"day before = {now - timedelta(days=1)}")
print(f"day next   = {now + timedelta(days=1)}")

print("---------------------------------------------")
print(f"week before = {now - timedelta(weeks=1)}")
print(f"week next   = {now + timedelta(weeks=1)}")

print("---------------------------------------------")
print(f"week before = {now - timedelta(days=1, hours=1, minutes=1)}")
print(f"week next   = {now + timedelta(days=1, hours=1, minutes=1)}")
