class Document():
    WELCOM_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # class method
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title = title, author = author, context = 'nothing')
    
    # normal method
    def get_context_length(self):
        return len(self.__context)
    
    # static method
    @staticmethod
    def get_welcome(context):
        return Document.WELCOM_STR.format(context)

empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')


print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))