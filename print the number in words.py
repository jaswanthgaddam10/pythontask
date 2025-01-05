def number_to_words(n):
    ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if n == 0:
        return "Zero"
    words = []
    if n >= 1000000000:
        billions = n // 1000000000
        words.append(number_to_words(billions) + " billion")
        n %= 1000000000
    if n >= 1000000:
        millions = n // 1000000
        words.append(number_to_words(millions) + " million")
        n %= 1000000
    if n >= 1000:
        thousands = n // 1000
        words.append(number_to_words(thousands) + " thousand")
        n %= 1000
    if n >= 100:
        hundreds = n // 100
        words.append(ones[hundreds] + " hundred")
        n %= 100
    if n >= 20:
        tens_place = n // 10
        words.append(tens[tens_place])
        n %= 10
    if n > 0:
        words.append(ones[n])
    return " ".join(words)
number = int(input("Enter a number: "))
print(number_to_words(number))
