from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79876543221"),
    Smartphone("Samsung", "Galaxy S24", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79345678901"),
    Smartphone("Google", "Pixel 8", "+79456789012"),
    Smartphone("OnePlus", "12", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
