from random import randint

from celery import shared_task

from apps.car.models import Car
from apps.location.models import Location

BATCH_SIZE = 1000


@shared_task
def update_car_locations():
    """
    Background task to update the current locations of cars.

    Retrieves all cars and locations from the database and updates the current location of each car
    with a randomly selected location. Performs bulk updates in batches for efficiency.

    Note:
        This task is designed to be executed by a task queue system like Celery.
    """
    cars = Car.objects.all()
    locations_list = Location.objects.all()
    locations_count = Location.objects.count()
    cars_batch = []
    for car in cars:
        random_index = randint(0, locations_count - 1)
        car.current_location = locations_list[random_index]
        cars_batch.append(car)
        if len(cars_batch) >= BATCH_SIZE:
            Car.objects.bulk_update(cars_batch, ("current_location",))
            cars_batch = []
    if cars_batch:
        Car.objects.bulk_update(cars_batch, ("current_location",))
