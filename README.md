# pymail

PyMail is a python wrapper that can be use to send beautiful email in any python base application. it allow developers to pass in their html template and the wrapper will render it and send the beautiful template out the reciepient. 

                                            DOCUMENTATION

INSTALLATION

We have to install the library into our virtual environment and we can do that by using the below command.

        pip install pymail

or

        pip3 install pymail


USAGE

After Installation, we need to create a directory in our project and name it "template" and then create another directory called "email" which will house all our html email files. ie

          project directory -> template -> email -> email html files


THEN

import all the functions

                      from email_client.pymail import clients, Email

Supply all the SMTP credentials that will be used to send the email out.

                      credential = clients(
                            email_host='smtp.gmail.com',
                            email_port='587',
                            email_user='sam.ilemobayo@gmail.com',
                            email_pass='Victoria@1992',
                            email_protocol='TLS',
                            email_sender='sam.ilemobayo@gmail.com'
                        )


                      send = Email()

Declare your HTML Template

                      html = 'templatename.html'

Load the HTML Template in the function and pass in the data you want to pass to the html template from python as a dictionary. 


                      template_data = send.load_template(html, {'name':'samson', 'amount':'1000'})

In our html template, we can now get the value of the data passed from python by using the the jinja2 pattern. ie 
                        {{name}} {{amount}}

Then we can now call the function to send the email by using the below function.

SEND WITHOUT ATTACHED FILE

                      send.sendEmail(
                        credential, 
                        template_data, 
                        receiver_email='reciever@gmail.com', 
                        subject="Python Test", 
                        bcc='test@gmail.com, test2@gmail.com'
                        )


SEND EMAIL WITH ATTACHED FILE

                      send.sendEmailWithFile(
                        credential, 
                        template_data, 
                        subject="Python Test", 
                        receiver_email='reciever@gmail.com',
                        pathToFile='path to file/Report.pdf', 
                        docName='test', 
                        bcc='test@gmail.com, test2@gmail.com'
                        )


NOTE

If you dont want to use bcc, kindly set it to None. ie *bcc=None.
        