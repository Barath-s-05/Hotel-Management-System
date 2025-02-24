class HotelFareCal:
    room_no_count = 0
    
    def __init__(self, rt="", s=0, p=0, r=0, t=0, a=1800, name="", address="", cindate="", coutdate=""):
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = HotelFareCal.room_no_count + 1
        HotelFareCal.room_no_count += 1

    def inputdata(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.cindate = input("Enter your check-in date: ")
        self.coutdate = input("Enter your checkout date: ")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):
        print("We have the following rooms for you:")
        print("1. SUITE -> Rs 7000 PN")
        print("2. EXECUTIVE -> Rs 5500 PN")
        print("3. DELUXE -> Rs 4000 PN")
        print("4. STANDARD -> Rs 2000 PN")
        
        try:
            x = int(input("Enter your choice: "))
            n = int(input("For how many nights would you like to stay? "))
            
            room_rates = {1: 7000, 2: 5500, 3: 4000, 4: 2000}
            
            if x in room_rates:
                self.s = room_rates[x] * n
                print(f"You have opted for room type {x}. Your total room rent is Rs {self.s}\n")
            else:
                print("Invalid choice. Please choose a valid room.")
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def restaurant_bill(self):
        print("***** RESTAURANT MENU *****")
        menu = {
            1: ("Water", 20),
            2: ("Tea", 10),
            3: ("Breakfast Combo", 90),
            4: ("Lunch", 110),
            5: ("Dinner", 150),
            6: ("Exit", 0)
        }

        while True:
            print("\n".join([f"{key}. {val[0]} -> Rs {val[1]}" for key, val in menu.items()]))
            try:
                c = int(input("Enter your choice: "))
                if c == 6:
                    break
                if c in menu:
                    qty = int(input("Enter the quantity: "))
                    self.r += menu[c][1] * qty
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        print("Total food cost: Rs", self.r, "\n")

    def laundry_bill(self):
        print("***** LAUNDRY MENU *****")
        laundry_menu = {
            1: ("Shorts", 3),
            2: ("Trousers", 4),
            3: ("Shirt", 5),
            4: ("Jeans", 6),
            5: ("Girlsuit", 8),
            6: ("Exit", 0)
        }

        while True:
            print("\n".join([f"{key}. {val[0]} -> Rs {val[1]}" for key, val in laundry_menu.items()]))
            try:
                e = int(input("Enter your choice: "))
                if e == 6:
                    break
                if e in laundry_menu:
                    qty = int(input("Enter the quantity: "))
                    self.t += laundry_menu[e][1] * qty
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        print("Total Laundry Cost: Rs", self.t, "\n")

    def game_bill(self):
        print("***** GAME MENU *****")
        game_menu = {
            1: ("Table Tennis", 300),
            2: ("Bowling", 400),
            3: ("Snooker", 400),
            4: ("Video Games", 300),
            5: ("Pool", 250),
            6: ("Exit", 0)
        }

        while True:
            print("\n".join([f"{key}. {val[0]} -> Rs {val[1]} per hour" for key, val in game_menu.items()]))
            try:
                g = int(input("Enter your choice: "))
                if g == 6:
                    break
                if g in game_menu:
                    hrs = int(input("No. of hours: "))
                    self.p += game_menu[g][1] * hrs
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        print("Total Game Bill: Rs", self.p, "\n")

    def display(self):
        print("\n****** HOTEL BILL ******")
        print(f"Customer Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Check-in Date: {self.cindate}")
        print(f"Check-out Date: {self.coutdate}")
        print(f"Room No: {self.rno}")
        print(f"Room Rent: Rs {self.s}")
        print(f"Food Bill: Rs {self.r}")
        print(f"Laundry Bill: Rs {self.t}")
        print(f"Game Bill: Rs {self.p}")
        self.rt = self.s + self.t + self.p + self.r
        print(f"Subtotal Bill: Rs {self.rt}")
        print(f"Service Charge: Rs {self.a}")
        print(f"Grand Total Bill: Rs {self.rt + self.a}\n")


def main():
    rooms = []
    customer = None

    while True:
        print("\n1. Enter Customer Data\n2. Room Rent\n3. Restaurant Bill\n4. Laundry Bill\n5. Game Bill\n6. Show Total Bill\n7. Rooms Booked\n8. Exit")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                customer = HotelFareCal()
                rooms.append({"room_no": customer.rno})
                customer.inputdata()
            elif choice in range(2, 6) and customer:
                [customer.roomrent, customer.restaurant_bill, customer.laundry_bill, customer.game_bill][choice - 2]()
            elif choice == 6 and customer:
                customer.display()
            elif choice == 7:
                print(rooms if rooms else "All rooms available")
            elif choice == 8:
                break
            else:
                print("Invalid choice or enter customer data first.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

main()
