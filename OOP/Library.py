class LibraryItem:
    """Represents a library item that a patron can check out from a library."""

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = str(title)
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """Returns the ID of the library item."""
        return self._library_item_id

    def get_title(self):
        """Returns the location of the library item."""
        return self._title

    def get_location(self):
        """Returns the location of the library item."""
        return self._location

    def set_location(self, location):
        """Sets the location of the library item."""
        self._location = location

    def get_checked_out_by(self):
        """Returns the patron that the library item was checked out by."""
        return self._checked_out_by

    def set_checked_out_by(self, checked_out_by):
        """Sets the patron that the item was checked out by."""
        self._checked_out_by = checked_out_by

    def get_requested_by(self):
        """Returns the patron that the library item was requested by."""
        return self._requested_by

    def set_requested_by(self, requested_by):
        """Sets the patron that the item was requested by."""
        self._requested_by = requested_by

    def get_date_checked_out(self):
        """Returns the date that the library item was checked out in days."""
        return self._date_checked_out

    def set_date_checked_out(self, date_checked_out):
        """Sets the date that the item was checked out on in days."""
        self._date_checked_out = date_checked_out


class Book(LibraryItem):
    """Represents a book that can be checked out from a library. This is a subclass of LibraryItem."""

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = str(author)

    def get_author(self):
        """Returns the author of the book."""
        return self._author

    @staticmethod
    def get_check_out_length():
        """Returns how long the book can be checked out for without incurring fines."""
        return 21


class Album(LibraryItem):
    """Represents an album that can be checked out from a library. This is a subclass of LibraryItem."""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = str(artist)

    def get_artist(self):
        """Returns the artist of the album."""
        return self._artist

    @staticmethod
    def get_check_out_length():
        """Returns how long the artist can be checked out for without incurring fines."""
        return 14


class Movie(LibraryItem):
    """Represents a movie that can be checked out from a library. This is a subclass of LibraryItem."""

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = str(director)

    def get_director(self):
        """Returns the director of the movie."""
        return self._director

    @staticmethod
    def get_check_out_length():
        """Returns how long the movie can be checked out for without incurring fines."""
        return 7


class Patron:
    """Represents a patron of a library. Patrons can check out books or request them to be put on hold. If the
    patron does not return books on time, they can incur fines. The patron can pay their fines."""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """Returns the patron's ID."""
        return self._patron_id

    def get_name(self):
        """Returns the patron's name."""
        return self._name

    def get_checked_out_items(self):
        """Returns a list of items the patron has checked out."""
        return self._checked_out_items

    def add_library_item(self, item):
        """Adds an item to the list of items checked out by the patron."""
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """Removes an item from the list of items checked out by the patron."""
        self._checked_out_items.remove(item)

    def get_fine_amount(self):
        """Returns how much the patron owes in fines."""
        return self._fine_amount

    def amend_fine(self, amount):
        """Increases or decreases the amount of fines the patron owes."""
        self._fine_amount += amount


