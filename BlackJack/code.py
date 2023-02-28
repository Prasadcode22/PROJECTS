import random

def dealer_card():
  """ Return a random card from deck """
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards): 
  """calculate the score of user and the computer """
  
  if sum(cards) and len(cards)==2:
    return 0
    
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  
users_card=[]
computers_card=[]
is_game_over=False
while not is_game_over:  
  for _ in range(2):
    users_card.append(dealer_card())
    computers_card.append(dealer_card())
      
  users_score=calculate_score(users_card)
  computers_score=calculate_score(computers_card)
  
  
  if users_score==0 or computers_score==0:
    is_game_over= True
  
  else:
    user_should_deal= input("Type 'yes' to get another card, Otherwise 'no': ").lower()
    if user_should_deal=='yes':
      users_card.append(dealer_card())
    else:
      is_game_over=True
    
    
    
  
    