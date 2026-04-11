import redis
from django.conf import settings
from .models import Product


# connecting to redis
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)


class Recommender:
    """This class helps on product recommendation."""

    def get_product_keys(self, id):
        return f"product:{id}:purchased_with"

    def products_bought(self, products):
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            # get the other products bought with each product.
            for with_id in product_ids:
                if with_id != product_id:
                    # increment the score for the products bought together.
                    r.zincrby(self.get_product_keys(product_id), 1, with_id)
