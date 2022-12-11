import numpy as np

#set variables and lists
day = 0
days = 1
dow = ['Monday','Tuesday','Wednesday','Thursday','Friday']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
cash = 1000
inventory = {}
check = list(inventory.keys())
market =    {'Wheat': np.random.binomial(1300, .5)
            , 'Corn': np.random.binomial(700, .5)
            , 'Soybean': np.random.binomial(1500, .5)
            , 'Feeder Cattle': np.random.binomial(200, .5)
            , 'Lean Hogs': np.random.binomial(150, .5)
            , 'ND Light Sweet': np.random.binomial(200, .5)
            , 'Gold': np.random.binomial(2000, .7)
            , 'Silver': np.random.binomial(40, .6)
            }
ticker = list(market)


def main():
    """Main window showing current stats presented to player.

    Prints 'window' showing current day, cash, inventory, and market prices.
    Asks player which action to take -- (B)uy, (S)ell, or (W)ait?
    
    Returns:
    choice (string) -- stores input of player when given choice of
                        (B)uy, (S)ell, or (W)ait?
    """
    #prints main window of stats
    print(   '╔══════════════════════════╗\n'
            +'║     Commodity Trader     ║\n'
            +'╚══════════════════════════╝\n'
            +f'   {dow[day]}, {days}       ${cash}\n'
            +'════════════════════════════\n'
            +'  1. Wheat             $'+str(market['Wheat'])+'\n'
            +'  2. Corn              $'+str(market['Corn'])+'\n'
            +'  3. Soybean           $'+str(market['Soybean'])+'\n'
            +'  4. Feeder Cattle     $'+str(market['Feeder Cattle'])+'\n'
            +'  5. Lean Hogs         $'+str(market['Lean Hogs'])+'\n'
            +'  6. ND Light Sweet    $'+str(market['ND Light Sweet'])+'\n'
            +'  7. Gold              $'+str(market['Gold'])+'\n'
            +'  8. Silver            $'+str(market['Silver'])+'\n'
            +'════════════════════════════\n'
            +'Inventory'
        )
    
    #prints everything in inventory
    for i in inventory:
        print(i, ' : ', inventory[i])

    #asks player to choose action
    choice = input('\n(B)uy, (S)ell, or (W)ait? ').lower()

    #based on player choice, runs relevent function
    match choice:
        case 'b': #buy
            buy()
        case 's': #sell
            sell()
        case 'w': #wait
            wait()
        case _: #empty
            print('...nothing?  Really?')
            wait()

    return choice


def buy():
    """Buys {qty} of {commodity}."""
    global cash
    global inventory
    #ask which commodity to buy
    buy = int(input('Buy which one (1-8)? ')) - 1
    commodity = str(ticker[buy])
    #ask how many to buy
    qty = int(input(f'How much {commodity}? '))
    choice = input(f'Purchase {qty} ' + commodity + ' for $' + str(qty*market[commodity]) + ' (y/n)? ').lower()
    if choice == 'y':
        #not enough money, returns to main()
        if cash < qty*market[commodity]:
            print('\n******Sorry, too poor!******\n')
            main()
        #purchase transaction processes, then returns to main()
        else:
            cash -= qty*market[commodity]
            inventory[commodity] = qty
            print(f'\n++++++++ Bought {qty} {commodity}...\n')
            main()
    #skips buying and returns to main()
    else:
        print("No worries, nothing purchased...")
        main()


def sell():
        """Sells {qty} of {commodity}."""
        global cash
        global inventory
        global check
        #asks which commodity to sell
        sell = int(input('Sell which one (1-8)? ')) - 1
        commodity = str(ticker[sell])
        #asks how much to sell
        qty = int(input(f'How many {commodity}? '))
        choice = input(f'Sell {qty} ' + commodity + ' for $' + str(qty*market[commodity]) + ' (y/n)? ').lower()
        
        if choice == 'y':
            #sell transaction processes, then returns to main()
            if commodity in inventory:
                cash += qty*market[commodity]
                inventory[commodity] -= qty
                print(f'\n-------- Sold {qty} {commodity}...\n')
                main()
            #not enough money, returns to main()
            else:
                print('\n********Oops, don'f't have enough {commodity}!********\n')
                main()
        #skips selling and returns to main()
        else:
            print("No worries, maybe next time...")
            main()


def wait():
    """Advances Day and updates market prices."""
    global market
    global day
    global days
    #updates market prices through binomial randomization
    market =    {'Wheat': np.random.binomial(1300, .6)
            , 'Corn': np.random.binomial(700, .6)
            , 'Soybean': np.random.binomial(1500, .6)
            , 'Feeder Cattle': np.random.binomial(200, .6)
            , 'Lean Hogs': np.random.binomial(150, .6)
            , 'ND Light Sweet': np.random.binomial(200, .6)
            , 'Gold': np.random.binomial(2000, .7)
            , 'Silver': np.random.binomial(40, .6)
            }
    #advances Day forward, skipping back to the beginning of the week
    #once it reaches the end, then returns to main()
    day += 1
    days += 1
    if day == 5:
        day = 0
    print('Waiting...')
    main()


if __name__=="__main__":
    main()