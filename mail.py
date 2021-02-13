import smtplib
def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("sairohith7050@gmail.com", "I@ulcww10os")
    s.sendmail("sairohith7050@gmail.com", "janasrihith@gmail,com", message)
    s.quit()