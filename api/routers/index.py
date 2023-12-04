from . import orders, order_details, recipes, resources, review, sandwiches

# resources won't import?
def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(review.router)
    app.include_router(sandwiches.router)