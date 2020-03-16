
# 避免调用len()两次的赋值
a = [1, 2, 3, 4, 5]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

# 可以用来在循环中读取文件
while (block := f.read(256)) != '':
    process(block)


