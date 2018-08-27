attempt = 0
max_attempts = 1

while attempt < max_attempts:
    if response.lower() == 'y':
        walking = True
    elif response.lower() == 'n':
        walking = False
    else:
        print("That is not a valid response. Please try again.")
        continue
    attempt += 1

