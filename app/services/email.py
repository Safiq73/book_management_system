class EmailService:
    async def send_email(from_email: str, to_email: str, message: str):
        print("SENT EMAIL")

        # This is a simulated code,
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # s.starttls()
        # s.login(from_email, "sender_email_id_password")
        # message = message
        # s.sendmail(from_email, to_email, message)
        # s.quit()
