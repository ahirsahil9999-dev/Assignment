# Write a recursive function in Python called reverse_string(s) that takes a string and returns it reversed (e.g., 'hello' becomes 'olleh').

def reverse_string(st):
    result = ""
    for ch in st:
        result = ch + result
        
    return result

st = input("Enter A String: ")
result = reverse_string(st)
print(result)