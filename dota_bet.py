from bs4 import BeautifulSoup
import requests
#TODO file IO
def processNewMatches():
	newMatches = readMatchResults()
	baseMMRs = getAllMMRs()
	newMMRs = baseMMRs
	for i in range(len(newMatches), 0):
		team1 = getMMR(baseMMRs, newMatches[i][0]
		team2 = getMMR(baseMMRs, newMatches[i][1]
		k = 15
		newMMRs[team1[1]][1] = team1[0] + k * (newMatches[i][2] - newMatches[i][3])
		newMMRs[team2[1]][1] = team2[0] + k * (newMatches[i][3] - newMatches[i][2])
	
	writeMMRs(newMMRs)	
		
	
def getMMR(allMMRs, team):
	#returns [mmr, position]
	return 
	
def getAllMMRs():
	#returns [team, mmr]
	
	
def writeMMRs(MMRs):



def readMatchResults():
	#reads new matchs. Output is [team1, team2, win1, win2]
	response = requests.get('http://www.gosugamers.net/dota2/gosubet')
	soup = BeautifulSoup(response.text)
	trs = soup.find_all('h2')[2].parent.find_all('tr')
	result = []
	for i in range(0,len(trs)):
		td = trs[i].find('td')
		team1 = td.select(".opp1 > span")[0].text
		team2 = td.select(".opp2 > span")[1].text
		
		td = td.find_next_sibling()
		win1 = td.select(".hidden > span")[0].text
		win2 = td.select(".hidden > span")[1].text
		
		
		result.append([team1, team2, win1, win2])
	
	print(result)
	return result
	
	
		
	
	
if __name__ == "__main__":
        readMatchResults()
