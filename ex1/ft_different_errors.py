#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 10:18:28 by juruan              #+#    #+#            #
#   Updated: 2026/03/11 16:44:25 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        int(5 / 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        plants = {"tomato": 5}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
