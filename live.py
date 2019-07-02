from pycricbuzz import Cricbuzz
import sys

def s(n):
	return ' ' * n

def print_line(n):
	print '-' * n

def print_teamscore(sc):
	print_line(53)

	team1 = sc.get('batting',{}).get('team','Team 1')
	team2 = sc.get('bowling', {}).get('team', 'Team 2')
	
	scores1 = sc.get('batting',{}).get('score')
	scores2 = sc.get('bowling',{}).get('score')

	score1 = scores1[0]['runs']+'/'+scores1[0]['wickets']+'('+scores1[0]['overs']+')' if scores1 else '/'
	score2 = scores2[0]['runs']+'/'+scores2[0]['wickets']+'('+scores2[0]['overs']+')' if scores2 else '/'

	innings = scores1[0]['inning_num'] if scores1 else ''

	print 'Innings{0}{1}{2}{3}'.format(s(7),team1, s(11-len(team1)), team2)
	print_line(51)
	print '{0}{1}{2}{3}{4}'.format(innings, s(14-len(innings)), score1, s(11-len(score1)), score2)

	print_line(53)

def print_batting_score(ba):
	if not ba:
		ba = {}
	print 'Name{0}Runs{1}Balls{2}Fours{3}Sixes'.format(s(10),s(7),s(5),s(6))
	print_line(53)
	batsmen = ba.get('batsman', [])

	for b in batsmen:
		bname = b['name'].split(' ')[0]
		print '{0}{1}{2}{3}{4}{5}{6}{7}{8}'.format(bname, s(14-len(bname)),\
		b['runs'], s(11-len(b['runs'])),\
		b['balls'],s(10-len(b['balls'])),\
		b['fours'], s(11-len(b['fours'])),\
		b['six'])

	print_line(53)

def print_bowling_score(bow):
	if not bow:
		bow = {}
	print 'Name{0}Runs{1}Overs{2}Wickets{3}Maidens'.format(s(10),s(7),s(5),s(4))
	print_line(53)
	bowler = bow.get('bowler', [])

	for b in bowler:
		bname = b['name'].split(' ')[0]
		print '{0}{1}{2}{3}{4}{5}{6}{7}{8}'.format(bname, s(14-len(bname)),\
		b['runs'], s(11-len(b['runs'])), \
		b['overs'], s(10-len(b['overs'])), \
		b['wickets'], s(11-len(b['wickets'])), \
		b['maidens'])
	
	print_line(53)

def print_com(com):
	if not com:
		return

	print '\n'
	comm = com.get('commentary', [{'comm':'No comments','over':u''}])[0]
	print (comm['over'] if comm['over'] else '') + ' : ' + comm['comm']

if __name__ == '__main__':
	match_id = sys.argv[1]
	c = Cricbuzz()
	sc = c.livescore(match_id)
	com = c.commentary(match_id)

	ba = sc.get('batting', None)
	bo = sc.get('bowling', None)
	
	print_teamscore(sc)
	print_batting_score(ba)
	print_bowling_score(bo)
	print_com(com)
