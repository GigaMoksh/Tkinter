import subprocess


data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]

for i in profiles:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
    try:
        print(f"{i:<30} | {results[0]:<}")
    except IndexError:
        print("{:<30} | {:<}".format(i, ""))


# def fib():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a + b


# ser = fib()
# print(next(ser))
# print(next(ser))
# print(next(ser))
# print(next(ser))
# print(next(ser))

# class Fibonacci:

#     def __init__(self, n):
#         self.start = 0
#         self.second = 1
#         self.end = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i > self.end:
#             raise StopIteration
#         for _ in range(self.end):
#             current = self.start
#             self.start, self.second = self.second, self.second + self.start
#             self.i += 1
#             return current


# obj = Fibonacci(10)
# # print(next(obj))
# # print(next(obj))
# # print(next(obj))
# # print(next(obj))
# # print(next(obj))
# # print(next(obj))
# # print(next(obj))
# for num in obj:
#     print(num)

# import os
# os.chdir('C:\\Users\\Dell_Owner\\Desktop\\MY DOCUMENTS\\python')
# print(os.listdir())
