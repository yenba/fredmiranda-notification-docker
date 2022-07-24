import psycopg2
import json
import argparse
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT  # <-- ADD THIS LINE
from pushoverSend import sendPushover

# setup the argument parser
parser = argparse.ArgumentParser(description="This is how you pass Pushover API keys into the script!",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--apikey", help="Pushover API Key")
parser.add_argument("--userkey", help="Pushover User Key")
parser.add_argument("--dbname", help="Database Name")
parser.add_argument("--dbuser", help="Database Username")
parser.add_argument("--dbpass", help="Database Password")
parser.add_argument("--dbhost", help="Database Host")
parser.add_argument("--dbport", default=5432, help="Database Port number")
args = vars(parser.parse_args())

# Set up parameters
apikey = args["apikey"]
userkey = args["userkey"]
dbname = args["dbname"]
dbuser = args["dbuser"]
dbpass = args["dbpass"]
dbhost = args["dbhost"]
dbport = args["dbport"]

# declare connection to database
connection = psycopg2.connect(dbname=dbname, user=dbuser, host=dbhost, port=dbport, password=dbpass)

# listen to channel
def db_listen():
    # set to autocommit
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = connection.cursor()
    cur.execute("LISTEN new_item_added;")
    while True:
        # select.select([connection],[],[])   #sleep until there is some data
        connection.poll()  # get the message
        while connection.notifies:
            notification = connection.notifies.pop()  # pop notification from list
            # now do anything needed!
            fred = notification.payload
            fredJSON = json.loads(fred)
            postID = fredJSON["post_id"]
            postTitle = fredJSON["post_title"]
            postURL = fredJSON["post_URL"]
            title = "New Fred Miranda Item"
            url = postURL
            poMessage = str(postID) + " - " + postTitle
            print(poMessage)
            sendPushover(apikey,userkey,poMessage,title,url)           
            print(f"channel: {notification.channel }")
            print(f"message: {notification.payload}")


db_listen()
