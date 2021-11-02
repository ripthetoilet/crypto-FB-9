def gcd(a,b):
     while a != 0 and b != 0:
          if a > b: a = a % b
          else: b = b % a
     return a+b

def inverted(a,n):
     q = [0,1]
     while a != 0 and n != 0:
          if a > n: q.append(a // n); a = a % n
          else: q.append(n // a); n = n % a

     for i in range(2,len(q)): q[i] = q[i-2] - q[i]*q[i-1]
     return q[-2]


def equation(a,b,n): # ax=b modn
     d = gcd(a,n)
     if d < 1: return 0
     elif d == 1: return (inverted(a,n)*b)%n
     else:
          if b%d == 0:
               a, b, n = a//d, b//d, n//d
               x = []
               x1 = equation(a, b, n)
               for i in range(d):
                    x.append(x1 + i*n)
               return x
          else: return 0

print(equation(5,1,12))