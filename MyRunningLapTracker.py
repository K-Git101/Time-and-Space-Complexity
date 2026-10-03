n = 4

guess = input("Predict: how many laps will be tracked for n = 4? ")

laps = list(range(1, n + 1))

print("Your guess:", guess, "  Laps:", laps, "  Total laps:", len(laps))

input("Predict: what happens to the number of laps as n grows? Press Enter ")

for laps_count in [4, 10, 100, 1000]:

    print(f"n = {laps_count:<5} Running tracker records {laps_count:>5} laps")