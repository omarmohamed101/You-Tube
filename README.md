<h1 align="center">You-tube Assistant</h1>
<p align="center">
  <img src="yt.PNG" alt="project running"  height="300px"/>
  <br>
  <i>Quickly calculating the playlist length and number of videos instead of doing it by hand
    <br>extremly useful with the very long play list</i>
  <br>
</p>

## Table of contents

- [Quick start](#Quick-start)
- [Step by step installation](#installation)
- [How to use it](How-to)


## Quick start

- in order to run this code you should install `python3` on your machine `pip install python3`
- Clone the repo `git clone `

## installation

First visit this [link](https://console.developers.google.com/) </br>

1- if you dont have any projects yet you should see `CREATE PROJECT` or you may find `New project` if you already did before, so after creating a new one give your project a name. then click `CREATE`</br>
2- then we have to enable our api, so click `api library` and search for youtube data api then click enable</br>
3- Now we need to make an api key, to do so, click on `CREATE CREDENTIALS` then it will ask you a couple of questions about what kind of credentials we need.</br>
  - `Which API are you using?` choose the api you just created which will be youtube data api </br>
  - then `Where will you be calling the API from?` choose other non-UI </br>
  - Finally below `What data will you be accessing?` choose public data which will do the job in our project. </br>
then click What credentials do i need?
and you should now be seeing the api key `COPY` that key and clilck done.</br>


We need to add this key to the enviroment variable to keep it away from the code</br>
<hr>
For windows </br>
1- open control panel</br>
2- select system and security</br>
3- navigate to system</br>
4- on the left choose advanced system settings</br>
5- click on environment variables</br>
under user variables click new then name the variable `YT_API_KEY` and put you key in the value and click ok. pay attention to this name here because it is used in the code and if 
you named it something else it will not wort unless you update the code.</br>
<hr>
For Mac & Linux:</br>
1- open you terminal and navigate to the home by typing `cd`</br>
2- open the path file in any text editor EX: `nano .bash_profile`</br>
3- at the top of the file type `export YT_API_KEY = ""` and in the double quotes insert the key we've generated above</br>
4- save the file</br>
</hr>

## How to

open any playlist you want and from the url grab the playlist id, you will found it after the equal sign. </br>
then paste it and click search playlist




