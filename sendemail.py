import smtplib
import sendemail_auth

megjo = True
def set_text(temp):
    global megjo
    msg = ""
    if temp <= 0:
        msg = "%.2f C - Itt már a viz is megvagy... Szerintem fogd a takaród huzd magadra és aludj tovább, de ha mégse akkor nagyon melegen öltözz és rétegesen. Sál, sapka, kesztyű kötelező!" % temp
    elif 0< temp <= 10:
        msg = "%.2f C - Azt ajánlom ha fázós vagy öltözz fel rétegesen és melegen, nehogy meglepetés érjen amint kilépsz az ajtón." % temp
    elif 10< temp <= 15:
        msg = "%.2f C - Nézz ki az ablakon, mert ha fúj a szél azért csipős lehet az idő, de anélkül is elég hűvös. Egyébként egy kabát elegendő lehet." % temp
    elif 15<temp<=20:
        msg = "%.2f C - Egész kellemes hűvöskés frissítő idő van. Ajánlok egy pulcsit vagy kis nyári kabátot,esetleg ha fázósabb vagy akkor pulcsi és kabát egyszerre." % temp
    elif 20<temp<=25:
        msg = "%.2f C - Véleményem szerint ez az idő pont kellemes a szabad levegőn legyél kicsit. Ajánlok rövid nadrágot és egy pólot, bár ha fázosabb vagy a rövid nadrág lehet még túl merész ötlet neked." % temp
    elif 25<temp<=30:
        msg ="%.2f C - Irány a strand! Készisd a fürdőruhád, de vigyázz nehogy napszurást kapj!" % temp
    elif temp < 30:
        msg = "Vigyázz a napon tartózkodással elég perzselő lehet. Persze egy jo frissítő strandolás ilyenkor is jólesik."
    else:
        msg = "Sajnos az ajánlás ma sikertelen"
    return msg

def send_email(msg,date,fromaddres="gaborka98@t-online.hu",toaddres="gaborka812@gmail.com",subject="Weather Station"):
    fromaddr=fromaddres
    toaddr=toaddres
    subj = subject
    footer = "Minden üzenet csak ajánlás nem kötelező betartani és komolyan venni."

    msg = "From: %s\nTo: %s\nSubject: %s\n\n%s\n\n%s" % (fromaddr, toaddr, subj,msg, footer)

    s = smtplib.SMTP(sendemail_auth.server)
    s.starttls()
    s.login(sendemail_auth.user,sendemail_auth.pw)
    global megjo
    if megjo and (date.hour==8 or date.hour==12 or date.hour==18):
        s.sendmail(fromaddr, toaddr, msg.encode("utf-8"))
        megjo = False
    else:
        megjo = True
    s.quit()
