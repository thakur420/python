import sys
import os
import zlib

def read_blob_object(file_hash):
    file_path = f"./.git/objects/{file_hash[:2]}/{file_hash[2:]}"
    with open(file_path, 'rb') as f:
        data = f.read()
        decompressed_data = zlib.decompress(data)
        content = decompressed_data.split(b'\x00')[1].strip()
        print(content.decode('utf-8'))

def init():
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")
    print("Initialized git directory")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "cat-file":
        read_blob_object(sys.argv[3])
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
