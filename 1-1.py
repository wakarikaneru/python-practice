import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello world!")

print("1 + 1 = %s" % (1+1))

print()

a=1
b=2
c=a+b
print('%s + %s = %s' % (a, b, c))
