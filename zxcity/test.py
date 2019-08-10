# -*- coding: utf-8 -*-


if __name__ == "__main__":
    try:
        raise Exception("发生异常")
    except Exception as e:
        print("发生了")
        print(e)
    finally:
        print("执行了")
