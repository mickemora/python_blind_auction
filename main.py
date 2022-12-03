
#*************
#*** STEPS ***
#*************
#1 - Display the logo - DONE
#2 - Display user input questions: DONE
#3 - Create a dictionary to store the name of the bidder and the bid - DONE
#4 - Create a list to store each dictionary with bidder + bid key pair - DONE
#4 - Create a process to read each dictionary and extract the bid  - DONE
#5 - Choose the one with the highest amount - 
#6 - Display the winner - 

#from replit import clear
import art
print (art.logo)

other_bidders = "yes"
bidders       = {}
final_list    = []

def identify_highest_bidder(dictionary):
  highest_bid    = 0;
  highest_bidder = ""
  for bidder in dictionary:
    bidder_name = bidder["name"]
    final_bid   = bidder["bid"]

    if final_bid > highest_bid:
      highest_bid    = final_bid
      highest_bidder = bidder_name
  
  print(f"The highest bidder is: {highest_bidder} with a bid of ${highest_bid} dollars.")


while other_bidders == "yes":
  name          = input("What's your name? ").lower()
  bid           = int(input("What's your bid? $"))
  other_bidders = input("are there any other bidders? Type Yes or No : ").lower()

  bidders = {
    "name": name,
    "bid":bid,
  }
  final_list.append(bidders)
  if other_bidders == "yes":
    #clear()
    print("Bye")
  else:
    identify_highest_bidder(final_list)