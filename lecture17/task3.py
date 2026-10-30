#SmartDevice

class SmartDevice:
    def __init__(self, brand) -> None:
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False    

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness) -> None:
        super().__init__(brand)
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            raise ValueError("Brightness is incorrect")

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand} Turned ON") 
        print(f"Brightness is {self.brightness}")

smartlight1 = SmartLight("Philips", 60)
smartlight1.turn_on()





