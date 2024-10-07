import CoolProp as CP


class Material:
    def __init__(self,density, TS = 0.0, YS = 0.0, BS = 0.0,  E=0.0, Charpy =0.0, Izod =0.0, 
                 resitivity=0.0, magneticPermeability =0.0, poissonsRatio =0.0,
                 specificHeatCapacity=0.0, k = 0.0, meanMeltingPoint = 0.0, CTE20C =0.0, CTE250C = 0.0, CTE500C = 0.0,shearStrength =0.0):
        self.density = density #kg/m3
        self.TS = TS #MPa
        self.YS = YS #MPa
        self.BS = BS #MPa
        self.E = E #GPa
        self.Charpy = Charpy #J
        self.Izod = Izod #J
        self.resistivity = resitivity #ohm-cm
        self.magneticPermeability = magneticPermeability
        self.poissonsRatio = poissonsRatio
        self.shearStrength = shearStrength
        self.specificHeatCapacity = specificHeatCapacity #J/kg-K
        self.k = k #W/m-K
        self.meanMeltingPoint = meanMeltingPoint #K
        self.CTE20C = CTE20C #micrometers/m-C
        self.CTE250C = CTE250C
        self.CTE500C = CTE500C


'''MATERIAL PROPERTIES SOURCED FROM MATWEB'''
SS316 = Material(density=8030, TS=580, YS=290, E=193, Charpy=105, Izod=129, resitivity=7.4e-5, magneticPermeability=1.008, specificHeatCapacity=500, k = 16.3, CTE20C = 16, CTE250C = 16.2, CTE500C = 17.5, meanMeltingPoint=1385)
Al6061 = Material(density=2700, TS=310, YS=276, BS=607, E=68.9, poissonsRatio=0.33, shearStrength= 207, resitivity=3.99e-6, specificHeatCapacity=896, k = 167, meanMeltingPoint=617)
# INCONEL718 = Material(density=c.lbcftokgcm(.296), TS=1375, YS=1100, resitivity= 0.000125, magneticPermeability=1.0011, CTE20C= 13, specificHeatCapacity=435)
def getMatProp(Material,prop):
    return getattr(Material, prop)