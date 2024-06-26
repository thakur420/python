import sys
# finding duplicate files using brute force
def data_match(file1,file2):
    with open(file1, "rb") as f1:
        with open(file2,"rb") as f2:
            data1 = f1.read()
            data2 = f2.read() 
            if data1 == data2:
                return True
    return False

def find_duplicates(filenames):
    n = len(filenames)
    duplicates = []
    for i in range(n-1):
        file1 = filenames[i]
        for j in range(i+1,n):
            file2 = filenames[j]
            if data_match(file1,file2):
                duplicates.append((file1,file2))
    return duplicates

# finding duplicate files using naive hash function
def cal_hash(file): 
    with open(file, "rb") as f1:
        return sum(f1.read()) % 13

def find_duplicate_using_hash(filenames):
    hash_groups={}
    for file in filenames:
        hash = cal_hash(file)
        hash_groups.setdefault(hash,[]).append(file)
    duplicates = []
    
    for groups in hash_groups.keys():
        dup = find_duplicates(hash_groups[groups])
        duplicates.extend(dup)
    return duplicates

# finding duplicte files using sha256 hash function
from hashlib import sha256
def cal_sha256_hash(file):
    with open(file,"rb") as f:
        data = f.read()
        return sha256(data).hexdigest()

def find_groups(filenames):
    groups = {}
    for file in filenames:
        hash = cal_sha256_hash(file)
        groups.setdefault(hash,[]).append(file)
    return groups

if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))