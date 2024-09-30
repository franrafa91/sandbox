from to_string.to_string import Format

a = 5000.14
fmt = Format()

for i in range(1,4):
    print(f"Number format #{i}")
    print(fmt(a))
    fmt.update(i)