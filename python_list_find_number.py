from random import randint

# create a function to generate a list of "size" random integers
# up to a maximum of "largest"

def random_list(largest,size):
  # create an empty list
  l = []
  # add a random number to the list the appropriate number of times
  for i in range(size):
    n = randint(0,largest-1)
    l.append(n)
  #print the list to check
  return(l)
#call the function
l = random_list(10,10)

def find_number():
  counter = 0
  for i in l:
   if (i == x):
     counter +=1
  return (counter) 

print(l)
x = int(input("Please enter a number to see how many times it repeats in the list"))
print("The number " +str(x)+ " has occured " +str(find_number()) + " times.")
