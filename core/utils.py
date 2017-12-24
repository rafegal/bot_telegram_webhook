import requests
TOKEN = '124348504:AAGdo3bBtuQBz3r7_hjiFvNxqwbNc39owNs'

from core.models import Interaction

def process_message(command):
    interaction = Interaction.objects.get(input=command)
    if interaction.execute_script:
        dic = interaction.execute()
        output = interaction.get_output(dic)
    else:
        output = interaction.output
    return output

def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
    print response.content