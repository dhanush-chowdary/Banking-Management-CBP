#greeting.py
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def greet(email,name1,name2):
    body = f"""
        <!DOCTYPE html>
<html>
<head>
    <title>Greeting Message</title>
</head>
<body style="margin:0; padding:0; font-family: Arial, sans-serif; background-color:#f4f4f4;">

    <div style="width:100%; padding:40px 0; background-color:#f4f4f4;">
        
        <div style="max-width:600px; margin:auto; background:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 2px 6px rgba(0,0,0,0.1);">

            <!-- Header -->
            <div style="background-color:#4CAF50; color:white; padding:20px; text-align:center;">
                <h2 style="margin:0;">Warm Greetings 🎉</h2>
            </div>

            <!-- Content -->
            <div style="padding:30px; text-align:center; color:#333;">
                
                <h3 style="margin-top:0;">Hello {name1},</h3>

                <p style="font-size:16px; line-height:1.6;">
                    Wishing you a wonderful <strong>{name2}</strong> filled with happiness, success, and positivity.
                </p>

                <p style="font-size:15px; color:#666;">
                    May this special occasion bring joy and great moments to you and your loved ones.
                </p>

                <div style="margin-top:25px;">
                    <span style="display:inline-block; background:#4CAF50; color:white; padding:10px 20px; border-radius:5px; font-size:14px;">
                        Best Wishes
                    </span>
                </div>

            </div>

            <!-- Footer -->
            <div style="background:#f0f0f0; padding:15px; text-align:center; font-size:13px; color:#777;">
                Sent with ❤️ from Your Team
            </div>

        </div>

    </div>

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

    
