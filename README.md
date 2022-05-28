# Capital Gains Project

Use this project to calculates how much tax you should pay based on the profit or losses of a stock market investment.

## Technical decisions

* This project is created without frameworks using python 3 and using pip to install one required library for tests. Based on the required features, python is just enough to complete with the scope and could be migrated to a framework in the future if it is needed.

* Project structure is this:
`````
main.py --> entrypoint
app --> aplication folder
 \ adapters/presenters --> components to capture and show information
 \ adapters/repositories --> components to store information
 \ domains --> problem domain classes
 \ use_cases --> app features, "calculate taxes" for example
tests --> tests folder
 \ main.py --> test entrypoint
 \ int_test.py --> integration tests to evaluate stdin and stdout
 \ mocks.py --> Mock classes
 \ adapters --> unit tests
 \ use_cases --> unit tests
 \ domains --> unit tests
`````
* This project uses pip to manage dependencies, it is using only faker library to create data for testing.
* This project is not using a dependency injection library, you can see how it works for this project in **main.py** file.
* Python does not have the interface concept. For that reason, this project uses prefix "base" to name "interfaces".

## Run

Open your terminal in root folder of this project and execute:

1. Install dependencies
````
pip install -r requirements.txt
````
2. Execute app 
`````
python3 main.py <simulation>
`````
For example:
`````
python3 main.py [{"operation":"buy", "unit-cost":10.00, "quantity": 100}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}]
`````
Or use a file 
`````
python3 main.py < ./tests/txt/test1.txt
`````
Note: You could use different examples in **./tests/txt/** folder

## Tests

Open your terminal in root folder of this project and execute:

1. Install dependencies
````
pip install -r requirements.txt
````
2. Execute tests 
`````
python3 ./tests/main.py
`````

## Docker environment

If you have problems to install required software, but you have docker, this project has a Dockerfile to create the environment. Execute next commands in root folder of this project:
`````
docker build -t capital-gains .
docker run -it capital-gains /bin/bash
`````
Inside container execute **Run** section second step and **Tests** section second step.