# crypto-com-exchange-api #
Crypto.com Exchange API

Read account information from crypto.com exchange API

### API ###
- https://exchange-docs.crypto.com/spot/index.html#introduction
- https://exchange-docs.crypto.com/spot/index.html?python#digital-signature
- https://exchange-docs.crypto.com/spot/index.html#public-get-instruments
- https://exchange-docs.crypto.com/spot/index.html#private-get-account-summary

##### Requirements #####
- https://www.python.org/downloads/

1. python3 installed:
   
   `python3 -v`
2. pip installed:
   
   `python3 -m pip --version`

3. python Virtual Environment installed
    - Ubuntu/Debian
        - sudo apt-get update
        - sudo apt-get install python-virtualenv
        - sudo pip install virtualenv
    - Mac / Windows
        - should be installed with python and pip 
##### Setup #####
Enter project root directory:
1. Edit the `.env` file your API Key and Secret
    ```
    API_KEY=changeme
    API_SECRET=changeme
    ```
- Follow this link to generate the API Key
    - https://exchange-docs.crypto.com/spot/index.html#generating-the-api-key

2. Create a Python Virtual Environment:
   
   `python3 -m venv env`
   
3. Activate the Virtual Environment:
   
   `source ./env/bin/activate`
   
    - your console should change adding `(env)` as prefix
    - To exit type refer to 'Deactivate the Virtual Environment'
   
4. Install dependencies:
   
   `pip3 install -r requirements.txt`
   
    Ignore warning messages.

5. Deactivate the Virtual Environment:
   
   `deactivate`
   - the `(env)` prefix should be removed from the console

##### Run #####
1. Enter the project root directory:
   `python3 app_cdc_account.py`

2. You should see something like:
   ```
   Reading account from API url 'https://api.crypto.com/v2/private/get-account-summary' at '2021-04-21 09:27:27'
   API Response '200' - 'OK'
   API accounts total balance is x.yz USDT
   ```