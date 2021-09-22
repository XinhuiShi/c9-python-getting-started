# Ask a user their name
f_name = input('What is your first name: ')
f_init = f_name.upper()[0:1]
l_name = input('What is your last name: ')
l_init = l_name.upper()[0:1]

# If their first name starts with A or B 
# tell them they go to room AB
if f_init == 'A' or f_init == 'B':
    print('Go to Room AB')
# IF their first name starts with C
# tell them to go to room CD
elif f_init == 'C':
    print('Go to Room CD')
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
elif l_init == 'Z':
    print('Go to Room Z')
# if their last name starts with any other letter, tell them to go to room OTHER
else:
    print('Go to Room OTHER')
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z