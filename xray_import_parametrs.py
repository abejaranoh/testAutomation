import requests

test_execution_key  = 'jira_test_execution_key'
test_key            = 'test_key' # dummy test key
parameter_file = 'dataset_ABC-123.csv'
auth_token = 'abcTOKEN123'
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
            import_parametrs(test['key'],test_execution_key,auth_token)
            print(test['key']+' is loaded')
    else:
        print('Request failed with status code:', response.status_code)


def import_parametrs(test_key,test_execution_key,auth_token):

    url = jira_url+'/rest/raven/2.0/api/dataset/import'
    params = {
        'testIssueKey': test_key,      # Test
        'contextIssueKey': test_execution_key
    }
    headers = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + auth_token
    }
    files = {
        'file': (parameter_file, open(parameter_file, 'rb'), 'application/vnd.ms-excel')
    }

    response = requests.post(url, params=params, headers=headers, files=files)
    print(response.status_code)

get_tests(test_execution_key,auth_token)










