from replit import clear

bids={}
next_bid=True
while next_bid:
  bidder_name= input("What is your name? : ")
  bid= int(input("What is your forthe current? : $"))
  bids[bidder_name]=bid
  should_continue = input("Type 'yes if there anybody left of biding, Otherwise 'no'.\n").lower()
  if should_continue=='no':
    next_bid=False
  elif should_continue=='yes':
    clear()

def highest_bidder():
  highest_bid=0
  for bidder_name in bids:
    if bid > highest_bid:
      highest_bid = bid
  print(f"The winner is {bidder_name} with bid of ${highest_bid}.")
  
  
  