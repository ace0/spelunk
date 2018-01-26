"""
Tests: run with `pytest`
"""
from spelunk import *

def testSearchTopLevelKey():
	assert(search('ImageId', sampleStructure) == ["structure['ImageId'] == ami-ace0ace0"])

def testSearchNestedValue():
	assert(search("buried subnet", sampleStructure) == ["structure['NetworkInterfaces'][3]['SubnetId'] == buried subnet"])

def testSearchMultiKeyCount():
	assert(len(search("PrivateIpAddress", sampleStructure)) == 32)

def testSearchInt():
	assert(search(16, sampleStructure) == ["structure['State']['Code'] == 16"])

def testSearchMissing():
	assert(search(128, sampleStructure) == [])
	assert(search("Not found", sampleStructure) == [])
	assert(search("PrivateDns", sampleStructure) == [])

def testPrintJson():
	from json import dumps
	print(dumps(sampleStructure))
	assert(False)

sampleStructure = {
    'AmiLaunchIndex': 0,
    'ImageId': 'ami-ace0ace0',
    'InstanceId': 'i-19791979',
    'InstanceType': 'c1.xlarge',
    'KeyName': '21jumpstreet',
    'LaunchTime': "2012-04-07",
    'Monitoring': {
        'State': 'disabled'
    },
    'Placement': {
        'AvailabilityZone': 'us-east',
        'GroupName': '',
        'Tenancy': 'default'
    },
    'PrivateDnsName': 'ip-10-10-10-10.ec2.internal',
    'PrivateIpAddress': '10.10.10.10',
    'ProductCodes': [{
        'ProductCodeId': '---ace0---ace0',
        'ProductCodeType': 'marketplace'
    }],
    'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
    'PublicIpAddress': '55.55.55.55',
    'State': {
        'Code': 16,
        'Name': 'running'
    },
    'StateTransitionReason': '',
    'SubnetId': 'subnb12b12b12b12b12',
    'VpcId': 'vpc-ccceeff',
    'Architecture': 'x86_64',
    'BlockDeviceMappings': [{
        'DeviceName': '/dev/xvda',
        'Ebs': {
            'AttachTime': "2010-05-18",
            'DeleteOnTermination': False,
            'Status': 'attached',
            'VolumeId': 'vol-1979881979'
        }
    }],
    'ClientToken': '144-1212121212-144',
    'EbsOptimized': False,
    'Hypervisor': 'xen',
    'IamInstanceProfile': {
        'Arn': 'arn:aws:iam::--------:instance-profile/profile-a',
        'Id': 'ACE000000000000ACE0'
    },
    'NetworkInterfaces': [{
        'Association': {
            'IpOwnerId': '12001200120079',
            'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
            'PublicIp': '55.55.55.55'
        },
        'Attachment': {
            'AttachTime': "2010-05-18",
            'AttachmentId': 'eni-attach-8ffff8ffff8',
            'DeleteOnTermination': True,
            'DeviceIndex': 0,
            'Status': 'attached'
        },
        'Description': 'Primary network interface',
        'Groups': [{
            'GroupName': 'EW Management',
            'GroupId': 'sg-12345678901234'
        }],
        'Ipv6Addresses': [],
        'MacAddress': '12:12:12:12:12:12:c5',
        'NetworkInterfaceId': 'eni-c12c12c12',
        'OwnerId': '12001200120079',
        'PrivateDnsName': 'ip-10-10-10-10.ec2.internal',
        'PrivateIpAddress': '10.10.10.10',
        'PrivateIpAddresses': [{
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': True,
            'PrivateDnsName': 'ip-10-10-10-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }],
        'SourceDestCheck': True,
        'Status': 'in-use',
        'SubnetId': 'subnet-b12b12b12b12b12',
        'VpcId': 'vpc-ccceeff'
    }, {
        'Attachment': {
            'AttachTime': "2010-05-18",
            'AttachmentId': 'eni-attach-8ffff8ffff8',
            'DeleteOnTermination': False,
            'DeviceIndex': 1,
            'Status': 'attached'
        },
        'Description': 'PA HA Interface',
        'Groups': [{
            'GroupName': 'default',
            'GroupId': 'sg-12345678901234'
        }],
        'Ipv6Addresses': [],
        'MacAddress': '12:12:12:12:12:12:c5',
        'NetworkInterfaceId': 'eni-c12c12c12',
        'OwnerId': '12001200120079',
        'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
        'PrivateIpAddress': '10.10.10.10',
        'PrivateIpAddresses': [{
            'Primary': True,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }],
        'SourceDestCheck': True,
        'Status': 'in-use',
        'SubnetId': 'subnet-b12b12b12b12b12',
        'VpcId': 'vpc-ccceeff'
    }, {
        'Association': {
            'IpOwnerId': '12001200120079',
            'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
            'PublicIp': '55.55.55.55'
        },
        'Attachment': {
            'AttachTime': "2010-05-18",
            'AttachmentId': 'eni-attach-18ffff8ffff8',
            'DeleteOnTermination': False,
            'DeviceIndex': 2,
            'Status': 'attached'
        },
        'Description': 'East-West',
        'Groups': [{
            'GroupName': 'East-West Plane',
            'GroupId': 'sg-12345678901234'
        }],
        'Ipv6Addresses': [],
        'MacAddress': '12:12:12:12:12:12:c5',
        'NetworkInterfaceId': 'eni-c12c12c12',
        'OwnerId': '12001200120079',
        'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
        'PrivateIpAddress': '10.10.10.10',
        'PrivateIpAddresses': [{
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': True,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-10.10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Association': {
                'IpOwnerId': '12001200120079',
                'PublicDnsName': 'ec2-55-55-55-55.compute-1.amazonaws.com',
                'PublicIp': '55.55.55.55'
            },
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-0-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }],
        'SourceDestCheck': False,
        'Status': 'in-use',
        'SubnetId': 'subnet-b12b12b12b12b12',
        'VpcId': 'vpc-ccceeff'
    }, {
        'Attachment': {
            'AttachTime': "2010-05-18",
            'AttachmentId': 'eni-attach-8ffff8ffff8',
            'DeleteOnTermination': False,
            'DeviceIndex': 3,
            'Status': 'attached'
        },
        'Description': 'PA Inside Interface',
        'Groups': [{
            'GroupName': 'EW Data Plane',
            'GroupId': 'sg-12345678901234'
        }],
        'Ipv6Addresses': [],
        'MacAddress': '12:12:12:12:12:12:c5',
        'NetworkInterfaceId': 'eni-c12c12c12',
        'OwnerId': '12001200120079',
        'PrivateDnsName': 'ip-10-10-2-10.ec2.internal',
        'PrivateIpAddress': '10.10.10.10',
        'PrivateIpAddresses': [{
            'Primary': True,
            'PrivateDnsName': 'ip-10-10-2-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }, {
            'Primary': False,
            'PrivateDnsName': 'ip-10-10-2-10.ec2.internal',
            'PrivateIpAddress': '10.10.10.10',
        }],
        'SourceDestCheck': False,
        'Status': 'in-use',
        'SubnetId': 'buried subnet',
        'VpcId': 'vpc-ccceeff'
    }],
    'RootDeviceName': '/dev/xvda',
    'RootDeviceType': 'ebs',
    'SecurityGroups': [{
        'GroupName': 'EW Management',
        'GroupId': 'sg-12345678901234'
    }],
    'SourceDestCheck': True,
    'Tags': [{
        'Key': 'environment',
        'Value': 'production'
    }, {
        'Key': 'type',
        'Value': 'node'
    }, {
        'Key': 'cluster',
        'Value': 'nodeCluster'
    }, {
        'Key': 'island',
        'Value': 'nodeIsland'
    }, {
        'Key': 'Name',
        'Value': 'EW-Master-Group'
    }],
    'VirtualizationType': 'vtype'
}