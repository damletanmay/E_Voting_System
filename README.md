# E-Voting System

We've Made this project to try to keep the maximum things online, except for candidate registration which requires document verification.

# Hosting

The website is hosted live [here.](https://e-voting--system.herokuapp.com/)

## Brief about E-Voting

E-Voting system is a concept website designed & developed by us for implementation of electronic voting. 

Here we have assumed that govt. already has a data of Voting Card distributed amongst citizens.

This data can be fetched and saved into the ``` django DB ``` in ``` voters ``` Table which can be found in [BASE_DIR\users\models.py](https://github.com/damletanmay/E_Voting_System/blob/master/users/models.py).

For the Time Being, We use [twilio](https://www.twilio.com/) as an API to send messages & here we've assumed that each number is registerd in the account from where OTP is to be sent.

## How to Access Website

Instructions to vote are given on the homepage  [here.](https://e-voting--system.herokuapp.com/)

First to log-in, one must have their voting number & registered mobile number.

Then after the user is logged in user can select the election they want to want in & it's candidates. (**Note**: one must be living in the same province where the election is held else one won't be able to vote)

## Why this project ?

Nowadays humanity is moving very fast.... however it is mandatory to vote & one must vote for a better tomorrow!

Now it might not be necessary that when an election is held the voter is in the same state & in such cases many votes are lost, for instance one might've went for a trip or is out of state/town for work/emergency etc. 


For such cases this website can been made available to all so that they can vote wherever they are, however they must vote in the given time else they can't vote.

## Pros
 
 1. Citizens don't have to stand in line for voting.
 2. Citizens don't need to be in the same state while voting. 
 3. Corruption at lower level will stop.
 4. In case of a virus outbreak like now, this system can be used.
 5. Multiple Elections Can be Held At the same time.
 6. Instantaneous Results can be Calculated.
 
## Cons

1. We haven't added much security except for ```django auth system ``` for authentication.
2. Due to lack of servers, on election day server may lag.



## Coding Part

1. Back-End - In ```Python```
2. Front-End - ```HTML,CSS,Java Script,Bootstrap,Jinja (Django Template Language)```
3. Integration -``` Django, Sqlite DB```

Comments are added wherever necessary so that the code can be easily understood.


## Requirements 

These are the APIs/Frameworks/Modules We used in order to make this website.
```
Python Programming Language
Django framework
django-mysql module
Twilio API
Heroku API
Bootstrap framework
Pillow module
psycopg2 module

```
