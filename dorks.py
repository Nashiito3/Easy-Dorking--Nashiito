# defs

import webbrowser

# custom

def CustomLookup():
    webbrowser.open("https://www.google.com/advanced_search")

# gmail

def Gmail():
    webbrowser.open("https://www.google.com/search?q=filetype%3Atxt+inurl%3A%22mail.txt%22+&ei=7NHaYenUFuLIgwfu3p14&ved=0ahUKEwjp-rPt0qT1AhVi5OAKHW5vBw8Q4dUDCA0&uact=5&oq=filetype%3Atxt+inurl%3A%22mail.txt%22+&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQu_IDWLvyA2DY8wNoBXAAeACAAUKIAUKSAQExmAEAoAEBwAEB&sclient=gws-wiz")

# host

def FTP():
    webbrowser.open("https://www.google.com/search?channel=fs&client=ubuntu&q=intitle%3A%22index+of%22+inurl%3Aftp")

def CFTP():
    webbrowser.open("https://www.google.com/search?q=intitle%3A%22index+of%22+inurl%3Aftp+%22intext%22&ei=iNPaYdO2JYeLlwSj9JKIBw&ved=0ahUKEwjTmv2x1KT1AhWHxYUKHSO6BHEQ4dUDCA0&uact=5&oq=intitle%3A%22index+of%22+inurl%3Aftp+%22intext%22&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABKBAhGGABQnQNYxyhg5DRoAnACeACAAZ4BiAHAB5IBBDEwLjKYAQCgAQHIAQbAAQE&sclient=gws-wiz")

# camera

def Camera():
    webbrowser.open("https://www.google.com/search?q=inurl%3A%22view.shtml%22+%22Network+Camera%22+&ei=ltPaYbWACe2RlwShu6LIDg&ved=0ahUKEwi1o7e41KT1AhXtyIUKHaGdCOkQ4dUDCA0&uact=5&oq=inurl%3A%22view.shtml%22+%22Network+Camera%22+&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQmARYmARgiwhoA3AAeACAAUSIAUSSAQExmAEAoAECoAEBwAEB&sclient=gws-wiz")

def LiveCam():
    webbrowser.open("https://www.google.com/search?q=%22Camera+Live+Image%22+inurl%3A%22guestimage.html%22&ei=49PaYfaVEYKua-X8v3g&ved=0ahUKEwi2k5vd1KT1AhUC1xoKHWX-Dw8Q4dUDCA0&uact=5&oq=%22Camera+Live+Image%22+inurl%3A%22guestimage.html%22&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABKBAhGGABQogNYogNgnAVoA3ACeACAAZABiAGQAZIBAzAuMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz")

# passwords

def Pass():
    webbrowser.open("https://www.google.com/search?q=site%3Apastebin.com+intext%3Aadmin.password&ei=BdTaYZWiMMmRlwTBgKagBA&ved=0ahUKEwjVuNXt1KT1AhXJyIUKHUGACUQQ4dUDCA0&uact=5&oq=site%3Apastebin.com+intext%3Aadmin.password&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQuQNYuQNgvwpoA3AAeACAAUKIAUKSAQExmAEAoAECoAEBwAEB&sclient=gws-wiz")
    # this is used to get leaked info

def ExPass():
    webbrowser.open("https://www.google.com/search?q=%22admin_password%22+ext%3Atxt+%7C+ext%3Alog+%7C+ext%3Acfg&ei=aNTaYd7mHdHKgwf5uo6YBA&ved=0ahUKEwjeut2c1aT1AhVR5eAKHXmdA0MQ4dUDCA0&uact=5&oq=%22admin_password%22+ext%3Atxt+%7C+ext%3Alog+%7C+ext%3Acfg&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQpQNYpQNgpgVoA3AAeACAAT6IAT6SAQExmAEAoAECoAEBwAEB&sclient=gws-wiz")
    # with this you can find passwords in exposed files

def Mpass():
    webbrowser.open("https://www.google.com/search?q=filetype%3Alog+intext%3Apassword+after%3A2016+intext%3A%40gmail.com+%7C+%40yahoo.com+%7C+%40hotmail.com&ei=rNTaYaa4FYq5gwfE9oaQCg&ved=0ahUKEwimvou91aT1AhWK3OAKHUS7AaIQ4dUDCA0&uact=5&oq=filetype%3Alog+intext%3Apassword+after%3A2016+intext%3A%40gmail.com+%7C+%40yahoo.com+%7C+%40hotmail.com&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQjANYjANg8whoA3AAeACAAUWIAUWSAQExmAEAoAECoAEBwAEB&sclient=gws-wiz")
    # acced to all logs that contain "password" and @gmail/@hotmail/@yahoo in the <body>

# commands

def Commands():
    print("""Other usefull commands are:


    site:static.ow.ly/docs/ intext:@gmail.com | Password
    filetype:sql intext:wp_users phpmyadmin
    intext:"Dumping data for table orders"
    "Index of /wp-content/uploads/backupbuddy_backups" zip
    Zixmail inurl:/s/login?
    inurl:/remote/login/ intext:"please login"|intext:"FortiToken clock drift detected"
    inurl:/WebInterface/login.html
    inurl:dynamic.php?page=mailbox
    inurl:/sap/bc/webdynpro/sap/ | "sap-system-login-oninputprocessing"
    intext:"Powered by net2ftp"

        """
    )

# db

def GoogleHackingDB():
    webbrowser.open("https://www.exploit-db.com/google-hacking-database")