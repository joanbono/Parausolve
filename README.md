# Parausolve

[Paraulògic](https://paraulogic.rodamots.cat/) Solver

Paraulògic is a game I have been playing with my family this Christmas. The game consists on use always the red letter and the rest of them to look for words bigger than 3 characters.

![image](https://user-images.githubusercontent.com/7288621/147486773-bae1c3bb-8efc-4ff0-9de8-5ee0537e61a8.png)

Every day the challenge changes, and every day the number of words to complete the challenge are different.

## Install

```sh
$ pip install -r requirements.txt
$ python parausolve.py -d 2021-12-27 | wc -l
      83

$ python parausolve.py -d 2021-12-27 | head -10
adnat
adnata
adotzenada
adotzenat
anant
andante
anet
ant
anta
antedata
``` 

> This kills the challenge and the main goal is not to cheat but I was curious how the game was validating the words.
