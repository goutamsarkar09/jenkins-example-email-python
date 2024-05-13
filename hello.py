print('hellow sarkar')
txt = "The best things in life are free!"
if "free" in txt:
#if "free" not in txt:
  print("Yes, 'free' is present.")


#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
