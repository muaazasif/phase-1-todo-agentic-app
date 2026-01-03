"""
Email configuration for the Todo CLI application
This file contains the configuration for sending real emails
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from typing import List, Optional
from dotenv import load_dotenv
load_dotenv()
class EmailConfig:
    """Configuration class for email settings"""
    
    def __init__(self):
        # Email server settings - these can be configured by the user
        self.smtp_server = os.getenv('EMAIL_SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('EMAIL_SMTP_PORT', '587'))
        self.sender_email = os.getenv('EMAIL_ADDRESS', 'your_email@gmail.com')
        self.sender_password = os.getenv('EMAIL_PASSWORD', 'your_app_password')
        self.use_tls = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'

def send_real_email(
    recipient_email: str,
    subject: str,
    message_body: str,
    attachments: List[str] = None,
    config: EmailConfig = None
) -> bool:
    """
    Send a real email with optional attachments
    
    Args:
        recipient_email: Email address of the recipient
        subject: Subject of the email
        message_body: Body content of the email
        attachments: List of file paths to attach
        config: Email configuration object
    
    Returns:
        True if email was sent successfully, False otherwise
    """
    if config is None:
        config = EmailConfig()
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = config.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(message_body, 'plain'))
        
        # Add attachments if any
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(file_path)}'
                    )
                    
                    msg.attach(part)
        
        # Create SMTP session
        server = smtplib.SMTP(config.smtp_server, config.smtp_port)
        server.starttls() if config.use_tls else None  # Enable security
        server.login(config.sender_email, config.sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(config.sender_email, recipient_email, text)
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False