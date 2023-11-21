# How to Contribute
[GameDB](https://github.com/niemasd/GameDB) was designed with ease of contribution in mind: different consoles, different games from the same console, and even different types of metadata from the same game are stored separately in order to prevent potential merge conflicts between contributions. If you want to contribute to this project (thank you in advance!!), this write-up will provide some guidance.

## Data Organization
Before I describe how to contribute to this project, I want to first describe how the data are organized. This will help you know where to look for any specific contributions you want to make.

Rather than storing all consoles in a single repository, each console is stored in its own repository named `GameDB-???`, where `???` is the name of the console. For example, data about Nintendo 64 (N64) games are stored in a repository named [`GameDB-N64`](https://github.com/niemasd/GameDB-N64). A complete list of console-specific GameDB repositories can be found in the [GameDB README](https://github.com/niemasd/GameDB/blob/main/README.md).

Within each console-specific repository is a `games` folder (e.g. [`GameDB-N64/games`](https://github.com/niemasd/GameDB-N64/tree/main/games)), which contains all actual game metadata. This is where any contributions to the database should be made.

Each individual game release (not "game": "game *release*") is stored within its own sub-folder, where the name of the sub-folder is the unique serial number or identifier of that specific game release. For example, the original USA release of [Super Mario 64](https://gamefaqs.gamespot.com/n64/198848-super-mario-64/data) has a serial number of `NUS-NSME-USA`, so metadata about this release can be found in [`GameDB-N64/games/NUS-NSME-USA`](https://github.com/niemasd/GameDB-N64/tree/main/games/NUS-NSME-USA). Note that a single game typically has multiple releases (e.g. multiple regions, or even multiple releases within the same region), so a single game will typically have multiple sub-folders in the `games` folder (one per release).

Within a game release's sub-folder exists the actual metadata for that game release. Each individual piece of metadata is stored within its own separate file. Currently, there are intentionally only plain-text (`.txt`) files, but additional file formats can be added in the future if there is strong enough desire. Typically, the following files exist within a game release's sub-folder (only `title.txt` is required; the others are optional but strongly preferred if available):

* `title.txt`, which contains the title of the game release
  * A single game might have different titles for its different releases (e.g. regional titles, special editions, etc.)
  * Every folder **must** have a `title.txt` file
* `region.txt`, which contains the region of the game release
  * I want to try to stick to `NTSC-U`, `NTSC-J`, and `PAL`, but I am open to changing it on a console-by-console bases if strongly desired
  * Every folder *should* have a `region.txt` file
* `release_date.txt`, which contains the release date of the game release
  * These **must** be in the following format: `YYYY-MM-DD`
  * The formats `YYYY-MM` and `YYYY` are also acceptable if the complete `YYYY-MM-DD` information is not known
* `developer.txt`, which contains the developer of the game release
  * If there were multiple developers, they can all be listed on their own line in the file
* `publisher.txt`, which contains the publisher of the game release
  * If there were multiple publishers, they can all be listed on their own line in the file
* `genre.txt`, which contains the genre of the game release
  * If there were multiple genres, they can all be listed on their own line in the file
* `rating.txt`, which contains the rating (e.g. ESRB, PEGI, etc.) of the game release
  * If there were multiple ratings, they can all be listed on their own line in the file

### Summary of Data Organization
The following folder tree structure summarizes the data organization of a given game:

```
GameDB-[CONSOLE 1]/
  games/
    [GAME 1 SERIAL]/
      developer.txt
      genre.txt
      publisher.txt
      rating.txt
      region.txt
      release_date.txt
      title.txt
    [GAME 2 SERIAL]/
      ...
    ...
GameDB-[CONSOLE 2]/
  games/
    ...
...
```
