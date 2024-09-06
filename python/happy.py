import datetime

if __name__ == "__main__":
    today = datetime.datetime.now()
    msg = "Nothing interesting"
    if today.strftime("%m%d") == "0913":
        msg = "Happy Programmer's Day!"
    print(msg)
