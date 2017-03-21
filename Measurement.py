class Measurement:
    """Wind Turbine Measurement - PLC Tag Values"""

    def __init__(self):
        self.readdatetime = None
        self.windspeed = 0.0
        self.winddirection = 0
        self.turbinedirection = 0
        self.lowspeedrpm = 0.0
        self.highspeedrpm = 0.0
        self.brakeopen = 0
        self.emergencybutton = 0
        self.manualmode = 0
        self.statesection = 0
        self.hubbatteryvoltage = 0.0
        self.externaltemp = 0.0
        self.internaltemp = 0.0
        self.gearboxtemp = 0.0
        self.hubtemp = 0.0
        self.bearingtemp = 0.0
        self.gearboxoillevellow = 0
        self.yawdriveerror = 0
        self.ethernetcomms = 0
        self.altswitchon = 0
        self.altswitchoff = 0
        self.highspeedrpmsetvalue = 0
        self.bladepitchmaxsetvalue = 0
        self.pacalternatorvoltageL1 = 0.0
        self.pacalternatorvoltageL2 = 0.0
        self.pacalternatorvoltageL3 = 0.0
        self.pacalternatorcurrentL1 = 0.0
        self.pacalternatorcurrentL2 = 0.0
        self.pacalternatorcurrentL3 = 0.0
        self.pacalternatorfrequency = 0.0

    def create_query_string(self):
        querystring = 'windmeasurement,brakeopen=@BO@,emergencybutton=@EB@ windspeed=@WS@,winddirection=@WD@,' \
                      'turbinedirection=@TD@,highspeedrpm=@HSR@ @DT@'

        querystring = querystring.replace('@BO@', self.brakeopen)
        querystring = querystring.replace('@EB@', self.emergencybutton)
        querystring = querystring.replace('@WS@', self.windspeed)
        querystring = querystring.replace('@WD@', self.winddirection)
        querystring = querystring.replace('@TD@', self.turbinedirection)
        querystring = querystring.replace('@HSR@', self.highspeedrpm)
        querystring = querystring.replace('@DT@', self.readdatetime)
        return querystring
