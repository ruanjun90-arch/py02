#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 16:51:57 by juruan              #+#    #+#            #
#   Updated: 2026/03/09 11:24:17 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def check_temperature(temp_str) -> int | None:
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp

    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number")


def test_temperature_input() -> None:
    if __name__ == "__main__":
        print("=== Garden Temperautre Checker ===")
        temp = input("Testing temperature: ")
        check_temperature(temp)
