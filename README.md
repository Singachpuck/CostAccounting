# Cost Accounting

## This application provides REST API to keep track of your expenses

### Available endpoints:

- Add category
    - Url:  
      ```/api/v1/categories```
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
      ```/api/v1/categories```
    - Method:  
      ```GET```
- Add user
    - Url:  
      ```/api/v1/users```
    - Method:  
      ```POST```
    - Payload:
      ```
      {
          "name": "string"
      }
      ```
- Add transaction
    - Url:  
      ```/api/v1/transactions```
    - Method:  
      ```POST```
    - Payload:
      ```
      {
          "userId": "int",
          "categoryId": "int",
          "amount": "decimal"
      }
      ```
- Get transactions for user with category
    - Url:  
      ```/api/v1/users/<userId>/transactions?category=<category name>```
    - Method:  
      ```GET```
    - Query parameter is optional