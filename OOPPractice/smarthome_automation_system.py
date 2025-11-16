class SmartHome:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def remove_device(self, device_name):
        for device in self._devices:
            if device.get_name() == device_name:
                self._devices.remove(device)
        

    def activate_all(self):
        for device in self._devices:
            device.turn_on()

    def perform_all_actions(self):
        for device in self._devices:
            device.perform_action()

    def get_device(self, device_name):
        for device in self._devices:
            if device.get_name() == device_name:
                return device
        raise ValueError("Device not found!")
    
    def turn_off_all(self):
        for device in self._devices:
            device.turn_off()

class Device:
    def __init__(self, name, status):
        self._name = name
        self._status = status

    def turn_on(self):
        self._status = 1

    def turn_off(self):
        self._status = 0

    def perform_action(self): # Polymorphism
        pass

    # Public Functions

    def get_status(self):
        return self._status

    def get_name(self):
        return self._name

class Light(Device):
    def __init__(self, brightness = 0):
        super().__init__(name = "myLight", status = 0)
        self._brightness = brightness

    def perform_action(self):
        if self._status == 1:
            return print("Brightness adjusted", self._brightness)
        else:
            return print("Not Open")

    def set_brightness(self, value):
        self._brightness = value

class Thermostat(Device):
    def __init__(self, temperature = 25):
        super().__init__(name = "myThermo", status = 0)
        self._temperature = temperature

    def perform_action(self):
        if self._status == 1:
            return print("Temperature Changed", self._temperature)
        else:
            return print("Not Open")
    
    def set_temperature(self, value):
        self._temperature = value

class SecurityCamera(Device):
    def __init__(self, resolution = 480):
        super().__init__(name = "mySecCam", status = 0)
        self._resolution = resolution

    def perform_action(self):
        if self._status == 1:
            return print("Recording started", self._resolution)
        else:
            return print("Not Open")
    
    def set_resolution(self, value):
        self._resolution = value

    def get_resolution(self):
        return print(self._resolution)


myHome = SmartHome()
myLight = Light()
myThermo = Thermostat()
mySecCam = SecurityCamera()
myDevices = [myLight, myThermo, mySecCam]

for device in myDevices:
    myHome.add_device(device)

myLight.set_brightness(80)
myThermo.set_temperature(18)
mySecCam.set_resolution(4320)

print("-----------")

myHome.activate_all()
myHome.perform_all_actions()

print("-----------")

myHome.turn_off_all()
myHome.perform_all_actions()

print("-----------")

myHome.activate_all()
myHome.remove_device("myThermo")
myHome.perform_all_actions()

print("-----------")
