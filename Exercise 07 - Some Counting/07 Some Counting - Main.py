# This counts from 0 up to 50 (it stops BEFORE 51).
for i in range(51):
   print(i)

# We start at 50, go down to 0 (stopping before -1), moving backwards by -1.
for i in range(50, -1, -1):
    print(i)

# Starts at 30 and goes up to 50 (stops before 51).
for i in range(30,51,+1):
    print(i)

# Starts at 50 and counts down by 2 each time (50, 48, 46...).
# Stops before getting to 9 (so the last number printed is 10).
for i in range(50,9,-2):
    print(i)

# Starts at 100 and adds 5 each time (100, 105, 110...).
# Stops before 205 (so the last number printed is 200).
for i in range(100,205,+5):
    print(i)