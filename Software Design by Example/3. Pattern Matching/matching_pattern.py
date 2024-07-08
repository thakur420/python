import matching_pattern_test as test 
class Match:
    def __init__(self,rest) -> None:
        self.rest = rest if rest is not None else Null()
    
    def match(self,text):
        result = self._match(text,0)
        return result == len(text)
    
class Null(Match):
    def __init__(self):
        self.rest = None
    
    def _match(self,text,start):
        return start
    
class Lit(Match):
    def __init__(self, chars,rest=None) -> None:
        super().__init__(rest)
        self.chars = chars
    
    def _match(self,text,start):
        # print(f"Lit match(text,start) => {text},{start}")
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text,end)
    
class Any(Match):
    def __init__(self, rest=None) -> None:
        super().__init__(rest)

    def _match(self,text,start):
        for i in range(start,len(text) + 1):
            end = self.rest._match(text,i)
            # print(f"i,end,text => {i},{end},{text}")
            if end == len(text):
                return end
        return None
    
class Either(Match):
    def __init__(self, left, right, rest=None) -> None:
        super().__init__(rest)
        self.left = left 
        self.right = right
    
    def _match(self,text,start):
        # print(f"left,right => {self.left.chars},{self.right.chars}")
        for pat in [self.left, self.right]:
            end = pat._match(text,start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
    
if __name__ == "__main__":
    print(Lit("2023-",Any(Lit(".",Any()))).match("2023-01.txt"))
    test.either_two_literal_first()
    test.either_two_literals_not_both()
    test.either_followed_by_literal_match()
    test.either_followed_by_literal_no_match()
