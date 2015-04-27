from fabric.api import local

def backup():
    '''
    Function to simple git commands
    '''
    local('git pull')
    local('git add .')
    
print('Enter your comment: ')
comment = raw_input()
local('git commit -m "%s"' % comment)

local('git push')

def deploy():
    '''
    
    '''
    local('pip freeze > requirements.txt')
    local('git pull')
    local('git add .')

    local('Enter your commit comment: ')
    comment = raw_input()
    local('git commit -m "%s"' % comment)

    local('git push')
