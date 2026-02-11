from enum import StrEnum, auto
from src.domain.service.coupon.coupon_strategy import (
    BackFridayCoupon, NatalCoupon, CouponStrategy
)
class TypeCoupon(StrEnum):
    BLACK_FRIDAY = auto()
    NATAL = auto()

class StrategyCouponFactory:
    _strategy_map = {
        TypeCoupon.BLACK_FRIDAY: BackFridayCoupon(),
        TypeCoupon.NATAL: NatalCoupon()
    }

    @classmethod
    def create(cls, type_coupon: TypeCoupon) -> CouponStrategy:
        try:
            return cls._strategy_map[type_coupon]
        except KeyError:
            raise ValueError(f'Type {type_coupon} not supported')
