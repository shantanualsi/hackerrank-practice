# TODO: Testcase 2 fails. Analyze further
def max_team(skillset):
	team_topics = '';
	maxskill = 0
	for person1 in skillset:
		for person2 in skillset:
			teamskill = str(bin(int(person2,2) | int(person1,2)))[2:].count('1')
			print("Team", person1, person2, teamskill)
			maxskill = teamskill if teamskill > maxskill else maxskill
			team_topics = team_topics+str(teamskill);
	return maxskill, team_topics.count(str(maxskill))/2 
			


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
