# Regular Expression...

import re

pattern = '^a...s$'
test_string = 'abyss'
'''re.match stop it its searching if it finds the match among the string'''
result = re.match(pattern , test_string)

if result:
    print('Search Successfull...')

else:
    
    print('Search Unsuccessfull...')


#Using re.search...
'''re.search search among the string'''
input_str = 'Life is too short to argue...'
result1 = re.search(r'[abc]' , input_str)
print('Usind re.search() function :',result1)

#Using re.findall...
'''re.findall search among the string and return all the matches as a list'''
input_str = 'Life is too short to argue...'
result2 = re.findall(r'[aeiou]' , input_str)
print('Usind re.findall() function :',result2)