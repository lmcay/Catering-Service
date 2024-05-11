#--------------------MAIN FUNCTIONS------------------------------------#
def MENU():
    print("O"+"="*37+"***BURI CATERING SERVICE***"+"="*38+"O")
    print("""\t\t\t\t[1] Read More
\t\t\t\t[2] Party Food
\t\t\t\t[3] Rentals and Party Needs
\t\t\t\t[4] Catering Services
\t\t\t\t[5] View your cart
\t\t\t\t[0] End Program""")
    print("O"+"="*102+"O")

def check_main(x):
    match x:
        case "1"|"2"|"3"|"4"|"5"|"0":
            x = int(x)
    return x

def BACK():
    print("O"+"="*102+"O")
    while True:
        back = input("Press [0] to go back: ")
        if back == "0":
            break
        else:
            print("Invalid Input")

def four_option(option):
    match option:
        case "1"|"2"|"3"|"4":
            option = int(option)
    return option

def pack_option():
    while True:
        pack_code = input("Input Pack Code [1-3]: ")
        match pack_code:
            case "1"|"2"|"3":
                break
            case _:
                print("Invalid Input")
    return int(pack_code)

def six_option():
    while True:
        six_option = input("Input Code [1-6]: ")
        match six_option:
            case "1"|"2"|"3"|"4"|"5"|"6":
                break
            case _:
                print("Invalid Input")
    return int(six_option)

def numberOfItems():
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity > 0:
                break
            else:
                print("Input must be greater than 0")
        except ValueError:
            print("Input must be an integer")
    return quantity

def ask_reset():
    print("\t\t\t\t[R] Reset Order\t[B] Back")
    while True:
        ask_reset = input("Input Operation[R/B]: ")
        ask_reset = ask_reset.upper()
        if ask_reset == "R" or ask_reset == "B":
            break
        else:
            print("Invalid Input")
    return ask_reset

def ask_if_order_q():
    print("\t\t\t\t[O] Order\t[B] Back")
    while True:
        ask_order_q = input("Input Operation[O/B]: ")
        ask_order_q = ask_order_q.upper()
        if ask_order_q == "O" or ask_order_q == "B":
            break
        else:
            print("Invallid Input")
    return ask_order_q
#------------------------------------------------------------------------#

#--------------------------------READ MORE FUNCTIONS--------------------------------#
def information_options():
    print("O"+"="*42+"***Regarding Us***"+"="*42+"O")
    print("""\t\t\t\t[1] About Us
    \t\t\t\t[2] Contact Us
    \t\t\t\t[3] Terms of Payment
    \t\t\t\t[4] Back""")
    print("O"+"="*102+"O")
    
def about_us():
    print("O"+"="*44+"***About Us***"+"="*44+"O")
    print("""\n             Since 2018, we at BURI Catering have been serving up joyful occasions. Curiosity led
    to the  founding  of   our  current  catering  company,  and as  we   gathered customers  and
    culinary expertise,  we  endeavored to  enhance  our  offerings. Carl  and  Vladimir  are the
    founders;  they  know caterers  who  have  studied  culinary  arts,  so  they  can offer  you
    with  a delectable  dinner whenever  you  need their services.  Mark organizes  the menus for
    celebrations such  as weddings and birthdays. He has catering and event organizing experience.
                
             In  five   years, BURI   Catering  has   established  itself  as  one  of the city's
    caterers (San Fernando, Pampanga)  with  the most rapid  expansion  and  highest demand. With
    30 people  that are accessible  for  weddings  and birthdays, we have  become one of the most
    well-known catering businesses. Since the  beginning of  our careers, we have been recognized
    as  the  catering industry's most  dependable brand. 

            The  catering  business  and  restaurant continue to  expand  in  popularity, and the
    restaurant's dedicated  team of professionals  and  personnel  give  all of its presentations
    5-star district-wide appeal. Both large and  small catering  companies offer social meals and
    floral  and décor arrangements for  birthdays and weddings.  Remember about BURI Catering.

    Call +63123456789 and  let us know what we can do for you.\n""")

def contact_us():
    print("O"+"="*102+"O")
    print("""\tNatakam ka ba? Hindi mo pa na try? Contact us here!

    \tFacebook: Buri Catering
    \tTwitter: @BuriCatering
    \tContact Number: +63917611539
                        +63123456789

    \tInterested at Buri Catering? Please message or look for one of the members below:

    \tFounder:
    \tLuis Miguel I. Cayanan""")

