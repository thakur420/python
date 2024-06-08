'''
Item6: Take advantage of each block in TRY/EXCEPT/ELSE
'''
import json
def load_json_key(data,key):
    try:
        result_dict = json.loads(data) #Raise ValueError
    except ValueError as e:
        print(f'error msg : {e}')
        raise KeyError from e
    else:
        return result_dict[key] #Raise KeyError
    

# try:
#     load_json_key('{"foo":1}','stuff')
#     assert False
# except KeyError:
#     print('Saw KeyError')


# USE OF TRY/EXCEPT/ELSE/FINALLY

UNDEFINED = object()

def divide_json(path):
    handle = open(path,'r+') # IOError
    try:
        data = handle.read() # UnicodeDecodeError
        json_data = json.loads(data) # ValueError
        result = json_data['numerator'] / json_data['denominator'] # DivideByZero
    except ZeroDivisionError:
        return UNDEFINED
    else:
        json_data['result'] = result
        data = json.dumps(json_data)
        handle.seek(0)
        handle.write(data) # IOError
        return result
    finally:
        handle.close()

temp_path = 'random.json'

with open(temp_path,'w') as f:
    f.write('{"numerator":1,"denominator":10}')

print(divide_json(temp_path))

