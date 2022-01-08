# lichess-bot
Fork of [lichess-bot](https://github.com/ShailChoksi/lichess-bot) with my own modifications.

## How to Install
First please refer to [ShailChoksi/lichess-bot/README](https://github.com/ShailChoksi/lichess-bot/blob/master/README.md)

I'll be including my own strategies and some might require additional configuration/installation. You don't need to configure all of them, just refer to the following and configure accordingly.

### Stockfish
1. Install [Stockfish](https://stockfishchess.org/download). You'll need a full path to its main program.
2. Modify [.env.tmp](.env.tmp), changing `stockfish-path` to yours. On windows could be _c:\stockfish\stockfish.exe_, on *unix _/usr/bin/stockfish_
3. Rename _.env.tmp_ to _.env_

# License
Same as [lichess-bot](https://github.com/ShailChoksi/lichess-bot) (AGPLv3). Check out LICENSE.txt for the full text.
