class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
class Ebook(book):
    def __init__(self,title,author,format):
        super().__init__(title,author)
        self.format=format
book = book("the great gatsby","f.scott fitzgerland")
ebook = Ebook("python crash couse","eric mathes","pdf")
print("book:",book.title,"by",book.author)
print("Ebook",ebook.title,"by",ebook.author,"in",ebook.format,"format")