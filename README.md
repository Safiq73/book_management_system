# Quick Start guide 
### Install Prerequisite

- Python version: 3.8.+ 
 
### Steps

- Install dependencies: `$pip3 install -r requirements.txt`
- Create ENV File: `$cp .env.example .env` [pass asynchronous SQLALCHEMY_DATABASE_URL in .env file ex: 'postgresql+asyncpg://postgres:postgres@localhost:5433/postgres']
- Update the configuration in `.env` file
- Start the server: `$make run_dev_server`