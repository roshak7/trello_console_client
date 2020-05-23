import sys
import requests


auth_params = {
    'key': "c0cbb24cd2ed66ad9a2f54ca36964a42",
    'token': "bda38c00ad831478e115e39c0e423426d9f7320f6a739c1a0ff109bcecadd45b",
}

base_url = "https://api.trello.com/1/{}"

board_id = "tZLvry3S" 

def read():
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    for column in column_data:
         print(column['name'])
    
         task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()

         if not task_data:
            print('\t' + 'Нет задач!')
            continue
         for task in task_data:
             print('\t' + task['name'])

def create(name, column_name):
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    for column in column_data:
        if column['name'] == column_name:
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

def move(name, column_name):
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    task_id = None
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        for task in column_tasks:
            if task['name'] == name:
                task_id = task['id']
                break
        if task_id:
            break

    for column in column_data:
        if column['name'] == column_name:
             requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})
             break       
if __name__ == "__main__":
    if len(sys.argv) <= 2:
        read()
    elif sys.argv[1] == 'create':    
        create(sys.argv[2], sys.argv[3])    
    elif sys.argv[1] == 'move':    
        move(sys.argv[2], sys.argv[3])  