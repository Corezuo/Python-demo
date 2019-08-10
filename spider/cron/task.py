# -*- coding: utf-8 -*-
"""
定时任务：刷新知乎热榜数据

第三方库定时调度 apscheduler
"""
from apscheduler.schedulers.background import BackgroundScheduler

from collect import collect

scheduler = BackgroundScheduler()


"""
定时任务每 10秒执行一次
"""
def start():
    scheduler.add_job(collect.start_collect, 'interval', seconds=5)
    scheduler.start()
