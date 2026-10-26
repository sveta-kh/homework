#Movie Ticket System

class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price) -> None:
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        
        MovieTicket.total_tickets_sold += 1

movieticket1 = MovieTicket("Titanic", "1", "4.0$")
print(movieticket1.movie_title)
print(movieticket1.seat_number)
print(movieticket1.price)
print(movieticket1.cinema_name)

movieticket2 = MovieTicket("Titanic", "2", "5.0$")
print(movieticket2.movie_title)
print(movieticket2.seat_number)
print(movieticket2.price)
print(movieticket2.cinema_name)

movieticket3 = MovieTicket("Titanic", "3", "6.0$")
print(movieticket3.movie_title)
print(movieticket3.seat_number)
print(movieticket3.price)
print(movieticket3.cinema_name)

print(MovieTicket.total_tickets_sold)
