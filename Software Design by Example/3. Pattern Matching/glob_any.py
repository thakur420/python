from glob_lit import Lit

class Any:
    def __init__(self, rest=None) -> None:
        self.rest = rest

    def match(self, text, start=0):
        if self.rest is None:
            return True
        for i in range(start,len(text)):
            if self.rest.match(text,i):
                return True
        return False
    
def test_any_matches_empty():
    assert Any().match("")

def test_any_matches_full_string():
    assert Any().match("abc")

def test_any_matches_as_prefix():
    assert Any(Lit("ab")).match("xyzab")

def test_any_matches_as_suffix():
    assert Lit("ab",Any()).match("abxyz")

def test_any_matches_interior():
    assert Lit("ab", Any(Lit("f"))).match("abcdef")

if __name__ == "__main__":
    test_any_matches_empty()
    test_any_matches_full_string()
    test_any_matches_as_prefix()
    test_any_matches_as_suffix()
    test_any_matches_interior()

