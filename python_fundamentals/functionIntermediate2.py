x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1.EXERCISE
# **********************************
# 1 How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][0]=15 
print (x)

# 2 How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['last_name'] = 'Bryant'
print(students)

# 3 For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0]='Andreas'
print (sports_directory)

# 4 For z, how would you change the value 20 to 30?
z[0]['y'] = 30
print(z)

# 2.EXERCISE
# *******************************************
# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(arr):
    for i in arr:
        print(i)

iterateDictionary(students)

# 3 EXERCISE
# **************************************
# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(arr,key):
    for i in arr:
        print(i[key])
iterateDictionary2(students,'first_name')
# 4 EXERCISE
# **************************************
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

def printDojoInfo(arr):
    print((len(arr['locations'])),"LOCATIONS",(arr['locations']))
    print ((len(arr['instructors'])),"INSTRUCTORS",(arr['instructors']))
printDojoInfo(dojo)
