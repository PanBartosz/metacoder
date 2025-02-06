# `metacoder` - a web app for coding x-phi papers using X-PHI TQRI V2

This is the web app designed to facilitate coding experimental philosophy papers using X-PHI Transparency and Quality of Reporting Inventory V2. 

## (Methodologically) Important files

In the `translations.yaml` file you can find **ALL** items in the inventory as well as coding instructions and additional elements. 

## Running it locally

You can run it locally using `conda` (https://docs.anaconda.com/miniconda/install/) or other Python distribution system.
- `environment.yml` contains an environment file for `conda`, so to create new environment you need to run `conda env create --name metacoder --file=environment.yml` and switch to it using `conda activate metacoder`
- to run the app you need to:
  - set `BASE_PATH` environmental variable to the directory containing the app and `FLASK_APP` to `__init__.py` 
  - run `flask shell` and `db.create_all()` inside the shell to create an empty database
  - run `flask run` in the app directory
