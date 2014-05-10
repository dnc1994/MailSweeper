# -*- encoding:utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header
import getpass

debug = 0

with open('maillist_13.txt', 'r') as f:
    mail_list = "".join(f.read().split()).split(",")

mail_host = "mail.fudan.edu.cn"
mail_postfix = "fudan.edu.cn"
# Fill in the account you wish to use for mail sweeping
mail_user = "13307130225"
print "Using %s for mail sweeping.\n" % mail_user
mail_pass = ''
#mail_pass = getpass.getpass()

# Fill in the subject of your mail
subject = "美芹社本学期讲座第二弹重磅来袭！—— 国际同传教你如何提升英语及规划未来"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = Header(subject, 'UTF-8')
msgRoot['From'] = "%s@%s" % (mail_user, mail_postfix)

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

# Embedded image
img_html = '<img src="cid:image1"><br>'
# Fill in the html code for your mail's text
text_html = '<p style="margin: 0px 0px 0.8em; padding: 0px; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font size="5" style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);"><span style="line-height: 33px;">想让大学四年更有收获</span></font><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250); font-size: x-large; line-height: 1.4;">却不知</span><span style="font-size: x-large; line-height: 1.4;">方向</span><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250); font-size: x-large; line-height: 1.4;">？</span></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font size="5"><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">对</span><span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 0);">如何<strong style="font-style: inherit;"><span style="text-decoration: underline;">规划英语学习</span></strong></span><font color="#333333" style="background-color: rgb(250, 250, 250);">、</font><span style="background-color: rgb(255, 255, 0);">进一步<strong style="font-style: inherit;">提升英语</strong></span><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">充满疑惑？</span></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; color: rgb(51, 51, 51); font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif; background-color: rgb(250, 250, 250);"><font size="5"><span style="font-style: inherit;">CET4、CET6、TOEFL、IELTS、中级口译、高级口译、BEC…………</span><strong style="font-style: inherit;">&nbsp;</strong>对<span style="background-color: rgb(255, 255, 0);">轻松通过各种<strong style="font-style: inherit;"><span style="text-decoration: underline;">英语考试</span></strong></span>充满憧憬？ &nbsp;</font></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font size="5"><font color="#333333" style="background-color: rgb(250, 250, 250);">对</font><span style="background-color: rgb(255, 255, 0); color: rgb(255, 0, 0);"><strong style="font-style: inherit;"><span style="text-decoration: underline;">同声传译</span></strong></span><font color="#333333" style="background-color: rgb(250, 250, 250);">这一高霸上的职业充满好奇？想亲眼目睹</font><b style="background-color: rgb(250, 250, 250); color: rgb(51, 51, 51);"><u>联合国同传</u></b><font color="#333333" style="background-color: rgb(250, 250, 250);">演示</font><font color="#ff0000"><u style="background-color: rgb(255, 255, 0);"><b>特殊的翻译技巧</b></u></font><font color="#333333" style="background-color: rgb(250, 250, 250);">？</font></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font size="5"><span style="color: rgb(255, 0, 0); background-color: rgb(255, 255, 0);"><strong style="font-style: inherit;">复旦美芹社</strong></span><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">诚邀&nbsp;<b>Transmax&nbsp;</b></span><strong style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250); font-style: inherit;">经验丰富的国际同传，</strong><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">揭秘</span><span style="background-color: rgb(250, 250, 250);"><font color="#0000ff"><b><u>英语学习方法</u></b></font></span><span style="background-color: rgb(250, 250, 250);"><font color="#333333">与</font><b><font color="#0000ff"><u>高效备考经验</u></font></b><font color="#333333">，并</font><b><u><font color="#0000ff">介绍</font></u></b><u><b><font color="#0000ff">同声传译</font></b></u><font color="#333333">与</font><u><b><font color="#0000ff">展示技巧</font></b></u><font color="#333333">。</font></span><b><font color="#ff0000"><span style="background-color: rgb(255, 255, 0);">&nbsp;4<span style="font-style: inherit;">月18日（下周五）</span></span></font></b><font color="#ff0000" style="background-color: rgb(255, 255, 0);">&nbsp;<strong style="font-style: inherit;">18：30</strong></font><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">，让我们共聚</span><strong style="color: rgb(255, 0, 0); background-color: rgb(255, 255, 0); font-style: inherit;">3208</strong>，<span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);">迎接这场英语盛宴！</span></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font size="5"><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);"><br></span></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);"><i><font size="4"><b>主讲人：国际资深同声传译员，主要工作经历包括：</b></font></i></span></p><p style="margin: 0px 0px 0.8em; padding: 0px; line-height: 1.4; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><span style="color: rgb(51, 51, 51); background-color: rgb(250, 250, 250);"><i><font size="4"><b>诺贝尔物理学奖获得者国际会议&nbsp;<span class="Apple-tab-span" style="white-space: pre;">	</span>同传</b></font></i></span></p><p style="margin: 0px 0px 0.8em; padding: 0px; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font color="#333333" size="4"><span style="line-height: 33px;"><i><b>英国汇丰银行年会&nbsp;<span class="Apple-tab-span" style="white-space: pre;">				</span>同传</b></i></span></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font color="#333333" size="4"><span style="line-height: 33px;"><i><b>联合国环境规划署可持续研讨会&nbsp;<span class="Apple-tab-span" style="white-space: pre;">	</span>同传</b></i></span></font></p><p style="margin: 0px 0px 0.8em; padding: 0px; font-family: Tahoma, Verdana, STHeiTi, simsun, sans-serif;"><font color="#333333" size="4"><span style="line-height: 33px;"><i><b>中欧经贸论坛&nbsp;<span class="Apple-tab-span" style="white-space: pre;">					</span>同传</b></i></span></font></p><br>--<br>祝学习进步、工作顺利。<br><br>章凌豪<br>计算机科学&nbsp;@&nbsp;复旦大学<br>美芹社&nbsp;|&nbsp;学生网&nbsp;|&nbsp;信息部<br><br>Tel:&nbsp;&nbsp;&nbsp;&nbsp;+86&nbsp;18321479268<br>Mail:&nbsp;&nbsp;&nbsp;<a href="mailto:13307130225@fudan.edu.cn" target="_blank">13307130225@fudan.edu.cn</a>&nbsp;/&nbsp;<a href="mailto:zlhdnc1994@gmail.com" target="_blank">zlhdnc1994@gmail.com</a><br><br>Blog:&nbsp;&nbsp;&nbsp;blog.dnc1994.com<br>GitHub:&nbsp;https://github.com/dnc1994<br>Wechat:&nbsp;dnc1994<br>'
html = img_html + text_html
msgText = MIMEText(html, 'html', 'UTF-8')
msgAlternative.attach(msgText)

with open('img1.png', 'rb') as f:
	msgImage = MIMEImage(f.read())
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Attachment
attFile = 'poster.jpg'
with open(attFile, 'rb') as f:
	msgAttachment = MIMEApplication(f.read())
msgAttachment.add_header('Content-Disposition', 'attachment', filename=attFile)
msgRoot.attach(msgAttachment)

# For debug
if debug:
	addrs = ["13307130225@fudan.edu.cn"]

# Manually set this
for x in range(0, 400, 100):
	s = smtplib.SMTP()
	addrs = mail_list[x:x+100]
	try:
		msgRoot['To'] = ', '.join(addrs)
		s.connect(mail_host)
		s.login(mail_user, mail_pass)
		s.sendmail(msgRoot['From'], addrs, msgRoot.as_string())
		s.close()
	except Exception, e:
		print str(e)
