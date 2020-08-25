def chooseUserProfile():
		userProfile = input("Press 'D' for driver or 'M' for merchant: \n")
		
		# print(userProfile)
		
		if userProfile != 'D' and userProfile != 'M' :
			print("Please use correct option")

		else:

			if userProfile =='D':
				print('Welcome to our driver registration app')
				
			elif userProfile =='M':
				print('Welcome to our merchant registration app')
		return(userProfile)	

def signUporSignIn():
		chooseOption = input("Please select your option SignUp (1) or SignIn (2) :\n")


		if chooseOption != '1' and chooseOption != '2' :
			print("Sorry please choose correct option")
		else:
			if chooseOption == '1':
				print('please enter your username :\n')
				
			elif chooseOption =='2':
				print('Welcome to merchant registration page')


selectedprofile = chooseUserProfile()
signUporSignIn()
