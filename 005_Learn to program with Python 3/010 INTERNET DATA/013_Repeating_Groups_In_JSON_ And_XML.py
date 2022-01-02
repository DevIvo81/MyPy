import os
os.system('cls')

# Demonstration of repeating blocks in JSON and XML

import json
import xml.etree.ElementTree as etree

# Build a JSON structure as a triple quoted string

myJson = '''{
    "bandMembers" : [
        {
        "name" : "Keith Emerson",
        "age" : 32,
        "instrument" : "keyboards"
        },
        {
        "name" : "Greg Lake",
        "age" : 42,
        "instrument" : "guitar"
        },
        {
        "name" : "Carl Palmer",
        "age" : 35,
        "instrument" : "drums"
        }
    ]
}'''

bandMembersDict = json.loads(myJson)

membersList = bandMembersDict['bandMembers']

print('\nPrint from JSON\n')

for member in membersList:
    print(member['name'], member['age'], member['instrument'])
    
# Build a XML structure as a triple quoted string

myXML = '''
<bandMembers>
    <member>
           <name>Keith Emerson</name>
           <age>32</age>
           <instrument>keyboards</instrument>
    </member>
    <member>
           <name>Greg Lake</name>
           <age>42</age>
           <instrument>guitar</instrument>
    </member>
    <member>
           <name>Carl Palmer</name>
           <age>35</age>
           <instrument>drums</instrument>
    </member>
</bandMembers>'''

tree = etree.fromstring(myXML)
bandMembersList = tree.findall('member')

print('\nPrint from XML\n')

for member in bandMembersList:
    print(member.find('name').text, member.find('age').text, \
            member.find('instrument').text)

print()