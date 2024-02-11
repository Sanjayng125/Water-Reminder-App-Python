import time
from plyer import notification

while True:
    if __name__ == "__main__":
        notification.notify(
            title="Drink Water",
            message="Time to get hydrated",
            app_icon="water_glass.ico"
        )
        time.sleep(60*60)