class Library:
    """Represents a library that has a collection of library items which can be books, albums, or movies.
    The library can be used by patrons, but only if they are library members.."""

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        """Adds an item to the library's holdings."""
        return self._holdings.append(item)

    def add_patron(self, patron):
        """Adds a patron to the list of the library's members."""
        return self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """Looks up a library item in the library's holdings using the item's ID."""

        # For each of the items in the library's holdings.
        for item in self._holdings:
            # If the item's ID is equal to the library item's ID, return the item.
            if item.get_library_item_id() == library_item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """Looks up a patron in the library's member list using the patron's ID."""

        # For each of the patrons in the library's membership list.
        for patron in self._members:
            # If the patron's ID is equal to the library member's ID, return the patron.
            if patron.get_patron_id() == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Checks out a particular library item for a particular patron."""

        # Initialize a patron and item variable for ease of use.
        patron = self.lookup_patron_from_id(patron_id)
        item = self.lookup_library_item_from_id(library_item_id)

        # If the patron entered is not in the member list, return an error.
        if patron is None:
            return print("patron not found")

        # If the item entered is not in the library's item list, return an error.
        if item is None:
            return print("item not found")

        # If the item entered is already checked out, return an error.
        if item.get_location() == "CHECKED_OUT":
            return print("item already checked out")

        # If the item is already requested by someone, return an error.
        if item.get_requested_by() is not None and item.get_requested_by() != patron:
            return print("item on hold by other patron")

        # Update the item to specify which patron checked it out.
        item.set_checked_out_by(patron_id)
        # Sets the date the item was checked out to the current date of the library.
        item.set_date_checked_out(self._current_date)
        # Sets the location of the item to Checked Out.
        item.set_location("CHECKED_OUT")

        # If the item was requested by the patron entered, update the requested by field of the item to none.
        if item.get_requested_by() == patron:
            item.set_requested_by(None)

        # Adds the item to the list of items the patron has checked out.
        patron.add_library_item(item)

        return print("check out successful")

    def return_library_item(self, library_item_id):
        """Initiates the return of a particular item to the library."""

        # Initialize a patron and item variable for ease of use.
        item = self.lookup_library_item_from_id(library_item_id)
        patron = self.lookup_patron_from_id(item.get_checked_out_by())

        # If the item does not exist in the library's catalogue, return an error.
        if item is None:
            return print("item not found")

        # If the item is not checked out, return an error.
        if item.get_location() != "CHECKED_OUT":
            return print("item already in library")

        # Remove the item from the patron's list of checked out items.
        patron.remove_library_item(item)

        # If the item was requested by another patron, set the location to the on hold shelf.
        if item.get_requested_by() is not None:
            item.set_location("ON_HOLD_SHELF")
        # Otherwise, return the item to the shelf.
        else:
            item.set_location("ON_SHELF")

        # Set the check-out status of the item to none.
        item.set_checked_out_by(None)

        return print("return successful")

    def request_library_item(self, patron_id, library_item_id):
        """Adds a request/hold on a particular library item for a particular patron."""

        # Initialize a patron and item variable for ease of use.
        patron = self.lookup_patron_from_id(patron_id)
        item = self.lookup_library_item_from_id(library_item_id)

        # If the patron does not exist in the list of the library's members, return an error.
        if patron is None:
            return print("patron not found")

        # If the item does not exist in the library's catalogue, return an error.
        if item is None:
            return print("item not found")

        # If the item was already requested by another patron, return an error.
        if item.get_requested_by() is not None:
            return print("item already on hold")

        # Otherwise, set the item's requested by field to the patron.
        item.set_requested_by(patron)

        # If the item's location is on the shelf, set the location to the hold shelf.
        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")

        return print("request successful")

    def pay_fine(self, patron_id, amount):
        """Reduces the amount of fines the patron owes."""

        # Initialize a patron variable for ease of use.
        patron = self.lookup_patron_from_id(patron_id)

        # If the patron is not in the list of library members, return an error.
        if patron is None:
            return print("patron not found")

        # Otherwise, reduce the patron's fine by the amount entered and return a confirmation.
        patron.amend_fine(-amount)

        return print("payment successful")

    def increment_current_date(self):
        """Increases the current date for the library."""

        # Increments the library's current day by 1.
        self._current_date += 1

        # For each of the patrons in the library's member list.
        for patron in self._members:
            # For each of the items that are checked out by each patron.
            for item in patron.get_checked_out_items():
                # Calculate the item's due date as a day, which is the sum of the day the item was checked out and how
                # long the particular item can be checked out for.
                due_date = item.get_date_checked_out() + item.get_check_out_length()
                # If the library's current day is greater than the calculated due date, add 0.10 cents per late book.
                if self._current_date > due_date:
                    patron.amend_fine(0.10)


def main():
    """The main function that is triggered when the file is run as a script."""

    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    lib.check_out_library_item("bcd", "456")
    for _ in range(7):
        lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item("abc", "567")
    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for _ in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")


if __name__ == '__main__':
    main()