__author__ = 'gauth_000'
with open('stateinfo.txt') as state_info:
    states={}
    for line in state_info.readlines():
        state_city=line.split(':')
        states.get(state_city[0], open(state_city[0], 'a')).write(state_city[1])
    for state in states:
        state.close()