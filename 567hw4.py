import requests
import unittest
from unittest import mock
import json
import os

def filereader(path):
    try:
        r=requests.get(path)
    except FileNotFoundError: 
        return "Can't open the web of whitehouse address"
    else:
        n=json.loads(r)
    return n
def commits1(path1):
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

    @mock.patch('requests.get')
    def testcommit1(self,mock_req):
        i=0
        n1=json.dumps([{'name':"hellogitworld"},{'name':"helloworld"},{'name':"Mocks"},{'name':"Project1"},{'name':"threads-of-life"}])
        n2=json.dumps([0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9])
        n3=json.dumps([1,2,3,4,5,6])
        n4=json.dumps([0,1,2,3,4,5,6,7,8])
        n5=json.dumps([1,2])
        n6=json.dumps([1])
        
        mock_req.side_effect = [n1,n2,n3,n4,n5,n6]
        feedback1=commits1('richkempinski')
        rightfeedback={"hellogitworld":30,"helloworld":6,"Mocks":9,"Project1":2,"threads-of-life":1}
        self.assertEqual(feedback1,rightfeedback)
    @unittest.expectedFailure
    def testfail(self):
        feedback2=commits1("sdfjvkeandvnsdfnj")



if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
