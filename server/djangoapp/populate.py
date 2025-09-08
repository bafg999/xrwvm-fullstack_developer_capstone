from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology", "createMarkYear": 1933},
        {"name": "Mercedes", "description": "Great cars. German technology", "createMarkYear": 1926},
        {"name": "Audi", "description": "Great cars. German technology", "createMarkYear": 1909},
        {"name": "Kia", "description": "Great cars. Korean technology", "createMarkYear": 1944},
        {"name": "Toyota", "description": "Great cars. Japanese technology", "createMarkYear": 1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'], 
                description=data['description'],
                createMarkYear=data['createMarkYear'],
            )
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "carMake": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "carMake": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "carMake": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "carMake": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "carMake": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "carMake": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "carMake": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "carMake": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "carMake": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "carMake": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "carMake": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "carMake": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "carMake": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "carMake": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "carMake": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            carMake=data['carMake'],
            type=data['type'],
            year=data['year'],
            dealerId=1 
        )