import os

def hello_every_minute():
    if not os.path.exists('/app/log/cron.log'):
        with open('/app/log/cron.log', 'a') as file:
            file.write()

    print("hello")
