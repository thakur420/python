from glob_lit import Lit

class Either:
    def __init__(self, left, right, rest=None) -> None:
        self.left = left
        self.right = right
        self.rest = rest    
    
    def match(self, text, start=0):
        return (self.left.match(text,start) and self.rest.match(text,start+ len())) or \
            (self.right.match(text,start) and self.rest.match(text,start+len()))
    
def test_either_two_literal_first():
    assert Either(Lit("a"), Lit("b")).match("a")

def test_either_two_literals_not_both():
    assert not Either(Lit("a"), Lit("b")).match("ab")

def test_either_followed_by_literal_match():
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")

def test_either_followed_by_literal_no_match():
    assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")

if __name__ == "__main__":
    test_either_two_literal_first()
    test_either_two_literals_not_both()
    test_either_followed_by_literal_match()
    test_either_followed_by_literal_no_match()
