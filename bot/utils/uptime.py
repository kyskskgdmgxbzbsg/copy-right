import time

def get_uptime(start_time):
    seconds = int(time.time() - start_time)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    uptime = f"{d}d {h}h {m}m {s}s"
    return uptime