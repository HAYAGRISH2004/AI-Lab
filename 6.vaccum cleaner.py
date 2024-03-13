

A = [[0 for i in range(105)] for j in range(105)]


ans = []


def printt():
	
	print("Yes, the house can be cleaned.")
	for i in range(len(ans)):
		print(ans[i][0], ans[i][1])
		

def solve(n):
	global ans
	
	
	for i in range(n):
		for j in range(n):
			if (A[i][j] == '.'):
				ans.append([i + 1, j + 1])
				break
			
	
	if (len(ans) == n):
		printt()
		return 0
		
	ans = []
	
	
	for i in range(n):
		for j in range(n):
			if (A[j][i] == '.'):
				ans.append([i + 1, j + 1])
				break
			
	
	if (len(ans) == n):
		printt()
		return 0
	print("house cannot be cleaned.")


n = 3
s = ""
s += ".**"
s += ".**"
s += ".**"
k = 0


for i in range(n):
	for j in range(n):
		A[i][j] = s[k]
		k += 1

solve(n)

