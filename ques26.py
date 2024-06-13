def check_prefix_suffix(str, prefix, suffix):
    if str.startswith(prefix):
        print("The string starts with the prefix ",prefix)
    else:
        print("The string does not start with the prefix ",prefix)
    
    if str.endswith(suffix):
        print("The string ends with the suffix ",suffix)
    else:
        print("The string does not end with the suffix ",suffix)

string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

check_prefix_suffix(string, prefix, suffix)
