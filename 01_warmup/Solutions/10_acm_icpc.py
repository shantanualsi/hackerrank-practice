"""
Problem Statement: 		Determine how many possible combinations of teams of 2 have the max skill
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

def max_team(skillset):
	teamskill = list(); 
	teams = 0;
	for person1 in skillset:
		for person2 in skillset:
			teamskill.append(str(bin(int(person2,2) | int(person1,2)))[2:].count('1'));
	teamskill = sorted(teamskill,reverse=True);
	for i in teamskill:
		if i==teamskill[0]:
			teams = teams+1;
		else:
			break

	return teamskill[0], teams/2
			


playerskills = raw_input();
N,M = playerskills.split(' ');

skillset = []
for i in range(0,int(N)):
	#  Needs validation here. We'll leave it for now.
	#  Input character length should be M characters and in 1s and 0s only.
	skillset.append(raw_input())
maxskill, teams = max_team(skillset)

print(maxskill)
print(teams)
