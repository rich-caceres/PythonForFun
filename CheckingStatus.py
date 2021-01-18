import urllib.request
import time


def CheckSiteStatus(website):

    status_code = urllib.request.urlopen(website).getcode()

    if status_code != 200 or status code != 302:

        print(f"The current code is {status_code}, please check configuration.")

    else:

        print(f"{status_code} was returned. all is well.")


if __name__ == '__main__':

    try:
        while True:

            time.sleep(30)
            CheckSiteStatus("https://starsales.patracompany.com/")
    except KeyboardInterrupt:
            pass
