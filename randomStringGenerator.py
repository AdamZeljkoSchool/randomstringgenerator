# Imports
import random
import string
import keyboard
import time

# Inputs
seed = int(input("Input the randomizer seed: "))
random.seed(seed)
i = ""
limit = int(input("Input a length: "))
ending = input("What is the ending string? ")
while len(ending) != limit:
    ending = input("Ending word isn't correct length, try again: ")
counter = 0

# Processing
startTime = time.perf_counter()
while i != ending:
    i = ''.join(random.choices(string.ascii_lowercase, k=limit))
    counter += 1
    print(i)
    if keyboard.is_pressed('space'):
        break
endTime = time.perf_counter()
totalTime = endTime - startTime

# Outputs
if i == ending:
    print(f"It took {counter} tries and {totalTime:.1f} seconds for the randomizer to hit '{ending}'")
else:
    print(f"Aborted, {counter} attempts were made before abortion at {totalTime:.1f} seconds")