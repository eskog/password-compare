
#Loads in 2 password files formated as user:password and opens a output file.
file1 = ""
file2 = ""
matches = open("matches.txt" ,"w")

#Opens the first file, Retrieved the Username and password, then search the other file for a identical password.
with open(file1 ,"r") as pw1:
	for line in pw1:
		line = line.rstrip('\n')
		temp = line.rsplit(':',1)
		user = temp[0]
		password = temp[1]
		
		#Starts to read the second passwords and compares them with the first ones.
		with open(file2 ,"r") as pw2:
			for line in pw2:
				line = line.rstrip('\n')
				temp = line.rsplit(':',1)
				user2 = temp[0]
				password2 = temp[1]
				
				#Check if password matches, if they do, write it to an outfile.
				if password == password2:
					#matches.write('z3user: ' + zon3user + ' and z2user: ' + zon2user + ' have same password in both zones') ##Send this to new file instead of cmd
					matches.write('User: ' + user + ' and User: ' + user2 + '\n') ##writing the results to file.
matches.close()
