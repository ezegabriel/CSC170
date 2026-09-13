# Can we read our file?
# hello.txt

# Step 1: Open the file
f = open("hello.txt", mode="r")

# Step 2: Read (or write)
# DON'T DO THIS!
# print(f)
s_text = f.read()
s_more = f.read() # what happens here?
print(s_more)
l_text = s_text.split('\n')

# Step 3: Close the file!
f.close()
##
##print("s_text =")
##print(s_text)
##print(len(s_text))
##print("s_more =")
##print(s_more)
##print(len(s_more))      
#print(l_text)
