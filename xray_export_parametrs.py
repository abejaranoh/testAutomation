import requests

test_execution_key  = 'ABC-123'
test_key            = 'ABC-456' # dummy test key
parameter_file = 'dataset_parameters_xyz.csv'
auth_token = 'T1a2O3b4K5c6E7d8N'
jira_url = 'https://server/jira'

def get_tests(test_execution_key,auth_token):

    url = jira_url+'/rest/raven/1.0/api/testexec/'+test_execution_key+'/test'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        for test in data:
            export_parametrs(test['key'],test_execution_key,auth_token)
            print(test['key']+' is exported')
    else:
        print('Request failed with status code:', response.status_code)

def export_parametrs(test_key,test_execution_key,auth_token):

    url = jira_url+'/rest/raven/2.0/api/dataset/export'
    params = {
        'testIssueKey': test_key,      # Test
        'contextIssueKey': test_execution_key
    }
    headers = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.get(url, params=params, headers=headers)
    print(response.status_code)
    print(response.text)
    f=open('dataset_'+test_execution_key+'_'+test_key+'.csv','w')
    f.write(response.text)
    f.close()

#export_parametrs(test_key,test_execution_key,auth_token)
get_tests(test_execution_key,auth_token)
