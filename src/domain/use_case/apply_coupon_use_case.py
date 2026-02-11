from src.domain.entities.cart import Cart
from src.domain.service.coupon.apply_coupon import ApplyCouponStrategy
from src.domain.factories.coupon_strategy_factory import (
    TypeCoupon, StrategyCouponFactory
)


class ApplyCouponUseCase:
    def execute(self, cart: Cart, type_coupon: TypeCoupon) -> dict:
        subtotal = cart.get_subtotal()
        strategy = StrategyCouponFactory.create(type_coupon)
        discount = ApplyCouponStrategy(strategy).apply_discount(subtotal)
        new_subtotal = subtotal - discount
        return {
            "discount_value": discount,
            "new_subtotal": new_subtotal,
            "cart_id": cart.get_cart_id()
        }
