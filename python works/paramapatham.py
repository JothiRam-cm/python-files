paramapatham=[int(x) for x in range(1,101)]
paramapatham[0]="start"
paramapatham[len(paramapatham)-1]="End"
print(paramapatham)
dice=[int(y) for y in (input("\nenter dice value for 10 roolls [1-12]:\n").split(" "))]
curr_pos=0
for roll in dice:
    if roll<(len(paramapatham)):
        curr_pos+=roll
        print("current positon : {}".format(paramapatham[curr_pos]))
        