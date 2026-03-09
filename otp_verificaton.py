from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random


def otp_validate(email):
    otp = random.randint(1111,9999)
    body = f"""
        <!DOCTYPE html>
        <html>
        <body style="margin:0; padding:0; background-color:#f2f2f2; font-family:Arial, sans-serif;">

        <table align="center" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; margin-top:40px; border-radius:6px;">

        <tr>
        <td style="background-color:#4CAF50; color:white; text-align:center; padding:20px; font-size:24px; font-weight:bold;">
        OTP Verification
        </td>
        </tr>

        <tr>
        <td style="padding:30px; text-align:center; color:#333; font-size:16px;">
        Hello,<br><br>

        Use the following One Time Password (OTP) to verify your account.
        </td>
        </tr>

        <tr>
        <td align="center" style="padding:10px;">
        <span style="font-size:32px; letter-spacing:10px; font-weight:bold; color:#4CAF50; border:2px dashed #4CAF50; padding:10px 25px; display:inline-block;">
        {otp}
        </span>
        </td>
        </tr>


        <td style="padding:20px; text-align:center; color:#555; font-size:14px;">
        This OTP is valid for the next <b>5 minutes</b>.<br>
        Please do not share this OTP with anyone.
        </td>
        </tr>

        <tr>
        <td style="background-color:#f4f4f4; text-align:center; padding:15px; font-size:13px; color:#888;">
        If you did not request this OTP, please ignore this email.
        </td>
        </tr>

        </table>

        </body>
        </html>
        """


    msg = MIMEMultipart()
    msg["To"] = email
    msg["From"] = "dhanushchowdarypodapati@gmail.com"
    msg["Subject"] = "OTP - Banking "
    msg.attach(MIMEText(body,"html"))

    server = SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("dhanushchowdarypodapati@gmail.com","blqa jcae opvp jjud")
    server.send_message(msg)
    server.quit()

    #Verification  of OTP
    print()
    x = int(input("Enter 4 digit OTP Recieved to Mail: "))
    if x == otp:
        return True
    else:
        return False

