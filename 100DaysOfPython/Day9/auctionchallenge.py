#Day 9 Secret auction code challenge
# show art, ask for name, ask for bid, name is key bid is value, add that to a dict, ask if theres other users, if YES then clear screen repeat questions and append to dictionary. 
#when done you say no for other bidders, use a comparision operator to see who the highest bidder is while looping through the dict of bidders
bidder_book = {}

def set_bidders():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder_book[name] = bid
    more_bids = input("Are there more bidders? y/n ").lower()
    if more_bids == "y":
        set_bidders()
    else:
        allBids = []
        for bids in bidder_book.values():
            allBids.append(bids)
        max_bid = allBids[0]
        for i in range(1, len(allBids)):
            if allBids[i] > max_bid:
                max_bid = allBids[i]
                highest_bidder = list(bidder_book.keys())[i]
        print(f"The highest bidder is {highest_bidder} \n with a bid of ${max_bid}")
       
set_bidders()
