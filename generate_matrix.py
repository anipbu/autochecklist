import urllib2
import re

data = urllib2.urlopen("https://meetings.opendaylight.org/opendaylight-integration/2018/testmeeting/opendaylight-integration-testmeeting.2018-02-26-22.48.log.txt")
for line in data:
    match = re.search(r'#project (\w+)', line)
    if match:
        print match.group(1)
