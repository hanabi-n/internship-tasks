# 1. Run receive.py file
# 2. Run send.py file

import json


class Car:
    instancesArr = []
    drivePath = 0

    def __init__(self, brand, model, door_count, fuel_cons, current_gas=0):
        self.brand = brand
        self.model = model
        self.door_count = door_count
        self.fuel_cons = fuel_cons
        if current_gas == 0:
            raise ValueError("No gasoline")
        else:
            self.current_gas = current_gas

        drivePath = round((self.current_gas * 100) / self.fuel_cons, 2)
        Car.instancesArr.append([self.model, drivePath])

    def getInfo(self):
        return (f"The brand of the machine: {self.brand} \n"
                f"Model: {self.model} \n"
                f"Number of doors: {self.door_count} \n"
                f"Fuel consumption: {self.fuel_cons} \n"
                f"Current gasoline: {self.current_gas} \n")

    def drive(self):
        return round((self.current_gas * 100) / self.fuel_cons, 2)

    def km_drive(self):
        return f"Kilometers that can be driven: {self.drive()}km"

    def hours_drive(self):
        return f"The numbers of hours that can be driven: {round(self.drive() / 80, 2)} hours\n"
        # assume that speed - 80km/h


class ProcessingMachines(object):
    def __init__(self, machine):
        self.machine = machine
        self.res = machine.fuel_cons

    def getResultsProcessing(self):
        array = Car.instancesArr
        myD = {}

        for n in range(len(array)):
            for k in range(len(array)):
                if array[n][1] - array[k][1] != 0:
                    myD[f'{array[n][0]} - {array[k][0]}'] = round(array[n][1] - array[k][1], 2)

                k += 1
        return myD


# |------JSON function------|

def encoder_machine(machine):
    if isinstance(machine, Car):  # converting to dictionary
        return {'Brand': machine.brand, 'Model': machine.model, 'Doors': machine.door_count,
                'Fuel consumption': machine.fuel_cons, 'Gasoline': machine.current_gas}

    raise TypeError(machine)


def mainContent():
    # |------I created instances, but to be honest I completely don't know anything------|
    # |------about machines. So I hope I wrote the right parameters :)            ------|

    print('--------------Output of mainClass.py----------------------------')
    machine1 = Car("Tayota", "machine1", 4, 15, 50)
    print(machine1.getInfo())
    print(machine1.km_drive())
    print(machine1.hours_drive())
    machine2 = Car("Mersedes", "machine2", 4, 11, 35)
    print(machine2.getInfo())
    print(machine2.km_drive())
    print(machine2.hours_drive())
    machine3 = Car("Mersedes", "machine3", 4, 9, 44)
    print(machine3.getInfo())
    print(machine3.km_drive())
    print(machine3.hours_drive())

    # ------|Results from ProcessingMachines class|------
    getElements = ProcessingMachines(machine1)
    print('\nSubtract objects: ', getElements.getResultsProcessing())

    print('--------------Output of mainClass.py----------------------------')

    # ------|Serialization|----------------------------------------------
    encoder_1 = json.dumps(machine1, default=encoder_machine)
    encoder_2 = json.dumps(machine2, default=encoder_machine)
    encoder_3 = json.dumps(machine3, default=encoder_machine)

    return encoder_1, encoder_2, encoder_3  # data will send to the send.py class




