#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import decimal
import atexit
import curses
import time
import psutil

lineno = 0


def tear_down():
    win.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


win = curses.initscr()
atexit.register(tear_down)
curses.endwin()


def convert_size(size_bytes, bit=False):
    if isinstance(size_bytes, decimal.Decimal):
        size_bytes = int(size_bytes)

    if size_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    if bit:
        size_name = ("bps", "Kbps", "Mbps", "Gbps", "Tbps", "Pbps", "Ebps", "Zbps", "Ybps")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def print_line(line, highlight=False):
    """A thin wrapper around curses's addstr()."""
    global lineno
    try:
        if highlight:
            line += " " * (win.getmaxyx()[1] - len(line))
            win.addstr(lineno, 0, line, curses.A_REVERSE)
        else:
            line += " " * (win.getmaxyx()[1] - len(line))
            win.addstr(lineno, 0, line, 0)
    except curses.error as e:
        lineno = 0
        win.refresh()
        raise
    else:
        lineno += 1


def network_stat():
    """
    network performance status
    """
    def poll(interval):
        tot_before = psutil.net_io_counters()
        pnic_before = psutil.net_io_counters(pernic=True)
        time.sleep(interval)
        tot_after = psutil.net_io_counters()
        pnic_after = psutil.net_io_counters(pernic=True)
        return (tot_before, tot_after, pnic_before, pnic_after)

    def refresh_window(tot_before, tot_after, pnic_before, pnic_after):
        global lineno
        print_line("total bytes:           sent: %-10s   received: %s" % (
            convert_size(tot_after.bytes_sent),
            convert_size(tot_after.bytes_recv))
            )
        print_line("total packets:         sent: %-10s   received: %s" % (
            tot_after.packets_sent, tot_after.packets_recv))
        print_line("")
        nic_names = list(pnic_after.keys())
        nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
        for name in nic_names:
            if name == 'lo':
                continue
            stats_before = pnic_before[name]
            stats_after = pnic_after[name]
            templ = "%-15s %15s %15s"
            print_line(templ % (name, "TOTAL", "PER-SEC"), highlight=True)
            print_line(templ % (
                "bytes-sent",
                convert_size(stats_after.bytes_sent),
                convert_size(
                    stats_after.bytes_sent - stats_before.bytes_sent) + '/s',
            ))
            print_line(templ % (
                "bytes-recv",
                convert_size(stats_after.bytes_recv),
                convert_size(
                    stats_after.bytes_recv - stats_before.bytes_recv) + '/s',
            ))
            print_line(templ % (
                "pkts-sent",
                stats_after.packets_sent,
                stats_after.packets_sent - stats_before.packets_sent,
            ))
            print_line(templ % (
                "pkts-recv",
                stats_after.packets_recv,
                stats_after.packets_recv - stats_before.packets_recv,
            ))
            print_line("")
        win.refresh()
        lineno = 0
    currnet_data = 0
    win.clear()
    while True:
        try:
            args = poll(currnet_data)
            refresh_window(*args)
            currnet_data = 1
        except (KeyboardInterrupt, SystemExit):
            win.refresh()
            break
        except Exception as e:
            print(e)
            win.refresh()
            break
    curses.endwin()


if __name__ == '__main__':
    network_stat()

# 반드시 psutil을 설치 후 구동해주세요.
# psutil 모듈을 통해서 테스트로 network_stat에 대한 결과값 입니다.
# 결론적으로 Code를 보시면 아시겠지만 핵심 Code는 116번줄 ~ 128번줄 입니다.
# 기다리실까봐 우선 빠르게 대략적으로 짜서 전달 드립니다.
# 추후에 다시 정리 할꺼구요, 해당 페이지도 우선적으로 내려놓을껍니다.