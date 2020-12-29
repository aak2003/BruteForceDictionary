# BruteForceDictionary

This is a program that will generate all the possible passwords for a wpa2-psk(Wi-Fi)

This is just for educational purpose and just something to tinker about.
Do not run the code to create the passlist.txt

The create() function will add all the passwords to the text file but:
1. To compute something this large you might need a quantum computer or a super computer at least.
2. The World's entire storage capacity is 295 exabyte.
3. This will create a file of size 750 octovigintillion (750 x 10^87) Yotabytes.
4. The file size will be 2537 quindecillion (2537 x 10^90) times more than the available storage in the world
5. All passwords of length 8 characters alone will be 32 Petabytes.

To use such a dictionary , we can do the following:
1. Use a computer with really high computation power.
2. Instead of saving it into a file, run it through a bruteforce attack through every iteration of the for loop(Every permutation directly used in a bruteforce attack).

Pros:
1. This program will generate all possible wifi passwords
2. We can run this without worrying about storage if we decide to run the iterated value through the loop instead of saving it.(But still you need high computation power) 

Cons:
1. Takes an impossible amount of storage.
2. Running this needs very high computational power, maybe that of a quantum computer. The total number of passwords generated will be:
   Sum of permutations of 94Pn , P is permutation, n is between 8-63. 94 because there are 94 keyboard characters.


Edit:
A 30 qubit quantum computer ,doing a trillion operations per second, will take (1 trillion/summation(94Pn))*60*60*24*365 years to finish this attack.

Try a distributed computing network of quantum computers.

This is just for passwords between 8-63 characters long.


Imagine for AES-256 or SHA-256. That will take up a decade of all of the sun's energy to crack one password.
