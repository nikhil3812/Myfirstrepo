import datetime
import time
import os
import platform

def get_alarm_time():
    while True:
        alarm_input = input("Set alarm time (HH:MM, 24-hour format): ")
        try:
            alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M").time()
            return alarm_time
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM.")

def play_alarm_sound():
    # Try to make a beep sound depending on OS
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 1000)  # frequency, duration
        else:
            print("\a")  # Beep for Linux/macOS
    except:
        print("Unable to play sound. Alarm triggered!")

def alarm_clock():
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time.strftime('%H:%M')}. Waiting...")

    while True:
        now = datetime.datetime.now().time().replace(second=0, microsecond=0)
        if now == alarm_time:
            print("⏰ Alarm! Wake up!")
            for _ in range(5):  # Repeat sound
                play_alarm_sound()
                time.sleep(1)
            break
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    alarm_clock()
