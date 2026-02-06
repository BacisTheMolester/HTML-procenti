import re

x = input()

filtered_str = re.sub(r'[^a-zA-Z0-9\s]', '', x).lower()
z = filtered_str[::-1]

if filtered_str == z:
    print("Atplicis vārds, yes")
else:
    print('*'*69)