def terms_of_payment():
    print("O"+"="*44+"Terms of Payment"+"="*42+"O")
    print("\n"," "*42, "Catering Agreement\n")
    print("""              Catering Agreement/General Agreement  for Buri.ph. The catering agreement  will  be
    created once the detail of the client is provided.  The client  will be required to  describe
    the  following  details:  name, date,  time, guest  count etc. They must also concur with the
    following:

\t1. DEPOSIT OF PAYMENT
    Fifty percent (50%) of  the anticipated cost (COST) is  required for order processing. If the
    order goes through, the deposit amount will be deducted from the final payment.\n
\t2. FINAL PAYMENT
    The  final  payment  is due  three to five days before the event. The  payment terms  must be
    adhered to.\n
\t3. PAYMENT METHOD 
    All orders are payable with GCASH or CASH. GCASH DETAILS.\n
\t4. GUEST COVERAGE
    A  final  headcount or guest  list should be provided  at the time of  order to avoid further
    miscalculation.\n
\t5. LEFTOVER 
    Guests who have leftover foods will be discarded by the Caterer.\n
\t6. BEVERAGES 
    The guests will be entertained with beverages, or support as agreed upon the agreement.\n
\t7. STRICTLY NO CANCELLATION OF ORDER 
    All  pre-payments  and post-payments won’t  be refunded  if the client cancels  the event and
    notifies the venue within one to three days prior to the event.\n
\t8. VENUE 
    The  caterer is not responsible for any damage or loss to furnishings, equipment, or clothing
    from the said venue. However, damages or loss of our products, equipment and more will be the
    customer’s responsibility and must be charged for the damaged items.\n
""")

#------------------------------------------------------------------------#
    
#-----------------------------Party Food----------------------------------#

def party_options():  
    print("O"+"="*38+"***PARTY PACK OPTIONS***"+"="*40+"O")
    print("""\t\t\t\t[1]Packs
    \t\t\t\t[2]Cart
    \t\t\t\t[3]Back""")
    print("O"+"="*102+"O")

def check_party_option(party_option):
    match party_option:
        case "1"|"2"|"3":
            party_option = int(party_option)          
    return party_option

def PARTY_PACKAGES():
    print("""O======================================================================================================O
|          PACKAGE CODE [1]      |          PACKAGE CODE [2]          |          PACKAGE CODE [3]      |
| Package 1: Occasional Package  | Package 2: Party Package Overload  | Package 3: Formal Package      |
| (Good for 20 People)           | (Good for 20 People)               | (Good for 20 People)           |
| Mixed Veggies and Seafood      | Fried Garlic Rice                  | Roast Beef                     |
| Spaghetti & Meatballs          | Hotdogs                            | Fried garlic and butter rice   |
| Plain Rice                     | Crispy Chicken Tacos               | Chicken Cordon Bleu            |
| Garlic Chicken                 | Pizza Hawaiian                     | Roast Pork with Oyster Sauce   |
| Roast Beef                     | Chicken Wings                      | Pescada en Salsa Verde         |
| Pork and Chicken BBQ           | BBQ Pork Sliders                   | Baked Spaghetti                |
| Fish Fillet                    | Spaghetti & Meatballs              | Mixed Vegetables with Ham      |
| Pork Lumpia                    | Sandwiches Roasted Beef            | Buko Fruit Salad               |
| Iced Tea Bottomless            | Iced Tea Bottomless                | Iced Tea Bottomless            |
| Ice Mineral Water              | Ice Mineral Water                  | Ice Mineral Water              |
| Price: P 10,261                | Price: P 11,707                    | Price: P 12,404                |
O======================================================================================================O""")

def show_cart_partypacks():
    print(" "*41+"***Party Food Cart***")
    if total_party_pack != 0:
        print("Package Ordered", "\t\t\t\t\tQuantity","\t\t\tPrice")
        if party_pack1 != 0:
            print("Party Package 1 [Occasional Package]:","\t\t\t",party_pack1, "\t\t\t\tP",format(pp1, ',.2f'))
        if party_pack2 != 0:
            print("Party Package 2 [Party Package Overload]:","\t\t",party_pack2, "\t\t\t\tP",format(pp2, ',.2f'))
        if party_pack3 != 0:
            print("Party Package 3 [Formal Package]:", "\t\t\t",party_pack3, "\t\t\t\tP",format(pp3, ',.2f'))
        print("\t     "*8,"Party Pack Total: P", format(total_party_pack, ',.2f'))
    else:
        print("\t\t\tThere are no current items in your shopping cart.\n")

