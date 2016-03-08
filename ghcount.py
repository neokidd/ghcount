#!/usr/bin/python
# coding=utf-8
import commands
import sys, getopt

# count of commits
commits = 0
# a dict holding status data
profiles = dict()
# current author of this commit
author = ''
# for collecting each author's code contribution
authors = ''
authorList = []
# additional param for git log
additional_git_param = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"",["author=","committer=","gparam="])
except getopt.GetoptError:
    print 'Wrong input!! \nUsage:\nghcount.py [--author=<comma separated author names>]'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'Usages:\nghcount.py [--author=<comma separated author names>]'
        sys.exit()
    elif opt in ("--committer", "--author"):
        authors = arg
    elif opt == '--gparam':
        additional_git_param = arg

authorList = authors.split(",")

# debugging for input option: authorList
#print authorList
print 'Collecting git log...'
(exitstatus, outtext) = commands.getstatusoutput('git log --numstat '+additional_git_param)

if exitstatus != 0:
    print 'Error! Check if you\'re in a git repository.'
    print 'Usage: run it in a git repo to show code statistics of authors'
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
            profiles[author] = [0, 0, set(), 1]
        else:
            profiles[author][3] += 1
    elif line[0].isdigit() and not line.endswith('pbxproj\n'):
        # print(line)
        segments = line.split('\t')
        profiles[author][0] += int(segments[0])
        profiles[author][1] += int(segments[1])
        profiles[author][2].add(segments[2])

print 'Done.'
print ('{:12}\t{:12}\t{:12}\t{:12}\t{:40}').format('INSERTIONS', 'DELETIONS', 'FILES', 'COMMITS', 'AUTHOR')
for (k, v) in profiles.items():
    # print ('{:40.39}:\t insertions:\t {:10},\t deletions:\t {:10},\t files:\t {:5},\t commits:\t {:5}').format(k, str(v[0]), str(v[1]), str(len(v[2])), str(v[3]))
    print ('{:12}\t{:12}\t{:12}\t{:12}\t{:40}').format(str(v[0]), str(v[1]), str(len(v[2])), str(v[3]), k)

if authors != '':
    print "\nIndividual code statistics:\n"
    for (k,v) in profiles.items():
        for author in authorList:
            if k.find(author.strip(' ')) != -1 or authors == 'all':
                print "Individual: " + k
                # print v
                individualFiles = list(v[2])
                individualFiles.sort()
                for f in individualFiles:
                    print f
                print "\n"


