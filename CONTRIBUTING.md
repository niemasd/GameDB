# How to Contribute
[GameDB](https://github.com/niemasd/GameDB) was designed with ease of contribution in mind: different consoles, different games from the same console, and even different types of metadata from the same game are stored separately in order to prevent potential merge conflicts between contributions. If you want to contribute to this project (thank you in advance!!), this write-up will provide some guidance. I want to preface by emphasizing that, because of GitHub's nice web interface, you can make any contributions you'd like without needing to code or do anything from the command line: contributions can be made completely in the GitHub web interface.

## Data Organization
Before I describe how to contribute to this project, I want to first describe how the data are organized. This will help you know where to look for any specific contributions you want to make.

Rather than storing all consoles in a single repository, each console is stored in its own repository named `GameDB-???`, where `???` is the name of the console. For example, data about Nintendo 64 (N64) games are stored in a repository named [`GameDB-N64`](https://github.com/niemasd/GameDB-N64). A complete list of console-specific GameDB repositories can be found in the [GameDB README](https://github.com/niemasd/GameDB/blob/main/README.md).

Within each console-specific repository is a `games` folder (e.g. [`GameDB-N64/games`](https://github.com/niemasd/GameDB-N64/tree/main/games)), which contains all actual game metadata. This is where any contributions to the database should be made.

Each individual game release (not "game": "game *release*") is stored within its own sub-folder, where the name of the sub-folder is the unique serial number or identifier of that specific game release. For example, the original USA release of [Super Mario 64](https://gamefaqs.gamespot.com/n64/198848-super-mario-64/data) has a serial number of `NUS-NSME-USA`, so metadata about this release can be found in [`GameDB-N64/games/NUS-NSME-USA`](https://github.com/niemasd/GameDB-N64/tree/main/games/NUS-NSME-USA). Note that a single game typically has multiple releases (e.g. multiple regions, or even multiple releases within the same region), so a single game will typically have multiple sub-folders in the `games` folder (one per release).

Within a game release's sub-folder exists the actual metadata for that game release. Each individual piece of metadata is stored within its own separate file. Currently, there are intentionally only plain-text (`.txt`) files, but additional file formats can be added in the future if there is strong enough desire.

### Metadata Files
Typically, the following files exist within a game release's sub-folder (only `title.txt` is required; the others are optional but strongly preferred if available):

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

## Step 1: Fork the Repository of Interest
In order to make your contribution, the first step is to "fork" the console-specific repository you want to contribute to (e.g. [`GameDB-N64`](https://github.com/niemasd/GameDB-N64)). You can read more about what "forking" a GitHub repository means in the [*Fork a repo*](https://docs.github.com/en/get-started/quickstart/fork-a-repo) page of the GitHub documentation, but in short, "forking" a repository means creating a copy of the repository in your own GitHub account. Every GitHub repository has a "Fork" button in the top-right of the page: just click that button, and GitHub will guide you in forking the repository. This will result in the creation of a new repository in your own GitHub account with the following URL:

```
https://github.com/[YOUR GITHUB USERNAME]/GameDB-[CONSOLE]
```

## Step 2: Make the Changes in Your Fork
The second step is to actually make the changes you want to contribute within your own fork of the repository. GitHub allows you to actually create new files and edit existing files directly within the web browser: no need to have any coding or command line skills!

### Editing an Existing File
If you want to correct an erroneous piece of existing metadata:

1. Navigate to the file you want to edit (e.g. `GameDB-N64/games/NUS-NSME-USA/release_date.txt`)
2. Click the "Edit this file" button in the top-right of the file viewer (the icon looks like a pencil)
3. Make the edits you'd like to make
4. Click "Commit changes..." (green button in the top-right)
5. Type in a descriptive "Commit message" and optionally an "Extended description"
6. Click "Commit changes" (green button)

### Creating a New File in an Existing Folder
If you want to add a new piece of metadata that was previously missing:

1. Navigate to the game release folder you want to create a new file within (e.g. `GameDB-N64/games/NUS-NSME-USA`)
2. Click the "Add file" button in the top-right
3. Click "Create new file"
4. In the "Name your file..." textbox at the top, enter the name of the metadata file you want to create (e.g. `release_date.txt`)
    * See the [Metadata Files](#metadata-files) section for a list of metadata files you can create
5. In the big textbox that says "Enter file contents here", type the metadata you want to contribute
    * Please use consistent formatting with respect to the same metadata in other game releases
6. Click "Commit changes..." (green button in the top-right)
7. Type in a descriptive "Commit message" and optionally an "Extended description"
8. Click "Commit changes" (green button)

### Creating a New Folder
If you want to add a new game release that was previously missing:

1. Navigate to the `games` folder (e.g. `GameDB-N64/games`)
2. Click the "Add file" button in the top-right
3. Click "Create new file"
4. In the "Name your file..." textbox at the top:
    1. Enter the serial number of the game release you want to add (e.g. `NUS-NSME-ABC`)
    2. Click the `/` (slash) button on your keyboard
        * This will make the serial number a folder instead of a file
    3. Enter `title.txt` in the now-empty "Name your file..." box
        * You could theoretically enter any filename, but because all game releases **must** have a `title.txt`, it's good to start with that
5. In the big textbox that says "Enter file contents here", type the metadata you want to contribute
    * Please use consistent formatting with respect to the same metadata in other game releases
6. Click "Commit changes..." (green button in the top-right)
7. Type in a descriptive "Commit message" and optionally an "Extended description"
8. Click "Commit changes" (green button)

## Step 3: Create a Pull Request (PR)
Once you have made all of the edits you would like to contribute, you can create a "Pull Request" (PR). You can read more about what "Pull Requests" are in the [*About pull requests*]([https://docs.github.com/en/get-started/quickstart/fork-a-repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)) page of the GitHub documentation, but in short, a "Pull Request" is a request to merge your edits into the original repository. Every GitHub repository has a "Pull requests" tab at the top of the page.

1. Click on the "Pull requests" tab in your forked repository that has the changes you would like to submit
2. Click "New pull request" (green button in the top-right)
3. Click "Create pull request" (green button in the top-right)
