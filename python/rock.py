# Задание 19-21

def g(F, W=set()):
    return {s for s in z if F(t >= 29 or t in W for t in (s + 1, s * 2))}


z = {*range(1, 29)}
w1 = g(any)
z -= w1
l1 = g(all, w1)
z -= l1
w2 = g(any, l1)
l2 = g(all, w1 | w2)
print(*l1)
print(*sorted(w2))
print(*l2)

# https://www.youtube.com/watch?v=JmPodPl786Q
