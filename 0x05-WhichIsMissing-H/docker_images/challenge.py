import random

def main():
    print("Some of the numbers are missing, can you figure out which?")
    print("The lowest and highest will always be in the string")
    print("If 2,5 and 6 are missing, return them in the form:2 5 6")

<<<<<<< HEAD
	for x in range(500):
		lower = random.randint(0,100)
		higher = random.randint(lower+11,lower+40)
		amount = higher-lower+1
		print(amount)
		sendString = []
		for x in range(lower,higher):
			sendString.append(str(x)) 
		random.shuffle(sendString)
		numMissing = random.randint(2,10)
		numReplaced = 0
		replacedNums = []
		while(numReplaced < numMissing):
			cur = random.randint(0,amount-2)
			if(sendString[cur]!='*' and sendString[cur]!=str(lower) and sendString[cur]!=str(higher)):
				replacedNums.append(sendString[cur])
				sendString[cur] = '*'
				numReplaced+=1
		print(sendString)
		print(replacedNums)
		response = input()
		splitResponse = response.split(" ")
		matched = 0
		for x in splitResponse:
			counter = 0
			for j in replacedNums:
				if x == j:
					replacedNums[counter] = '0'
					counter+=1
					matched+=1
		if(matched!=numMissing):
			print("FAILURE")
			return 0
	print("monkeyCTF{alot_of_rules_huh}")
=======
    for x in range(500):
        lower = random.randint(0,100)
        higher = random.randint(lower+10,lower+40)
        amount = higher-lower+1
        sendString = [ str(x) for x in range(lower, higher) ]

        numMissing = random.randint(2,8)
        numReplaced = 0
        replacedNums = []
        while(numReplaced < numMissing):
            cur = random.randint(1, len(sendString) - 2)
            if(sendString[cur]!='*'):
                replacedNums.append(sendString[cur])
                sendString[cur] = '*'
                numReplaced += 1

        random.shuffle(sendString)
        print(sendString)
        response = input()
        splitResponse = response.split(" ")
        matched = 0
        try:
            for x in splitResponse:
                i = replacedNums.index(x)
                replacedNums.pop(i)
                matched += 1
        except ValueError:
            print("FAILURE")
            return 0
        if(matched!=numMissing):
            print("FAILURE")
            return 0

    print("monkeyCTF{alot_of_rules_huh}")
>>>>>>> 86f0e716ed2488c6ed416b96647737a08d13af35


main()
