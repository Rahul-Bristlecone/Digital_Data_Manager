import smtplib
from Utilities import otp_generator

message = """
your OTP is """ + otp_generator.generate_otp()


def otp_extraction():
    otp = ""
    for i in message:
        if i.isdigit():
            otp += str(i)
    return otp


def send_email_otp(password, sender, receiver):
    try:
        server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")


# password = 'MTGrHWd3m61hZYFV'
# sender = 'rsshrma.92@gmail.com'
# receiver = 'tiffanyannf35@nresponsea.com'
# send_email_otp(password,sender,receiver)
