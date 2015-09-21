# ghcount: a python script for code contribution statistics.
Usage: 
  1. Copy this script to a GIT repo, and cd to this repo for code contribution statistics.
  2. Check out the *correct branch*.
  3. Run this python script in a GIT repo, it shows a list of authors and their contributions (lines of insertions \
    and deletions, touched files, and total number of commits).
  4. Without any option, it collect statistics for all authors in current GIT repo.
  5. Use "--author" option to limit commit authors, and each author is separated with comma. For example:
    
    ./ghcount.py --author="yanqiang.luan, neokidd"


Note:
  1. It shows statistics *only in the current branch*, so no duplicate works are counted due to merges.
  2. It *MUST* run in a GIT repo.

