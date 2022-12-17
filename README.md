# Cost Accounting (v2)

## This application provides REST API to keep track of your expenses

## Release notes:
- **Add Account entity (Variant 3)**
- Update version of api to ```v2```
- You can add accounts for a specific user
- You can view created accounts
- Now you can create transactions between 2 accounts (see endpoint description)
- You can view transactions for a user that is the owner of account where the money was taken from


### Available endpoints:

- Add category
    - Url:  
      ```/api/v2/categories```
    - Method:  
      ```POST```
    - Payload:
      ```
      {
          "name": "string"
      }
      ```
- Get categories
    - Url:  
      ```/api/v2/categories```
    - Method:  
      ```GET```
- Add user
    - Url:  
      ```/api/v2/users```
    - Method:  
      ```POST```
    - Payload:
      ```
      {
          "name": "string"
      }
      ```
- Add account
  - Url:  
    ```/api/v2/accounts```
  - Method:  
    ```POST```
  - Payload:
    ```
    {
        "name": "string",
        "amount": "decimal"
    }
    ```
- Get accounts
  - Url:  
    ```/api/v2/accounts```
  - Method:  
    ```GET```
- Add transaction between specific accounts
    - Url:  
      ```/api/v2/transactions```
    - Method:  
      ```POST```
    - Payload:
      ```
      {
          "accountFrom": "int",
          "accountTo": "int",
          "categoryId": "int",
          "amount": "decimal"
      }
      ```
- Get transactions for user with category
    - Url:  
      ```/api/v2/users/<userId>/transactions?category=<category name>```
    - Method:  
      ```GET```
    - Query parameter is optional
    - Returns list of transactions where user is owner of Account where the money was taken from (accountFrom)

### To run locally:

- Clone this repository
- Make sure you have flask installed: ```flask --version```
- Set environmental variable with the name ```DATABASE_URI``` with the value that contains database connection string for ```sqlite3```.  
  Example of connection string:  ```sqlite:///D:\path\to\database\database.db```  
  For testing purposes you can use project database under the path ```/db/database.db```
- In the repository root run:
  - ```flask --app rest run```