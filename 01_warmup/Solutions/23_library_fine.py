from __future__ import print_function
import math

if __name__ == '__main__':
    # Read input from STDIN
    ret_day, ret_mon, ret_yr = map(int, raw_input().split(' '))
    act_day, act_mon, act_yr = map(int, raw_input().split(' '))

    diff_yr = (ret_yr - act_yr)
    diff_mon = (ret_mon - act_mon)
    diff_days = (ret_day - act_day)

    if diff_yr > 0:
        print(10000)
    elif diff_mon > 0 and diff_yr == 0:
        print(500 * abs(diff_mon))
    elif diff_days > 0 and diff_mon == 0 and diff_yr == 0:
        print(15 * abs(diff_days))
    else:
        print(0)


