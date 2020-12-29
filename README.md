# BruteForceDictionary

This is a program that will generate all the possible passwords for a wpa2-psk(Wi-Fi)

This is just for educational purpose and just something to tinker about.
Do not run the code to create the passlist.txt

The create() function will add all the passwords to the text file but:
1. To compute something this large you might need a super computer.
2. The World's entire storage capacity is 295 exabyte.
3. This will create a file of size 750 octovigintillion (750 x 10^87) Yotabytes. Approximately (exaggerated by a factor of maybe 2)
4. The file size will be 2537 quindecillion (2537 x 10^90) times more than the available storage in the world. (My brain stopped at this point so I'm not sure about this calculated value.)
5. All passwords of length 8 characters alone will be 32 Petabytes.

To use such a dictionary , we can do the following:
1. Use a computer with really high computation power.
2. Instead of saving it into a file, run it through a bruteforce attack through every iteration of the for loop(Every permutation directly used in a bruteforce attack).

Pros:
1. This program will generate all possible wifi passwords
2. We can run this without worrying about storage if we decide to run the iterated value through the loop instead of saving it.(But still you need high computation power) 
3. Running this at 41 in the for loop will generate all the possible instagram password as the max length for an Instagram password is 40 characters.
4. 21 For a facebook account as Facebook's password's max length is 20 characters.

Cons:
1. Takes an impossible amount of storage.
2. Running this needs very high computational power, maybe that of a super computer. The total number of passwords generated will be:
   Sum of permutations of 94Pn , P is permutation, n is between 8-63. 94 because there are 94 keyboard characters.


Edit:
1. A super computer ,doing a trillion operations per second, will take (1 trillion/summation(94Pn)) x 60 x 60 x 24 x 365 years to finish this attack. (Next point has the calculated value.)

2. Considering a super computer is doing a trillion calculations a second , the time will be : 2.43 x 10^-87 seconds to get all the possible passwords.

3. This is just for passwords between 8-63 characters long.
