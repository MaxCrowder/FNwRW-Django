# FNwRW-Django
Django - Flash News with River Waters

This repo contains source code for the Flash News website using Django. The code is not production ready as the settings have not been configured for security. 

Flash News with River Waters is a financial news podcast made primarly as a skill for Amazon Alexa. The live website currently has problems with scaling. There is no solution for email signups, donations and mp3 data. To solve these problems, I recreated the website using Django. 

The Django admin page allows me to manage mp3 data needed for the JSON file that Alexa reads for deployment like unique identifies, date and URLs. When the podcast is created and deployed everyday this information piles up quickly. The admin page also allow me to securely store donation data which allows me to send merch to the donors. Lastly, the email signup form on the website is automatically sent and stored in the database allowing easy access for bulk emails with Python. 

The current live website is at: https://fnwrw.com/
The current live website repo is available at https://github.com/MaxCrowder/Flash-News-with-River-Waters
The live website is currently being deployed by Netlify using the above repo. The mp3 files are currently uploaded directly to the repo and the JSON file is updated manually everyday for new podcasts. The email signup form is supported by Netlify forms.

