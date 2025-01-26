class Car():
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def acelerate(self):
        return f'A {self.brand} do modelo {self.model} está acelerando'
    
    def breaak(self):
        return f'A {self.brand} {self.model} freiou'
    
    def actualSpeed(self):
        return f'A {self.model} foi detectado numa velocidade de {self.speed}km/h'
    
car1 = Car(brand='Ferrari', model='488 pista',speed=280)
car2 = Car(brand='Lamborghini', model='Aventador',speed=250)

print(car1.acelerate())
print(car1.actualSpeed())
print(car2.breaak())