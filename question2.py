my_list = [10, "hello", 5.5, "world", 42]

check_type = lambda x: "Integer" if isinstance(x, int) else "String"

result = list(map(check_type, my_list))

print(result)