import xml.etree.ElementTree as ET

def parseXml(xmlfile):
    
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for value in root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body'):
            for arrayType in value.findall('Event'):
                for event in arrayType.findall('EventStruct'):
                    for eventCode in event.findall('EventCode'):
                        print eventCode.text
            for param in value.findall('ParameterList'):
                for paramvalue in param.findall('ParameterValueStruct'):
                        if paramvalue[0].text ==  'Device.LAN.IPAddress':
                            print paramvalue[1].text
                            
                        
            
parseXml('practice2.xml')
          

    

