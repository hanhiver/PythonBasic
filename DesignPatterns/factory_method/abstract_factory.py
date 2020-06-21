'''Abstract Factory'''

class AbstractFactory(object):
    computer_name = ''
    def createCpu(self):
        pass
    def createMainboard(self):
        pass 

class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer '
    def createCpu(self):
        return IntelCpu('I7-10700')
    def createMainboard(self):
        return IntelMainboard('Intel-X490')

class AmdFactory(AbstractFactory):
    computer_name = 'AMD Rayzen computer '
    def createCpu(self):
        return AmdCpu('Rayzen 3700X')
    def createMainboard(self):
        return AmdMainboard('AMD-B450')

class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''

class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series

class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series

class AbstractMainboard(object):
    series_name = ''

class IntelMainboard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series

class AmdMainboard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series

class ComputerEngineer(object):
    def makeComputer(self, factory_obj):
        self.prepareHardwares(factory_obj)
    
    def prepareHardwares(self, factory_obj):
        self.cpu = factory_obj.createCpu()
        self.mainboard = factory_obj.createMainboard()
        info = '''
        ------- computer [%s] info:
        cpu: %s
        mainboard: %s
        -------- End --------
        ''' % (factory_obj.computer_name, self.cpu.series_name, self.mainboard.series_name)
        
        print(info)

if __name__ == '__main__':
    engineer = ComputerEngineer()

    intel_factory = IntelFactory() 
    engineer.makeComputer(intel_factory)

    amd_factory = AmdFactory()
    engineer.makeComputer(amd_factory)
