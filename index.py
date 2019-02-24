from model.file2Dict import File2Dict
from model.diafaanDao import DiafaanDao
import requests,urllib,datetime,json


# Read configuration file.
try:
    config = File2Dict.read("config.json")
except FileNotFoundError as e:
    exit(e)


# Method
method_request = config['request']['method'].upper()

# Prepare request
if method_request == "POST":
    response = requests.post(url=config['request']['url'],data=config['request']['param'])
elif method_request == "GET":
    response = requests.get(url=config['request']['url'] + urllib.parse.urlencode(config['request']['param']))
else:
    exit("Sorry, this method has not been implemented yet. Use only the GET and POST methods. :) ")


if response.status_code != 200:
    exit("Expected code 200.")

# Check for success.
if response.text.find(config['successString']) == -1:
    exit("Success indicator string could not be found.")

try:
    data = json.loads(response.text)
except json.JSONDecodeError as e:
    exit(e)


payload = data[config['payloadName']]

if not isinstance(payload,list):
    exit("A list was expected.")

# Establish connection to the database.
diafaanDao = DiafaanDao(**config['database'])

for msg in payload:
    # Converts date supplied to format expected by diafaan.
    sendTime = datetime.datetime.strptime(msg[config['expectedResponseParameters']['sendTime']],config['expectedResponseParameters']['formatDate']).strftime("%Y-%m-%d %H:%M:%S")
    sms_from = msg[config['expectedResponseParameters']['from']]
    if len(config['expectedResponseParameters']['to']) > 0:
        sms_to = msg[config['expectedResponseParameters']['to']] # optional
    else:
        sms_to = ""
    sms_text = msg[config['expectedResponseParameters']['text']]

    # Saves information in the diafaan database.
    result = diafaanDao.insert_answer(database_table=config['databaseTableTarget'],\
                             time=sendTime,\
                             sms_from=sms_from,\
                             sms_to=sms_to,\
                             sms_text=sms_text)

    if result:
        print("Response inserted in the diafaan database.")
    else:
        print("Something went wrong.")

