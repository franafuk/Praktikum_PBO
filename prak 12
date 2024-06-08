import datetime
import pytz


def my_decorator(inner):
    def inner_decorator():

        utc_now = datetime.datetime.now(pytz.utc)

        jakarta_tz = pytz.timezone("Asia/Jakarta")
        jakarta_now = utc_now.astimezone(jakarta_tz)

        print("Nama : Francisco\nNim : 064002300044\n")
        print("TimeZone : Asia/Jakarta")

        print("Tanggal :", jakarta_now.strftime("%d-%m-%Y"))
        print("waktu :", jakarta_now.strftime("%H:%M:%S:%f"))

        inner()
        utc_now = datetime.datetime.now(pytz.utc)
        jakarta_now = utc_now.astimezone(jakarta_tz)

        print("\nberubah menjadi : ")
        print("Tanggal :", jakarta_now.strftime("%d-%m-%Y"))
        print("waktu :", jakarta_now.strftime("%H:%M:%S:%f"))

    return inner_decorator


@my_decorator
def decorated():
    pass


if __name__ == "__main__":
    decorated()