#-------------------------------------------------------------------------#

#------------------------RENTALS AND PARTY NEEDS FUNCTIONS---------------#
def rental_options():
    print("O"+"="*33+"***RENTAL AND EQUIPMENT OPTIONS***"+"="*35+"O")
    print("""\t\t\t\t[1] Packs
    \t\t\t\t[2] Individal Items
    \t\t\t\t[3] Cart
    \t\t\t\t[4] Back""")
    print("O"+"="*102+"O")

            
def rentalMenuPacks():
    print("O"+"="*38+"***RENTAL PACK OPTIONS***"+"="*39+"O")
    print("""\t\t[1]Complete Catering Equipment Rental Package - 100/person
\t\t[2]Complete Catering Equipment Rental Package with Waiters - 130/person
\t\t[3]Complete Catering Equipment with Flower Arrangement and Waiters - 160/person""")
    print("O"+"="*102+"O")

def rentalMenuItems():
    print("O"+"="*38+"***RENTAL ITEM OPTIONS***"+"="*39+"O")
    print("""\t\t[1]Tents - 100/pc
\t\t[2]Tables - 100/pc
\t\t[3]Chairs - 20/pc
\t\t[4]Table Cloth Linen -  50/pc
\t\t[5]Ribbons - 15/pc
\t\t[6]Complete Utensils and Silverware - 50/pc""")
    print("O"+"="*102+"O")

def show_cart_rentals():
    print(" "*39+"***Equipment Rental Cart***")
    if total_rentals != 0:
        print("Package Ordered", "\t\t\t\t\tQuantity","\t\t\tPrice")
        if rental_pack1 != 0:
            print("Complete Catering Eq. Rental Package:", "\t\t\t",rental_pack1, "\t\t\t\tP", format(p1, ',.2f'))
        if rental_pack2 != 0:
            print("Complete Catering Eq. Rental Package w/ Waiters:","\t",rental_pack2, "\t\t\t\tP", format(p2, ',.2f'))
        if rental_pack3 != 0:
            print("Complete Catering Eq. w/ Flower Arrangement & Waiters:",  "\t",rental_pack3, "\t\t\t\tP", format(p3, ',.2f'))
        if item1 != 0:
            print("Tents:","\t\t\t\t\t\t\t", item1, "\t\t\t\tP", format(p4, ',.2f'))
        if item2 != 0:
            print("Tables:","\t\t\t\t\t\t", item2, "\t\t\t\tP", format(p5, ',.2f'))
        if item3 != 0:
            print("Chairs:","\t\t\t\t\t\t", item3, "\t\t\t\tP", format(p6, ',.2f'))
        if item4 != 0:
            print("Table Cloth Linen:","\t\t\t\t\t", item4, "\t\t\t\tP", format(p7, ',.2f'))
        if item5 != 0:
            print("Ribbons:", "\t\t\t\t\t\t",item5, "\t\t\t\tP", format(p8, ',.2f'))
        if item6 != 0:
            print("Complete Utensils and Silverware:", "\t\t\t",item6, "\t\t\t\tP", format(p9, ',.2f'))
        print("\t      "*8,"Equipment Total: P", format(total_rentals,',.2f'))
    else:
        print("\t\t\tThere are no current items in your shopping cart.\n")

#-------------------------------------------------------------------------#

#-----------------------------Catering Services---------------------------#

def catering_options():
    print("O"+"="*40+"***CATERING SERVICES***"+"="*39+"O")
    print("""\t\t\t\t[1] Wedding Packages
    \t\t\t\t[2] Birthday Packages
    \t\t\t\t[3] Cart
    \t\t\t\t[4] Back""")
    print("O"+"="*102+"O")

