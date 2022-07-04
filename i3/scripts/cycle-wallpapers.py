import os, time

fileDir = "{}/.config/i3/wallpapers/8bit-day/{}".format(os.getenv("HOME"), '{}')
hourRange = {
    "6-10":"Morning.png",
    "10-12":"LateMorning.png",
    "12-15":"Afternoon.png",
    "15-17":"LateAfternoon.png",
    "17-19":"Evening.png",
    "19-21":"LateEvening.png",
    "21-24":"Night.png",
    "0-6":"LateNight.png",
}

def run():
    while(True):
        now = time.localtime().tm_hour
        for interval, img in hourRange.items():
            intervalStart, intervalEnd = [int(x) for x in interval.split('-')]
            if now > intervalStart and now <= intervalEnd:
                os.system('feh --bg-scale {}'.format(fileDir.format(img)))
        time.sleep(5)

if __name__=='__main__':
    run()
