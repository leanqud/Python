from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        shelf = self.head
        count = 0
        while shelf != None:
            count += 1
            shelf = shelf.getNext()
        return count

    def insertBook(self, book):
        now = self.head
        before = None
        stop = False
        while now != None and not stop:
            if now.getData() > book:
                stop = True
            else:
                before = now
                now = now.getNext()
        newNode = BookCollectionNode(book)
        if before == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(now)
            before.setNext(newNode)

    def getBooksByAuthor(self, author):
        shelf = self.head
        authorList = ""
        while shelf != None:
            if shelf.getData().getAuthor().upper() == author.upper():
                authorList = authorList + shelf.getData().getBookDetails() + "\n"
            shelf = shelf.getNext()
        return authorList

    def getAllBooksInCollection(self):
        shelf = self.head
        authorList = ""
        while shelf != None:
            authorList = authorList + shelf.getData().getBookDetails() + "\n"
            shelf = shelf.getNext()
        return authorList
    
    def removeAuthor(self, author):
        now = self.head
        before = None
        while now != None and now.getData().getAuthor().lower() == author.lower():
            self.head = now.getNext()
            now = self.head
        while now:
            while now != None and now.getData().getAuthor().lower() != author.lower():
                before = now
                now = now.getNext()
            if now == None:
                return
            before.setNext(now.getNext())
            now = before.getNext()
        
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        return BookCollection.recursiveSearchTitle(self, title, bookNode.getNext())
