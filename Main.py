from Measurement import Measurement
import requests
import datetime

values = []

# WTPLCTAGID                   int            0
# READDATETIME                 datetime       1
# WINDSPEED                    float          2
# WINDDIRECTION                int            3
# TURBINEDIRECTION             int            4
# LOWSPEEDRPM                  float          5
# HIGHSPEEDRPM                 float          6
# BRAKEOPEN                    bool?          7
# EMERGENCYBUTTON              bool?          8
# MANUALMODE                   bool?          9
# STATESECTION                 bool?         10
# HUBBATTERYVOLTAGE            float         11
# EXTERNALTEMP                 float         12
# INTERNALTEMP                 float         13
# GEARBOXTEMP                  float         14
# HUBTEMP                      float         15
# BEARINGTEMP                  float         16
# GEARBOXOILLEVELLOW           bool?         17
# YAWDRIVEERROR                bool?         18
# ETHERNETCOMMS                bool?         19
# ALTSWITCHON                  bool?         20
# ALTSWITCHOFF                 bool?         21
# HIGHSPEEDRPMSETVALUE         int           22
# BLADEPITCHMAXSETVALUE        int           23
# PACALTERNATORVOLTAGEL1       float         24
# PACALTERNATORVOLTAGEL2       float         25
# PACALTERNATORVOLTAGEL3       float         26
# PACALTERNATORCURRENTL1       float         27
# PACALTERNATORCURRENTL2       float         28
# PACALTERNATORCURRENTL3       float         29
# PACALTERNATORFREQUENCY       int           30


querystring = 'windmeasurement, brakeopen=@BO@, emergencybutton=@EB@ windspeed=@WS@, winddirection=@WD@, ' \
              'turbinedirection=@TD@, highspeedrpm=@HSR@ @@DT@@'


def read_measurements():
    print Measurement.__doc__

    with open(r'WTPLCTAGS.csv', 'r') as f:
        for line in f:
            rows = line.split(";")
            if rows[1] == "READDATETIME":
                continue
            m = Measurement()
            m.readdatetime = datetime.datetime.strptime(rows[1], "%Y-%m-%d %H:%M:%S.%f").isoformat() + 'Z'
            m.windspeed = rows[2]
            m.winddirection = rows[3]
            m.turbinedirection = rows[4]
            m.lowspeedrpm = rows[5]
            m.highspeedrpm = rows[6]
            m.brakeopen = rows[7]
            m.emergencybutton = rows[8]

            values.append(m)


def print_measurements():
    for k in values:
        print k.readdatetime, k.windspeed, k.winddirection, k.turbinedirection, k.lowspeedrpm, k.highspeedrpm


if __name__ == "__main__":
    read_measurements()
    print_measurements()
    payload = 'windspeed,region=tr-center value=' + repr(windspeed)
    try:
        r = requests.post('http://dev.soyut.com:8086/write?db=mydb2', data=payload)
    except requests.exceptions.RequestException as e:
        print "Connection Error. Retrying - ", e
