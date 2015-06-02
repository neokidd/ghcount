import commands
import sys

# count of commits
commits = 0
# a dict holding status data
profiles = dict()
# current author of this commit
author = ''

(exitstatus, outtext) = commands.getstatusoutput('git log --numstat --first-parent')

if exitstatus != 0:
    print 'Error! Check if you\'re in a git repository.'
    print 'Usage: run it in a git repo to show status of authors and '
    sys.exit(0)

lines = outtext.split('\n')

for line in lines:
    if line == '':
        continue
    elif line[0:6] == "commit":
        commits += 1
        # print(line)
    elif line[0:6] == "Author":
        author = line[8:]
        if line[8:] not in profiles.viewkeys():
            # it's a new author, make new map item
            profiles[author] = [0, 0, set()]
    elif line[0].isdigit() and not line.endswith('pbxproj\n'):
        # print(line)
        segments = line.split('\t')
        profiles[author][0] += int(segments[0])
        profiles[author][1] += int(segments[1])
        profiles[author][2].add(segments[2])

for (k, v) in profiles.items():
    print ('{:<40}: insertions: {:10}, deletions: {:10}, files: {:5}').format(k, str(v[0]), str(v[1]), str(len(v[2])))