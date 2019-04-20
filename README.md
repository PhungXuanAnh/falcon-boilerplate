This is sample api using falcon

# Run app

```shell
source env/../
pip install -r requirements.txt
./falcon.sh
Usage: falcon.sh {start|stop|db}
```

# Run command without auth

```shell
curl -XGET http://localhost:6000/users | json_pp
# or 
# source env before run below command
http http://localhost:6000/users
```