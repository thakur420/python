class Lit:
    def __init__(self, chars, rest=None) -> None:
        self.chars = chars
        self.rest = rest

    def match(self, text, start=0):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return False
        if self.rest :
            return self.rest.match(text,end)
        return end == len(text)
    
def test_literal_match_entire_string():
    assert Lit("abc").match("abc")

def test_literal_substring_alone_no_match():
    assert not Lit("ab").match("abc")

def test_literal_superstring_no_match():
    assert not Lit("abc").match("ab")

def test_literal_followed_by_literal_match():
    assert Lit("a", Lit("b")).match("ab")

def test_literal_followed_by_literal_no_match():
    assert not Lit("a", Lit("b")).match("ac")

if __name__ == "__main__":
    test_literal_match_entire_string()
    test_literal_substring_alone_no_match()
    test_literal_superstring_no_match()
    test_literal_followed_by_literal_match()
    test_literal_followed_by_literal_no_match()