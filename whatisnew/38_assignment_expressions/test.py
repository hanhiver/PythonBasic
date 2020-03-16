
# 避免调用len()两次的赋值
a = [1, 2, 3, 4, 5]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
