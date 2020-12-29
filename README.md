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
conda activate spy-bot
cd .\Desktop\spy-bot
atom .
chalice deploy
```

### Run locally

```
chalice local
```

### Add changes to git

```
git add .
git commit -m 'some message here'
git push origin main
```