def WEDDING_PACKAGES():
    
    print("""O======================================================================================================O
| WEDDING PACKAGE                | Set-up and Props Inclusion         | Wedding Package                |
| 1 Rice Menu                    | Buffet Set-up                      |                                |
| 1 Fish Menu                    | Formal Uniform for Caterers        | Package [1] - P 24,000         |
| 1 Chicken Menu                 | Complete Wedding Equipments        | Good for 30 People             |
| 1 Beef Menu                    | Entrance Arch , Red Carpet, etc.   |                                |
| 1 Vegetable Menu               | Invitation Cards & A Special Gift  | Package [2] - P38,000          |
| 1 Dessert Menu                 | Complete Equipment for             | Good for 50 People             |
| 1 Soup Menu                    | Catering (Utensils)                |                                |
| Round Bottomless Softdrinks    | Complete Catering Equipments       | Package [3] - P75,000          |
| Purified Water With Tube Ice   | Wedding Party Host and Co-Host     | Good for 100 People            |
O======================================================================================================O""")

def BIRTHDAY_PACKAGES():
    print("""O======================================================================================================O
| BIRTHDAY PACKAGE               | Set-up and Props Inclusion         | Birthday Packages              |
| Plain Rice                     | Buffet Set-up                      |                                |
| Garlic Rice                    | Formal Uniform for Caterers        | Good for N People              |
| 1 Beef Menu                    | Presentable Backdrop with          |                                |
| 1 Chicken Menu                 | Color Motive                       | Package [1] - P 18,000         |
| 1 Fish Menu                    | Complete Equipment for             | 30 People                      |
| 1 Vegetable Menu               | Catering (Utensils)                |                                |
| 1 Appetizer Dish               | Complete Tables and Chairs         | Package [2] - P 28,000         |
| 1 Dessert                      | with Presentable Center Piece      | 50 People                      |
| 1 Soup                         | and Color Motive                   |                                |
| Purified Water W/Tube Ice      | Presentable Cake Table/Stand       | Package [3] - P 55,000         |
| Bottomless Softdrinks          | Set-up and Photobooth              | 100 People                     |
O======================================================================================================O
| BIRTHDAY PACKAGE - KIDDIE      | Set-up and Props Inclusion         | Birthday Packages - Kiddie     |
| Plain Rice                     | Loot Bags and Accent Lights        |                                |
| 1 Beef Menu                    | Buffet Set-up                      | Package [4] - P 13,000         |
| 1 Vegetable Menu               | Formal Uniform for Caterers        | Good for 30 People             |
| Spaghetti                      | Party Props (Hats, Lights, etc.)   |                                |
| Hotdog                         | Complete Equipment for             | Package [5] - P 21,000         |
| Cotton Candy Station           | Catering (Utensils)                | Good for 50 People             |
| Kiddie Cake                    | Complete Tables and Chairs         |                                |
| 1 Round Bottomless Softdrinks  | with Presentable Center Piece      | Package [6] - P 38,000         |
| Purified Water With Tube Ice   | and Color Motive                   | Good for 100 People            |
O======================================================================================================O""")

def show_cart_catering():
    print(" "*42+"***Catering Cart***")
    if total_catering_packs != 0:
        print("Package Ordered", "\t\t\t\t\tQuantity","\t\t\tPrice")
        if wed_pack1 != 0:
            print("Wedding Package 1:\t\t\t\t\t", wed_pack1, "\t\t\t\tP", format(c1, ',.2f'))
        if wed_pack2 != 0:
            print("Wedding Package 2:\t\t\t\t\t", wed_pack2, "\t\t\t\tP", format(c2, ',.2f'))
        if wed_pack3 != 0:
            print("Wedding Package 3:\t\t\t\t\t", wed_pack3, "\t\t\t\tP", format(c3, ',.2f'))
        if b_pack1 != 0:
            print("Birthday Package 1:\t\t\t\t\t", b_pack1, "\t\t\t\tP", format(c4, ',.2f'))
        if b_pack2 != 0:
            print("Birthday Package 2:\t\t\t\t\t", b_pack2, "\t\t\t\tP", format(c5, ',.2f'))
        if b_pack3 != 0:
            print("Birthday Package 3:\t\t\t\t\t", b_pack3, "\t\t\t\tP", format(c6, ',.2f'))
        if b_pack4 != 0:
            print("Birthday Package 4 - Kiddie:\t\t\t\t", b_pack4, "\t\t\t\tP", format(c7, ',.2f'))
        if b_pack5 != 0:
            print("Birthday Package 5 - Kiddie:\t\t\t\t", b_pack5, "\t\t\t\tP", format(c8, ',.2f'))
        if b_pack6 != 0:
            print("Birthday Package 6 - Kiddie:\t\t\t\t", b_pack6, "\t\t\t\tP", format(c9, ',.2f'))
        print("\t"*8,"Catering Pack Total: P", format(total_catering_packs, ',.2f'))
    else:
        print("\t\t\tThere are no current items in your shopping cart.\n")

