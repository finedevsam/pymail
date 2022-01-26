import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import pathlib
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader


"""Declare function to get Email configuration"""
def clients(email_host, email_port, email_user, email_pass, email_protocol, email_sender):
    if email_protocol is not "SSL":
        print("Email Protocol must be either SSL or TLS")
        return False
    else:
        data = {
            "host": email_host,
            "port": email_port,
            "username": email_user,
            "password": email_pass,
            "protocol": email_protocol,
            "sender": email_sender
        }
        return data



class EmailBackEnd:
    
    env = Environment(
        loader=PackageLoader('template', 'email'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    def sendEmail(self, credential, html, receiver_email, subject):
        d = self.env.get_template(html)
        # data = clients()
        template = d.render({
            'name':'samson',
            'amount': '1000'
        })
        msg = MIMEMultipart()
        msg['From'] = credential['sender']
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(template, 'html'))

    
        # msg.attach(part)

        try:
            server = smtplib.SMTP(credential['host'], int(credential['port']))
            server.ehlo()
            server.starttls()
            server.login(credential['username'], credential['password'])
            text = msg.as_string()
            server.sendmail(credential['sender'], receiver_email, text)
            print('email sent')
            server.quit()
        except:
            print("SMPT server connection error")
        return True


    def sendEmailWithFile(self, credential, template, subject, receiver_email, pathToFile, docName):
        
        # data = clients()
        username = credential['username']
        password = credential['password']
        port = credential['port']
        host = credential['host']

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = credential['sender']
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(template, "html"))

        # filename = './cv.pdf'  # In same directory as script

        # Open PDF file in binary mode
        with open(pathToFile, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        file_extension = pathlib.Path(pathToFile).suffix
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {docName}{file_extension}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        # context = ssl.create_default_context()
        try:
            if credential['protocol'] == "TLS":
                with smtplib.SMTP(host, port) as server:
                    server.login(username, password)
                    server.sendmail(credential['sender'], receiver_email, text)
                    server.quit()
            else:
                with smtplib.SMTP_SSL(host, port) as server:
                    server.login(username, password)
                    server.sendmail(credential['sender'], receiver_email, text)
                    server.quit()
                    
            print('email sent')
        except:
            print("SMPT server connection error")
        return True