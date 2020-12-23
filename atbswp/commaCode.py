spam=['apples', 'bananas', 'tofu', 'cats']

s=spam[0]
for i in range(1,len(spam)):
    s = s+", "+spam[i]

print(s)
