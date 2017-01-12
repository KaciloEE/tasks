<<<<<<< HEAD
import itertools
def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs)) #230
print(choose_best_sum(430, 8, xs)) #None
xs = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, xs)) #228
=======
import itertools
def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs)) #230
print(choose_best_sum(430, 8, xs)) #None
xs = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, xs)) #228
>>>>>>> 7043ebe108d4468dd6cb30e4f503e22f3be429f9
