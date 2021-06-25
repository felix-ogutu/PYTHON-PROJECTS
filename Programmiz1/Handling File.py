# create the file
text_file = open("text.txt", "w+")
text_file.write("Hello my people am learning python programming")
text_file.close()
# add something in the file
text_file = open("text.text", "a")
text_file.write("Programming is just wonderful")
text_file.close()
# to read file
text_file = open("text.txt", "r")
print(text_file.read())
text_file.close()
