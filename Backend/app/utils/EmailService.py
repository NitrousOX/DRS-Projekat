from flask_mail import Message
from flask import render_template, render_template_string
import os

def send_email(subject, recipients, template_name, **kwargs):
    """Send an HTML email using Flask-Mail."""
    
    # Import mail here to avoid circular import
    from app import mail  
    
    template_path = os.path.join("app", "utils", "emails_templates", template_name)
    
    try:
        # Read the HTML file manually
        with open(template_path, "r", encoding="utf-8") as file:
            html_body = file.read()
        
        # Render the template with dynamic values
        html_body = render_template_string(html_body, **kwargs)

        msg = Message(subject=subject, recipients=recipients, html=html_body)
        mail.send(msg)
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise e
