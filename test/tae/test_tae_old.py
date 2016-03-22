'''
Created on Nov 19, 2015

@author: lindauer
'''
import unittest
import shlex
import logging

from smac.tae.execute_ta_run_old import ExecuteTARunOld
from smac.tae.execute_ta_run import StatusType


class TaeOldTest(unittest.TestCase):

    def test_run(self):
        '''
            running some simple algo in old style
        '''
        eta = ExecuteTARunOld(ta=shlex.split("python dummy_ta_wrapper.py 1"))
        status, cost, runtime, ar_info = eta.run(config={})
        assert status == StatusType.SUCCESS
        assert cost == 1.0
        assert runtime == 1.0
        
        print(status, cost, runtime)
        
        eta = ExecuteTARunOld(ta=shlex.split("python dummy_ta_wrapper.py 2"))
        status, cost, runtime, ar_info = eta.run(config={})
        assert status == StatusType.SUCCESS
        assert cost == 2.0
        assert runtime == 2.0
        
        print(status, cost, runtime)
        
        eta = ExecuteTARunOld(ta=shlex.split("python dummy_ta_wrapper.py 2"), run_obj="quality")
        status, cost, runtime, ar_info = eta.run(config={},)
        assert status == StatusType.SUCCESS
        assert cost == 4.0
        assert runtime == 2.0
        
        print(status, cost, runtime, ar_info)
        
        
if __name__ == "__main__":
    unittest.main()
