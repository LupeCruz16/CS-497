#Possible rewards for each selection
G = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927,
6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]

B = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528,
3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]

R = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216,
8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]

#Initial values 
QG = 0
QB = 0
QR = 0

#Number of times a choice has been selected
NG = 0
NB = 0
NR = 0

#Epsilon 
EPSILON = 0.01

def loop():
    for i in range(0, 100):

 
    #Counter 100-200 times for loop
    #Counter for each time a choice is selected
    #Each reward for the selections
    #Reward received
    #Epsilon = 0.01

    #Action taken, follow A to select
    #if 1 percent select random action, 99% select greedy
    #If same max value then take a random value 

def chooseA():
    '''
        Steps

        1. Find the greedy action => find the action to take
        2. Generate the random reward
        --> from the list
        -- follow a distribution
        3. Update the Q from the action

        All three steps are functions 
    '''
    print("Hi")

loop()