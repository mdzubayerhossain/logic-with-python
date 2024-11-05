# import libraries to make get request
import requests
import json
import datetime
import csv
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN1')
print(TOKEN)
CHANNEL_ID = '1126873503354859711'

# your API Key goes here (see README.md on how to find out your own api key)
h = {'authorization': TOKEN} #ENTER KEY HERE




authorID = '1118414985815670795'
before = '1205573831884800000'
after = '1180206681292800000'

def get_message_from_channel(channel_id,author_id,befor,after):
    r = requests.get('https://discord.com/api/v9/guilds/1126873502381768816/messages/search?author_id='+ author_id + '&max_id=' + before + '&min_id='+after+ '',headers=h)
    j = json.loads(r.text)
    return j['messages']


def save_messages_to_csv(output_data, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Content', 'Author Username', 'Message Date'])
        
        for messages_list in output_data:
            for message in messages_list:
                content = message['content']
                author_username = message['author']['username']
                message_date = datetime.datetime.strptime(message['timestamp'], "%Y-%m-%dT%H:%M:%S.%f+00:00").strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([content, author_username, message_date])


