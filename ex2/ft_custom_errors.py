#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 17:00:24 by juruan              #+#    #+#            #
#   Updated: 2026/03/11 18:12:54 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name: str) -> None:
    if plant_name == "tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
