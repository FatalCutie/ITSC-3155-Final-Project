from . import orders, order_details, recipes, sandwiches, resources, person

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    person.Base.metadata.create_all(engine)
    #coupon.Base.metadata.create_all(engine) not working?
