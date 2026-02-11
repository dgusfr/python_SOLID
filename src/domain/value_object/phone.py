from pydantic import BaseModel, field_validator
import re


class Phone(BaseModel):
    country_code: str
    phone_number: str
    area_code: str

    @field_validator('country_code')
    def _only_digits(cls, value: str) -> str:
        value = re.sub('[^0-9]', '', value)
        if not value:
            raise ValueError('Country code is invalid')
        return value

    @field_validator('country_code')
    def _validate_country_code(cls, value: str) -> str:
        if not (1 <= len(value) <= 3):
            raise ValueError('Country code is invalid')
        return value

    @field_validator('are_code')
    def _validate_area_code(cls, value: str) -> str:
        if not (1 <= len(value) <= 3):
            raise ValueError('Area code is invalid')
        return value

    @field_validator('phone_number')
    def _validate_phone_number(cls, value: str) -> str:
        if not (8 <= len(value) <= 9):
            raise ValueError('Phone number is invalid')
        return value

    def format_with_area_code(self) -> str:
        return f'({self.area_code}) {self.phone_number}'

    def format_phone_number_complete(self) -> str:
        return f'{self.country_code} - ({self.area_code}) {self.phone_number}'

    def get_all_number(self):
        return f'{self.country_code}{self.area_code}{self.phone_number}'