import time
from datetime import datetime as dt

hosts_temp = 'hosts'
hosts_path = '/etc/hosts'
redirect = '0.0.0.0'
blocked_websites = ['facebook.com', 'www.facebook.com', 'delfi.lt', 'www.delfi.lt']
starting_hours = dt(dt.now().year, dt.now().month, dt.now().day, 8)
ending_hours = dt(dt.now().year, dt.now().month, dt.now().day, 17)

while True:
    if starting_hours < dt.now() < ending_hours:
        print('Productive hours...')
        with open(hosts_temp, 'r+') as file:
            hosts_content = file.read()
            for site in blocked_websites:
                if site in hosts_content:
                    pass
                else:
                    file.write('{0} {1}\n'.format(redirect, site))
    else:
        print('Relax hours...')
        with open(hosts_temp, 'r+') as file:
            hosts_content = file.readlines()
            file.seek(0)
            for line in hosts_content:
                if not any(site in line for site in blocked_websites):
                    file.write(line)
            file.truncate()
    time.sleep(15)
