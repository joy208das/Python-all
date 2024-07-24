'''nilam bidding'''


end=True
bids={}

def find_maximum(bids):
    maximum=0
    winner=""
    for n in bids:
      bid_amount=bids[n]
      if bid_amount>maximum:
        maximum=bid_amount
        winner=n
    print(f"the winner is {winner} and the price is {maximum}")       

while end:
    name=input("What is your name:")
    price=input("what is your price:")
    bids[name]=int(price)
    should_continue=input("if you want continue print yes either not: ")
    if should_continue=="no":
        end=False
        find_maximum(bids)
    elif should_continue=="yes" :
        end=True 

     