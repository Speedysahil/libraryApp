class Liabrary:
  def __init__(self,liabrary_name,*list1ofbooks):
    self.list1ofbook = list(list1ofbooks)
    self.liabrary_name = liabrary_name
    self.lending_books = {}

  def displaybooks(self):
    for items in self.list1ofbook:
      print(items)

  def add_book(self):
      addbook= input("Enter the book name")
      return self.list1ofbook.append(addbook)

  def lendingbook(self):
      def lendercanissuebook(self):
          for key,value in self.lending_books.items:
              if value == lender_name:
                  return False
          return True

      lender_name = input("enter your name").lower()

      if lendercanissuebook():
          book_to_issue = input("Enter the name of book")
          if book_to_issue in self.list1ofbook:
              new_item = {book_to_issue,lender_name}
              self.lending_books.update(new_item)
              self.list1ofbook.remove(book_to_issue)
              print("book issued succesfully")

          else:
              print("we dont have that book")
      else:
          print("sorry you cant issue more than one book")


  def return_book(self):
      name = "enter your name"
      booktoissue = "Enter the name of book "
      if booktoissue != self.list1ofbook:
          self.list1ofbook.append(booktoissue)
          del self.lending_books[booktoissue]

      else:
          print("sorry this book is not part of the liabrary ")


se1 = Liabrary("harry","geeta","mahabarat")

def main():
    while 1:
        print ("""
        displaybooks - to display the books 
        addbook - to add the book 
        lendbook - to lend the book 
        returnbook - to return the book
        exit - to exit the liabrary"""
        )
        take_input = input("enter the choice\n").lower()

        if take_input == "displaybooks":
            se1.displaybooks()

        elif take_input == "addbook":
            se1.add_book()
        elif take_input == "lendbook":
            se1.lending_books()
        elif take_input == "returnbook":
            se1.return_book()

        elif take_input == "exit":
            break
        else:
            print("not a valid input ")
main()











