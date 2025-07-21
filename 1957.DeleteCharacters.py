s = "leeetcode"
fancy_string = ""

letter_count = 1
for i, letter in enumerate(s):
    if i == 0:
        fancy_string += letter
    else:
        print(f"Index: {i}, Letter: {letter}")
        last_letter = s[i-1]
        if letter == last_letter:
            letter_count += 1
            print(f"Letter count increased: {letter_count}")
        else:
            letter_count = 1
        if letter_count < 3:
            fancy_string += letter
        print(f"Current fancy string: {fancy_string}")

print(fancy_string)
print("Final fancy string:", fancy_string)


def delete_characters(s):
    fancy_string = ""
    letter_count = 1
    for i, letter in enumerate(s):
        if i == 0:
            fancy_string += letter
        else:
            print(f"Index: {i}, Letter: {letter}")
            last_letter = s[i-1]
            if letter == last_letter:
                letter_count += 1
                print(f"Letter count increased: {letter_count}")
            else:
                letter_count = 1
            if letter_count < 3:
                fancy_string += letter
            print(f"Current fancy string: {fancy_string}")

    return fancy_string

print("test: " + delete_characters("leeetcode"))