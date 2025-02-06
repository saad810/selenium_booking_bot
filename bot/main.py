# bot
from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='USD')
    bot.search_place_to_visit(place_to_visit='New York')
    bot.select_date()
    bot.select_adults()
    bot.click_search()
    bot.apply_sort()
    bot.add_more_filters()
    print("[main] Exiting")

