global username
global mobileNo
def Login():		
	
	username = str(input('Please enter a preferred username : \n'))
	mobileNo = str(input('Please enter a mobileNo:  :\n'))
	return username,mobileNo

def checkDriverSignUpDetails():
	uname,mobNo =  Login();
	print(uname)
	print(mobNo)
	
	while (len(uname) < 4 ):
		print('please enter min 4 characters for username')
		checkDriverSignUpDetails()
		break
	else:
		print("Successfully registered as a driver")


checkDriverSignUpDetails()


