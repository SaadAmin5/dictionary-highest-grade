# find the subject with highest grade
dict1={'maths':5,
      'english': 8,
      'history':10}
print(dict1)

#finding highest grade
print('Highest grade is =', max(dict1.values()))

#find subject with highest grade
print('Subject having highest grade is =', max(dict1, key=dict1.get).capitalize())

#printing both subject with highest grade
print('Printing both subject with highest grade:',  max(dict1, key=dict1.get).capitalize(), '=', max(dict1.values())) 