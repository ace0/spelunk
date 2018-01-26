# JSON Spelunking

Quickly find the path to a target key or value in deeply nested structures or JSON.

Example:
```
$ python3 spelunk.py IpOwnerId sample.json

structure['NetworkInterfaces'][0]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][0]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][2]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][3]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][4]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][5]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][6]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][7]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][8]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][9]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][10]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][11]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][12]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][13]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][14]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][15]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][16]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][17]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][18]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][19]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][20]['Association']['IpOwnerId'] == 12001200120079
structure['NetworkInterfaces'][2]['PrivateIpAddresses'][21]['Association']['IpOwnerId'] == 12001200120079
```