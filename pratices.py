# lesser of two events: write a function that returns the lesser of two given numbers if
# both numbers are even, but returns the greater if one or both are odd
# lesser_of_two_evens(2,4) -->2
# lesser_of_two_evens(2,5) -->5

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # both numbers are even
        # if a < b:
        #     result = a
        # else:
        #     result =
        result = min(a,b)
    else:
        # one or both numbers are odd!
        # if a > b:
        #     result = a
        # else:
        #     result = b
        result = max(a,b)

    return result

# check
my_numbers= lesser_of_two_evens(8,4)
print(my_numbers)

# Animal crackers: write a function takes a two-word string and returns True if both words
# begin with same letter

def animal_crackers(text):
    # we can use upper() or lower() into the function
    worldlist = text.lower().split()
    print(worldlist)
    return worldlist[0][0] == worldlist[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('krazy Kangaroo'))

# makes twenty; given two integers, return True if the sum of the integers is 20 or if
# if one of the integers is 20. if not, return False.
def makes_twenty(x,y):
    # if x + y == 20:
    #     return True
    # elif x == 20:
    #     return True
    # elif y == 20:
    #     return True
    # else:
    #     return False
    return (x+y) == 20 or x == 20 or y == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# Master Yoda: Given a sentence, return a sentence with the words reversed
def master_yoda(sentence):
    words = sentence.split()
    reversed_sentence = words[::-1]
    return ' '.join(reversed_sentence)
# we want to have string rather than array
print(master_yoda('I am home'))
print(master_yoda('We are ready'))


