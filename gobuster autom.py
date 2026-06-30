import subprocess

print('Gobuster - Directory research tool')

url = input('URL: ').strip()
wordlist = input('Wordlist: ').strip()

print('Running Gobuster...')

command = [
    'gobuster', 
    'dir',
    '-u', url, 
    '-w', wordlist
]

subprocess.run(command)


