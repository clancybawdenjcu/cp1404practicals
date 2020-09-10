"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATES_DICT = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATES_DICT)

# state_code = input("Enter short state: ").upper()
# while state_code != "":
for state_code in STATES_DICT:
    print(f"{state_code:3} is {STATES_DICT[state_code]}")
    # else:
    #     print("Invalid short state")
    # state_code = input("Enter short state: ").upper()
