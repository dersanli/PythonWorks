import sys
from Measurement import Measurement

values = []


def read_measurements():
    print Measurement.__doc__

    with open(r'WTPLCTAGS.csv', 'r') as f:
        for line in f:
            rows = line.split(";")
            if rows[1] == "READDATETIME":
                continue
            m = Measurement()
            m.windspeed = rows[2]
            m.winddirection = rows[3]
            
            values.append(m)


def print_measurements():
    for k in values:
        print k.windspeed, k.winddirection


if __name__ == "__main__":
    read_measurements()
    print_measurements()
