#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 21:46:44 by juruan              #+#    #+#            #
#   Updated: 2026/03/11 21:50:35 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        if not isinstance(plant_name, str) or plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
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

        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")


def test_garden_management() -> None:
    manager = GardenManager()

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}\n")

    print("Watering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Error watering plants: {e}")

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
