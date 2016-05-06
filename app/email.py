from flask import current_app, render_template, redirect
from flask.ext.mail import Message
from threading import Thread
from app import mail

def send_mail_conc(app, msg):
    '''Uses a worker thread to send mail
    '''
    with app.app_context():
        mail.send(msg)


def send_email(sender, to, subject, template, **kwargs):
    print 'Sending mail'
    app = current_app._get_current_object()
    msg = Message(app.config['PAIRPROGRAM_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=sender, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_mail_conc, args=[app, msg])
    thr.start()
    return thr