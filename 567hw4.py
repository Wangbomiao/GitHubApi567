import urllib.request
import unittest
import json
import os
def filereader(path):
    try:
        name=urllib.request.Request(url=path)
    except FileNotFoundError: 
        return "Can't open the web of whitehouse address"
    else:
        webfile=urllib.request.urlopen(name).read().decode()
    n=json.loads(webfile)
    return n
def commits(path1):
    paths11='https://api.github.com/users/{}/repos'.format(path1)
    refeedback=filereader(paths11)
    n=list()
    for i in refeedback:
        repo=i['name']
        n.append(repo)
    commitnum=dict()
    for i in n:
        paths="https://api.github.com/repos/{}/{}/commits".format(path1,i)
        fpget=filereader(paths)
        num=len(fpget)
        commitnum[i]=num
    return commitnum


class CommitTest(unittest.TestCase):
    def testmain(self):
        feedback1=commits('richkempinski')
        rightfeedback={"hellogitworld":30,"helloworld":6,"Mocks":9,"Project1":2,"threads-of-life":1}
        self.assertEqual(feedback1,rightfeedback)



if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)