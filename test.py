with open('creds.txt') as f:
    lines = f.readlines()

count = 0
username = lines[0]
password = lines[1]

print(username.strip())
print(password)
