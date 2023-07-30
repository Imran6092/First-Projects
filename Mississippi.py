def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


word = "Mississippi"
letter_to_find = "s"
result = count_letter(word, letter_to_find)

print(f"The letter '{letter_to_find}' appears {result} times in the word '{word}'.")
