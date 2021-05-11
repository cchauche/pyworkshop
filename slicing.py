import random

my_list = list("Hello")
#print last two elements
print(my_list[-2:])

#print even numbers from 30 to 70 w/ slice
nums = list(range(0,100))
slice_nums = nums[30:70:2]
print(slice_nums)
#reverse the slice
slice_rev = slice_nums[::-1]
print(slice_rev)


# Zip names and scores
names = ["Colin", "Cody", "Aharon", "Anton"]
scores = [random.randint(0, 100) for i in range(1,len(names))]
print([tuple([name, score]) for name, score in zip(names, scores)])