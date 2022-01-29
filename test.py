from email_client.pymail import clients, Email



credential = clients(
    email_host='smtp.gmail.com',
    email_port='587',
    email_user='',
    email_pass='',
    email_protocol='TLS',
    email_sender=''
)


send = Email()

### Send email ##
html = 'a.html'
template_data = send.load_template(html, {'name':'samson', 'amount':'1000'})
# send.sendEmail(credential, template_data, receiver_email='', subject="Good Job", bcc=',')
send.sendEmailWithFile(credential, template_data, subject="Good Job", receiver_email='',pathToFile='/Users/apple/Documents/Report.pdf', docName='test', bcc=',')