# Types of Loops in Python

# -------------------------------
# 1. FOR LOOP
# -------------------------------
print("For loop: Print numbers from 1 to 5")
for i in range(1, 6):
    print(i)

print("\n-------------------------------")

# -------------------------------
# 2. WHILE LOOP
# -------------------------------
print("While loop: Print numbers from 1 to 5")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n-------------------------------")

# -------------------------------
# 3. BREAK STATEMENT
# -------------------------------
print("Break statement: Stop loop when i == 4")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n-------------------------------")

# -------------------------------
# 4. CONTINUE STATEMENT
# -------------------------------
print("Continue statement: Skip when i == 3")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n-------------------------------")

# -------------------------------
# 5. PASS STATEMENT
# -------------------------------
print("Pass statement: Do nothing when i == 3")
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
