# ghcount: a python script for code contribution statistics.
Usage: 
  1. Copy this script to a GIT repo, then CD to git repository for statistics.
  2. Check out the *correct branch* you wish to collect stat data.
  3. Run this python script in a GIT repo, it shows a list of authors and their contributions (lines of insertions and deletions, touched files, and total number of commits).
  4. Without any option, it collect statistics for all authors in current GIT repo.
  5. Use "--author" option to limit commit authors, and each author is separated with comma. For example:

<pre><code>
  ./ghcount.py --author="yanqiang.luan, neokidd"
</code></pre>

  6. Use "--gparam" option to add more params to git log command. For example, using "--no-merges" params as below, it counts commits only on this branch, no incoming merge branches are counted. Usually it means that code stats for "release" branch, while without this param, it counts both "release" and "dev". 

<pre><code>
  ./ghcount.py --gparam="--no-merges"
</code></pre>

Note:
  1. It *must* run in a GIT repo.

