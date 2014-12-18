#!/usr/bin/env python
#coding:utf-8

def get_min(sec):
    return sec // 60 + (sec % 60 > 0)

def get_cost(min):
    if min > 100:
        min += min - 100
    return min

def total_cost(calls):
    pre_date = calls[0].split()[0]
    coins, today_min = 0, 0
    for call in calls:
        today_info = call.split()
        sec = int(today_info[2])
        date = today_info[0]
        if date != pre_date:
            coins += get_cost(today_min)
            today_min = 0
        today_min += get_min(sec)
        pre_date = date
    return coins + get_cost(today_min)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
