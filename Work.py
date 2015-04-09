#  File: Work.py 

#  Description: Program to maximize Vayasa's sleep for a given n and k

#  Student Name: Garner Vincent  

#  Date Created: 3-24-15

#  Date Last Modified: 3-27-15

#this equation evaluates the number beneath a number that returns lines of code greater than what vyasa needs
#if the number below the number it is checking produces a better solution, the original number is not the solution. go back to the search.
def underNum(mid, codeLines, kFactor):
	x = 0
	totalCode = 0
	mid -= 1
	while True:
		totalCode += (mid // kFactor ** x)
		
		if (totalCode >= codeLines):
			return 1

		elif(totalCode < codeLines) and ((mid // kFactor ** (x + 1)) == 0):
			return 2
		x += 1

#this number evaluates the number of lines of code the number produces in sequence
def checkSeq(mid, codeLines, kFactor):
	x = 0
	totalCode = 0

	while True:
		totalCode += (mid // kFactor ** x)
		if (totalCode > codeLines):
			return underNum(mid, codeLines, kFactor)
		elif (totalCode == codeLines) and ((mid // kFactor ** (x + 1)) == 0):
			return 2
		elif (totalCode < codeLines) and ((mid // kFactor ** (x + 1)) == 0):
			return 3
		x += 1

#binary search to find the number of lines of code (v) that vyasa must begin his assignment with
def binSearch(codeLines, kFactor):
	lo = 0
	hi = codeLines

	while lo <= hi:
		mid = (lo + hi) // 2

		val = checkSeq(mid, codeLines, kFactor)
		if val == 2:
			return mid
		elif val == 1:
			hi = mid - 1
		elif val ==  3:
			lo = mid + 1

def main():
	inFile = open("./work.txt", "r")
	#read first line in as cases
	cases = int(inFile.readline().strip())

	for i in range(cases):
		#read new line and assign n and k
		line = inFile.readline().split()
		codeLines = int(line[0])
		kFactor = int(line[1])

		v = binSearch(codeLines, kFactor)

		print(v)

	inFile.close()

main()