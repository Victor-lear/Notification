# -*- coding: utf-8 -*-
"""
@author: victor
"""
import sys
sys.path.append("..")

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer
import catch_data
import time
import datetime
nodeID="6c7bc2fa-aa56-4bfd-aee3-cf622c87e937"
apiURL="https://api-dccs-ensaas.education.wise-paas.com/"
CredentialKEY="d5dc9053a29c4e740180665753cfb4ci"
edgeAgentOptions = EdgeAgentOptions(nodeId = nodeID)#nodeID
edgeAgentOptions.connectType = constant.ConnectType['DCCS']
dccsOptions = DCCSOptions(apiUrl = apiURL, credentialKey = CredentialKEY)
edgeAgentOptions.DCCS = dccsOptions
_edgeAgent = EdgeAgent(edgeAgentOptions)
_edgeAgent.connect()


#creat data connect

def creatdataconnect(_edgeAgent,data):
    config = __generateConfig(data)
    _edgeAgent.uploadConfig(action = constant.ActionType['Create'], edgeConfig = config)
def __generateConfig(data):
    config = EdgeConfig()
    nodeConfig = NodeConfig(nodeType = constant.EdgeType['Gateway'])
    config.node = nodeConfig
    for i in range(1):
        deviceConfig = DeviceConfig(id = 'Pingcheck',
          name = 'Pingcheck',
          description = 'Pingcheck',
          deviceType = 'Smart Device',
          retentionPolicyName = '')
        for j in range(len(data)):
            analog = AnalogTagConfig(name = data[j]['ap_name'],
                description = data[j]['ap_ip_address'],
                readOnly = False,
                arraySize = 10,
                spanHigh = 1000,
                spanLow = 0,
                engineerUnit = '',
                integerDisplayFormat = 4,
                fractionDisplayFormat = 2)
            deviceConfig.analogTagList.append(analog)
              
            
        config.node.deviceList.append(deviceConfig)
    return config    
def exe_create_pingcheck(url,DB,Collection):
    data=catch_data.nowdata(url,DB,Collection)
    creatdataconnect(_edgeAgent,data)
url="mongodb://admin:bmwee8097218@140.118.122.115:30415/"
DB="AP_test"
Collection="Controller4"
exe_create_pingcheck(url,DB,Collection)