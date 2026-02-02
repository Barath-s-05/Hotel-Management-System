class HotelFareCal:
    room_no_count = 0

    def __init__(self, name, address, cindate, coutdate):
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = HotelFareCal.room_no_count + 1
        HotelFareCal.room_no_count += 1

        self.s = 0  # Room rent
        self.r = 0  # Restaurant
        self.t = 0  # Laundry
        self.p = 0  # Games
        self.a = 1800  # Service charge

    def book_room(self, room_type, nights):
        rates = {1: 7000, 2: 5500, 3: 4000, 4: 2000}
        self.s = rates.get(room_type, 0) * nights

    def add_food(self, price, qty):
        self.r += price * qty

    def add_laundry(self, price, qty):
        self.t += price * qty

    def add_game(self, price, hours):
        self.p += price * hours

    def generate_bill(self):
        subtotal = self.s + self.r + self.t + self.p
        return {
            "Customer Name": self.name,
            "Room No": self.rno,
            "Room Rent": self.s,
            "Food Bill": self.r,
            "Laundry Bill": self.t,
            "Game Bill": self.p,
            "Service Charge": self.a,
            "Grand Total": subtotal + self.a
        }
