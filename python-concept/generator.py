def index_words(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

text = '''In Python, a generator is a type of iterable that can be iterated over only once. 
        They are used to create iterators more easily.Generators are defined using a function 
        with one or more yield statements. The main difference between a regular function and 
        a generator function is that a generator function returns a generator object when called.'''

print(index_words(text))

# problem with above code
# 1. code is bit dense and noisy
# 2. memory(RAM) insufficient
# solution use generator instead of list

def index_words2(text):
    if text:
        yield 0
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index+1

it = index_words2(text)
print(next(it))
print(next(it))
print(next(it))