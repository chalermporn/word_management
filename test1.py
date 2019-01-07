import re
# text = 'dd ggg;'
# m = re.search('(?;', 'abcdefddddddd ;')
# print(m.group(0))

# myString = 'dd ggg;'
# c = ';'
# count = myString.rfind(c)
# print(count)


# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
print(str)
tuples = str.endswith(';')
print (tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]

# for tuple in tuples:
#     print (tuple[0])  ## username
#     print (tuple[1])  ## host