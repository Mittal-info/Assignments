def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat Type:", seat_type)
    print("Snacks:", snacks)
    print("------------------")


# 1. Only positional arguments
book_movie_ticket("Jawan", "VIP", "Popcorn")

# 2. Only keyword arguments
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="Premium",
    snacks="Cold Drink"
)

# 3. Mix of positional and keyword arguments
book_movie_ticket("Jawan", snacks="Nachos", seat_type="VIP")