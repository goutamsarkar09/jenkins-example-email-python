import smtplib

email = "goutam.sarkar09@gmail.com"
password = 'hqza cnfc wbzs dxay' # which you got from app password of your gmail account
receiver_email = "goutam.sarkar09@gmail.com"

subject = "email from python"
message = "hello this email is sent from python"
text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",465)
server.starttls()

server.login(email, password)
server.sendmail(email, receiver_email, text)
print("Email was sent successfully to : " , receiver_email)
