How to use it :

You need to have the following library installed :

For the use of the env file :```pip install python-decouple```

For the Web App : ```pip install streamlit```

For the test : ``` pip install unittest```

For the api : 
```sh
pip install fastapi
pip install uvicorn
```
For the main fonctions : 
```sh
pip install panda
pip install requests
pip install beautifulsoup4
pip install pydantic
pip install pymongo
```
Create MongoDB Database named : DanMachiScraping \
Add Collection named : Weapons


If you want another name, go to the file Database.py and change the line 8 and 9

## || Summary File || : 

- Folder Pages :  Pages of the web app :
   - WeaponPage : Home page of the app
   -  WeaponFormAdd : Form page for the add weapon
- Api.py : Contains the API function (see || Run API || for more information)
- Database.py : Contains all function to manipulate data with database

- DataMaker.py : Allows to install the app data in our machine (see || First step || for more information)
- MainManager.py : Allows to load wep app (see || Run Web APP || for more information)
- MultiPage.py :  Allows to maintains the web app in multipages format, it's not my code, it's from internet
- Scraper.py : Contains all fonctions to scrapper a website
- style.css :  used in the web app
- TestUnit.py : Contains many test for the project, (see || Run Test || for more information)
- Weapon.py : Contains the structure of a weapon, used in all the project. Contains also the structure of the data sent for the api call.
.env : Contains the web link for the scraped data


## || First step ||
Before to make everything, you have to install the data and insert them into the database.\
You have to make the command : ```python DataMaker.py```\
It will put inside the database all the data took on the website.\
The link on the website is in the .env file.



## || Run Test ||

To load test, make the command:  

```python TestUnit.py```

You need to uncomment the test you want to make in the bottom of the file : TestUnit.py  
For some test, you have to make the ID manually  

## || Run Web APP ||

 You have to make the command : ```streamlit run MainManager.py```  
From the App, you can add a weapon from a form, and remove a weapon from the main page.  

## || Run API ||

You have to make the command :```uvicorn Api:app --reload```  
Once done, you can use Postman (or other app you want) and load the following routes :  

- GET (Take all weapons): http://localhost:8000/weapons 
- POST (Add) : http://localhost:8000/weapons/add

Data example Add : 
```sh
{
    "id": "64108c2e01adab428f318fd1",
    "name": "Fragarach",
    "owner": "Olgus",
    "description": "A mythic weapon",
    "price": 100000000
}
```



- PUT (Edit) : http://localhost:8000/weapons/edit
```sh
{
    "id": "64108c2e01adab428f318fd1",
    "name": "Fragarach",
    "owner": "Olgus",
    "description": "A mythic weapon forged by Sidonie",
    "price": 300000000
}
```
- DELETE (Remove) : http://localhost:8000/weapons/remove
```sh
{
    "id": "64108c2e01adab428f318fd1",
    "name": "Fragarach",
    "owner": "Olgus",
    "description": "A mythic weapon forged by Sidonie",
    "price": 300000000
}
```
