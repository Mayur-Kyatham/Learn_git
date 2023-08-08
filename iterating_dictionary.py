file_content = {"jpg": 10, "csv": 2, "py": 3, "txt":45}
for extensions in file_content:
    print(extensions)


for ext, amount in file_content.items():
    print("There are {} files with the .{} extension".format(amount, ext))


print(file_content.keys())

print(file_content.values())


for value in file_content.values():
    print(value)
