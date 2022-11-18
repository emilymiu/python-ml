import socket

def is_running(website):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((website, 80))
        return True
    except:
        return False

if __name__ == '__main__':
    while True:
        website = input('Please enter website to check: ')
        if is_running(f'{website}.com'):
            print(f'{website}.com is running!')
        else:
            print(f'There is an error with {website}.com')
        if input('Would you like to check another website? (Y/N)') in {'n', 'N'}:
            break

