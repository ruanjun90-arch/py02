#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 16:51:57 by juruan              #+#    #+#            #
#   Updated: 2026/03/09 12:35:10 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def check_temperature(temp_str) -> int | None:
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp

    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    test = ["25", "abc", "100", "-50"]
    for temp in test:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
