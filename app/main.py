from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cb = CinemaBar()
    customer_objects = []
    for cust in customers:
        customer_obj = Customer(name=cust["name"], food=cust["food"])
        customer_objects.append(customer_obj)
        cb.sell_product(customer=customer_obj, product=customer_obj.food)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
