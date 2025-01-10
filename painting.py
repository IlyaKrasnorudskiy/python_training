import math

def calculate_paint_cans(wall_length, wall_height, mosaic_length, mosaic_height, coverage_per_can):
    # Рассчитываем площадь стены и мозаики
    wall_area = wall_length * wall_height
    mosaic_area = mosaic_length * mosaic_height

    # Рассчитываем площадь для покраски
    paintable_area = wall_area - mosaic_area

    # Рассчитываем количество банок краски
    cans_needed = paintable_area / coverage_per_can

    # Округляем в большую сторону
    cans_needed = math.ceil(cans_needed)

    return cans_needed


wall_length = 5.5  # длина стены (м)
wall_height = 3.0  # высота стены (м)
mosaic_length = 0  # длина мозаики (м)
mosaic_height = 0  # высота мозаики (м)
coverage_per_can = 14  # площадь, покрываемая одной банкой краски (м^2)

# Вычисляем количество банок краски
cans = calculate_paint_cans(wall_length, wall_height, mosaic_length, mosaic_height, coverage_per_can)

print(f"Необходимо {cans} банок краски.")
