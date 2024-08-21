# from replit import clear
bids = {}
run_the_bid = True

def highest_bid(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder  # As last bidder is highest
    print(f"The winner is {winner} with bid {highest_bid} $ ")


while run_the_bid:
    name = input("Give the bidder name :-> ")
    bid = int(input("Enter the bid :-> $"))
    bids[name] = bid
    run_the_bid = input("Are there any more bidder 'yes or 'no' ->")
    if run_the_bid == 'yes':
        run_the_bid = True
        # clear()
    elif run_the_bid == 'no':
        run_the_bid = False
        highest_bid(bids)