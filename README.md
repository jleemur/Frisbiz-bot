# Frisbiz Discord Bot

Playing around with discord & riot api. Main use case will be to post a completed league of legends match to channel whenever a new match is found for a registered player.

### Riot rate limits
```
20 requests every 1 seconds(s)
100 requests every 2 minutes(s)
```

### Requirements
```
Python 3.8.2
```

### Supported commands
```
Prefix for bot commands is <BIZ>

Random roles for all players
<BIZ>junkyard <str: p1> <str: p2> <str: p3> <str: p4> <str: p5>

Post a meme from reddit
<BIZ>memes <optional str: subreddit>

Show top 5 champions played
<BIZ>top_champions <str: summonerName>
```

### Champion data
http://ddragon.leagueoflegends.com/cdn/10.8.1/data/en_US/champion.json
http://ddragon.leagueoflegends.com/cdn/10.8.1/data/en_US/champion/Ahri.json
http://ddragon.leagueoflegends.com/cdn/10.8.1/img/champion/Ahri.png
