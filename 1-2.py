import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello FizzBuzz world!")

args = sys.argv

start = 1
end = int(args[1])
print(str(start) + 'から' + str(end) + "までのFizzBuzz")

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
