import requests
import hashlib
import sys



def req_api_data(query_char):
    url = 'http://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise ReferenceError(f'Error fetching : {res.status_code}, check this api and try again')
    return res

def get_pass_leak_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char , tail = sha1password[:5] , sha1password[5:]
    response = req_api_data(first5_char)
    #print(first5_char,tail)
    return get_pass_leak_count(response,tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times...you should make strong your password.')
        else:
            print(f'{password} was not not found.Carry on!')
    return 'done'


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))









