import typing

StrList = typing.List[str]

class Book:
    """
    This class represents a book in the system.
    """
    
    def __init__(self, name: str, authors: StrList, tags: StrList, difficulty: int):
        """
        
        parameters:
            name: str           the name of the book
            authors: List[str]  the authors
            tags: List[str]     tags (like ['comm_alg', 'ring_theory'])
            difficulty: int     an integer from 1-10 describing the book's difficulty level.
        """
        self.name = name
        self.authors = authors[:]
        self.tags = tags[:]
        self.difficulty = difficulty

    def __str__(self):
        authors_s = '@"{}"'.format('" , @"'.join(self.authors)) if self.authors else ''
        tags_s = '#' + ', #'.join(self.tags) if self.tags else ''
        return '{}, {}, {}, difficulty: {}/10'.format(self.name, authors_s, tags_s, self.difficulty)

    def __repr__(self):
        return 'Book{{{}}}'.format(str(self))

class BookList:
    """
    This class represents a Book list.
    """

    def __init__(self):
        self.books = []
        self.tagmap = {}

    def __getitem__(self, key):
        if isinstance(key, str):
            if key[0] == '#':
                tag_alias = key[1:]
                tag = self.tagmap.get(tag_alias, tag_alias)
                return [book for book in self.books if tag in book.tags]
            elif key[0] == '@':
                author = book[1:]
                return [book for book in self.books if author in book.authors]
            return [book for book in self.books if book.name == key]
        raise IndexError()

    def append(self, book):
        self.books.append(book)

def main():
    b = Book('Introduction to Commutative Algebra',
            ['M.F. Atiyah', 'I.G. Macdonald'],
            ['comm_alg', 'alg_geo', 'alg_num_th'],
            3)
    bl = BookList()
    bl.append(b)
    print(bl['#comm_alg'])

if __name__ == '__main__':
    main()

