from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_Book():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert b.getTitle() == "Ready Player One"
    assert b.getAuthor() == "Cline, Ernest"
    assert b.getYear() == 2011

def test_BookCollectionNode():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    n = BookCollectionNode(b)
    n.setNext(1)
    assert n.getData().getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert n.getNext() == 1
    
def test_BookCollection1():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    print(bc.getBooksByAuthor("KING, Stephen"))

def test_BookCollection2():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    print(bc.getAllBooksInCollection())
    bc.removeAuthor("King, Stephen")
    print(bc.getAllBooksInCollection())
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b3)
    bc.removeAuthor("Cline, Ernest")
    print(bc.getAllBooksInCollection())

if __name__ == "__main__":
#def test_BookCollection3():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False
