"""
Tim's python Port Scanner written in python 


"""
import platform
import socket

wontBlameMe = False #Terms and agreement is by default accepted
loop = True         #will break nested loops when needed

def initialization():
	print ( platform.platform() )   #long version, includes SP info
	print ( platform.system()   )   #short hand OS
	print ( platform.release()  )   #the "7" in windows 7
	print ( platform.version()  )	#just numbers and dots

def termsOfAgreement():
	print ("By running this program, you are acknowledging that what you are doing is probably illegal, and that this tool is to be used in an educational manner only. I am in no way responsible for you getting into legal trouble for using this application in an ill manner.")
	ans = input("1. Disagree. You need a scapegoat to blame.\n99.Agree to not blaming me!")
	if (ans == 1):
		print ("Shame, get outta here.")
		loop == false
	elif (ans == 99):
		print ("Terrific, lets get scanning!!")
		wontBlameMe = True



def startMenu():
	print ("Welcome to Tim's Port Scanner. You must first accept\nthe terms and agreements before you begin")
	termsOfAgreement()  #possible, if tOa not true, loop it until it is??
	scanSettings()


initialization()