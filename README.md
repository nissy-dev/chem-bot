# chem-bot

Slack bot for chemist

## Feature

| smiles bot                |
|---------------------------|
| <img  src="https://raw.githubusercontent.com/nd-02110114/chem-bot/master/gif/smiles.gif" width="420" height="380"/> |


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
$ heroku config:set BOT_USER_OAUTH_ACCESS_TOKEN=XXXXXXXXXXXXX

$ git add . && git commit -m "commit"
$ heroku stack:set container
$ git push heroku master
```
