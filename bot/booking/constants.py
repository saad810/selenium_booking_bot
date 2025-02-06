BASE_URL = 'https://www.booking.com'
# BASE_URL = 'https://docs.pytest.org/en/stable/how-to/tmp_path.html'

sorting_options = {
    "our_top_picks" :'aria-label="Our top picks"',
    "price_highest" :'aria-label="Price (highest first)"',
    "price_lowest " :'aria-label="Price (lowest first)"',
    "top_reviewed":'aria-label="Top reviewed"'
}

print(sorting_options.get('top_reviewed'))