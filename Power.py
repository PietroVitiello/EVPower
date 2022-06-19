class Power():

    def __init__(self, weight, wheel_radius, max_speed, time2max):
        self.m = weight + 80
        self.r = wheel_radius
        self.max_v = max_speed / 3.6  #from km/h to m/s
        self.time2max = time2max
        self.a = self.max_v / time2max #m/s^2

        self.rho = 1.23 #kg/m^3
        self.Cw = 0.4 #air resistance coeficcient
        self.Crr = 0.02 #rolling resistance coefficient

        self.area = 0.9 #m^2
        self.motor_eff = 0.85 #efficiency of electric motor
        self.transmission_efficiency = 0.95 #power loss in transmission is about 5% 

    ## Set parameters
    def setRho(self, rho):
        self.rho = rho

    def setCw(self, cw):
        self.Cw = cw

    def setMaxv(self, v):
        self.max_v = v * 3.6

    def setAcc(self, time):
        self.a = self.max_v / time

    def setArea(self, area=0.9, width=None, heigth=None):
        if width != None and height != None:
            self.area = width * height
        else:
            self.area = area

    def setMotorEff(self, eff):
        self.motor_eff = eff

    def setTransmEff(self, eff):
        self.transmission_efficiency = eff

    ## Get parameters

    ## Methods
    def accDistance(self):
        return 0.5*self.a*(self.time2max**2)

    def airResistance(self, v):
        return 0.5*self.rho*(v**2)*self.Cw*self.area

    def accAirResPower(self):
        const = (1/6)*self.rho*self.Cw*self.area
        return const * self.max_v

    def rollingResistance(self):
        weight = self.m * 9.81
        return self.Crr * weight

    def accRolResPow(self):
        d = self.accDistance()
        res = self.rollingResistance()
        return (d * res) / self.time2max

    def dragForce(self, v):
        air_f = airResistance(v)
        rolling_f = rollingResistance()
        return air_f + rolling_f

    def cruisePower(self, v):
        drag_force = dragForce(v)
        return drag_force * v

    def accPower(self):
        Eacc = 0.5 * self.m * (self.max_v**2) #Energy needed for acceleration (1/2 mv^2)
        time = self.time2max #Time taken to reach desired velocity

        Pacc = Eacc / time
        Pair = self.accAirResPower()
        Prol = self.accRolResPow()
        return Pacc + Pair + Prol