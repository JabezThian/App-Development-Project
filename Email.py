import smtplib, passGenerate

# Sender email address (Mine)
gmail_user = 'appdevproject9@gmail.com'
gmail_password = 'p@ssword1234'


def Email(email, first_name, last_name):
    sent_from = gmail_user
    to = email
    subject = 'Queensway Shopping Center: Forgot Password'
    new_password = passGenerate.new_pass()
    body = 'Dear {} {},\n\nYour new password is {}. \nPlease Change your Password as soon as you login.'.format(first_name, last_name, new_password)

    email_text = "Subject: {}\n\n{}".format(subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('For Programmer: SUCCESS --> Email sent!')
        return new_password
    except Exception as e:
        # e is the error of not sending the email
        print('For Programmer: ERROR --> Email was not sent! ')
        print(e)
