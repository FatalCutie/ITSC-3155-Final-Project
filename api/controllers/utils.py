from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import recipes as recipe_model


def validate_order_items(order_request, db: Session):
    for order_item in order_request.order_details:
        recipe = get_recipe_by_sandwich_and_resource(
            db, order_item.sandwich_id, order_item.resource_id
        )
        if not recipe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid order item: sandwich_id={order_item.sandwich_id}, resource_id={order_item.resource_id}"
            )


def get_recipe_by_sandwich_and_resource(db: Session, sandwich_id: int, resource_id: int):
    return db.query(recipe_model.Recipe).filter(
        recipe_model.Recipe.sandwich_id == sandwich_id,
        recipe_model.Recipe.resource_id == resource_id
    ).first()
