#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_raise_errors.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 20:46:31 by juruan              #+#    #+#            #
#   Updated: 2026/03/11 21:29:51 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:

    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
