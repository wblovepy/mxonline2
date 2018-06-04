from user.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from mxonline.settings import EMAIL_HOST,EMAIL_HOST_USER,EMAIL_FROM

def send_register_email(email, send_type ='register'):
    """先保存到数据库，方便发送后比对"""
    email_record = EmailVerifyRecord()
    random_str = generate_random_str(16)
    email_record.code =random_str
    email_record.email =email
    email_record.send_type =send_type
    email_record.save()
    email_title =''
    email_body =''

    if send_type =='register':
        email_title ="慕学在线网注册激活链接"
        email_body ="请点击下面链接激活你的账号：http://127.0.0.2:8000/active/{0}".format(random_str)
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type =="forget":
        email_title = "慕学在线网密码重置链接"
        email_body = "请点击下面链接重置账号密码：http://127.0.0.2:8000/reset/{0}".format(random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

def generate_random_str(randomlenth =8):
    str = ''
    chars ="SDFGHJKWERTY6Uasdfghjp2oiuytvbnmasdfg2hQWEasdf8gFGHhjVBNcvbnQAZzxfg0uPLKMNrtyuSDVmnbvQAZBVCTYUI234569IJN"
    length = len(chars)-1
    random = Random()
    for i in range(randomlenth):
        str+=chars[random.randint(0,length)]
    return str
