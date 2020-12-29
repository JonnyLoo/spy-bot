# spy-bot


### TradingView message format

```
{
    "open": {{open}},
    "high": {{high}},
    "low": {{low}},
    "close": {{close}},
    "exchange": "{{exchange}}",
    "ticker": "{{ticker}}",
    "volume": {{volume}},
    "time": "{{time}}",
    "timenow": "{{timenow}}"
}
```

### Deploy

```
chalice deploy
```

### Run locally

```
chalice local
```

### Make changes

```
conda activate spy-bot
cd .\Desktop\spy-bot
atom .
```

### Add changes to git

```
git add .
git commit -m 'some message here'
git push origin main
```
