```python
# theme_development/documentation/troubleshooting.py

# List of common issues and their solutions
common_issues = {
    "Theme not loading": "Check if the theme files are correctly placed in the themes directory and the theme is activated in Odoo.",
    "Changes not reflecting": "Ensure you have cleared the cache after making changes to the theme files.",
    "Broken layout on certain screen sizes": "Check the responsiveness of your theme. Make sure you have defined proper breakpoints and styles for each.",
    "Images not loading": "Ensure the image paths are correct and the images exist in the specified path.",
    "Slow loading time": "Optimize your images and scripts. Minimize the use of heavy JS libraries."
}

def troubleshoot(issue):
    try:
        print(f"Issue: {issue}")
        print(f"Possible Solution: {common_issues[issue]}")
    except KeyError:
        print("The issue you're facing is not listed in common issues. Please seek help from the support channels.")

# Support Channels
support_channels = {
    "Email": "support@odootheme.com",
    "Forum": "https://forum.odootheme.com",
    "Chat": "Available on our website from 9AM to 5PM (GMT)"
}

def get_support(channel):
    try:
        print(f"Support Channel: {channel}")
        print(f"Contact Info: {support_channels[channel]}")
    except KeyError:
        print("The support channel you're looking for is not available. Please choose from Email, Forum, or Chat.")
```
