
# ladder.ly 

Development of a working prototype for automated aggregation and visualization of laddering interview data

## Installation Backend

* clone the GitHub repo ```https://github.com/bodejan/ladder.ly```
* navigate to the backend folder
* create venv: ```python -m venv venv```
    * run ```venv\Scripts\activate.bat``` (Windows)
    * or ```source venv/bin/activate``` (Mac/Linux) to activate the virtual environment 
* use [pip](https://pip.pypa.io/en/stable/) to install the requirements: ```pip install -r requirements.txt```
* run app.py to start the BE server


## Installation Frontend

* navigate to the frontend folder
* ```npm install```
* ```npm run serve```   
    * your FE server is now running 


## Documentation
Detailed documentation:

* [Backend](https://htmlpreview.github.io/?https://github.com/bodejan/ladder.ly/blob/master/backend/docs/index.html) :
  * [app.py](https://htmlpreview.github.io/?https://github.com/bodejan/ladder.ly/blob/master/backend/docs/app.html) 
  * [functions.py](https://htmlpreview.github.io/?https://github.com/bodejan/ladder.ly/blob/master/backend/docs/functions.html)

  
* [Frontend](frontend/docs/About.md)
    * [About.vue](frontend/docs/About.md)
    * [Home.vue](frontend/docs/Home.md)
    * [Data.vue](frontend/docs/Data.md)
    * [Hvm.vue](frontend/docs/Hvm.md)
    * [Aim.vue](frontend/docs/Aim.md)
    * [api/index.js](frontend/docs/ApiIndex.md)
    * [store/index.js](frontend/docs/StoreIndex.md)


* generate docs using [pydoc3](https://pypi.org/project/pdoc3/) (.py), [vuedoc](https://github.com/vuedoc/md) (.vue) and [jsdoc2md](https://github.com/jsdoc2md) (.js):
   * ```export PYTHONPATH="$PWD/ladder_ly"```
   * ```pdoc ladder_ly --html --force --skip-errors```
   * ```vuedoc.md src/components/*.vue --output docs/```
   * ```npx jsdoc2md src/store/index.js  ```
   * ```npx jsdoc2md src/api/index.js  ```


    




## Usage
* start BE server (using the venv python interpreter e.g. in VSC)
* start FE server
* open local/network host in your browser
* upload your data 
    * make sure it is in the right format, use example_ladders.xlsx and example_labels.xlsx as template
    * if the backend throws an error related to the xlsx files, try to open and save the files anew
* you will be redirected to your hierarchical value map
* your uploaded data is displayed @ /data in a grid layout

____

![hierachical value map](example_pictures/hvm.png)
____

* configure your hierachical value map:
    * cutoff-level
    * only direct, direct and indirect implications
    * treatment
    * submit to update the hierachical value map

___
![configure](example_pictures/configure.png)
___

## Built With

* [flask](https://flask.palletsprojects.com/en/1.1.x/) - Backend
   * Pandas (data manipulation, file ex-, import)
   * NumPy (multi-dimensional arrays)  
* [vue.js](https://vuejs.org/) - Frontend
   * Vuetify (design material components)
   * Vuex (state management)
   * Grid.js (visualization of tabels)
   * Axios (frontend-backend communication)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment
The tool has been developed by Jan Bode 

Supervision: Tim Rietz 

@IISM - Karlsruhe Institute of Technology

## License
[MIT](LICENSE.md)
