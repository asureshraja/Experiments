ip=raw_input()
sin=0
ein=0
i=0
s="*"
for e in ip:
	s=s+e+"*"
#making new string ex: *b*a*n*a*n*a*
#considering every char as center of lps and traverse left and right to check pal
while i <len(s):     
	l=i-1
	r=i+1
	while (l>=0 and r<len(s)):
		if(s[l]==s[r]):
			if(ein-sin<r-l):
				ein=r
				sin=l
			l=l-1
			r=r+1
		else:
			break
	i=i+1

print ip[sin/2:(ein+1)/2]