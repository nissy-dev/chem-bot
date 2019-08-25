# chem-bot

Slack bot for chemist

## Usage (I use conda)

### create the environment
```
$ git clone git@github.com:nd-02110114/chem-bot.git
$ conda env create
$ conda activate chem-bot

```

### create `.env` file
```
BOT_USER_OAUTH_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXX
OAUTH_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXX
```

### start bot server
```
$ python run.py
```

## Deploy for Heroku

```
$ heroku login
$ heroku container:login
$ heroku create heroku-chem-bot

$ heroku container:push worker
$ heroku container:release worker
```

<!-- ### set up heroku
```
$ heroku login
$ heroku 

```

### create `.env` file
```
$ heroku run bash

// in server
$ export "BOT_USER_OAUTH_ACCESS_TOKEN=XXXXXXXXXXXX" > .env
```

### Run server
```
``` -->