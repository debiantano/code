import smtplib

sender_email = "cromozzc@gmail.com"
rec_email = "richar.quispe@gmail.com"
password = input(str("> "))
message = "Hola, este es un mensaje usando python"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("[+] Login success")

server.sendmail(sender_email, rec_email, message)
print("Email enviado a " + rec_email)
