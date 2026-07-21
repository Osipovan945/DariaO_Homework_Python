from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Тверская", "15", "42")
to_address = Address("654321", "Санкт-Петербург", "Невский", "10", "7")
mailing = Mailing(to_address=to_address,
                  from_address=from_address,
                  cost=350.50,
                  track="ABC123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
