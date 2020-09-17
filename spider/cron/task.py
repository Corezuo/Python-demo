# -*- coding: utf-8 -*-
"""
定时任务：刷新知乎热榜数据

第三方库定时调度 apscheduler
"""
from apscheduler.schedulers.background import BackgroundScheduler

from spider.collect import collect

scheduler = BackgroundScheduler()


def start():
    """定时任务每 10秒执行一次"""
    scheduler.add_job(collect.start_collect, 'interval', seconds=5)
    scheduler.start()
