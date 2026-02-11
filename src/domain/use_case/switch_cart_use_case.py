from typing import List
from src.domain.ports.outbound.repository_protocol import CartRepositoryProtocol
from src.domain.ports.outbound.notifier_protocol import NotifyByEmail, NotifyByCellPhone
from src.domain.value_object.phone import Phone
from src.domain.value_object.email import Email
from src.domain.entities.cart import CartStatus


class SwitchCartUseCase:
    def __init__(
            self,
            repository: CartRepositoryProtocol,
            notify_emails: List[NotifyByEmail],
            notify_cellphones: List[NotifyByCellPhone],
    ):
        self._repository = repository
        self._notify_emails = notify_emails
        self._notify_cellphones = notify_cellphones

    def execute(self, cart_id: str, cellphone: Phone, email: Email, new_status: CartStatus):
        cart_entity = self._repository.read(cart_id)
        cart_entity.switch(new_status)
        message = f"cart change status: {new_status.value}"
        for notify_email in self._notify_emails:
            notify_email.send_message(message, email)

        for notify_cellphone in self._notify_cellphones:
            notify_cellphone.send_message(message, cellphone)
        return cart_entity



