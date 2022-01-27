# MassMail
Send Emails en Masse with Personalized Scripts.

## Rules for Writing the Script:

- You must include "{name}" as a placeholder inside your title and body.
  - Example: Hello {name}!

- You must include it **once** for each.

- As of now, the only customizable value is the name.

## Prerequisites:

Before using MassMail, you must complete these two steps:
- Create Google App Password - https://myaccount.google.com/security
    1. Turn on 2-Step Verification
    2. Create 'App Password'

Then, you must type this information in:
- assets/personal/gmail_app_password.txt

You must also type your Gmail address in:
- assets/personal/gmail_username.txt

## Subscriber Data:
1. Use Google Sheets or Excel
2. First column should be name, second column should be email
3. Download as .csv (comma-separated-values)
4. Name the file "subscribers.csv"
5. Place the file inside the assets folder
