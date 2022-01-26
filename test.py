from email_client.pymail import clients, EmailBackEnd



credential = clients(
    email_host='smtp.mailtrap.io',
    email_port='2525',
    email_user='38c207b30aaed1',
    email_pass='268069f96f1e35',
    email_protocol='SSL',
    email_sender='test@gmail.com'
)


send = EmailBackEnd()

### Send email ##
html = 'a.html'

send.sendEmail(credential, html, receiver_email='samson@gmail.com', subject="hello")