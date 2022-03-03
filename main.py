import getpass
import sys

print('Welcome, please log in')

input("User:")

if True:
    password = getpass.getpass('Password:')

    if password == 'samplepassword':
        print("Successfully logged in 🎉")
        sys.exit()

    else:
        print('Wrong password 👿')
        sys.exit()
