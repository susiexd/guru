#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : readguru.py    
@Author : Susie
@Create : 2022/8/29 下午7:58
@Desc   : 
"""


from bs4 import BeautifulSoup
import re


# 解析html，获取我们需要的字段
def get_data_from_html(html):
    print(html)
    soup = BeautifulSoup(html)
    list1 = []
    title = soup.select('div > strong').__getitem__(0).text  # 获取title
    list1.append(title)

    # 获取前置条件
    pre = str(soup.fieldset)
    pre = pre.replace('<fieldset>', '').replace('<legend>前置条件</legend>', '').replace('</fieldset>', '').replace('<br/>', '')  # 获取步骤-预期
    pre = pre.strip()
    list1.append(pre)

    link = soup.find_all('td', attrs={'class': 'text-left'})  # 提取所有的步骤和预期
    list_step = []  # 存储处理过后的步骤和预期

    for step in link:
        m = str(step).replace('<td class="text-left">', '').replace('<div class="input-group">', '').replace('</div>','').replace('</td>', '').replace('<br/>', '').replace('&gt;', '>')
        if "step-item-id" in m :  # 若存在step-item-id（返回true），则为子步骤，类型设置为2
            step_id = re.findall(r">(.+?)<", m)
            step = re.findall(r"span>(.*)", m)
            list_step.append([2, step_id[0], step[0]])
        else:  # 不是 step-item-id，则为一级步骤，类型设置为1
            list_step.append([1, m])

    lst = iter(range(len(list_step)))
    step_num = 1  # 一级步骤计数器
    for i in lst:
        if list_step[i][0] == 2:
            list1.append(list_step[i][1])  # 子步骤id
            list1.append("item")  # 子步骤类型
            list1.append(list_step[i][2])  # 子步骤详情
            list1.append(list_step[i + 1][1])  # 子步骤预期
        else:
            list1.append(str(step_num))  # 一级步骤id
            list1.append("group")  # 一级步骤类型
            list1.append(list_step[i][1])  # 一级步骤详情
            list1.append(list_step[i+1][1])  # 一级步骤预期
            step_num += 1

        lst.__next__()  # 下个item是预期，所以跳过
    return list1


html1 = """
{"1forge.com":{"added":"2017-05-30T08:34:14.000Z","preferred":"0.0.1","versions":{"0.0.1":{"added":"2017-05-30T08:34:14.000Z","info":{"contact":{"email":"contact@1forge.com","name":"1Forge","url":"http://1forge.com"},"description":"Stock and Forex Data and Realtime Quotes","title":"1Forge Finance APIs","version":"0.0.1","x-apisguru-categories":["financial"],"x-logo":{"backgroundColor":"#24292e","url":"https://api.apis.guru/v2/cache/logo/https_1forge.com_assets_images_f-blue.svg"},"x-origin":[{"format":"swagger","url":"http://1forge.com/openapi.json","version":"2.0"}],"x-providerName":"1forge.com"},"updated":"2017-06-27T16:49:57.000Z","swaggerUrl":"https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json","swaggerYamlUrl":"https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.yaml","openapiVer":"2.0"}}},"1password.com:events":{"added":"2021-07-19T10:17:09.188Z","preferred":"1.0.0","versions":{"1.0.0":{"added":"2021-07-19T10:17:09.188Z","info":{"description":"1Password Events API Specification.","title":"Events API","version":"1.0.0","x-apisguru-categories":["security"],"x-logo":{"url":"https://api.apis.guru/v2/cache/logo/https_upload.wikimedia.org_wikipedia_commons_thumb_e_e3_1password-logo.svg_1280px-1password-logo.svg.png"},"x-origin":[{"format":"openapi","url":"https://i.1password.com/media/1password-events-reporting/1password-events-api.yaml","version":"3.0"}],"x-providerName":"1password.com","x-serviceName":"events"},"updated":"2021-07-22T10:32:52.774Z","swaggerUrl":"https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.json","swaggerYamlUrl":"https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.yaml","openapiVer":"3.0.0"}}}}
"""
list1 = get_data_from_html(html1)
print("***************")
for i in range(len(list1)):
    print(str(list1[i]))

