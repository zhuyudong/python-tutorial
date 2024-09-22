import time
from datetime import datetime, timedelta

d = datetime.now()

# NOTE: 0-6, 0 is Monday
print(d.weekday()) # 0
print(d.isoweekday()) # 1
print(d.isoformat()) # 2024-09-09T22:28:12.590360
print(d.date()) # 2024-09-09
print(d.time()) # 22:28:12.590360
print(d.timetz()) # 22:28:12.590360
# NOTE: replace 是一个替换方法, 用于替换时间的某个部分,
print(d.replace(year=2021)) # 2021-09-09T22:28:12.590360

print(d.now()) # 2024-09-09 22:28:12.590438
print(d.combine(d.date(), d.time())) # 2024-09-09 22:28:12.590360

print(d.strftime('%Y-%m-%d %H:%M:%S')) # 2024-09-09 22:28:12
print(d.strftime('%Y-%m-%d %H:%M:%S %p')) # 2024-09-09 22:28:12 PM
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z')) # 2024-09-09 22:28:12 PM
print(d.strftime('%Y-%m-%d %H:%M:%S %p %z')) # 2024-09-09 22:28:12 PM +0000
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z')) # 2024-09-09 22:28:12 PM UTC +0000
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j')) # 2024-09-09 22:28:12 PM UTC +0000 189
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U')) # 2024-09-09 22:28:12 PM UTC +0000 189 27
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x %X')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020 15:00:00
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x %X %f')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020 15:00:00 000000
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x %X %f %z')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020 15:00:00 000000 +0000
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x %X %f %z %Z')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020 15:00:00 000000 +0000 UTC
print(d.strftime('%Y-%m-%d %H:%M:%S %p %Z %z %j %U %W %w %a %A %b %B %c %x %X %f %z %Z %Z')) # 2024-09-09 22:28:12 PM UTC +0000 189 27 27 1 Tue Tuesday Jul July Tue Jul  7 15:00:00 2020 15:00:00 000000 +0000 UTC UTC


# NOTE: timedelta 是一个时间差 #
# NOTE: 加减时间
print(d + timedelta(days=1)) # 2024-09-10 22:28:12.590360
print(d + timedelta(days=-1)) # 2024-09-08 22:28:12.590360

print(time.time()) # 1725894028.562954
# NOTE: 暂停 1 秒
time.sleep(1)
print(time.localtime()) # time.struct_time(tm_year=2024, tm_mon=9, tm_mday=9, tm_hour=23, tm_min=0, tm_sec=29, tm_wday=0, tm_yday=253, tm_isdst=0)

# NOTE: 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) # 2024-09-09 23:00:29

# NOTE: 测量时间
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print(f"execution time: {end - start} seconds") # execution time: 0.015625 seconds