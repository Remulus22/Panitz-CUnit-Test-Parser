import xml.etree.ElementTree as ET

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tree = ET.parse('cunit_results.xml')
root = tree.getroot()


tests = root.findall('testcase')
passedTests = 0

print("\n")
for test in tests:
    
    testResult = not test.find("success") is None
    print((bcolors.OKGREEN if testResult else bcolors.FAIL)+ test.attrib.get('name'))

    if testResult: 
        passedTests += 1
    else:
        message = test.find("failure").attrib.get("message")
        print(bcolors.FAIL + f'^^^^^{message}')

summaryColor = None

if passedTests == len(tests):
    summaryColor = bcolors.OKGREEN
elif passedTests >= len(tests)/2:
    summaryColor = bcolors.WARNING
else:
    summaryColor = bcolors.FAIL

print(summaryColor + f'{passedTests}/{len(tests)} tests passed.')