# class Book:
#     book="Book"
#     def __init__(self,id,tittle,year,price):
#         self.price=price
#         self.year=year
#         self.tittle=tittle
#         self.id=id
#     def __str__(self):
#         return f"[{self.id}],{self.tittle},{self.year},{self.price}"
# class Add_Book_class:
#     def __init__(self):
#           self.books=[]
#           self.next_id=1
#     def add_book(self,tittle,year,price):
#         b=Book(self.next_id,tittle,year,price)
#         self.books.append(b)
#         self.next_id+=1
#         return b
#     def get_all(self):
#         return self.books
#     def get_id(self,book_id):
#         return next((b for b in self.books if b.id == book_id),None)
#     def updade_book(self,book_id,tittle=None,year=None,price=None):
#         b=self.get_id(book_id)
#         if not b:
#             return False
#         b.tittle=tittle or b.tittle
#         b.year=year or b.year
#         b.pruce=price or b.price
#         return True
#     def __len__(self):
#             return len(self.books)

# m=Add_Book_class()
# m.add_book("skazki",1988,101)
# m.add_book("skazki2",1989,102)
# m.add_book("skazki3",1990,103)
# m.add_book("skazki4",19891,104)

# for b in m.get_all():
#      print(b)

# class Author:
#     def __init__(self,id,full_name,birth_year,country):
#         self.id=id
#         self.fullname=full_name
#         self.birth_yera=birth_year
#         self.country=country
#     def __str__(self):
#             return f"[{self.id}],{self.full},{self.year},{self.price}"

        



# Задача 2

# class Publication:
#     def __init__(self,tittle,year):
#         self.tittle=tittle
#         self.year=year
# class Book(Publication):
#     def get_info_book(self,pages):
#         print(f"Book:{self.tittle} {self.year},Pages:{self.pages}") 
# class Magazine(Publication):
#     def get_info__magazine(self,issu_number):
#         print(f"Book:{self.tittle} {self.year},Issue:{self.issue_numver}")
# p=Publication("skazka",1998)
# b=Book()
# b.get_info_book()

















