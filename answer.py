# -*- coding: utf-8 -*-

import re
import requests
import json


def onQQMessage(bot, contact, member, content):
    #    gl = bot.List('group', '玄魂工作室1群')
    #    if gl:
    #        group = gl[0]
    #        bot.Update(group)
    #    gl = bot.List('group', '玄魂工作室2群')
    #    if gl:
    #        group = gl[0]
    #        bot.Update(group)
    #    gl = bot.List('group', '玄魂工作室3群')
    #    if gl:
    #        group = gl[0]
    #        bot.Update(group)
    if '@ME' in content:
        if '测试' in content:
            # print(dir(contact))
            # print(dir(member))
            if member.name == '初音过去':
                bot.SendTo(contact, contact.name + '-机器人返回测试')
        elif '唱' in content:
            bot.SendTo(contact, '不会唱啊小哥哥')
        elif '跪安' in content:
            bot.SendTo(contact, '嗻')
        elif '爱' in content:
            bot.SendTo(contact, '我也爱你喔～')
        elif '移除' in content:
            #print('test kick')
            if member.qq == '2672406516':
                gl = bot.List('group', contact.name)
                if gl:
                    group = gl[0]
                    bot.Update(group)
                    kickt = re.split('@', content)[-1].strip()
                    membs = bot.List(group, kickt)
                    # print(dir(membs))
                    # print(kickt)
                    # print(membs)
                    if membs:
                        bot.SendTo(contact, kickt + ' 拖出去枪毙五分钟')
                        bot.GroupKick(group, membs)
                    else:
                        bot.SendTo(contact, kickt + '么有这个人啊～')
        else:
            # print(content)
            question = re.split(']', content)[1].strip()
            print(question)
            tuling_post = {
                "reqType": 0,
                "perception":
                {
                    "inputText":
                    {
                        "text": "%s" % question
                    }
                },
                "userInfo": {
                    "apiKey": "8654ff0db1f649f5b5b6c9c1eadab588",
                    "userId": "1234567890"
                }
            }
            try:
                r = requests.post('http://openapi.tuling123.com/openapi/api/v2',
                                  data=json.dumps(tuling_post))
            except Exception, e:
                print(e)
                bot.SendTo(contact, member.name + '，@我干嘛呢？')
            r = json.loads(r.text)
            r_result = r['results'][0]
            if r_result['resultType'] == 'text':
                # print(r_result['values'])
                # print(type(r_result['values']))
                bot.SendTo(contact, r_result['values']['text'])
    else:
        if '资料' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 玄小妹温馨提示你，学习资料可以参考群文件')
        if '开车' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name +
                       ' 上山的路已经被封，随时可以开车!(不对，都停下来，不准开车!)')
        if '问' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 问什么问，交学费没有(手动滑稽)？')
        if '怎么' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 什么怎么?怎么什么?')
        if '拿站' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 起床拿站了拿站了!')
        if '无聊' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name +
                       ' 无聊就多看看UNIX环境高级编程三卷本和TCP/IP三卷本!')
        if '大家好' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 新人是不是要爆照先？')
        if '问题' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 有什么问题@初音过去 ？')
        if '能不能' in content and member.name != '玄小妹':
            bot.SendTo(contact, '@' + member.name + ' 不能')
        if 'http' in content and member.name != '玄小妹':
            if member.qq != '2672406516':
                #bot.SendTo(contact, '@'+member.name+' 发链接枪毙五分钟')
                gl = bot.List('group', contact.name)
                if gl:
                    group = gl[0]
                    bot.Update(group)
                    kickt = member.name
                    membs = bot.List(group, kickt)
                    # print(dir(membs))
                    # print(kickt)
                    # print(membs)
                    if membs:
                        pass
                        #bot.SendTo(contact, '@' + kickt + ' 拖出去枪毙五分钟')
                        #bot.GroupKick(group, membs)
                    else:
                        pass
                        #bot.SendTo(contact, kickt + '么有这个人啊～')
        if '傻逼' in content and member.name != '玄小妹':
            if member.qq != '2672406516':
                #bot.SendTo(contact, '@'+member.name+' 发链接枪毙五分钟')
                gl = bot.List('group', contact.name)
                if gl:
                    group = gl[0]
                    bot.Update(group)
                    kickt = member.name
                    membs = bot.List(group, kickt)
                    # print(dir(membs))
                    # print(kickt)
                    # print(membs)
                    if membs:
                        bot.SendTo(contact, '@' + kickt + ' 拖出去枪毙五分钟')
                        bot.GroupKick(group, membs)
                    else:
                        bot.SendTo(contact, kickt + '么有这个人啊～')
