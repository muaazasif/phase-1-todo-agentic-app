# Email Configuration for Todo CLI Application

## Setting up Real Email Functionality

To enable real email sending functionality, you need to configure your email settings. The application uses environment variables for security.

### For Gmail Users:

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail" 
   - Use this app password instead of your regular password

### Environment Variables:

Set these environment variables in your system:

```bash
# For Linux/Mac (add to ~/.bashrc, ~/.zshrc, or run before executing):
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
export EMAIL_SMTP_SERVER="smtp.gmail.com"
export EMAIL_SMTP_PORT="587"

# For Windows (Command Prompt):
set EMAIL_ADDRESS=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
set EMAIL_SMTP_SERVER=smtp.gmail.com
set EMAIL_SMTP_PORT=587

# For Windows (PowerShell):
$env:EMAIL_ADDRESS="your_email@gmail.com"
$env:EMAIL_PASSWORD="your_app_password"
$env:EMAIL_SMTP_SERVER="smtp.gmail.com"
$env:EMAIL_SMTP_PORT="587"
```

### Alternative Method - Create a .env file:

Create a `.env` file in the project root directory:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_USE_TLS=True
```

Then install python-dotenv to load these variables:
```bash
pip install python-dotenv
```

### Supported Email Providers:

- **Gmail**: smtp.gmail.com:587
- **Outlook/Hotmail**: smtp-mail.outlook.com:587
- **Yahoo**: smtp.mail.yahoo.com:587
- **Custom SMTP**: Configure with your provider's settings

### Security Note:

Never commit your email credentials to version control. The application is designed to read credentials from environment variables to keep them secure.

### Testing the Configuration:

Once configured, run the application and use the "Send Email" feature (option 8). The application will attempt to send a real email if configuration is detected, otherwise it will use simulation mode.