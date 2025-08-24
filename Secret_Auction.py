print("Welcome to the Secret Auction Program.")
bidders = {"names":[],"bids":[]}
flag = True
while flag:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    bidders["names"].append(name)
    bidders["bids"].append(bid)
    other_bidders = input("Are there any other bidders for this auction? Type 'yes' or 'no': \n").lower()
    if other_bidders == "yes":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif other_bidders == "no":
        flag = False
    else :
        print("incorrect input")
        flag = False
max = 0
for i in range(len(bidders["bids"])):
    if max < bidders["bids"][i]:
        max = bidders["bids"][i]
        idx = i
print("The winner is " + bidders["names"][idx] + " with a bid of " + str(max))
print("Thank for your participation")


