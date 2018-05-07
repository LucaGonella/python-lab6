import requests
import json


def print_tasks_from_server():
    '''
    Get the list of tasks from the server in JSON
    '''

    #get JSON from server
    resp = requests.get('http://127.0.0.1:5000/api/v1.0/tasks')
    if resp.status_code != 200:
        print("Error: the list of tasks is not available at this moment.")
    else:
        #for each element in tasks we print the content
        for task in json.loads(resp.text)['tasks']:
            print(task['description'] + " " +str(task['urgent']))


if __name__ == '__main__':
    # main program
    print_tasks_from_server()