msg = "      Hello, World        "
print(msg.strip())

msg2 = "*********Hello, World*********"
print(msg2.strip("*"))

print(msg.replace("World","Paul"))

url = 'http://www.babson.edu'

print(url.startswith("htt"))
#RETURNS TRUE OR FALSE.

print(url.startswith("https"))
#RETURNS FALSE AS THE WEBSITE IS NOT HTTPS

print(url.endswith("edu"))
#RETURNS TRUE OR FALSE. IN THIS CASE TRUE!

s = 'jalapeno'
s = 'jalape\u00f1o'
print(s)
#This shows the use of unicode.

