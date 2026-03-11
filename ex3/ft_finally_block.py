#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 18:15:15 by juruan              #+#    #+#            #
#   Updated: 2026/03/11 20:48:12 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    good = ["tomato", "lettuce", "carrots"]
    bad = ["tomato", None]

    print("Testing normal watering...")
    water_plants(good)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
