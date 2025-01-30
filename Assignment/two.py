def string_first_last(s):
    return s if len(s) < 2 else s[:2] + s[-2:]

# Test cases
print(string_first_last("university"))  
print(string_first_last("un"))         
print(string_first_last("a"))          
