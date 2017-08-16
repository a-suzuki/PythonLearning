def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
    else:
        response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    return response

with open('pybot.txt', encoding='utf-8') as open_file:
    raw_data = open_file.read()

lines = raw_data.splitlines()
bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    if '平成' in command:
        response = heisei_command(command)
    if not response:
        response = '何ヲ言ッテイルカ、ワカリマセン'
    print(response)

    if 'さようなら' in command:
        break