#-------------------------------------------------------------------------#

#------------------------------ALL CART CONCLUSION------------------------------------------#

def confirm_checkout():
    print(("\t\t\t\t[1]CHECKOUT\n\t\t\t\t[2]RESET ALL ORDERS\n\t\t\t\t[3]BACK"))
    print("O"+"="*102+"O")
    while True:
        checkout = input("Input Operation[1-3]: ")
        match checkout:
            case "1"|"2"|"3":
                return int(checkout)
                break
            case _:
                print("Invalid Input")

def details():
    print("O"+"="*102+"O")
    print("Place your details and accurate data. Invalid information will not be processed by the management.")
    name = input("Full Name: ")
    number = input("Contact Number: ")
    address = input("Venue Address: ")
    date_order = input("Input date of order (Ex. January 3,2022): ")
    date_req = input("Input date of order delivery (Ex. January 13, 2022): ")
    guest_count = input("Guest Count: ")
    payment = input("Mode of Payment [GCASH/Paymaya]: ")
    print("O"+"="*102+"O")
    print("\n\t\t\t\tFull Name:",name,"\n\t\t\t\tContact Number:", number,
          "\n\t\t\t\tVenue Address:",address,"\n\t\t\t\tDate of order:",date_order,
          "\n\t\t\t\tDate of order deadline:",date_req,"\n\t\t\t\tGuest Count:",guest_count,
          "\n\t\t\t\tMode of Payment:",payment,"\n\n\t\t\t\tTotal Payment P:", format(total_cart, ',.2f'))
    print("\n   Make sure to print out all details accurately as our management will check the data submitted.")
    print("   Any form of innacuracy or invalid data will not be processed. Thank you for your understanding.")
    print("O"+"="*102+"O")
    return name

def final_confirmation():
    print("\t\t\t\tHave you confirmed your details?\n\t\t\t\t[1] Yes\t[2] Reset my details")
    print("O"+"="*102+"O")
    while True:
        confirmation = input("Input Operation: ")
        match confirmation:
            case "1"|"2":
                break
            case _:
                print("Invalid Option")
    return int(confirmation)

def final_output():
    print("O"+"="*102+"O")
    print("\n\tThank you", name, """for placing this order. Your order will be processed and you will
    \tbe contacted by one of our staff within 1-3 business days.""")
    print("\n\tYour bill came to a total of P", format(total_cart, ',.2f'),
          ".\n\tPlease prepare 50% of your total bill which is" , format(total_cart/2, ',.2f'),
          "php\n\tfor the processing of your order.")
    print("""\n\tOnce your order is processed, an agreement will be provided for \n\tservice finalization.\n
        Thank you for being our valued customer! We’ll make sure that you will have a blast!\n""")

def order_again():
    print("O"+"="*102+"O")
    print("\t\t\t\tDo you want to create another order?\n\t\t\t\t[1]Yes\t[2] No")
    print("O"+"="*102+"O")
    while True:
        order_again = input("Input Operation: ")
        match order_again:
            case "1"|"2":
                break
            case _:
                print("Invalid Option")
    return int(order_again)

#-------------------------------------------------------------------------#

#PARTY PACKS VARIABLES
party_pack1,party_pack2,party_pack3 = 0,0,0 #NUMBER OF PARTY PACKS ORDERED
price_pp1,price_pp2,price_pp3 = 10261.00, 11707.00, 12404.00 #PRICES OF EACH PARTY PACKS
pp1,pp2,pp3 = 0.00,0.00,0.00 #DISPLAYS THE TOTAL OF EACH ITEM ORDERED IN PARTY PACKS
total_party_pack = 0.00 #TOTAL IN PARTY PACKS

#RENTAL PACKS/ITEMS VARIABLES
rental_pack1,rental_pack2,rental_pack3 = 0,0,0 #NUMBER OF RENTAL PACKS ORDERED
price_rp1,price_rp2,price_rp3 = 100.00, 130.00, 160.00 #PRICES OF EACH EQUIPMENT PACKS
item1,item2,item3,item4,item5,item6 = 0,0,0,0,0,0 #NUMBER OF RENTAL ITEMS ORDERED
price_i1,price_i2,price_i3,price_i4,price_i5,price_i6=100.00,100.00,20.00,50.00,15.00,50.00 #PRICES OF EACH EQUIPMENT ITEMS
p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00 #DISPLAYS THE TOTAL OF EACH ITEM ORDERED IN EQUIPMENT RENTAL
total_rentals = 0.00 #TOTAL IN RENTAL AND EQUIPMENT PACKS/ITEMS

