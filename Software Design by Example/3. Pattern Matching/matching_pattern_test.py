from matching_pattern import Lit, Any, Either

def any_matches_empty():
    assert Any().match("")

def any_matches_full_string():
    assert Any().match("abc")

def any_matches_as_prefix():
    assert Any(Lit("ab")).match("xyzab")

def any_matches_as_suffix():
    assert Lit("ab",Any()).match("abxyz")

def any_matches_interior():
    assert Lit("ab", Any(Lit("f"))).match("abcdef")

def either_two_literal_first():
    assert Either(Lit("a"), Lit("b")).match("a"), "Not Matching .."

def either_two_literals_not_both():
    assert not Either(Lit("a"), Lit("b")).match("ab")

def either_followed_by_literal_match():
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")

def either_followed_by_literal_no_match():
    assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")

def literal_match_entire_string():
    assert Lit("abc").match("abc")

def literal_substring_alone_no_match():
    assert not Lit("ab").match("abc")

def literal_superstring_no_match():
    assert not Lit("abc").match("ab")

def literal_followed_by_literal_match():
    assert Lit("a", Lit("b")).match("ab")

def literal_followed_by_literal_no_match():
    assert not Lit("a", Lit("b")).match("ac")
