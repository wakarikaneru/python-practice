import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello Prime world!")

args = sys.argv

start = 2
end = int(args[1])
print('落ち着いて' + str(start) + 'から' + str(end) + "までの素数を数えるんだ…")

for i in range(start, end + 1):
    isPrime = True
    for j in range(2, i):
        if i%j==0:
            isPrime=False
    if isPrime:
        print(i)
