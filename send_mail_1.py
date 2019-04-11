import smtplib

import urllib.request

import requests

import urllib

from io import BytesIO, StringIO

import webbrowser

from string import Template

from PIL import Image

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.image import MIMEImage

MY_ADDRESS = 'koushiknallapuneni@gmail.com'

PASSWORD = 'password'

dataset_dir = r"C:\Users\MyPC\Downloads\face-recognition-opencv\face-recognition-opencv\dataset"

def get_contacts(mycontacts):
    """

    Return two lists names, emails containing names and email addresses

    read from a file specified by filename.

    """

    names = []

    emails = []

    with open(mycontacts, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])

            emails.append(a_contact.split()[1])

    return names, emails


def read_template(message):
    """

    Returns a Template object comprising the contents of the

    file specified by filename.

    """

    with open(message, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)


def main():
    names, emails = get_contacts('mycontacts.txt')  # read contacts

    message_template = read_template('message1.txt')

    # set up the SMTP server

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)

    s.starttls()

    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:

    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template

        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake

        print(message)

        # setup the parameters of the message

        msg['From'] = MY_ADDRESS

        msg['To'] = email

        msg['Subject'] = "SECURITY ALERT!!!"

        # add in the message body
        filename = "p1.jpg"

        fp = open(filename, 'rb')
        img = MIMEImage(fp.read())

        imgurl = MIMEText(
            '<b>URL <i>image</i> </b> <br><img src="https://lumiere-a.akamaihd.net/v1/images/eu_frozen_gt_rush_r_f17ace62.jpeg"><br>',
            'html')

        # imgurl=MIMEImage(urllib.request.urlopen('https://lumiere-a.akamaihd.net/v1/images/eu_frozen_gt_rush_r_f17ace62.jpeg'))

        fp.close()
        # sending text
        msg.attach(MIMEText(message, 'plain'))
        # senging image
        msg.attach(img)
        # sending img url
        ##msg.attach(imgurl)

        # send the message via the server set up earlier.

        s.send_message(msg)
        # s.sendPhoto(msg,'https://lumiere-a.akamaihd.net/v1/images/eu_frozen_gt_rush_r_f17ace62.jpeg')

        del msg

    # Terminate the SMTP session and close the connection

    s.quit()


if __name__ == '__main__':
    main()
