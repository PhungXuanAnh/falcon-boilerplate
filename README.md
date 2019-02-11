
# Item 1 doesn't use authentication

```shell
curl -XGET http://localhost:6000/item1
# or 
# source env before run below command
http http://localhost:6000/item1
```


# Item2 uses Basic

To create base64 encoded string, access [http://www.utilities-online.info/base64/#.XGFG7VX7SIZ](http://www.utilities-online.info/base64/#.XGFG7VX7SIZ), then enter username and password with format `username:password`

*For example*:

username: test1
password: 12345

Then, we will enter `test1:12345`

```shell
curl -XGET http://localhost:6000/item2 -H "Authorization: Basic dGVzdDE6MTIzNDU="
# or 
http http://localhost:6000/item2 "Authorization: Basic dGVzdDE6MTIzNDU="
```


# Item 3 use Token

```shell
curl -XGET http://localhost:6000/item3 -H "Authorization: Token 123456789"
# or 
http http://localhost:6000/item3 "Authorization: Token 123456789"

# RUN post API without auth
curl -XPOST http://localhost:6000/item3
# or 
http POST http://localhost:6000/item3
```


# Item 4 use JWT token

To create JWT for test, access: [https://jwt.io/](https://jwt.io/), then fill **PAYLOAD** and **VERIFY SIGNATURE** as below:

Payload:
```json
{   "user": {
        "id": 12345,
        "username": "test-user"
    },
    "iat": 1516239022,
    "nbf": 1516239022,
    "exp": 29951113567
}
```

VERIFY SIGNATURE (or Secret key): `secret_key_123`

Then run in terminal:

```shell
curl -XGET http://localhost:6000/item4 -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxMjM0NSwidXNlcm5hbWUiOiJ0ZXN0LXVzZXIifSwiaWF0IjoxNTE2MjM5MDIyLCJuYmYiOjE1MTYyMzkwMjIsImV4cCI6Mjk5NTExMTM1Njd9.U9yuGdn9imVfARMNpGuAzfD4gpizEZ0nNPfBSPGL3OM"
# or 
http http://localhost:6000/item4 "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxMjM0NSwidXNlcm5hbWUiOiJ0ZXN0LXVzZXIifSwiaWF0IjoxNTE2MjM5MDIyLCJuYmYiOjE1MTYyMzkwMjIsImV4cCI6Mjk5NTExMTM1Njd9.U9yuGdn9imVfARMNpGuAzfD4gpizEZ0nNPfBSPGL3OM"
```


# Item 5 disabled authentication
```shell
curl -XGET http://localhost:6000/item5
# or 
http http://localhost:6000/item5
```
