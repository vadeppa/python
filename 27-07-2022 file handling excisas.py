'''f=open("vadeppa.txt",mode="w")
f.write("hello\n")
f.write("good morning\n")
print("success")
f.close() '''


'''
f = open('student.txt', mode='r', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)'''




# Opening for Reading
'''
f = open('student.txt', mode='r', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)'''


# Opening for Writing

'''
f = open('student.txt', mode='w', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Opening for Appending

'''
f = open('student.txt', mode='a', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''



# Opening for Exclusive Creation

'''
f = open('student1.txt', mode='x', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''



# Open for reading and then writing

'''
f = open('student.txt', mode='r+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for writing and then reading
'''

f = open('student.txt', mode='w+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for appending and then reading


'''
f = open('student.txt', mode='a+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''

# Open for reading

'''
f = open('pythona.jpg', mode='rb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''

# Open for Writing

'''
f = open('pythona.jpg', mode='wb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''



# Open for Appending

'''
f = open('pythona.jpg', mode='ab')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for Exlusive Creation

'''
f = open('pythona1.jpg', mode='xb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for reading and then writing

'''
f = open('pythona1.jpg', mode='rb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for writing and then reading

'''
f = open('pythona.jpg', mode='wb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# Open for Appending and then reading

'''
f = open('pythona.jpg', mode='ab+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed) '''


# file exists

'''
import os
print(os.path.isfile('student.txt')) '''

# file exists2

'''
import os
if os.path.isfile('student.txt'):
	f = open('student.txt')
	print('File Opened')
	f.close()
else:
	print('File Not Found') '''


#Writing Data with x mode

'''
f = open('student4.txt', mode='x')
f.write('Hello\n')
f.write('great.!!\n')
f.write('How are you')
f.close()
print('Success') '''


# Writing Data with a mode

'''
f = open('student.txt', mode='a')
f.write('Hello\n')
f.write('great.!\n')
f.write('How are you')
f.close()
print('Success') '''


# Writing Data with w mode

'''
f = open('student.txt', mode='w')
lst = ['vadeppa', 'sonu', 'Ramu', 'Laxman', 'Rani']
f.writelines(lst)
f.close()
print('Success') '''

# Writing Data with w mode

'''
f = open('student.txt', mode='w')
lst = ['vadeppa\n', 'sonu\n', 'Ramu\n', 'Laxman\n', 'Rani\n']
f.writelines(lst)
f.close()
print('Success')'''


# Writing Data with a mode

'''
f = open('student.txt', mode='a')
lst = ['hari\n', 'priyanka\n', 'veena\n', 'shoba\n', 'praveen\n']
f.writelines(lst)
f.close()
print('Success') '''


# Reading Data with r mode

'''
f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()
print('Completed!!!!') '''


# Reading Data with r mode

'''
f = open('student.txt', mode='r')
data1 = f.read(2)
data2 = f.read(2)
print(data1)
print(data2)
f.close() '''

# Reading Data with r mode

'''
f = open('student.txt', mode='r')
data1 = f.readline()
data2 = f.readline()
print(data1)
print(data2)
f.close() '''

# Reading Data with r mode

'''
f = open('student.txt', mode='r')
data = f.readlines()
print(data)
for i in data:
	print(i, end='')
f.close() '''

# tell method

'''
f = open('student.txt', mode='r')
print(f.tell())
data1 = f.read(5)
print(data1)
print(f.tell())
data2 = f.read(3)
print(data2)
print(f.tell()) '''

# seek method

'''
f = open('student.txt', mode='r')
print(f.tell())
f.seek(3)
print(f.tell())
data1 = f.read()
print(data1)
f.seek(2)
print(f.tell())
data2 = f.read()
print(data2) '''

# Read then Write

'''
f = open('student.txt', mode='r+')
print(f.tell())
data = f.read()
print(f.tell())
f.write('Youtube')
print(f.tell())
print(data)
print(f.tell())'''


# writing and then reading It will overwrite existing data

'''
f = open('student.txt', mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
data = f.read()
print(f.tell())
print(data) '''


# writing and then reading It will overwrite existing data
'''

f = open('student.txt', mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)'''



# appending and then reading It wont overwrite existing data

'''
f = open('student.txt', mode='a+')
print(f.tell())
f.write('Youtube')
print(f.tell())
data = f.read()
print(f.tell())
print(data) '''


# Appending and then reading It wont overwrite existing data

'''
f = open('student.txt', mode='a+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)'''


# Copy Contents of a file to another file

'''
f1 = open('student.txt', mode='r')
f2 = open('student1.txt', mode='w')
data = f1.read()
f2.write(data)
print('Success') '''

# with statement
'''
with open('student.txt') as f:
	data = f.read()
	print(data)
	print('File Closed:',f.closed)
print('File Closed:',f.closed)'''

f=open("student4.txt")
d=f.read()
d=d.replace("k","H")
f.close()
f=open("poem.txt","w")
f.write(d)
f.close()

