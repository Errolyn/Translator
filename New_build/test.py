from ericpyg import translate

# Test 1

test_string_1 = 'hey there!'
expected = 'Eyhay heretay'

result = translate(test_string_1)

if result == expected:
    print "Passed 1!"
else:
    print "Failed 1!"
    print "Expected: " + expected
    print "Got: " + result


# Test 2


test_string_2 = "Staying at Eric's house. Oh yeah."
expected = "I told you not to use a conjunction."

result = translate(test_string_2)

if result == expected:
    print "Passed 2!"
else:
    print "Failed 2!"
    print "Expected: " + expected
    print "Got: " + result



