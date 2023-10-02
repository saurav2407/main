from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from pytube import YouTube



hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
year = int(datetime.datetime.now().year)
if hour >= 0 and hour < 12:
    wish="Good Morning! "

elif hour >= 12 and hour < 18:
    wish="Good Afternoon!"
else:
    wish="Good Evening!"


def index(request):
    return render(request,'index.html')


def owner(request):
    name = request.GET.get('name','default')
    email = request.GET.get('email','default')
    phone = request.GET.get('phone','default')
    address = request.GET.get('address','Not mentioned')
    form_group = request.GET.get('course','default')
    if  form_group == "All Subject":
        form_group = "Maths, Physics, Chemistry"
    else:
        form_group = request.GET.get('course', 'default')

    params = {'purpose': 'capital text', 'analyzed_text': f'Hello {name}', 'wish':f"{wish}"}

    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'

    to_email = "sauravpathak24072003@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = "Gyanam Institute "

    body = f"Name: {name} choose for {form_group}\n\nContact info:\nPhone Number:{phone}\nEmail-Id:{email}\n\nAddress:\n{address}\n\nsubmission time:{hour}:{minute}\nsubmission date:{day}/{month}/{year}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
def coaching(request):

    name = request.GET.get('name','default')
    email = request.GET.get('email','default')
    phone = request.GET.get('phone','default')
    address = request.GET.get('address','you do not mention your Address')
    form_group = request.GET.get('course','default')
    if form_group == "All Subject":
        form_group = "Maths, Physics, Chemistry"
    else:
        form_group = request.GET.get('course', 'default')

    params = {'purpose': 'capital text', 'analyzed_text': f'Hello {name}', 'wish':f"{wish}"}

    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'

    to_email = email

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = "Gyanam Institute "

    body = f"Hello {name}\n.welcome to Gyanam Institute verification.You choose for {form_group}\n.Thank you for visiting our Website.We will contact you soon.\nContact info:\nPhone Number:{phone}\nEmail-Id:{email}\n\nsubmission time:{hour}:{minute}\nsubmission date:{day}/{month}{year}\nAddress:\n{address}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
        owner(request)

    except Exception as e:
        print(f"Error: {str(e)}")
        return render(request, 'error.html')


    return render(request, 'confirm.html', params)

def notes(request):
    return render(request, 'notes.html')



def report(request):
    issue = request.GET.get('issue', 'default')
    email = request.GET.get('email', 'default')
    phone = request.GET.get('phone', 'default')


    params = {'purpose': 'Contact Us', 'analyzed_text': f'An{issue} has issued on {email}. Contact number:{phone}'}

    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'

    to_email = "sauravpathak24072003@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = " Report Gyanam Institute "

    body = f"An issue has organised in {email}.\nISSUE:\n{issue}\n\nReport time:{hour}:{minute}\nReport date:{day}/{month}{year}\n\n\nDiscription:\nAn{issue} has issued on {email}. Contact number:{phone}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()


    except Exception as e:
        print(f"Error: {str(e)}")
        return render(request, 'error.html')


    return render(request, 'contact.html')

def contact(request):
    return render(request, 'contact.html')

def error(request):
    return render(request, 'error.html')
def download_link(request):
    link = request.GET.get('link','default')
    video_url = link
    try:
        download_path = "C:/"
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        return render(request, 'notes.html')
    except Exception as e:
        print(f"Error: {str(e)}")
        return render(request, 'error.html')



