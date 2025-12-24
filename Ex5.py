import itertools, random
team_list = ["Tigers", "Dragons","“Eagles", "Sharks", "Wolves", "Bears"]
random.shuffle(team_list)
list = list(itertools.combinations(team_list, 2))

print("--- Tournament Schedule ---")
for i in range(len(list)):
    print(f"Match {i} {list[i][0]} vs {list[i][1]}")
print("---------------------------")
print(f"Total Matches to play: {len(list)}")