from enum import Enum


class LoadLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


# добавим аннотирование)
def calculate_delivery(distance_km: float, is_big: bool, fragile: bool, load: LoadLevel) -> float:
    if fragile and distance_km > 30:
        raise ValueError("Хрупкий груз нельзя перевозить на расстояние более 30 км")

    # Расстояние
    if distance_km <= 2:
        cost = 50
    elif distance_km <= 10:
        cost = 100
    elif distance_km <= 30:
        cost = 200
    else:
        cost = 300

    # Габариты
    cost += 200 if is_big else 100

    # Хрупкость
    if fragile:
        cost += 300

    # Коэффициент загруженности
    multiplier = {
        LoadLevel.LOW: 1,
        LoadLevel.MEDIUM: 1.2,
        LoadLevel.HIGH: 1.4,
        LoadLevel.VERY_HIGH: 1.6
    }[load]

    total_cost = cost * multiplier

    # Минимальная стоимость
    return max(total_cost, 400)
