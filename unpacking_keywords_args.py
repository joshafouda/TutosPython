############## Arguments Nommés variables ################

# 1. Présentation
def named(**kwargs):
    print(kwargs)

#named(name="Bob", age=25)

#named(name="Bob", age=25, activity="Data Scientist")

# 2. Cas concret d'utilisation
'''
def send_email(to, subject, **kwargs):
    print(f"To: {to}")
    print(f"Subject: {subject}")

    # Ajout des fonctionnalités pour cc et bcc
    if "cc" in kwargs:
        print(f"CC: {kwargs['cc']}")
    if "bcc" in kwargs:
        print(f"BCC: {kwargs['bcc']}")
'''
#send_email("user@example.com", "Meeting Reminder")



# 3. sans **kwargs
def send_email(to, subject, cc, bcc):
    print(f"To: {to}")
    print(f"Subject: {subject}")

    # Ajout des fonctionnalités pour cc et bcc
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")
'''
send_email(
       "user@example.com",
       "Meeting Reminder",
       cc="manager@example.com",
       bcc="team@example.com"
   )
'''

send_email("user@example.com", "Meeting Reminder")
