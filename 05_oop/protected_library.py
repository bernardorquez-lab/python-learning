class LibraryItem:

    def __init__(self, title):
            self.title = title
            self._loan_days = 7
            self._is_borrowed = False

    def borrow(self):
        self._is_borrowed = True
        print(f"{self.title} borrowed. Please return within {self._loan_days} day(s).")


class Book(LibraryItem):

    def __init__(self, title, author):
            super().__init__(title)
            self.author = author
            self._loan_days = 14

    def show(self):
        print(f'Book: {self.title} by {self.author} | Loan Days: {self._loan_days}')

class DVD(LibraryItem):

    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
        self._loan_days = 3

    def show(self):
        print(f'DVD: {self.title} | {self.duration} mins | Loan Days: {self._loan_days}')


if __name__ == "__main__":
    book = Book('Noli Me Tangere', 'Jose Rizal')
    dvd = DVD('Heneral Luna', 120)

    book.show()
    book.borrow()  
    dvd.show()
    dvd.borrow()      
    print('Accessed from outside:', book._loan_days)
