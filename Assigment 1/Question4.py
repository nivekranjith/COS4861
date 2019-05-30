def main(filename):
    f = open(filename, "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    else:
        print("File not found")



filename = input("Please enter filename including extension\n")
main(filename)
