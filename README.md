This is a tool to help you get Google OAuth2 tokens.
To run scripts, you need client_secret and client_id (find them at credentials settings of your application at Google console).
For more info about Google OAuth2 configuration, see [documentation](https://developers.google.com/identity/protocols/oauth2/web-server#httprest_4) 

# Installation
Install dependencies using pip3:
```shell script
pip3 install -r requirements.txt
```

# How to run
Run using python3 command:
```shell script
python3 authorizer.py --client_id=<CLIENT_ID> --client_secret=<CLIENT_SECRET>
```
or 
```shell script
chmod +x authorizer.py
./authorizer.py --client_id=<CLIENT_ID> --client_secret=<CLIENT_SECRET>
```

If the default port 5000 is used on your machine, you can specify the required one as parameter, for example:
```shell script
./authorizer.py --client_id=<CLIENT_ID> --client_secret=<CLIENT_SECRET> --port=8000
``` 
will start the server on 8000 port.

After execution, press CTRL+C to stop server