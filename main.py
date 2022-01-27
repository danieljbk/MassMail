import os
import smtplib
from datetime import datetime
from email.message import EmailMessage


def absolute_path(path):  # input relative path, output absolute path
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)


def personalize_script(name):
    with open(absolute_path('script/title.txt')) as title_text:
        fetched_title = title_text.readline().strip()
        fetched_title = fetched_title.split("{name}")
    title_text.close()
    
    with open(absolute_path('script/body.txt')) as body_text:
        fetched_body = "".join(body_text.readlines()).strip()
        fetched_body = fetched_body.split("{name}")
    body_text.close()
    
    fetched_title = fetched_title[0] + name + fetched_title[1]
    fetched_body = fetched_body[0] + name + fetched_body[1]

    return fetched_title, fetched_body


def gather_personal_data():  # from relative path assets/private
    GMAIL_USERNAME = open(absolute_path(
        "assets/personal/gmail_username.txt"), "r").readline().strip()
    GMAIL_API_KEY = open(absolute_path(
        "assets/personal/gmail_app_password.txt"), "r").readline().strip()

    return GMAIL_USERNAME, GMAIL_API_KEY


def gather_subscriber_data(subscription_type):
    path = absolute_path("assets/")
    path += "/" + subscription_type

    f = open(path, "r")
    subscribers = f.read().split("\n")
    f.close()

    # filter empty strings
    subscribers = list(filter(lambda item: item, subscribers))
    subscribers = list(map(lambda x: x.split(","), subscribers))

    return subscribers


def send():  # most important: for sending the email
    print(f"\nSending...\n")

    GMAIL_USERNAME, GMAIL_API_KEY = gather_personal_data()
    email_subscribers = gather_subscriber_data("subscribers.csv")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(GMAIL_USERNAME, GMAIL_API_KEY)

    for data in email_subscribers:
        name = data[0]
        email_address = data[1]
        title, body = personalize_script(name)
        
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = title
        msg['to'] = email_address
        msg['from'] = GMAIL_USERNAME

        server.send_message(msg)
        print("    " + "- sent to:", data[1])
    
    server.quit()
    print(f"\nSuccess!\n")


if input(f"Send {len(gather_subscriber_data('subscribers.csv'))} emails? (Y/N)\n") == "Y":
    send()
else:
    print("Understood.")
