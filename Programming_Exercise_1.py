

def accept_purchase(tickets_left):
    max_tickets = 4
    while True:
        how_many_tickets = int(input(f'How many tickets will that be? You can buy up to {max_tickets}: '))
        if 1 <= how_many_tickets <= 4:
            if how_many_tickets <= tickets_left:
                return how_many_tickets
            else:
                print(f'Sorry, there are only {tickets_left} tickets left.')
        else:
            print(f'Sorry, you cannot buy more than {max_tickets} tickets!')

def manage_ticket_sales():
    total_tickets = 10 #taking the total number of tickets down from 20 to 10
    buyer_count = 0
    while total_tickets > 0:
        tickets_bought = accept_purchase(total_tickets)
        total_tickets -= tickets_bought
        buyer_count += 1
        print (f'Number of tickets left is: {total_tickets}')

    print('All the tickets are gone!')
    print(f'The total number of buyers was: {buyer_count}')

manage_ticket_sales()