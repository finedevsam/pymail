from email_client.pymail import clients, Email



credential = clients(
    email_host='smtp.mailtrap.io',
    email_port='2525',
    email_user='38c207b30aaed1',
    email_pass='268069f96f1e35',
    email_protocol='TLS',
    email_sender='test@gmail.com'
)


send = Email()

### Send email ##
html = 'a.html'
template_data = send.load_template(html, {'name':'samson', 'amount':'1000'})
send.sendEmail(credential, template_data, receiver_email='samson@gmail.com', subject="Good Job")