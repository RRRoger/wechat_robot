# coding=UTF-8
import datetime
LOG_PATH = 'log'

def log(info, level="INFO"):
    print(info)
    now = datetime.datetime.now()
    with open('%s/log-%s.log' % (LOG_PATH, now.strftime("%Y%m%d")), 'a+') as f:
        f.write('%s %s    %s\n' % (now.strftime("%Y-%m-%d %H:%M:%S"), level, info))

log_info = lambda s: log(s, "INFO")
log_error = lambda s: log(s, "ERROR")
log_warn = lambda s: log(s, "WARNING")
