# Overview

This is a tool to help you obtain OAuth2 tokens for services (so far, only Google is supported). The tool is useful for command-line
applications working with APIs where OAuth2 is the only method of authorization (example [EventNative](https://github.com/jitsucom/eventnative) — connections to [Firebase](https://docs.eventnative.org/configuration-1/sources-configuration/firebase), [Google Analytics](https://docs.eventnative.org/configuration-1/sources-configuration/google-analytics), [Google Play](https://docs.eventnative.org/configuration-1/sources-configuration/google-play), etc). Likewise, it could be useful for debugging.

To run scripts, you need client_secret and client_id (find them at credentials settings of your application at Google console).
For more info about Google OAuth2 configuration, see [documentation](https://developers.google.com/identity/protocols/oauth2/web-server#httprest_4) 

# Configuring oauth for Google

To run scripts you need to obtain client_secret and client_id, and add authorized redirect URL
 * Go to [Google API console](https://console.developers.google.com/). Make sure that you selected a correct google account (top-right corner) and correct project (top-left corner)
 * Go to Credentials section
 * Create a new client under "OAuth 2.0 Client IDs" section (or reuse an existing one). The type of Client should be "Web Application"
 * Open Client ID settings, add http://localhost to "Authorized Origin" 
 * Add https://localhost:5000 to "Authorized redirect URIs". Change 5000 to other port if you're going to use non-standart port
 
Read more about [Google OAuth](https://developers.google.com/identity/protocols/oauth2/web-server#httprest_4) configuration here.


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

Run with custom scopes:
```shell script
./authorizer.py --client_id=<CLIENT_ID> --client_secret=<CLIENT_SECRET> --scope='https://www.googleapis.com/auth/drive.metadata.readonly https://www.googleapis.com/auth/spreadsheets.readonly'
``` 

Once script is started, the browser will be opened. Follow instructions and get a OAuth JSON secret at the end. Use `access_token` and `refresh_token`

After execution, press CTRL+C to stop server

# Additional options

By default, OAuth scope is https://www.googleapis.com/auth/analytics.readonly (Google Analytics API). Use `--scope=<SCOPE>` to redefine scopt
