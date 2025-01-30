def count_case(s):
    upper_count = sum(1 for char in s if char.isupper()) 
    lower_count = sum(1 for char in s if char.islower())  
    
    print("No. of Upper case characters :", upper_count)
    print("No. of Lower case Characters :", lower_count)

sample_string = 'The quick Brow Fox'
count_case(sample_string)
