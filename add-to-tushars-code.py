from random import *

'''legend for health status:
    0: healthy
    1: recovered
    2: dead
    3: hospitalised
    4: infected but not showing symptoms
'''
def close_enough(s, t):
    sq = (s[0]-t[0])**2 + (s[1]-t[1])**2
    distance = sq**0.5
    if distance <= 10.0:
        return True
    else:
        return False


population = [] # a !D array of humans
x = 1250   # x * y = total area of the state
y = 2000    # it is a random distribution
pop = 5000 # total population

health_status = 0 # index of health status

for i in range(pop):
    a = [0, [randint(1, x), randint(1, y)], 0 , 0] # each element has 3 attributes: status, coordinates, time , day of death
    for m in range (1,13):  #predefine day of death
        c = random()
        if c <=0.05:
            break          # probability of dying
    if m<12:
        a[3]=m
    elif c<=0.05:
        a[3]=12
    population.append(a[:])

I0 = sample(list(range(pop)), 10)       # randomly infecting 10 people
for i in range(10):
    random_guy = population[I0[i]]
    infected = 4
    random_guy[health_status] = infected

days = 5        # choose days for simulation

while True:


    all_done = True

    for i in range(pop):
        a = population[i]     # this where I am checking
                                # and updating health status
        if a[health_status] > 2: # if human is sick
            all_done = False
            a[2] += 1               # first, we increase the days
            if a[2]==a[3]:
                a[health_status] = 2
            elif a[2] == 5:         # if sick guy is on day5, hospitalise
                a[health_status] = 3
            elif a[2] == 12:         # if human survives till day7, recover
                a[health_status] = 1
    if all_done:
        break

    indices = sample(list(range(pop)), 20)      # choosing 20 random people to move
    for i in range(20):
        a = population[indices[i]]              # movement is denoted as change
        a[1] = [randint(1, x), randint(1, y)]    # in x and y coordinates


    for i in range(pop-1):                      # now, everybody in 10m radius of
        if population[i][0] != 4:               # sick people will get infected
            continue
        else:
            for j in range(1, pop):
                v = population[i]
                t = population[j]
                if t[health_status] == 0 and close_enough(v[1], t[1]):
                    t[health_status] = 4


    fine = 0
    deadcount = 0
    immune = 0
    sick = 0
    hospitalised = 0
    for i in range(pop):
        person = population[i]

        if person[health_status] == 2:
            deadcount += 1
        elif person[health_status] ==1:
            immune += 1
        elif person[health_status] == 0:
            fine += 1
        elif person[health_status] == 3:
            hospitalised +=1
        else:
            sick += 1

print(f"dead: {deadcount}")
print(f"immune: {immune}")
print(f"sick: {sick}")
print(f"fine: {fine}")
print(f"admitted: {hospitalised}")
print('')

