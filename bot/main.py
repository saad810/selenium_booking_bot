# bot
from booking.booking import Booking

# booking_bot = Booking()
# booking_bot.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    print("Exiting")