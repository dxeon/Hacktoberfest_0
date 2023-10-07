'''
-> All output and data which are temp.
-> If we want to save it on our machine we use file handling method(read/write).

'''

#READ DATA
f = open('READ.txt','y')

# open method, READ = File Name, r = Mode(read)
print(f.read()) #this will print a entrire file data

print(f.readline()) #this will only print 1st line # pointer on 1st line
print(f.readline())

#when we want to print specific chars.
print(f.readline(4))


#WRITE DATA
f = open('READ.txt','x')
# if we have file -> it will write on it otherwise it will create it.
f.write('Java')
f.write('C++')

# int this we override whole data

# for append anything in file
f = open('READ.txt','a')
f.write('harsh')


#COPY DATA FROM ANOTHER FILE
f = open('READ.txt','r')

f1 = open('WRITE.txt','w')

for data in f:
	f1.write(data)

# if copy image data - work with binary
f = open('class.jpeg','rb')

f1 = open('WRITE.txt','wb')

for data in f:
	f1.write(data)
