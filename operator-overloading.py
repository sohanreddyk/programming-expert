class Page:
    def __init__(self, words, page_number):
        self.word=words
        self.page_number=page_number

    def __add__(self,other):
        new_words=self.word + other.word
        new_page_number =max(self.page_number, other.page_number)+1
        return Page(new_words, new_page_number)
    
page1=Page("This is content of page 1",1)
page2=Page(" This is content of page 2",2)
page3=page1 + page2
print(page3.word , page3.page_number)  # This is content of page 1This is content of page 2 3