#RCATERING SERVICES VARIABLES
wed_pack1,wed_pack2,wed_pack3 = 0,0,0 #NUMBER OF WEDDING PACKS ORDERED
price_wp1,price_wp2,price_wp3 = 24000.00, 38000.00, 75000.00 #PRICES OF EACH WEDDING PACKS
b_pack1,b_pack2,b_pack3,b_pack4,b_pack5,b_pack6 = 0,0,0,0,0,0 #NUMBER OF BIRHTDAY PACKS ORDERED
price_bp1,price_bp2,price_bp3,price_bp4,price_bp5,price_bp6=18000.00,28000.00,55000.00,13000.00,21000.00,38000.00 #PRICES OF EACH BIRHTDAY PACKS
c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00 #DISPLAYS THE TOTAL OF EACH ITEM ORDERED IN CATERING SERVICES
total_catering_packs = 0.00 #TOTAL IN CATERING SERVICES PACKS

#----------------------MAIN CODE--------------------#

while True:
    MENU()
    main_opt = input("Input Operation[0-5]: ")
    main_option = check_main(main_opt)

    if main_option == 1:
        while True:
            information_options()
            select = input("Input Operation[1-4]: ")
            opt = four_option(select)
            if opt == 1:
                about_us()
                BACK()
            elif opt == 2:
                contact_us()
                BACK()
            elif opt == 3:
                terms_of_payment()
                BACK()
            elif opt == 4:
                break

                #If opt is 4, break the information options look and go back to MENU()
            
            else:
                print("Invalid Input")
                
            #Once done execetuing if-else, loop back to information_options()

                
    elif main_option == 2:
        while True:
            party_options()
            answer = input("Input Operation[1-3]: ")
            party_option = check_party_option(answer)
            
            
            if party_option == 1:
                PARTY_PACKAGES()
                ask_order_q = ask_if_order_q()     
                if ask_order_q == "O":
                    party_code = pack_option()
                    quantity = numberOfItems()
                    if party_code == 1:
                        total_party_pack += price_pp1*quantity
                        party_pack1 += quantity
                        pp1 = party_pack1*price_pp1
                    elif party_code == 2:
                        total_party_pack += price_pp2*quantity
                        party_pack2 += quantity
                        pp2 = party_pack2*price_pp2
                    else:
                        total_party_pack += price_pp3*quantity
                        party_pack3 += quantity
                        pp3 = party_pack3*price_pp3
                    print("\n\t\t\t\t[Successfully added to your cart!!!]\n")
                    
                ## If ask_order_q is B, automatically loop back to party_options()
                
            elif party_option == 2:
                show_cart_partypacks()
                ask_resets = ask_reset()
                if ask_resets == "R":
                    #RESET PARTY PACKS
                    party_pack1,party_pack2,party_pack3 = 0,0,0

                    pp1,pp2,pp3 = 0.00,0.00,0.00
                    
                    total_party_pack = 0.00
                    print("\n\t\t\t\tSuccessfully Cleared Your Party Cart!!!]\n")
                    
                ## If ask_resets is B, automatically loop back to party_options()

            elif party_option == 3:
                break

                ## If party_option is 3, break the party options loop and go back to MENU()
            
            else:
                print("Invalid Input")
            
    elif main_option == 3:
        while True:
            rental_options()
            select = input("Input Operation[1-4]: ")
            rental_option = four_option(select)
            
            if rental_option == 1:
                rentalMenuPacks()
                ask_order_q = ask_if_order_q()
                if ask_order_q == "O":
                    pack_code = pack_option()
                    quantity = numberOfItems()
                    if pack_code == 1:
                        total_rentals += price_rp1*quantity
                        rental_pack1 += quantity
                        p1 = rental_pack1*price_rp1
                    elif pack_code == 2:
                        total_rentals += price_rp2*quantity
                        rental_pack2 += quantity
                        p2 = rental_pack2*price_rp2
                    else:
                        total_rentals += price_rp3*quantity
                        rental_pack3 += quantity
                        p3 = rental_pack3*price_rp3
                    print("\n\t\t\t\t[Successfully added to your cart!!!]\n")
                    
                    ##Once done ordering, loop back to rental_options()

                ## If ask_order_q is B, automatically loop back to rental_options()

            elif rental_option == 2:
                rentalMenuItems()
                ask_order_q = ask_if_order_q()
                if ask_order_q == "O":
                    item_code = six_option()
                    quantity = numberOfItems()
                    if item_code == 1:
                        total_rentals += price_i1*quantity
                        item1 += quantity
                        p4 = item1*price_i1
                    elif item_code == 2:
                        total_rentals += price_i2*quantity
                        item2 += quantity
                        p5 = item2*price_i2
                    elif item_code == 3:
                        total_rentals += price_i3*quantity
                        item3 += quantity
                        p6 = item3*price_i3
                    elif item_code == 4:
                        total_rentals += price_i4*quantity
                        item4 += quantity
                        p7 = item4*price_i4
                    elif item_code == 5:
                        total_rentals += price_i5*quantity
                        item5 += quantity
                        p8 = item5*price_i5
                    else:
                        total_rentals += price_i6*quantity
                        item6 += quantity
                        p9 = item6*price_i6
                    print("\n\t\t\t\t[Successfully added to your cart!!!]\n")

                    ##Once done ordering, loop back to rental_options()
                    
                ## If ask_order_q is B, automatically loop back to rental_options()
                
            elif rental_option == 3:
                show_cart_rentals()
                ask_resets = ask_reset()
                if ask_resets == "R":
                    #RESET RENTAL PACKS
                    
                    rental_pack1,rental_pack2,rental_pack3 = 0,0,0
                    item1,item2,item3,item4,item5,item6 = 0,0,0,0,0,0
                    p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
                    total_rentals = 0.00
                    print("\n\t\t\t\t[Successfully Cleared Your Rental Cart!!!]\n")

                    ##Once done resetting, loop back to rental_options()

                ##If ask_reserts is B, automatically loop back to rental_options()
                
            elif rental_option == 4:
                break

                ## If rental_option is 4, break the rental options loop and go back to MENU()
            
            else:
                print("Invalid Input")

    elif main_option == 4:
        while True:
            catering_options()
            response = input("Input Operation[1-4]: ")
            catering_option = four_option(response)

            if catering_option == 1:
                WEDDING_PACKAGES()
                ask_order_q = ask_if_order_q()
                if ask_order_q == "O":
                    wed_pack_code = pack_option()
                    quantity = numberOfItems()
                    if wed_pack_code == 1:
                        total_catering_packs += price_wp1*quantity
                        wed_pack1 += quantity
                        c1 = wed_pack1*price_wp1
                    elif wed_pack_code == 2:
                        total_catering_packs += price_wp2*quantity
                        wed_pack2 += quantity
                        c2 = wed_pack2*price_wp2
                    else:
                        total_catering_packs += price_wp3*quantity
                        wed_pack3 += quantity
                        c3 = wed_pack3*price_wp3
                    print("\n\t\t\t\t[Successfully added to your cart!!!]\n")

                    ##Once done ordering, loop back to catering_options()
                    
                ## If ask_order_q is B, automatically loop back to catering_options()

                    
            elif catering_option == 2:
                BIRTHDAY_PACKAGES()
                ask_order_q = ask_if_order_q()
                if ask_order_q == "O":
                    bday_pack = six_option()
                    quantity = numberOfItems()
                    if bday_pack == 1:
                        total_catering_packs += price_bp1*quantity
                        b_pack1 += quantity
                        c4 = b_pack1*price_bp1
                    elif bday_pack == 2:
                        total_catering_packs += price_bp2*quantity
                        b_pack2 += quantity
                        c5 = b_pack2*price_bp2
                    elif bday_pack == 3:
                        total_catering_packs += price_bp3*quantity
                        b_pack3 += quantity
                        c6 = b_pack3*price_bp3
                    elif bday_pack == 4:
                        total_catering_packs += price_bp4*quantity
                        b_pack4 += quantity
                        c7 = b_pack4*price_bp4
                    elif bday_pack == 5:
                        total_catering_packs += price_bp5*quantity
                        b_pack5 += quantity
                        c8 = b_pack5*price_bp5
                    else:
                        total_catering_packs += price_bp6*quantity
                        b_pack6 += quantity
                        c9 = b_pack6*price_bp6
                    print("\n\t\t\t\t[Successfully added to your cart!!!]\n")

                    ##Once done ordering, loop back to catering_options()
                    
                ## If ask_order_q is B, automatically loop back to catering_options()

            elif catering_option == 3:
                show_cart_catering()
                ask_resets = ask_reset()
                if ask_resets == "R":
                    #RESET CATERING PACKS
                    
                    wed_pack1,wed_pack2,wed_pack3 = 0,0,0
                    b_pack1,b_pack2,b_pack3,b_pack4,b_pack5,b_pack6 = 0,0,0,0,0,0
                    c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
                    total_catering_packs = 0.00
                    print("\n\t\t\t\t[Successfully Cleared Your Catering Cart!!!]\n")

                    ##Once done resetting, loop back to catering_options()

                ##If ask_reserts is B, automatically loop back to catering_options()
                
            elif catering_option == 4:
                break

                ## If catering_option is 4, break the catering options loop and go back to MENU()
            
            else:
                print("Invalid Input")

    elif main_option == 5:
        if total_party_pack == 0 and total_rentals == 0 and total_catering_packs == 0:
            print("\t\t\t\tYou have no current orders")
            BACK()
        else:
            total_cart = total_party_pack + total_rentals + total_catering_packs
            print("O"+"="*43+"***Your Cart***"+"="*44+"O"+"\n")
            if total_party_pack != 0:
                show_cart_partypacks()
            if total_rentals != 0:
                show_cart_rentals()
            if total_catering_packs != 0:
                show_cart_catering()
            print("O"+"="*45+"***Total***"+"="*46+"O")
            print("\t"*8+"Your current total is P "+str(format(total_cart, ',.2f')))
            checkout = confirm_checkout()
            if checkout == 1:
                while True:
                    name = details()
                    confirmation = final_confirmation()
                    if confirmation == 1:
                        final_output()
                        break

                    #If confirmation is 2, automatically loop back to name=details()
                    
                order_again_program = order_again()
                
                if order_again_program == 1:
                    #RESET PARTY PACKS 
                    party_pack1,party_pack2,party_pack3 = 0,0,0
                    pp1,pp2,pp3 = 0,0,0
                    total_party_pack = 0

                    #RESET RENTAL PACKS
                    rental_pack1,rental_pack2,rental_pack3 = 0,0,0
                    item1,item2,item3,item4,item5,item6 = 0,0,0,0,0,0
                    p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0,0,0,0,0,0,0,0,0
                    total_rentals = 0

                    #RESET CATERING PACKS
                    wed_pack1,wed_pack2,wed_pack3 = 0,0,0
                    b_pack1,b_pack2,b_pack3,b_pack4,b_pack5,b_pack6 = 0,0,0,0,0,0
                    c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0,0,0,0,0,0,0,0,0             
                    total_catering_packs = 0
                else:
                    break

                    #If an order succeeded and the user answers 2 [No], the main loop breaks
                
            elif checkout == 2:
                #RESET PARTY PACKS   
                party_pack1,party_pack2,party_pack3 = 0,0,0
                pp1,pp2,pp3 = 0,0,0  
                total_party_pack = 0

                #RESET RENTAL PACKS
                rental_pack1,rental_pack2,rental_pack3 = 0,0,0
                item1,item2,item3,item4,item5,item6 = 0,0,0,0,0,0
                p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0,0,0,0,0,0,0,0,0
                total_rentals = 0

                #RESET CATERING PACKS
                wed_pack1,wed_pack2,wed_pack3 = 0,0,0
                b_pack1,b_pack2,b_pack3,b_pack4,b_pack5,b_pack6 = 0,0,0,0,0,0
                c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0,0,0,0,0,0,0,0,0            
                total_catering_packs = 0
                print("\n\t\t\t\tSUCCESSFULLY CLEARED ALL OF YOUR ORDERS!!!\n")

            ##If checkout is 3, automatically loop back to MENU()
                

    elif main_option == 0:
        break

    else:
        print("Invalid Input")

print("O"+"="*102+"O")
print("""
\t\t\t\tThanks for using our program.

\t\t\t\tProgrammed by:
\t\t\t\tLuis Miguel Cayanan
""")
print("O"+"="*102+"O")




















