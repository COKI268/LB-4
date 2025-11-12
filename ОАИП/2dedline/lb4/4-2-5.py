from collections import Counter
import string

t = input("Text: ").lower()
w = [x.strip(string.punctuation) for x in t.split() if x.strip(string.punctuation)]

if w:
    print(f"L:{max(w,key=len)} S:{min(w,key=len)}")
    print(f"Avg:{sum(len(x)for x in w)/len(w):.1f}")
    print(f"Top:{Counter(w).most_common(5)}")
