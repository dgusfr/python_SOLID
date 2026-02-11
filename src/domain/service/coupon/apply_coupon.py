from src.domain.service.coupon.coupon_strategy import CouponStrategy


class ApplyCouponStrategy:
    def __init__(self, strategy: CouponStrategy):
        self._strategy = strategy

    def update_strategy(self, new_strategy: CouponStrategy):
        self._strategy = new_strategy

    def apply_discount(self, value: float):
        return self._strategy.apply_discount(value)
