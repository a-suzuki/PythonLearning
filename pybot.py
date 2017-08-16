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
    if not response:
        response = '何ヲ言ッテイルカ、ワカリマセン'
    print(response)

    if 'さようなら' in command:
        break
