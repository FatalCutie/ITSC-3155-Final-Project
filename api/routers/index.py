from . import orders, order_details, recipes, resources
<<<<<<< HEAD

=======
>>>>>>> f43cbf5d924e16c9c6b542e75fa750e29124302c

# resources won't import?
def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
