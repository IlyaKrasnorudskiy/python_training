h = int(input())
m = int(input())
n = int(input())
minutes = h*60+m
#(n-1) - подразумевается, что последнему уроку не нужна перемена.
amount = minutes + n * 45 + (n-1) * 10


print("Урок N ", n, " заканчивается в ", amount//60, amount - (amount//60)*60 )