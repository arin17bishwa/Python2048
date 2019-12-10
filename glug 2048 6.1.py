# cook your dish here
#go=0 means game continues
#go=1 means game over
#go=2 means game won
import random as ra
import time

def leaderboard(lname,lscore,ltime):
	l=ltime
	print("\n\n")
	l.sort()
	ma=0
	mb=0
	mc=0
	for i in range(len(lname)):
		len1=max(ma,len(str(lname[i])))
		len2=max(mb,len(str(lscore[i])))
		len3=max(mc,len(str(ltime[i])))
		
	p=max((len1-4)//2,2)
	q=max((len2-5)//2,2)
	r=max((len3-4)//2,2)
	i=1
	print(" "*p,"NAME"," "*(len1-p-4)," "*6,"SCORE","     TIME")
	while len(l)!=0:
		ind=ltime.index(l[0])
		print(i,")",lname[ind],"-"*(len1-len(lname[ind])+4),lscore[ind],"-"*(len2-len(str(lscore[ind]))+7),ltime[ind])
		i+=1
		#print(i,"   ",l,ltime)
		del l[0]
		#del ltime[ind]
		del lname[ind]
		del lscore[ind]



def blankij(l1):
	lij=[]
	count=0
	for i in range(4):
		for j in range(4):
			if l1[i][j]==0:
				count+=1
				lij.append([i,j])
	return(lij)

def gameverdict(l1):
	go=1
	l2=[j for sub in l1 for j in sub]
	#if 0 in l2:
		#return(0)
	if 2048 in l2:
		return(2)
	if 0 in l2:
		return(0)
	for j in range(4):#loop to check presence of same no. in any column
		for i in range(3):
			if l1[i][j]==l1[i+1][j]:
				return(0)
	for i in range(4):#loop to check presence of any no. in any row
		for j in range(3):
			if l1[i][j]==l1[i][j+1]:
				return(0)
	return(go)

def in2(l1):
	lij=blankij(l1)
	r=ra.choice(lij)
	l1[r[0]][r[1]]=2
			 
	return(l1)
	 
def pr(l1):
	print("","-"*33)
	for i in l1:
		print(" | ",end="")
		for j in i:
				if j==0:
					print(str((4-len(str(j)))*" "+str(" "))," | ",end="")
				else:
					print(str((4-len(str(j)))*" "+str(j))," | ",end="")
		
		print("")
		print("","-"*33)

def addup(l1):
	global score
	for j in range(4):
		for i in range(3):
			if l1[i][j]==l1[i+1][j]:
				l1[i][j]+=l1[i+1][j]
				l1[i+1][j]=0
				score+=l1[i][j]
	return(l1)
	 
def adddown(l1):
	global score
	for j in range(4):
		for i in range(3,0,-1):
			if l1[i][j]==l1[i-1][j]:
				l1[i][j]+=l1[i-1][j]
				l1[i-1][j]=0
				score+=l1[i][j]
	return(l1)
	 
def addleft(l1):
	global score
	for i in range(4):
		for j in range(3):
			if l1[i][j]==l1[i][j+1]:
				l1[i][j]+=l1[i][j+1]
				l1[i][j+1]=0
				score+=l1[i][j]
	return(l1)

def addright(l1):
	global score
	for i in range(4):
		for j in range(3,0,-1):
			if l1[i][j]==l1[i][j-1]:
				l1[i][j]+=l1[i][j-1]
				l1[i][j-1]=0
				score+=l1[i][j]
	return(l1)
	 
def right(l1):
	for i in range(4):
		#print("i in for loop is:",i)################
		if l1[i][0]==0 or l1[i][1]==0 or l1[i][2]==0 or l1[i][3]==0:
			for j in range(3,0,-1):
				#k=i
				if l1[i][j]==0:
					k=j
					#print("k in for loop :",k)#############
					while l1[i][k]==0 and k>0:
						k-=1
						#print("k in while loop",k)#############
						#break
				 
					l1[i][k],l1[i][j]=l1[i][j],l1[i][k]
					#print("swapped",l1[k][j],l1[i][j])#############
	return(l1)
	 
def down(l1):
	for j in range(4):
		#print("j in for loop is:",j)################
		if l1[0][j]==0 or l1[1][j]==0 or l1[2][j]==0 or l1[3][j]==0:
			for i in range(3,0,-1):
				#k=i
				if l1[i][j]==0:
					k=i
					#print("k in for loop :",k)#############
					while l1[k][j]==0 and k>0:
						k-=1
						#print("k in while loop",k)#############
						#break
				 
					l1[k][j],l1[i][j]=l1[i][j],l1[k][j]
					#print("swapped",l1[k][j],l1[i][j])################
	return(l1)

def left(l1):
	for i in range(4):
		#print("i in for loop is:",i)################
		if l1[i][0]==0 or l1[i][1]==0 or l1[i][2]==0 or l1[i][3]==0:
			for j in range(3):
				if l1[i][j]==0:
					k=j
					#print("k in for loop :",k)#############
					while l1[i][k]==0 and k<3:
						k+=1
						#print("k in while loop",k)#############
						 
					l1[i][k],l1[i][j]=l1[i][j],l1[i][k]##if l1[i][k] is 0,then dont swap
					#print("swapped",l1[k][j],l1[i][j],"at positions`")###########
					 
	return(l1)

def up(l1):

	for j in range(4):
		#print("j in for loop is:",j)################
		if l1[0][j]==0 or l1[1][j]==0 or l1[2][j]==0 or l1[3][j]==0:
			for i in range(3):
				#k=i
				if l1[i][j]==0:
					k=i
					#print("k in for loop :",k)#############
					while l1[k][j]==0 and k<3:
						k+=1
						#print("k in while loop",k)#############
						#break
				 
					l1[k][j],l1[i][j]=l1[i][j],l1[k][j]
					#print("swapped",l1[k][j],l1[i][j])#################
	return(l1)
'''def leaderboard(lname,lscore,ltime):
	l=ltime
	l.sort()
	i=1
	print("    NAME      ","   SCORE","    TIME")
	while len(l)!=0:
		ind=ltime.index(l[0])
		print(i,")",lname[ind],"-"*5,lscore[ind],"-"*4,ltime[ind])
		i+=1
		del l[0]
		del lname[ind]
		del lscore[ind]'''
	 
lname=[]
lscore=[]
ltime=[]
play="yes"
while play=="yes":
	score=0
	lname.append(input("ENTER YOUR NAME:").lower().upper())
	l1=[[0 for i in range(4)]for i in range(4)]
	#validinp=["u","d","r","l"]##
	l1[ra.randint(0,3)][ra.randint(0,3)]=2
	l1=in2(l1)
	go=0
	pr(l1)
	t1=time.time()
	ltest=tuple([j for sub in l1 for j in sub])
	#print("ltest is",ltest)
	while go==0:
		#t1=time.time()
		inp=input(" ENTER YOUR MOVE: ").lower().rstrip().lstrip()
		#inp=m.getch()
		#print(inp)
		if m.kbhit() is False or inp==b'\xff':
			continue
		print("\n")
		ltest=tuple([j for sub in l1 for j in sub])
		#print("ltest is",ltest)
		if inp=="w":
			l1=up(l1)
			l1=addup(l1)
			l1=up(l1)
		elif inp=="s":
			l1=down(l1)
			l1=adddown(l1)
			l1=down(l1)
		elif inp=="a":
			l1=left(l1)
			l1=addleft(l1)
			l1=left(l1)
		elif inp=="d":
			l1=right(l1)
			l1=addright(l1)
			l1=right(l1)
		else:
			print(" INVALID INPUT! ENTER YOUR MOVE AGAIN!")
			continue
		go=gameverdict(l1)
		if go!=0:
			break
		#print([j for sub in l1 for j in sub],ltest)
		if [j for sub in l1 for j in sub]==list(ltest):
			print(" MOVE IS NOT POSSIBLE! CHOOSE ANOTHER MOVE\n")
			continue
		 
		l1=in2(l1)
		pr(l1)
		print(" YOUR CURRENT SCORE: ",score)
	t2=time.time()
	if go==1:
		pr(l1)
		print(" YOU LOSE!")
	else:
		pr(l1)
		print(" YOU WIN!")
		 
	lscore.append(score)
	ltime.append(t2-t1)
	print(" YOUR SCORE IS: ",score)
	play=input(" WANNA PLAY AGAIN??JUST SAY YES IF YOU WANNA: ").lower()


leaderboard(lname,lscore,ltime)
