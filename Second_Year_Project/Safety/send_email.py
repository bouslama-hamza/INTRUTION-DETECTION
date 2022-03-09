import smtplib
import random

def send_email():
    EMAIL_ADDRESS = 'test.herbaly@gmail.com'
    EMAIL_PASSWORD = 'badBOY@2020'
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        n = random.randint(11111111,99999999)
        subject = 'Request To change Password'
        body = 'Your request to change your password has been added successfuly please use the following code to access : \n'+str(n)
        msg = f'Subject : {subject} \n\n {body}'
        smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)
        return n