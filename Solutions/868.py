def f(s, t):
    if s == t:
        return 0
    i = t.index(s[-1])
    a = f(s[:-1], t[:i] + t[i+1:])
    if a % 2 == 0:
        return a * len(s) + len(s) - i - 1
    else:
        return a * len(s) + i

target = "NOWPICKBELFRYMATHS"
s = "".join(sorted(target))
print(f(s, target))