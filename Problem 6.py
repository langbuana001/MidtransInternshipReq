#Problem 6 - uncommonality
#We can use the operator XOR to find the difference.

"""
    Some notes on XOR:
    (Note to self: You saw this in Math216)
    XOR is an Exclusive OR. It's either of the two, but not both.
    Think about your love relationship,
    You have a crush on a girl but you already have a girlfriend.
    XOR! It's either your crush or your girlfriend.
    Gotta choose one, but can't have both.
"""


def find_uncommon_char(string1, string2):

    #Let us make our string a set so we can compare them
    string1_set = set(string1)
    string2_set = set(string2)

    #Our result should also be a set, this way we can manipulate
    #   it further when necessary
    uncommon = string1_set ^ string2_set

    return uncommon

output = find_uncommon_char("abcde", "bczah")
print("removing", len(output), "chars: ", output)
