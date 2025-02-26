def calculate_frequency(text):
    freq = [0] * 26 
    for char in text:
        freq[ord(char) - ord('a')] += 1 
    result = ""
    for i in range(26):
        if freq[i] > 0:  
            result += chr(i + ord('a')) + str(freq[i])
    return result
text = input()
print(calculate_frequency(text))
