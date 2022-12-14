#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : getGuruFromJson.py    
@Author : Susie
@Create : 2022/9/1 上午9:37
@Desc   : 
"""
import json
import xlrd
import xlwt
def getGuruFromJson(dict_data):
    # 表头
    result = [{"project":"project","title":"title","description":"description","categories":"categories","logo":"logo","origin_format":"origin_format","origin_url":"origin_url","swaggerYamlUrl":"swaggerYamlUrl","swaggerUrl":"swaggerUrl"}]
    keys = dict_data.keys()
    values = dict_data.values()

    # 需要提取的字段：projectName=keys
    # 、title、description
    # 、x-apisguru-categories
    # 、x-logo的url
    # 、x-origin 数组 [{"format":"swagger","url":"http:xxx","version":"2.0"}]
    # swaggerYamlUrl、swaggerUrl
    for i in keys:
        # print("OriginalDetail = ", dict_data[i])
        item = dict(project=i #ok
                    , title="", description=""
                    , categories="", logo=""
                    , origin_format="", origin_url=""
                    , swaggerYamlUrl="", swaggerUrl="") #ok

        detail = dict_data[i]['versions'].values()[0]
        if(detail.get("swaggerUrl")):
            item['swaggerUrl'] = detail['swaggerUrl']
        if (detail.get("swaggerUrl")):
            item['swaggerYamlUrl'] = detail['swaggerYamlUrl']
        if (detail['info'].get("title")):
            item['title'] = detail['info']['title']
        if (detail['info'].get("description")):
            item['description'] = detail['info']['description'] #标签符替换
            # item['description'] = desc.replace("<fullname>(.*)</fullname>","").replace()
        if (detail['info'].get("x-apisguru-categories")):
            item['categories'] = detail['info']['x-apisguru-categories']
        if (detail['info'].get("x-logo")):
            item['logo'] = detail['info']['x-logo']['url']
        if (detail['info'].get("x-origin")): #??这里的数组都只有一个元素吗，确认
            x_origin = detail['info']['x-origin'][0]
            if (x_origin.get("format")):
                item['origin_format'] = x_origin['format']
            if (x_origin.get("url")):
                item['origin_url'] = x_origin['url']

        for i in item.keys():
            print(i, item[i])
        result.append(item)
    return result

def writeToExcel(result):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('guru')
    print(len(result))
    # sheet.write(0, 0, "HELLO")

    for r in range(len(result)):
        sheet.write(r, 0, result[r]['project'])
        sheet.write(r, 1, result[r]['title'])
        sheet.write(r, 2, result[r]['description'])
        sheet.write(r, 3, result[r]['categories'])
        sheet.write(r, 4, result[r]['logo'])
        sheet.write(r, 5, result[r]['origin_format'])
        sheet.write(r, 6, result[r]['origin_url'])
        sheet.write(r, 7, result[r]['swaggerYamlUrl'])
        sheet.write(r, 8, result[r]['swaggerUrl'])

    workbook.save('../data/result/result04_2.xls')


if __name__=="__main__":
    data_2 = """
    {"1forge.com":{"added":"2017-05-30T08:34:14.000Z","preferred":"0.0.1","versions":{"0.0.1":{"added":"2017-05-30T08:34:14.000Z","info":{"contact":{"email":"contact@1forge.com","name":"1Forge","url":"http://1forge.com"},"description":"Stock and Forex Data and Realtime Quotes","title":"1Forge Finance APIs","version":"0.0.1","x-apisguru-categories":["financial"],"x-logo":{"backgroundColor":"#24292e","url":"https://api.apis.guru/v2/cache/logo/https_1forge.com_assets_images_f-blue.svg"},"x-origin":[{"format":"swagger","url":"http://1forge.com/openapi.json","version":"2.0"}],"x-providerName":"1forge.com"},"updated":"2017-06-27T16:49:57.000Z","swaggerUrl":"https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json","swaggerYamlUrl":"https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.yaml","openapiVer":"2.0"}}},"1password.com:events":{"added":"2021-07-19T10:17:09.188Z","preferred":"1.0.0","versions":{"1.0.0":{"added":"2021-07-19T10:17:09.188Z","info":{"description":"1Password Events API Specification.","title":"Events API","version":"1.0.0","x-apisguru-categories":["security"],"x-logo":{"url":"https://api.apis.guru/v2/cache/logo/https_upload.wikimedia.org_wikipedia_commons_thumb_e_e3_1password-logo.svg_1280px-1password-logo.svg.png"},"x-origin":[{"format":"openapi","url":"https://i.1password.com/media/1password-events-reporting/1password-events-api.yaml","version":"3.0"}],"x-providerName":"1password.com","x-serviceName":"events"},"updated":"2021-07-22T10:32:52.774Z","swaggerUrl":"https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.json","swaggerYamlUrl":"https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.yaml","openapiVer":"3.0.0"}}}}
    """
    data = """
    {    "1forge.com": {
        "added": "2017-05-30T08:34:14.000Z",
        "preferred": "0.0.1",
        "versions": {
            "0.0.1": {
                "added": "2017-05-30T08:34:14.000Z",
                "info": {
                    "contact": {
                        "email": "contact@1forge.com",
                        "name": "1Forge",
                        "url": "http://1forge.com"
                    },
                    "description": "Stock and Forex Data and Realtime Quotes",
                    "title": "1Forge Finance APIs",
                    "version": "0.0.1",
                    "x-apisguru-categories": [
                        "financial"
                    ],
                    "x-logo": {
                        "backgroundColor": "#24292e",
                        "url": "https://api.apis.guru/v2/cache/logo/https_1forge.com_assets_images_f-blue.svg"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "http://1forge.com/openapi.json",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "1forge.com"
                },
                "updated": "2017-06-27T16:49:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "1password.com:events": {
        "added": "2021-07-19T10:17:09.188Z",
        "preferred": "1.0.0",
        "versions": {
            "1.0.0": {
                "added": "2021-07-19T10:17:09.188Z",
                "info": {
                    "description": "1Password Events API Specification.",
                    "title": "Events API",
                    "version": "1.0.0",
                    "x-apisguru-categories": [
                        "security"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_upload.wikimedia.org_wikipedia_commons_thumb_e_e3_1password-logo.svg_1280px-1password-logo.svg.png"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://i.1password.com/media/1password-events-reporting/1password-events-api.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "1password.com",
                    "x-serviceName": "events"
                },
                "updated": "2021-07-22T10:32:52.774Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "1password.local:connect": {
        "added": "2021-04-16T15:56:45.939Z",
        "preferred": "1.3.0",
        "versions": {
            "1.3.0": {
                "added": "2021-04-16T15:56:45.939Z",
                "info": {
                    "contact": {
                        "email": "support@1password.com",
                        "name": "1Password Integrations",
                        "url": "https://support.1password.com/"
                    },
                    "description": "REST API interface for 1Password Connect.",
                    "title": "1Password Connect",
                    "version": "1.3.0",
                    "x-apisguru-categories": [
                        "security"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_upload.wikimedia.org_wikipedia_commons_thumb_e_e3_1password-logo.svg_1280px-1password-logo.svg.png"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://i.1password.com/media/1password-connect/1password-connect-api.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "1password.local",
                    "x-serviceName": "connect"
                },
                "updated": "2021-07-26T08:51:53.432Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/1password.local/connect/1.3.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/1password.local/connect/1.3.0/openapi.yaml",
                "openapiVer": "3.0.2"
            }
        }
    },
    "6-dot-authentiqio.appspot.com": {
        "added": "2017-03-15T14:45:58.000Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2017-03-15T14:45:58.000Z",
                "info": {
                    "contact": {
                        "email": "hello@authentiq.com",
                        "name": "Authentiq team",
                        "url": "http://authentiq.io/support"
                    },
                    "description": "Strong authentication, without the passwords.",
                    "license": {
                        "name": "Apache 2.0",
                        "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
                    },
                    "termsOfService": "http://authentiq.com/terms/",
                    "title": "Authentiq API",
                    "version": "6",
                    "x-apisguru-categories": [
                        "security"
                    ],
                    "x-logo": {
                        "backgroundColor": "#F26641",
                        "url": "https://api.apis.guru/v2/cache/logo/https_www.authentiq.com_theme_images_authentiq-logo-a-inverse.svg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/AuthentiqID/authentiq-docs/master/docs/swagger/issuer.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "6-dot-authentiqio.appspot.com"
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/6-dot-authentiqio.appspot.com/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/6-dot-authentiqio.appspot.com/6/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "ably.io:platform": {
        "added": "2019-07-13T11:28:07.000Z",
        "preferred": "1.1.0",
        "versions": {
            "1.1.0": {
                "added": "2019-07-13T11:28:07.000Z",
                "info": {
                    "contact": {
                        "email": "support@ably.io",
                        "name": "Ably Support",
                        "url": "https://www.ably.io/contact",
                        "x-twitter": "ablyrealtime"
                    },
                    "description": "The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.",
                    "title": "Platform API",
                    "version": "1.1.0",
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_ablyrealtime_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/ably/open-specs/main/definitions/platform-v1.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "ably.io",
                    "x-serviceName": "platform"
                },
                "updated": "2021-07-26T09:42:14.653Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/ably.io/platform/1.1.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/ably.io/platform/1.1.0/openapi.yaml",
                "openapiVer": "3.0.1"
            }
        }
    },
    "ably.net:control": {
        "added": "2021-07-26T09:45:31.536Z",
        "preferred": "1.0.14",
        "versions": {
            "1.0.14": {
                "added": "2021-07-26T09:45:31.536Z",
                "info": {
                    "contact": {
                        "x-twitter": "ablyrealtime"
                    },
                    "description": "Use the Control API to manage your applications, namespaces, keys, queues, rules, and more.Detailed information on using this API can be found in the Ably <a href=\"https://ably.com/documentation/control-api\">developer documentation</a>.Control API is currently in Beta.",
                    "title": "Control API v1",
                    "version": "1.0.14",
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_ablyrealtime_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/ably/open-specs/main/definitions/control-v1.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "ably.net",
                    "x-serviceName": "control"
                },
                "updated": "2021-07-26T09:47:48.565Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/ably.net/control/1.0.14/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/ably.net/control/1.0.14/openapi.yaml",
                "openapiVer": "3.0.1"
            }
        }
    },
    "abstractapi.com:geolocation": {
        "added": "2021-04-14T17:12:40.648Z",
        "preferred": "1.0.0",
        "versions": {
            "1.0.0": {
                "added": "2021-04-14T17:12:40.648Z",
                "info": {
                    "description": "Abstract IP geolocation API allows developers to retrieve the region, country and city behind any IP worldwide. The API covers the geolocation of IPv4 and IPv6 addresses in 180+ countries worldwide. Extra information can be retrieved like the currency, flag or language associated to an IP.",
                    "title": "IP geolocation API",
                    "version": "1.0.0",
                    "x-apisguru-categories": [
                        "location"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_global-uploads.webflow.com_5ebbd0a566a3996636e55959_5ec2ba29feeeb05d69160e7b_webclip.png"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://documentation.abstractapi.com/ip-geolocation-openapi.json",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "abstractapi.com",
                    "x-serviceName": "geolocation"
                },
                "externalDocs": {
                    "description": "API Documentation",
                    "url": "https://www.abstractapi.com/ip-geolocation-api#docs"
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/abstractapi.com/geolocation/1.0.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/abstractapi.com/geolocation/1.0.0/openapi.yaml",
                "openapiVer": "3.0.1"
            }
        }
    },
    "adafruit.com": {
        "added": "2018-02-10T10:41:43.000Z",
        "preferred": "2.0.0",
        "versions": {
            "2.0.0": {
                "added": "2018-02-10T10:41:43.000Z",
                "info": {
                    "description": "### The Internet of Things for EveryoneThe Adafruit IO HTTP API provides access to your Adafruit IO data from any programming language or hardware environment that can speak HTTP. The easiest way to get started is with [an Adafruit IO learn guide](https://learn.adafruit.com/series/adafruit-io-basics) and [a simple Internet of Things capable device like the Feather Huzzah](https://www.adafruit.com/product/2821).This API documentation is hosted on GitHub Pages and is available at [https://github.com/adafruit/io-api](https://github.com/adafruit/io-api). For questions or comments visit the [Adafruit IO Forums](https://forums.adafruit.com/viewforum.php?f=56) or the [adafruit-io channel on the Adafruit Discord server](https://discord.gg/adafruit).#### AuthenticationAuthentication for every API request happens through the `X-AIO-Key` header or query parameter and your IO API key. A simple cURL request to get all available feeds for a user with the username \"io_username\" and the key \"io_key_12345\" could look like this:    $ curl -H \"X-AIO-Key: io_key_12345\" https://io.adafruit.com/api/v2/io_username/feedsOr like this:    $ curl \"https://io.adafruit.com/api/v2/io_username/feeds?X-AIO-Key=io_key_12345Using the node.js [request](https://github.com/request/request) library, IO HTTP requests are as easy as:```jsvar request = require('request');var options = {  url: 'https://io.adafruit.com/api/v2/io_username/feeds',  headers: {    'X-AIO-Key': 'io_key_12345',    'Content-Type': 'application/json'  }};function callback(error, response, body) {  if (!error && response.statusCode == 200) {    var feeds = JSON.parse(body);    console.log(feeds.length + \" FEEDS AVAILABLE\");    feeds.forEach(function (feed) {      console.log(feed.name, feed.key);    })  }}request(options, callback);```Using the ESP8266 Arduino HTTPClient library, an HTTPS GET request would look like this (replacing `---` with your own values in the appropriate locations):```arduino/// based on/// https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/examples/Authorization/Authorization.ino#include <Arduino.h>#include <ESP8266WiFi.h>#include <ESP8266WiFiMulti.h>#include <ESP8266HTTPClient.h>ESP8266WiFiMulti WiFiMulti;const char* ssid = \"---\";const char* password = \"---\";const char* host = \"io.adafruit.com\";const char* io_key = \"---\";const char* path_with_username = \"/api/v2/---/dashboards\";// Use web browser to view and copy// SHA1 fingerprint of the certificateconst char* fingerprint = \"77 00 54 2D DA E7 D8 03 27 31 23 99 EB 27 DB CB A5 4C 57 18\";void setup() {  Serial.begin(115200);  for(uint8_t t = 4; t > 0; t--) {    Serial.printf(\"[SETUP] WAIT %d...\\", t);    Serial.flush();    delay(1000);  }  WiFi.mode(WIFI_STA);  WiFiMulti.addAP(ssid, password);  // wait for WiFi connection  while(WiFiMulti.run() != WL_CONNECTED) {    Serial.print('.');    delay(1000);  }  Serial.println(\"[WIFI] connected!\");  HTTPClient http;  // start request with URL and TLS cert fingerprint for verification  http.begin(\"https://\" + String(host) + String(path_with_username), fingerprint);  // IO API authentication  http.addHeader(\"X-AIO-Key\", io_key);  // start connection and send HTTP header  int httpCode = http.GET();  // httpCode will be negative on error  if(httpCode > 0) {    // HTTP header has been send and Server response header has been handled    Serial.printf(\"[HTTP] GET response: %d\\", httpCode);    // HTTP 200 OK    if(httpCode == HTTP_CODE_OK) {      String payload = http.getString();      Serial.println(payload);    }    http.end();  }}void loop() {}```#### Client LibrariesWe have client libraries to help you get started with your project: [Python](https://github.com/adafruit/io-client-python), [Ruby](https://github.com/adafruit/io-client-ruby), [Arduino C++](https://github.com/adafruit/Adafruit_IO_Arduino), [Javascript](https://github.com/adafruit/adafruit-io-node), and [Go](https://github.com/adafruit/io-client-go) are available. They're all open source, so if they don't already do what you want, you can fork and add any feature you'd like.",
                    "title": "Adafruit IO REST API",
                    "version": "2.0.0",
                    "x-apisguru-categories": [
                        "iot"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_adafruit_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://raw.githubusercontent.com/adafruit/io-api/gh-pages/v2.json",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "adafruit.com"
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adafruit.com/2.0.0/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adafruit.com/2.0.0/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "adobe.com:aem": {
        "added": "2019-01-03T07:01:34.000Z",
        "preferred": "3.5.0-pre.0",
        "versions": {
            "3.5.0-pre.0": {
                "added": "2019-01-03T07:01:34.000Z",
                "info": {
                    "contact": {
                        "email": "opensource@shinesolutions.com",
                        "name": "Shine Solutions",
                        "url": "http://shinesolutions.com",
                        "x-twitter": "Adobe"
                    },
                    "description": "Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API",
                    "title": "Adobe Experience Manager (AEM) API",
                    "version": "3.5.0-pre.0",
                    "x-apisguru-categories": [
                        "marketing"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adobe_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/shinesolutions/swagger-aem/master/conf/api.yml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "adobe.com",
                    "x-serviceName": "aem",
                    "x-unofficialSpec": true
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adobe.com/aem/3.5.0-pre.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adobe.com/aem/3.5.0-pre.0/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "adyen.com:AccountService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Account API provides endpoints for managing account-related entities on your platform. These related entities include account holders, accounts, bank accounts, shareholders, and KYC-related documents. The management operations include actions such as creation, retrieval, updating, and deletion of them.For more information, refer to our [documentation](https://docs.adyen.com/platforms).## AuthenticationTo connect to the Account API, you must use basic authentication credentials of your web service user. If you don't have one, contact the [Adyen Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use its credentials to authenticate your request, for example:```curl-U \"ws@MarketPlace.YourMarketPlace\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningThe Account API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://cal-test.adyen.com/cal/services/Account/v6/createAccountHolder```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen for Platforms: Account API",
                    "version": "6",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/AccountService-v6.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "AccountService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/AccountService/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/AccountService/6/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:BalancePlatformService": {
        "added": "2021-06-14T12:42:12.263Z",
        "preferred": "1",
        "versions": {
            "1": {
                "added": "2021-06-14T12:42:12.263Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Balance Platform API enables you to create a platform, onboard users as account holders, create balance accounts, and issue cards.For information about use cases, refer to [Adyen Issuing](https://docs.adyen.com/issuing). ## AuthenticationYour Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example: ```curl-H \"Content-Type: application/json\" \\-H \"X-API-Key: YOUR_API_KEY\" \\...```Alternatively, you can use the username and password to connect to the API using basic authentication. For example:```curl-H \"Content-Type: application/json\" \\-U \"ws@BalancePlatform.YOUR_BALANCE_PLATFORM\":\"YOUR_WS_PASSWORD\" \\...```## VersioningBalance Platform API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://balanceplatform-api-test.adyen.com/bcl/v1```## Going liveWhen going live, your Adyen contact will provide your API credential for the live environment. You can then use the API key or the username and password to send requests to `https://balanceplatform-api-live.adyen.com/bcl/v1`.For more information, refer to our [Going live documentation](https://docs.adyen.com/issuing/integration-checklist#going-live).",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Issuing: Balance Platform API",
                    "version": "1",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_adyen.com_.resources_adyen-website_themes_images_apple-icon-180x180.png"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/BalancePlatformService-v1.json",
                            "version": "3.1"
                        }
                    ],
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "BalancePlatformService"
                },
                "updated": "2021-11-22T23:16:57.458Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/BalancePlatformService/1/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/BalancePlatformService/1/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:BinLookupService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "50",
        "versions": {
            "50": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The BIN Lookup API provides endpoints for retrieving information, such as cost estimates, and 3D Secure supported version based on a given BIN.",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen BinLookup API",
                    "version": "50",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/BinLookupService-v50.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "BinLookupService"
                },
                "updated": "2021-11-01T23:17:40.475Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/BinLookupService/50/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/BinLookupService/50/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:CheckoutService": {
        "added": "2021-11-01T23:17:40.475Z",
        "preferred": "68",
        "versions": {
            "68": {
                "added": "2021-11-01T23:17:40.475Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "Adyen Checkout API provides a simple and flexible way to initiate and authorise online payments. You can use the same integration for payments made with cards (including 3D Secure), mobile wallets, and local payment methods (for example, iDEAL and Sofort).This API reference provides information on available endpoints and how to interact with them. To learn more about the API, visit [Checkout documentation](https://docs.adyen.com/online-payments).## AuthenticationEach request to the Checkout API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the `X-API-Key` header value, for example:```curl-H \"Content-Type: application/json\" \\-H \"X-API-Key: Your_Checkout_API_key\" \\...```Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningCheckout API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://checkout-test.adyen.com/v68/payments```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen Checkout API",
                    "version": "68",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_adyen.com_.resources_adyen-website_themes_images_apple-icon-180x180.png"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/CheckoutService-v68.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "CheckoutService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/CheckoutService/68/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/CheckoutService/68/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:CheckoutUtilityService": {
        "added": "2021-06-18T13:57:32.889Z",
        "preferred": "1",
        "versions": {
            "1": {
                "added": "2021-06-18T13:57:32.889Z",
                "info": {
                    "contact": {
                        "email": "support@adyen.com",
                        "name": "Adyen Support",
                        "url": "https://support.adyen.com/",
                        "x-twitter": "Adyen"
                    },
                    "description": "A web service containing utility functions available for merchants integrating with Checkout APIs.## AuthenticationEach request to the Checkout Utility API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described in [How to get the Checkout API key](https://docs.adyen.com/developers/user-management/how-to-get-the-checkout-api-key). Then set this key to the `X-API-Key` header value, for example:```curl-H \"Content-Type: application/json\" \\-H \"X-API-Key: Your_Checkout_API_key\" \\...```Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/developers/api-reference/live-endpoints).## VersioningCheckout API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://checkout-test.adyen.com/v1/originKeys```",
                    "termsOfService": "https://docs.adyen.com/legal/terms-conditions",
                    "title": "Adyen Checkout Utility Service",
                    "version": "1",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "converter": {
                                "url": "https://github.com/lucybot/api-spec-converter",
                                "version": "2.7.11"
                            },
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/adyen/adyen-openapi/master/specs/3.0/CheckoutUtilityService-v1.json",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "adyen.com",
                    "x-serviceName": "CheckoutUtilityService"
                },
                "updated": "2021-06-18T13:57:32.889Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/CheckoutUtilityService/1/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/CheckoutUtilityService/1/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "adyen.com:FundService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Fund API provides endpoints for managing the funds in the accounts on your platform. These management operations include actions such as the transfer of funds from one account to another, the payout of funds to an account holder, and the retrieval of balances in an account.For more information, refer to our [documentation](https://docs.adyen.com/platforms).## AuthenticationTo connect to the Fund API, you must use basic authentication credentials of your web service user. If you don't have one, please contact the [Adyen Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use its credentials to authenticate your request, for example:```curl-U \"ws@MarketPlace.YourMarketPlace\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningThe Fund API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://cal-test.adyen.com/cal/services/Fund/v6/accountHolderBalance```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen for Platforms: Fund API",
                    "version": "6",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/FundService-v6.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "FundService"
                },
                "updated": "2021-11-01T23:17:40.475Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/FundService/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/FundService/6/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:HopService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Hosted onboarding API provides endpoints that you can use to generate links to Adyen-hosted pages, such as an [onboarding page](https://docs.adyen.com/platforms/hosted-onboarding-page) or a [PCI compliance questionnaire](https://docs.adyen.com/platforms/platforms-for-partners). Then you can provide the link to your account holder so they can complete their onboarding.## AuthenticationTo connect to the Hosted onboarding API, you must use basic authentication credentials of your web service user. If you don't have one, contact our [Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use your credentials to authenticate your request, for example:```curl-U \"ws@MarketPlace.YourMarketPlace\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningThe Hosted onboarding API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://cal-test.adyen.com/cal/services/Hop/v6/getOnboardingUrl```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen for Platforms: Hosted Onboarding",
                    "version": "6",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/HopService-v6.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "HopService"
                },
                "updated": "2021-11-01T23:17:40.475Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/HopService/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/HopService/6/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:MarketPayNotificationService": {
        "added": "2021-06-21T10:54:37.877Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2021-06-21T10:54:37.877Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Notification API sends notifications to the endpoints specified in a given subscription. Subscriptions are managed through the Notification Configuration API. The API specifications listed here detail the format of each notification.For more information, refer to our [documentation](https://docs.adyen.com/platforms/notifications).",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen for Platforms: Notifications",
                    "version": "6",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/MarketPayNotificationService-v6.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "MarketPayNotificationService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/MarketPayNotificationService/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/MarketPayNotificationService/6/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:NotificationConfigurationService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "6",
        "versions": {
            "6": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Notification Configuration API provides endpoints for setting up and testing notifications that inform you of events on your platform, for example when a KYC check or a payout has been completed.For more information, refer to our [documentation](https://docs.adyen.com/platforms/notifications).## AuthenticationTo connect to the Notification Configuration API, you must use basic authentication credentials of your web service user. If you don't have one, contact our [Adyen Support Team](https://support.adyen.com/hc/en-us/requests/new). Then use its credentials to authenticate your request, for example:```curl-U \"ws@MarketPlace.YourMarketPlace\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningThe Notification Configuration API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://cal-test.adyen.com/cal/services/Notification/v6/createNotificationConfiguration```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen for Platforms: Notification Configuration API",
                    "version": "6",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/NotificationConfigurationService-v6.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "NotificationConfigurationService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/NotificationConfigurationService/6/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/NotificationConfigurationService/6/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:PaymentService": {
        "added": "2021-11-01T23:17:40.475Z",
        "preferred": "68",
        "versions": {
            "68": {
                "added": "2021-11-01T23:17:40.475Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "A set of API endpoints that allow you to initiate, settle, and modify payments on the Adyen payments platform. You can use the API to accept card payments (including One-Click and 3D Secure), bank transfers, ewallets, and many other payment methods.To learn more about the API, visit [Classic integration](https://docs.adyen.com/classic-integration).## AuthenticationTo connect to the Payments API, you must use your basic authentication credentials. For this, create your web service user, as described in [How to get the WS user password](https://docs.adyen.com/development-resources/api-credentials). Then use its credentials to authenticate your request, for example:```curl-U \"ws@Company.YourCompany\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningPayments API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://pal-test.adyen.com/pal/servlet/Payment/v68/authorise```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen Payment API",
                    "version": "68",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/PaymentService-v68.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "PaymentService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/PaymentService/68/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/PaymentService/68/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:PayoutService": {
        "added": "2021-11-01T23:17:40.475Z",
        "preferred": "68",
        "versions": {
            "68": {
                "added": "2021-11-01T23:17:40.475Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "A set of API endpoints that allow you to store payout details, confirm, or decline a payout.For more information, refer to [Online payouts](https://docs.adyen.com/online-payments/online-payouts).## AuthenticationTo use the Payout API, you need to have [two API credentials](https://docs.adyen.com/online-payments/online-payouts#payouts-to-bank-accounts-and-wallets): one for storing payout details and submitting payouts, and another one for confirming or declining payouts. If you don't have the required API credentials, contact our [Support Team](https://support.adyen.com/hc/en-us/requests/new).Both of these API credentials must be authenticated with [basic authentication](https://docs.adyen.com/development-resources/api-credentials#basic-authentication).The following example shows how to authenticate your request when submitting a payout:```curl-U \"storePayout@Company.[YourCompany]\":\"YourBasicAuthenticationPassword\" \\-H \"Content-Type: application/json\" \\...```When going live, you need to generate new API credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen Payout API",
                    "version": "68",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/PayoutService-v68.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "PayoutService"
                },
                "updated": "2021-11-12T23:18:19.544Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/PayoutService/68/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/PayoutService/68/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:RecurringService": {
        "added": "2021-11-01T23:17:40.475Z",
        "preferred": "68",
        "versions": {
            "68": {
                "added": "2021-11-01T23:17:40.475Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request.For more information, refer to our [Tokenization documentation](https://docs.adyen.com/online-payments/tokenization).## AuthenticationTo connect to the Recurring API, you must use your basic authentication credentials. For this, create your web service user, as described in [How to get the WS user password](https://docs.adyen.com/development-resources/api-credentials). Then use its credentials to authenticate your request, for example:```curl-U \"ws@Company.YourCompany\":\"YourWsPassword\" \\-H \"Content-Type: application/json\" \\...```Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).## VersioningRecurring API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://pal-test.adyen.com/pal/servlet/Recurring/v68/disable```",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen Recurring API",
                    "version": "68",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/RecurringService-v68.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "RecurringService"
                },
                "updated": "2021-11-02T23:15:52.596Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/RecurringService/68/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/RecurringService/68/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:TestCardService": {
        "added": "2020-11-03T12:51:40.318Z",
        "preferred": "1",
        "versions": {
            "1": {
                "added": "2020-11-03T12:51:40.318Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Test Cards API provides endpoints for generating custom test card numbers. For more information, refer to [Custom test cards](https://docs.adyen.com/development-resources/test-cards/create-test-cards) documentation.",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Adyen Test Cards API",
                    "version": "1",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/TestCardService-v1.json",
                            "version": "3.1"
                        }
                    ],
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "TestCardService"
                },
                "updated": "2021-08-09T23:18:27.796Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/TestCardService/1/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/TestCardService/1/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "adyen.com:TransferService": {
        "added": "2021-11-01T23:17:40.475Z",
        "preferred": "2",
        "versions": {
            "2": {
                "added": "2021-11-01T23:17:40.475Z",
                "info": {
                    "contact": {
                        "email": "developer-experience@adyen.com",
                        "name": "Adyen Developer Experience team",
                        "url": "https://www.adyen.help/hc/en-us/community/topics",
                        "x-twitter": "Adyen"
                    },
                    "description": "The Balance Platform Transfers API provides an endpoint that you can use to move funds within your balance platform, or to send funds from your balance platform to a [transfer instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/transferInstruments).For information on how the API is used in Adyen Issuing, refer to [Manage funds](https://docs.adyen.com/issuing/manage-funds#transfer).## AuthenticationYour Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example: ```curl-H \"Content-Type: application/json\" \\-H \"X-API-Key: YOUR_API_KEY\" \\...```Alternatively, you can use the username and password to connect to the API using basic authentication. For example:```curl-H \"Content-Type: application/json\" \\-U \"ws@BalancePlatform.YOUR_BALANCE_PLATFORM\":\"YOUR_WS_PASSWORD\" \\...```## Roles and permissionsTo use the Balance Platforms Transfers API, you need an additional role for your API credential. Transfers must also be enabled for the source balance account. Your Adyen contact will set up the roles and permissions for you.## VersioningThe Balance Platform Transfers API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.For example:```https://balanceplatform-api-test.adyen.com/btl/v1```## Going liveWhen going live, your Adyen contact will provide your API credential for the live environment. You can then use the username and password to send requests to `https://balanceplatform-api-live.adyen.com/btl/v1`.For more information, refer to our [Going live documentation](https://docs.adyen.com/issuing/integration-checklist#going-live).",
                    "termsOfService": "https://www.adyen.com/legal/terms-and-conditions",
                    "title": "Balance Platform Transfers API",
                    "version": "2",
                    "x-apisguru-categories": [
                        "payment"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_Adyen_profile_image"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/Adyen/adyen-openapi/master/json/TransferService-v2.json",
                            "version": "3.1"
                        }
                    ],
                    "x-preferred": true,
                    "x-providerName": "adyen.com",
                    "x-publicVersion": true,
                    "x-serviceName": "TransferService"
                },
                "updated": "2021-11-02T23:15:52.596Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/adyen.com/TransferService/2/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/adyen.com/TransferService/2/openapi.yaml",
                "openapiVer": "3.1.0"
            }
        }
    },
    "afterbanks.com": {
        "added": "2017-09-20T14:12:57.000Z",
        "preferred": "3.0.0",
        "versions": {
            "3.0.0": {
                "added": "2017-09-20T14:12:57.000Z",
                "info": {
                    "description": "La estandarización de la conexión con cualquier banco en tiempo real.",
                    "title": "Afterbanks API",
                    "version": "3.0.0",
                    "x-apisguru-categories": [
                        "financial"
                    ],
                    "x-description-language": "es",
                    "x-logo": {
                        "backgroundColor": "#FFFFFF",
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_AfterbanksAPI_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://www.afterbanks.com/api/documentation/es/swagger.yaml",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "afterbanks.com"
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/afterbanks.com/3.0.0/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/afterbanks.com/3.0.0/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "agco-ats.com": {
        "added": "2018-03-03T18:20:03.000Z",
        "preferred": "v1",
        "versions": {
            "v1": {
                "added": "2018-03-03T18:20:03.000Z",
                "info": {
                    "contact": {
                        "x-twitter": "AGCOcorp"
                    },
                    "title": "AGCO API",
                    "version": "v1",
                    "x-apisguru-categories": [
                        "ecommerce"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_AGCOcorp_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://secure.agco-ats.com:443/swagger/docs/v1",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "agco-ats.com"
                },
                "updated": "2021-08-09T09:15:57.964Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/agco-ats.com/v1/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/agco-ats.com/v1/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "aiception.com": {
        "added": "2019-02-26T16:02:41.000Z",
        "preferred": "1.0.0",
        "versions": {
            "1.0.0": {
                "added": "2019-02-26T16:02:41.000Z",
                "info": {
                    "contact": {
                        "x-twitter": "AIception"
                    },
                    "description": "Here you can play & test & prototype all the endpoints using just your browser! Go ahead!",
                    "title": "AIception Interactive",
                    "version": "1.0.0",
                    "x-apisguru-categories": [
                        "machine_learning"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_AIception_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://aiception.com/static/swagger.json",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "aiception.com"
                },
                "updated": "2019-02-26T16:02:41.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/aiception.com/1.0.0/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/aiception.com/1.0.0/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "airbyte.local:config": {
        "added": "2021-02-18T18:44:25.146Z",
        "preferred": "1.0.0",
        "versions": {
            "1.0.0": {
                "added": "2021-02-18T18:44:25.146Z",
                "info": {
                    "contact": {
                        "email": "contact@airbyte.io"
                    },
                    "description": "Airbyte Configuration API[https://airbyte.io](https://airbyte.io).This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.Here are some conventions that this API follows:* All endpoints are http POST methods.* All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params.* The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`.* For all `update` methods, the whole object must be passed in, even the fields that did not change.Change Management:* The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create`* Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests.* All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):  * Adding fields to request or response bodies.  * Adding new HTTP endpoints.",
                    "license": {
                        "name": "MIT",
                        "url": "https://opensource.org/licenses/MIT"
                    },
                    "title": "Airbyte Configuration API",
                    "version": "1.0.0",
                    "x-apisguru-categories": [
                        "developer_tools"
                    ],
                    "x-origin": [
                        {
                            "format": "openapi",
                            "url": "https://raw.githubusercontent.com/airbytehq/airbyte/master/airbyte-api/src/main/openapi/config.yaml",
                            "version": "3.0"
                        }
                    ],
                    "x-providerName": "airbyte.local",
                    "x-serviceName": "config",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_apis.guru_assets_images_no-logo.svg"
                    }
                },
                "externalDocs": {
                    "description": "Find out more about Airbyte",
                    "url": "https://airbyte.io"
                },
                "updated": "2021-08-02T09:20:32.823Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/airbyte.local/config/1.0.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/airbyte.local/config/1.0.0/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "airport-web.appspot.com": {
        "added": "2017-09-26T15:09:23.000Z",
        "preferred": "v1",
        "versions": {
            "v1": {
                "added": "2017-09-26T15:09:23.000Z",
                "info": {
                    "description": "Get name and website-URL for airports by ICAO code. Covered airports are mostly in Germany.",
                    "title": "airportsapi",
                    "version": "v1",
                    "x-apisguru-categories": [
                        "transport"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_user-images.githubusercontent.com_21603_37955263-098e5b38-31a0-11e8-96fd-5755b16341e3.png"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://airport-web.appspot.com/api/docs/swagger.json",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "airport-web.appspot.com"
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/airport-web.appspot.com/v1/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/airport-web.appspot.com/v1/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "akeneo.com": {
        "added": "2019-04-30T10:47:37.000Z",
        "preferred": "1.0.0",
        "versions": {
            "1.0.0": {
                "added": "2019-04-30T10:47:37.000Z",
                "info": {
                    "contact": {
                        "x-twitter": "akeneopim"
                    },
                    "title": "Akeneo PIM REST API",
                    "version": "1.0.0",
                    "x-apisguru-categories": [
                        "enterprise"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_akeneopim_profile_image.jpeg"
                    },
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://raw.githubusercontent.com/akeneo/pim-api-docs/master/content/swagger/akeneo-web-api.json",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "akeneo.com"
                },
                "updated": "2021-07-05T15:07:17.927Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/akeneo.com/1.0.0/swagger.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/akeneo.com/1.0.0/swagger.yaml",
                "openapiVer": "2.0"
            }
        }
    },
    "amadeus.com": {
        "added": "2020-09-04T08:31:58.705Z",
        "preferred": "2.2.0",
        "versions": {
            "2.2.0": {
                "added": "2020-09-04T08:31:58.705Z",
                "info": {
                    "description": "Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token. Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).",
                    "title": "Flight Offers Search",
                    "version": "2.2.0",
                    "x-apisguru-categories": [
                        "location"
                    ],
                    "x-origin": [
                        {
                            "format": "swagger",
                            "url": "https://developers.amadeus.com/PAS-EAS/api/v0/documents/10181/file",
                            "version": "2.0"
                        }
                    ],
                    "x-providerName": "amadeus.com",
                    "x-release-note": {
                        "2.0.0": [
                            "Initial Version",
                            "Includes search and price flight offer"
                        ],
                        "2.1.0": [
                            "Add currencies, aircraft and carriers dictionary"
                        ],
                        "2.2.0": [
                            "Add maxPrice filtering"
                        ]
                    },
                    "x-status": "validated",
                    "x-tags": [
                        "#online-retail",
                        "#mobile-services",
                        "#ama-for-dev"
                    ],
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_apis.guru_assets_images_no-logo.svg"
                    }
                },
                "updated": "2021-06-21T12:16:53.715Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amadeus.com/2.2.0/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amadeus.com/2.2.0/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:AWSMigrationHub": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-05-31",
        "versions": {
            "2017-05-31": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-05-31",
                    "x-release": "v4",
                    "title": "AWS Migration Hub",
                    "description": "<p>The AWS Migration Hub API methods help to obtain server and application migration status and integrate your resource-specific migration tool by providing a programmatic interface to Migration Hub.</p> <p>Remember that you must set your AWS Migration Hub home region before you call any of these APIs, or a <code>HomeRegionNotSetException</code> error will be returned. Also, you must make the API calls while in your home region.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "AWSMigrationHub",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/AWSMigrationHub-2017-05-31.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/mgh/"
                },
                "updated": "2020-04-16T18:45:33.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/AWSMigrationHub/2017-05-31/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/AWSMigrationHub/2017-05-31/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:accessanalyzer": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-11-01",
        "versions": {
            "2019-11-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-11-01",
                    "x-release": "v4",
                    "title": "Access Analyzer",
                    "description": "<p>Identity and Access Management Access Analyzer helps identify potential resource-access risks by enabling you to identify any policies that grant access to an external principal. It does this by using logic-based reasoning to analyze resource-based policies in your Amazon Web Services environment. An external principal can be another Amazon Web Services account, a root user, an IAM user or role, a federated user, an Amazon Web Services service, or an anonymous user. You can also use IAM Access Analyzer to preview and validate public and cross-account access to your resources before deploying permissions changes. This guide describes the Identity and Access Management Access Analyzer operations that you can call programmatically. For general information about IAM Access Analyzer, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html\">Identity and Access Management Access Analyzer</a> in the <b>IAM User Guide</b>.</p> <p>To start using IAM Access Analyzer, you first need to create an analyzer.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "accessanalyzer",
                    "x-aws-signingName": "access-analyzer",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/accessanalyzer-2019-11-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/access-analyzer/"
                },
                "updated": "2020-04-27T20:04:05.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/accessanalyzer/2019-11-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/accessanalyzer/2019-11-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:acm": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-12-08",
        "versions": {
            "2015-12-08": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-12-08",
                    "x-release": "v4",
                    "title": "AWS Certificate Manager",
                    "description": "<fullname>Amazon Web Services Certificate Manager</fullname> <p>You can use Amazon Web Services Certificate Manager (ACM) to manage SSL/TLS certificates for your Amazon Web Services-based websites and applications. For more information about using ACM, see the <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/\">Amazon Web Services Certificate Manager User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "acm",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/acm-2015-12-08.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/acm/"
                },
                "updated": "2020-03-23T09:21:07.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/acm/2015-12-08/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/acm/2015-12-08/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:acm-pca": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-08-22",
        "versions": {
            "2017-08-22": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-08-22",
                    "x-release": "v4",
                    "title": "AWS Certificate Manager Private Certificate Authority",
                    "description": "<p>This is the <i>ACM Private CA API Reference</i>. It provides descriptions, syntax, and usage examples for each of the actions and data types involved in creating and managing private certificate authorities (CA) for your organization.</p> <p>The documentation for each action shows the Query API request parameters and the XML response. Alternatively, you can use one of the AWS SDKs to access an API that's tailored to the programming language or platform that you're using. For more information, see <a href=\"https://aws.amazon.com/tools/#SDKs\">AWS SDKs</a>.</p> <p>Each ACM Private CA API operation has a quota that determines the number of times the operation can be called per second. ACM Private CA throttles API requests at different rates depending on the operation. Throttling means that ACM Private CA rejects an otherwise valid request because the request exceeds the operation's quota for the number of requests per second. When a request is throttled, ACM Private CA returns a <a href=\"https://docs.aws.amazon.com/acm-pca/latest/APIReference/CommonErrors.html\">ThrottlingException</a> error. ACM Private CA does not guarantee a minimum request rate for APIs. </p> <p>To see an up-to-date list of your ACM Private CA quotas, or to request a quota increase, log into your AWS account and visit the <a href=\"https://console.aws.amazon.com/servicequotas/\">Service Quotas</a> console.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "acm-pca",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/acm-pca-2017-08-22.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/acm-pca/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/acm-pca/2017-08-22/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/acm-pca/2017-08-22/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:alexaforbusiness": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-11-09",
        "versions": {
            "2017-11-09": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-11-09",
                    "x-release": "v4",
                    "title": "Alexa For Business",
                    "description": "Alexa for Business helps you use Alexa in your organization. Alexa for Business provides you with the tools to manage Alexa devices, enroll your users, and assign skills, at scale. You can build your own context-aware voice skills using the Alexa Skills Kit and the Alexa for Business API operations. You can also make these available as private skills for your organization. Alexa for Business makes it efficient to voice-enable your products and services, thus providing context-aware voice experiences for your customers. Device makers building with the Alexa Voice Service (AVS) can create fully integrated solutions, register their products with Alexa for Business, and manage them as shared devices in their organization. ",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "alexaforbusiness",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/alexaforbusiness-2017-11-09.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/a4b/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/alexaforbusiness/2017-11-09/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/alexaforbusiness/2017-11-09/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:amp": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-08-01",
        "versions": {
            "2020-08-01": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-08-01",
                    "x-release": "v4",
                    "title": "Amazon Prometheus Service",
                    "description": "Amazon Managed Service for Prometheus",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "amp",
                    "x-aws-signingName": "aps",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/amp-2020-08-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/aps/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amp/2020-08-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amp/2020-08-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:amplify": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-07-25",
        "versions": {
            "2017-07-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-07-25",
                    "x-release": "v4",
                    "title": "AWS Amplify",
                    "description": "Amplify enables developers to develop and deploy cloud-powered mobile and web apps. The Amplify Console provides a continuous delivery and hosting service for web applications. For more information, see the <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html\">Amplify Console User Guide</a>. The Amplify Framework is a comprehensive set of SDKs, libraries, tools, and documentation for client app development. For more information, see the <a href=\"https://docs.amplify.aws/\">Amplify Framework.</a> ",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "amplify",
                    "x-aws-signingName": "amplify",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/amplify-2017-07-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/amplify/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amplify/2017-07-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amplify/2017-07-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:amplifybackend": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-08-11",
        "versions": {
            "2020-08-11": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-08-11",
                    "x-release": "v4",
                    "title": "AmplifyBackend",
                    "description": "AWS Amplify Admin API",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "amplifybackend",
                    "x-aws-signingName": "amplifybackend",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/amplifybackend-2020-08-11.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/amplifybackend/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amplifybackend/2020-08-11/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/amplifybackend/2020-08-11/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:apigateway": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-07-09",
        "versions": {
            "2015-07-09": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-07-09",
                    "x-release": "v4",
                    "title": "Amazon API Gateway",
                    "description": "<fullname>Amazon API Gateway</fullname> <p>Amazon API Gateway helps developers deliver robust, secure, and scalable mobile and web application back ends. API Gateway allows developers to securely connect mobile and web applications to APIs that run on AWS Lambda, Amazon EC2, or other publicly addressable web services that are hosted outside of AWS.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "apigateway",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/apigateway-2015-07-09.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/apigateway/"
                },
                "updated": "2020-05-04T20:09:16.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigateway/2015-07-09/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigateway/2015-07-09/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:apigatewaymanagementapi": {
        "added": "2018-12-18T23:56:32.000Z",
        "preferred": "2018-11-29",
        "versions": {
            "2018-11-29": {
                "added": "2018-12-18T23:56:32.000Z",
                "info": {
                    "version": "2018-11-29",
                    "x-release": "v4",
                    "title": "AmazonApiGatewayManagementApi",
                    "description": "The Amazon API Gateway Management API allows you to directly manage runtime aspects of your deployed APIs. To use it, you must explicitly set the SDK's endpoint to point to the endpoint of your deployed API. The endpoint will be of the form https://{api-id}.execute-api.{region}.amazonaws.com/{stage}, or will be the endpoint corresponding to your API's custom domain and base path, if applicable.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "apigatewaymanagementapi",
                    "x-aws-signingName": "execute-api",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/apigatewaymanagementapi-2018-11-29.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/execute-api/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigatewaymanagementapi/2018-11-29/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigatewaymanagementapi/2018-11-29/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:apigatewayv2": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-11-29",
        "versions": {
            "2018-11-29": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-11-29",
                    "x-release": "v4",
                    "title": "AmazonApiGatewayV2",
                    "description": "Amazon API Gateway V2",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "apigatewayv2",
                    "x-aws-signingName": "apigateway",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/apigatewayv2-2018-11-29.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/apigateway/"
                },
                "updated": "2020-04-21T06:33:24.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigatewayv2/2018-11-29/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apigatewayv2/2018-11-29/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appconfig": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-10-09",
        "versions": {
            "2019-10-09": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-10-09",
                    "x-release": "v4",
                    "title": "Amazon AppConfig",
                    "description": "<fullname>AWS AppConfig</fullname> <p>Use AWS AppConfig, a capability of AWS Systems Manager, to create, manage, and quickly deploy application configurations. AppConfig supports controlled deployments to applications of any size and includes built-in validation checks and monitoring. You can use AppConfig with applications hosted on Amazon EC2 instances, AWS Lambda, containers, mobile applications, or IoT devices.</p> <p>To prevent errors when deploying application configurations, especially for production systems where a simple typo could cause an unexpected outage, AppConfig includes validators. A validator provides a syntactic or semantic check to ensure that the configuration you want to deploy works as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.</p> <p>During a configuration deployment, AppConfig monitors the application to ensure that the deployment is successful. If the system encounters an error, AppConfig rolls back the change to minimize impact for your application users. You can configure a deployment strategy for each application or environment that includes deployment criteria, including velocity, bake time, and alarms to monitor. Similar to error monitoring, if a deployment triggers an alarm, AppConfig automatically rolls back to the previous version. </p> <p>AppConfig supports multiple use cases. Here are some examples.</p> <ul> <li> <p> <b>Application tuning</b>: Use AppConfig to carefully introduce changes to your application that can only be tested with production traffic.</p> </li> <li> <p> <b>Feature toggle</b>: Use AppConfig to turn on new features that require a timely deployment, such as a product launch or announcement. </p> </li> <li> <p> <b>Allow list</b>: Use AppConfig to allow premium subscribers to access paid content. </p> </li> <li> <p> <b>Operational issues</b>: Use AppConfig to reduce stress on your application when a dependency or other external factor impacts the system.</p> </li> </ul> <p>This reference is intended to be used with the <a href=\"http://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig.html\">AWS AppConfig User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appconfig",
                    "x-aws-signingName": "appconfig",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appconfig-2019-10-09.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/appconfig/"
                },
                "updated": "2020-05-07T20:22:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appconfig/2019-10-09/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appconfig/2019-10-09/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appflow": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-08-23",
        "versions": {
            "2020-08-23": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-08-23",
                    "x-release": "v4",
                    "title": "Amazon Appflow",
                    "description": "<p>Welcome to the Amazon AppFlow API reference. This guide is for developers who need detailed information about the Amazon AppFlow API operations, data types, and errors. </p> <p>Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between software as a service (SaaS) applications like Salesforce, Marketo, Slack, and ServiceNow, and Amazon Web Services like Amazon S3 and Amazon Redshift. </p> <p>Use the following links to get started on the Amazon AppFlow API:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Operations.html\">Actions</a>: An alphabetical list of all Amazon AppFlow API operations.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Types.html\">Data types</a>: An alphabetical list of all Amazon AppFlow data types.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonParameters.html\">Common parameters</a>: Parameters that all Query operations can use.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonErrors.html\">Common errors</a>: Client and server errors that all operations can return.</p> </li> </ul> <p>If you're new to Amazon AppFlow, we recommend that you review the <a href=\"https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html\">Amazon AppFlow User Guide</a>.</p> <p>Amazon AppFlow API users can use vendor-specific mechanisms for OAuth, and include applicable OAuth attributes (such as <code>auth-code</code> and <code>redirecturi</code>) with the connector-specific <code>ConnectorProfileProperties</code> when creating a new connector profile using Amazon AppFlow API operations. For example, Salesforce users can refer to the <a href=\"https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm\"> <i>Authorize Apps with OAuth</i> </a> documentation.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appflow",
                    "x-aws-signingName": "appflow",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appflow-2020-08-23.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/appflow/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appflow/2020-08-23/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appflow/2020-08-23/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appintegrations": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-07-29",
        "versions": {
            "2020-07-29": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-07-29",
                    "x-release": "v4",
                    "title": "Amazon AppIntegrations Service",
                    "description": "<p>The Amazon AppIntegrations service enables you to configure and reuse connections to external applications.</p> <p>For information about how you can use external applications with Amazon Connect, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/crm.html\">Set up pre-built integrations</a> in the <i>Amazon Connect Administrator Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appintegrations",
                    "x-aws-signingName": "app-integrations",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appintegrations-2020-07-29.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/app-integrations/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appintegrations/2020-07-29/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appintegrations/2020-07-29/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:application-autoscaling": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-02-06",
        "versions": {
            "2016-02-06": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-02-06",
                    "x-release": "v4",
                    "title": "Application Auto Scaling",
                    "description": "<p>With Application Auto Scaling, you can configure automatic scaling for the following resources:</p> <ul> <li> <p>Amazon AppStream 2.0 fleets</p> </li> <li> <p>Amazon Aurora Replicas</p> </li> <li> <p>Amazon Comprehend document classification and entity recognizer endpoints</p> </li> <li> <p>Amazon DynamoDB tables and global secondary indexes throughput capacity</p> </li> <li> <p>Amazon ECS services</p> </li> <li> <p>Amazon ElastiCache for Redis clusters (replication groups)</p> </li> <li> <p>Amazon EMR clusters</p> </li> <li> <p>Amazon Keyspaces (for Apache Cassandra) tables</p> </li> <li> <p>Lambda function provisioned concurrency</p> </li> <li> <p>Amazon Managed Streaming for Apache Kafka broker storage</p> </li> <li> <p>Amazon SageMaker endpoint variants</p> </li> <li> <p>Spot Fleet (Amazon EC2) requests</p> </li> <li> <p>Custom resources provided by your own applications or services</p> </li> </ul> <p> <b>API Summary</b> </p> <p>The Application Auto Scaling service API includes three key sets of actions: </p> <ul> <li> <p>Register and manage scalable targets - Register Amazon Web Services or custom resources as scalable targets (a resource that Application Auto Scaling can scale), set minimum and maximum capacity limits, and retrieve information on existing scalable targets.</p> </li> <li> <p>Configure and manage automatic scaling - Define scaling policies to dynamically scale your resources in response to CloudWatch alarms, schedule one-time or recurring scaling actions, and retrieve your recent scaling activity history.</p> </li> <li> <p>Suspend and resume scaling - Temporarily suspend and later resume automatic scaling by calling the <a href=\"https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html\">RegisterScalableTarget</a> API action for any Application Auto Scaling scalable target. You can suspend and resume (individually or in combination) scale-out activities that are triggered by a scaling policy, scale-in activities that are triggered by a scaling policy, and scheduled scaling.</p> </li> </ul> <p>To learn more about Application Auto Scaling, including information about granting IAM users required permissions for Application Auto Scaling actions, see the <a href=\"https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html\">Application Auto Scaling User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "application-autoscaling",
                    "x-aws-signingName": "application-autoscaling",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/application-autoscaling-2016-02-06.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/application-autoscaling/"
                },
                "updated": "2020-04-23T20:32:41.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/application-autoscaling/2016-02-06/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/application-autoscaling/2016-02-06/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:application-insights": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-11-25",
        "versions": {
            "2018-11-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-11-25",
                    "x-release": "v4",
                    "title": "Amazon CloudWatch Application Insights",
                    "description": "<fullname>Amazon CloudWatch Application Insights</fullname> <p> Amazon CloudWatch Application Insights is a service that helps you detect common problems with your applications. It enables you to pinpoint the source of issues in your applications (built with technologies such as Microsoft IIS, .NET, and Microsoft SQL Server), by providing key insights into detected problems.</p> <p>After you onboard your application, CloudWatch Application Insights identifies, recommends, and sets up metrics and logs. It continuously analyzes and correlates your metrics and logs for unusual behavior to surface actionable problems with your application. For example, if your application is slow and unresponsive and leading to HTTP 500 errors in your Application Load Balancer (ALB), Application Insights informs you that a memory pressure problem with your SQL Server database is occurring. It bases this analysis on impactful metrics and log errors. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "application-insights",
                    "x-aws-signingName": "applicationinsights",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/application-insights-2018-11-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/applicationinsights/"
                },
                "updated": "2020-03-25T18:54:51.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/application-insights/2018-11-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/application-insights/2018-11-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:applicationcostprofiler": {
        "added": "2021-06-18T13:57:32.889Z",
        "preferred": "2020-09-10",
        "versions": {
            "2020-09-10": {
                "added": "2021-06-18T13:57:32.889Z",
                "info": {
                    "version": "2020-09-10",
                    "x-release": "v4",
                    "title": "AWS Application Cost Profiler",
                    "description": "<p>This reference provides descriptions of the AWS Application Cost Profiler API.</p> <p>The AWS Application Cost Profiler API provides programmatic access to view, create, update, and delete application cost report definitions, as well as to import your usage data into the Application Cost Profiler service.</p> <p>For more information about using this service, see the <a href=\"https://docs.aws.amazon.com/application-cost-profiler/latest/userguide/introduction.html\">AWS Application Cost Profiler User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "applicationcostprofiler",
                    "x-aws-signingName": "application-cost-profiler",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/applicationcostprofiler-2020-09-10.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/application-cost-profiler/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/applicationcostprofiler/2020-09-10/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/applicationcostprofiler/2020-09-10/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appmesh": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-01-25",
        "versions": {
            "2019-01-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-01-25",
                    "x-release": "v4",
                    "title": "AWS App Mesh",
                    "description": "<p>App Mesh is a service mesh based on the Envoy proxy that makes it easy to monitor and control microservices. App Mesh standardizes how your microservices communicate, giving you end-to-end visibility and helping to ensure high availability for your applications.</p> <p>App Mesh gives you consistent visibility and network traffic controls for every microservice in an application. You can use App Mesh with Amazon Web Services Fargate, Amazon ECS, Amazon EKS, Kubernetes on Amazon Web Services, and Amazon EC2.</p> <note> <p>App Mesh supports microservice applications that use service discovery naming for their components. For more information about service discovery on Amazon ECS, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service Discovery</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. Kubernetes <code>kube-dns</code> and <code>coredns</code> are supported. For more information, see <a href=\"https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/\">DNS for Services and Pods</a> in the Kubernetes documentation.</p> </note>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appmesh",
                    "x-aws-signingName": "appmesh",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appmesh-2019-01-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/appmesh/"
                },
                "updated": "2020-03-07T10:12:22.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appmesh/2019-01-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appmesh/2019-01-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:apprunner": {
        "added": "2021-06-18T13:57:32.889Z",
        "preferred": "2020-05-15",
        "versions": {
            "2020-05-15": {
                "added": "2021-06-18T13:57:32.889Z",
                "info": {
                    "version": "2020-05-15",
                    "x-release": "v4",
                    "title": "AWS App Runner",
                    "description": "<fullname>AWS App Runner</fullname> <p>AWS App Runner is an application service that provides a fast, simple, and cost-effective way to go directly from an existing container image or source code to a running service in the AWS cloud in seconds. You don't need to learn new technologies, decide which compute service to use, or understand how to provision and configure AWS resources.</p> <p>App Runner connects directly to your container registry or source code repository. It provides an automatic delivery pipeline with fully managed operations, high performance, scalability, and security.</p> <p>For more information about App Runner, see the <a href=\"https://docs.aws.amazon.com/apprunner/latest/dg/\">AWS App Runner Developer Guide</a>. For release information, see the <a href=\"https://docs.aws.amazon.com/apprunner/latest/relnotes/\">AWS App Runner Release Notes</a>.</p> <p> To install the Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command line tools that you can use to access the API, see <a href=\"http://aws.amazon.com/tools/\">Tools for Amazon Web Services</a>.</p> <p> <b>Endpoints</b> </p> <p>For a list of Region-specific endpoints that App Runner supports, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/apprunner.html\">AWS App Runner endpoints and quotas</a> in the <i>AWS General Reference</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "apprunner",
                    "x-aws-signingName": "apprunner",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/apprunner-2020-05-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/apprunner/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apprunner/2020-05-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/apprunner/2020-05-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appstream": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-12-01",
        "versions": {
            "2016-12-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-12-01",
                    "x-release": "v4",
                    "title": "Amazon AppStream",
                    "description": "<fullname>Amazon AppStream 2.0</fullname> <p>This is the <i>Amazon AppStream 2.0 API Reference</i>. This documentation provides descriptions and syntax for each of the actions and data types in AppStream 2.0. AppStream 2.0 is a fully managed, secure application streaming service that lets you stream desktop applications to users without rewriting applications. AppStream 2.0 manages the AWS resources that are required to host and run your applications, scales automatically, and provides access to your users on demand. </p> <note> <p>You can call the AppStream 2.0 API operations by using an interface VPC endpoint (interface endpoint). For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html\">Access AppStream 2.0 API Operations and CLI Commands Through an Interface VPC Endpoint</a> in the <i>Amazon AppStream 2.0 Administration Guide</i>.</p> </note> <p>To learn more about AppStream 2.0, see the following resources:</p> <ul> <li> <p> <a href=\"http://aws.amazon.com/appstream2\">Amazon AppStream 2.0 product page</a> </p> </li> <li> <p> <a href=\"http://aws.amazon.com/documentation/appstream2\">Amazon AppStream 2.0 documentation</a> </p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appstream",
                    "x-aws-signingName": "appstream",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appstream-2016-12-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/appstream2/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appstream/2016-12-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appstream/2016-12-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:appsync": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-07-25",
        "versions": {
            "2017-07-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-07-25",
                    "x-release": "v4",
                    "title": "AWS AppSync",
                    "description": "AppSync provides API actions for creating and interacting with data sources using GraphQL from your application.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "appsync",
                    "x-aws-signingName": "appsync",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/appsync-2017-07-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/appsync/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appsync/2017-07-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/appsync/2017-07-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:athena": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-05-18",
        "versions": {
            "2017-05-18": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-05-18",
                    "x-release": "v4",
                    "title": "Amazon Athena",
                    "description": "<p>Amazon Athena is an interactive query service that lets you use standard SQL to analyze data directly in Amazon S3. You can point Athena at your data in Amazon S3 and run ad-hoc queries and get results in seconds. Athena is serverless, so there is no infrastructure to set up or manage. You pay only for the queries you run. Athena scales automatically—executing queries in parallel—so results are fast, even with large datasets and complex queries. For more information, see <a href=\"http://docs.aws.amazon.com/athena/latest/ug/what-is.html\">What is Amazon Athena</a> in the <i>Amazon Athena User Guide</i>.</p> <p>If you connect to Athena using the JDBC driver, use version 1.1.0 of the driver or later with the Amazon Athena API. Earlier version drivers do not support the API. For more information and to download the driver, see <a href=\"https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html\">Accessing Amazon Athena with JDBC</a>.</p> <p>For code samples using the Amazon Web Services SDK for Java, see <a href=\"https://docs.aws.amazon.com/athena/latest/ug/code-samples.html\">Examples and Code Samples</a> in the <i>Amazon Athena User Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "athena",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/athena-2017-05-18.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/athena/"
                },
                "updated": "2020-03-25T07:24:09.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/athena/2017-05-18/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/athena/2017-05-18/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:auditmanager": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2017-07-25",
        "versions": {
            "2017-07-25": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2017-07-25",
                    "x-release": "v4",
                    "title": "AWS Audit Manager",
                    "description": "<p>Welcome to the Audit Manager API reference. This guide is for developers who need detailed information about the Audit Manager API operations, data types, and errors. </p> <p>Audit Manager is a service that provides automated evidence collection so that you can continuously audit your Amazon Web Services usage, and assess the effectiveness of your controls to better manage risk and simplify compliance.</p> <p>Audit Manager provides pre-built frameworks that structure and automate assessments for a given compliance standard. Frameworks include a pre-built collection of controls with descriptions and testing procedures, which are grouped according to the requirements of the specified compliance standard or regulation. You can also customize frameworks and controls to support internal audits with unique requirements. </p> <p>Use the following links to get started with the Audit Manager API:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Operations.html\">Actions</a>: An alphabetical list of all Audit Manager API operations.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Types.html\">Data types</a>: An alphabetical list of all Audit Manager data types.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonParameters.html\">Common parameters</a>: Parameters that all Query operations can use.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonErrors.html\">Common errors</a>: Client and server errors that all operations can return.</p> </li> </ul> <p>If you're new to Audit Manager, we recommend that you review the <a href=\"https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html\"> Audit Manager User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "auditmanager",
                    "x-aws-signingName": "auditmanager",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/auditmanager-2017-07-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/auditmanager/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/auditmanager/2017-07-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/auditmanager/2017-07-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:autoscaling": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2011-01-01",
        "versions": {
            "2011-01-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2011-01-01",
                    "x-release": "v4",
                    "title": "Auto Scaling",
                    "description": "<fullname>Amazon EC2 Auto Scaling</fullname> <p>Amazon EC2 Auto Scaling is designed to automatically launch or terminate EC2 instances based on user-defined scaling policies, scheduled actions, and health checks.</p> <p>For more information about Amazon EC2 Auto Scaling, see the <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html\">Amazon EC2 Auto Scaling User Guide</a>. For information about granting IAM users required permissions for calls to Amazon EC2 Auto Scaling, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/APIReference/ec2-auto-scaling-api-permissions.html\">Granting IAM users required permissions for Amazon EC2 Auto Scaling resources</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "autoscaling",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/autoscaling-2011-01-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/autoscaling/"
                },
                "updated": "2020-03-29T15:19:43.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/autoscaling/2011-01-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/autoscaling/2011-01-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:autoscaling-plans": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-01-06",
        "versions": {
            "2018-01-06": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-01-06",
                    "x-release": "v4",
                    "title": "AWS Auto Scaling Plans",
                    "description": "<fullname>AWS Auto Scaling</fullname> <p>Use AWS Auto Scaling to create scaling plans for your applications to automatically scale your scalable AWS resources. </p> <p> <b>API Summary</b> </p> <p>You can use the AWS Auto Scaling service API to accomplish the following tasks:</p> <ul> <li> <p>Create and manage scaling plans</p> </li> <li> <p>Define target tracking scaling policies to dynamically scale your resources based on utilization</p> </li> <li> <p>Scale Amazon EC2 Auto Scaling groups using predictive scaling and dynamic scaling to scale your Amazon EC2 capacity faster</p> </li> <li> <p>Set minimum and maximum capacity limits</p> </li> <li> <p>Retrieve information on existing scaling plans</p> </li> <li> <p>Access current forecast data and historical forecast data for up to 56 days previous</p> </li> </ul> <p>To learn more about AWS Auto Scaling, including information about granting IAM users required permissions for AWS Auto Scaling actions, see the <a href=\"https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html\">AWS Auto Scaling User Guide</a>. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "autoscaling-plans",
                    "x-aws-signingName": "autoscaling-plans",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/autoscaling-plans-2018-01-06.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/autoscaling-plans/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/autoscaling-plans/2018-01-06/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/autoscaling-plans/2018-01-06/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:backup": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-11-15",
        "versions": {
            "2018-11-15": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-11-15",
                    "x-release": "v4",
                    "title": "AWS Backup",
                    "description": "<fullname>Backup</fullname> <p>Backup is a unified backup service designed to protect Amazon Web Services services and their associated data. Backup simplifies the creation, migration, restoration, and deletion of backups, while also providing reporting and auditing.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "backup",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/backup-2018-11-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/backup/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/backup/2018-11-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/backup/2018-11-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:batch": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-08-10",
        "versions": {
            "2016-08-10": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-08-10",
                    "x-release": "v4",
                    "title": "AWS Batch",
                    "description": "<fullname>Batch</fullname> <p>Using Batch, you can run batch computing workloads on the Cloud. Batch computing is a common means for developers, scientists, and engineers to access large amounts of compute resources. Batch uses the advantages of this computing workload to remove the undifferentiated heavy lifting of configuring and managing required infrastructure. At the same time, it also adopts a familiar batch computing software approach. Given these advantages, Batch can help you to efficiently provision resources in response to jobs submitted, thus effectively helping you to eliminate capacity constraints, reduce compute costs, and deliver your results more quickly.</p> <p>As a fully managed service, Batch can run batch computing workloads of any scale. Batch automatically provisions compute resources and optimizes workload distribution based on the quantity and scale of your specific workloads. With Batch, there's no need to install or manage batch computing software. This means that you can focus your time and energy on analyzing results and solving your specific problems. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "batch",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/batch-2016-08-10.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/batch/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/batch/2016-08-10/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/batch/2016-08-10/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:braket": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2019-09-01",
        "versions": {
            "2019-09-01": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2019-09-01",
                    "x-release": "v4",
                    "title": "Braket",
                    "description": "The Amazon Braket API Reference provides information about the operations and structures supported in Amazon Braket.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "braket",
                    "x-aws-signingName": "braket",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/braket-2019-09-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/braket/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/braket/2019-09-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/braket/2019-09-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:budgets": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-10-20",
        "versions": {
            "2016-10-20": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-10-20",
                    "x-release": "v4",
                    "title": "AWS Budgets",
                    "description": "<p>The AWS Budgets API enables you to use AWS Budgets to plan your service usage, service costs, and instance reservations. The API reference provides descriptions, syntax, and usage examples for each of the actions and data types for AWS Budgets. </p> <p>Budgets provide you with a way to see the following information:</p> <ul> <li> <p>How close your plan is to your budgeted amount or to the free tier limits</p> </li> <li> <p>Your usage-to-date, including how much you've used of your Reserved Instances (RIs)</p> </li> <li> <p>Your current estimated charges from AWS, and how much your predicted usage will accrue in charges by the end of the month</p> </li> <li> <p>How much of your budget has been used</p> </li> </ul> <p>AWS updates your budget status several times a day. Budgets track your unblended costs, subscriptions, refunds, and RIs. You can create the following types of budgets:</p> <ul> <li> <p> <b>Cost budgets</b> - Plan how much you want to spend on a service.</p> </li> <li> <p> <b>Usage budgets</b> - Plan how much you want to use one or more services.</p> </li> <li> <p> <b>RI utilization budgets</b> - Define a utilization threshold, and receive alerts when your RI usage falls below that threshold. This lets you see if your RIs are unused or under-utilized.</p> </li> <li> <p> <b>RI coverage budgets</b> - Define a coverage threshold, and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold. This lets you see how much of your instance usage is covered by a reservation.</p> </li> </ul> <p>Service Endpoint</p> <p>The AWS Budgets API provides the following endpoint:</p> <ul> <li> <p>https://budgets.amazonaws.com</p> </li> </ul> <p>For information about costs that are associated with the AWS Budgets API, see <a href=\"https://aws.amazon.com/aws-cost-management/pricing/\">AWS Cost Management Pricing</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "budgets",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/budgets-2016-10-20.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/budgets/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/budgets/2016-10-20/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/budgets/2016-10-20/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ce": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-10-25",
        "versions": {
            "2017-10-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-10-25",
                    "x-release": "v4",
                    "title": "AWS Cost Explorer Service",
                    "description": "<p>You can use the Cost Explorer API to programmatically query your cost and usage data. You can query for aggregated data such as total monthly costs or total daily usage. You can also query for granular data. This might include the number of daily write operations for Amazon DynamoDB database tables in your production environment. </p> <p>Service Endpoint</p> <p>The Cost Explorer API provides the following endpoint:</p> <ul> <li> <p> <code>https://ce.us-east-1.amazonaws.com</code> </p> </li> </ul> <p>For information about the costs that are associated with the Cost Explorer API, see <a href=\"http://aws.amazon.com/aws-cost-management/pricing/\">Amazon Web Services Cost Management Pricing</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ce",
                    "x-aws-signingName": "ce",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ce-2017-10-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ce/"
                },
                "updated": "2020-04-21T20:02:04.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ce/2017-10-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ce/2017-10-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:chime": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-05-01",
        "versions": {
            "2018-05-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-05-01",
                    "x-release": "v4",
                    "title": "Amazon Chime",
                    "description": "<p>The Amazon Chime API (application programming interface) is designed for developers to perform key tasks, such as creating and managing Amazon Chime accounts, users, and Voice Connectors. This guide provides detailed information about the Amazon Chime API, including operations, types, inputs and outputs, and error codes. It also includes some server-side API actions to use with the Amazon Chime SDK. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime/latest/dg/meetings-sdk.html\"> Using the Amazon Chime SDK </a> in the <i>Amazon Chime Developer Guide</i>.</p> <p>You can use an AWS SDK, the AWS Command Line Interface (AWS CLI), or the REST API to make API calls. We recommend using an AWS SDK or the AWS CLI. Each API operation includes links to information about using it with a language-specific AWS SDK or the AWS CLI.</p> <dl> <dt>Using an AWS SDK</dt> <dd> <p> You don't need to write code to calculate a signature for request authentication. The SDK clients authenticate your requests by using access keys that you provide. For more information about AWS SDKs, see the <a href=\"http://aws.amazon.com/developer/\">AWS Developer Center</a>. </p> </dd> <dt>Using the AWS CLI</dt> <dd> <p>Use your access keys with the AWS CLI to make API calls. For information about setting up the AWS CLI, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/installing.html\">Installing the AWS Command Line Interface</a> in the <i>AWS Command Line Interface User Guide</i>. For a list of available Amazon Chime commands, see the <a href=\"https://docs.aws.amazon.com/cli/latest/reference/chime/index.html\">Amazon Chime commands</a> in the <i>AWS CLI Command Reference</i>. </p> </dd> <dt>Using REST APIs</dt> <dd> <p>If you use REST to make API calls, you must authenticate your request by providing a signature. Amazon Chime supports signature version 4. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\">Signature Version 4 Signing Process</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>When making REST API calls, use the service name <code>chime</code> and REST endpoint <code>https://service.chime.aws.amazon.com</code>.</p> </dd> </dl> <p>Administrative permissions are controlled using AWS Identity and Access Management (IAM). For more information, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/security-iam.html\">Identity and Access Management for Amazon Chime</a> in the <i>Amazon Chime Administration Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "chime",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/chime-2018-05-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/chime/"
                },
                "updated": "2020-04-09T06:28:07.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/chime/2018-05-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/chime/2018-05-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloud9": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-09-23",
        "versions": {
            "2017-09-23": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-09-23",
                    "x-release": "v4",
                    "title": "AWS Cloud9",
                    "description": "<fullname>Cloud9</fullname> <p>Cloud9 is a collection of tools that you can use to code, build, run, test, debug, and release software in the cloud.</p> <p>For more information about Cloud9, see the <a href=\"https://docs.aws.amazon.com/cloud9/latest/user-guide\">Cloud9 User Guide</a>.</p> <p>Cloud9 supports these operations:</p> <ul> <li> <p> <code>CreateEnvironmentEC2</code>: Creates an Cloud9 development environment, launches an Amazon EC2 instance, and then connects from the instance to the environment.</p> </li> <li> <p> <code>CreateEnvironmentMembership</code>: Adds an environment member to an environment.</p> </li> <li> <p> <code>DeleteEnvironment</code>: Deletes an environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.</p> </li> <li> <p> <code>DeleteEnvironmentMembership</code>: Deletes an environment member from an environment.</p> </li> <li> <p> <code>DescribeEnvironmentMemberships</code>: Gets information about environment members for an environment.</p> </li> <li> <p> <code>DescribeEnvironments</code>: Gets information about environments.</p> </li> <li> <p> <code>DescribeEnvironmentStatus</code>: Gets status information for an environment.</p> </li> <li> <p> <code>ListEnvironments</code>: Gets a list of environment identifiers.</p> </li> <li> <p> <code>ListTagsForResource</code>: Gets the tags for an environment.</p> </li> <li> <p> <code>TagResource</code>: Adds tags to an environment.</p> </li> <li> <p> <code>UntagResource</code>: Removes tags from an environment.</p> </li> <li> <p> <code>UpdateEnvironment</code>: Changes the settings of an existing environment.</p> </li> <li> <p> <code>UpdateEnvironmentMembership</code>: Changes the settings of an existing environment member for an environment.</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloud9",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloud9-2017-09-23.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloud9/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloud9/2017-09-23/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloud9/2017-09-23/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:clouddirectory": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-01-11",
        "versions": {
            "2017-01-11": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-01-11",
                    "x-release": "v4",
                    "title": "Amazon CloudDirectory",
                    "description": "<fullname>Amazon Cloud Directory</fullname> <p>Amazon Cloud Directory is a component of the AWS Directory Service that simplifies the development and management of cloud-scale web, mobile, and IoT applications. This guide describes the Cloud Directory operations that you can call programmatically and includes detailed information on data types and errors. For information about Cloud Directory features, see <a href=\"https://aws.amazon.com/directoryservice/\">AWS Directory Service</a> and the <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html\">Amazon Cloud Directory Developer Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "clouddirectory",
                    "x-aws-signingName": "clouddirectory",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/clouddirectory-2017-01-11.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/clouddirectory/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/clouddirectory/2017-01-11/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/clouddirectory/2017-01-11/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudformation": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2010-05-15",
        "versions": {
            "2010-05-15": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2010-05-15",
                    "x-release": "v4",
                    "title": "AWS CloudFormation",
                    "description": "<fullname>AWS CloudFormation</fullname> <p>CloudFormation allows you to create and manage Amazon Web Services infrastructure deployments predictably and repeatedly. You can use CloudFormation to leverage Amazon Web Services products, such as Amazon Elastic Compute Cloud, Amazon Elastic Block Store, Amazon Simple Notification Service, Elastic Load Balancing, and Auto Scaling to build highly-reliable, highly scalable, cost-effective applications without creating or configuring the underlying Amazon Web Services infrastructure.</p> <p>With CloudFormation, you declare all of your resources and dependencies in a template file. The template defines a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources of the stack together and manages all dependencies between the resources for you.</p> <p>For more information about CloudFormation, see the <a href=\"http://aws.amazon.com/cloudformation/\">CloudFormation Product Page</a>.</p> <p>CloudFormation makes use of other Amazon Web Services products. If you need additional technical information about a specific Amazon Web Services product, you can find the product's technical documentation at <a href=\"https://docs.aws.amazon.com/\"> <code>docs.aws.amazon.com</code> </a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudformation",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudformation-2010-05-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudformation/"
                },
                "updated": "2020-04-09T06:28:07.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudformation/2010-05-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudformation/2010-05-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudfront": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-05-31",
        "versions": {
            "2020-05-31": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-05-31",
                    "x-release": "v4",
                    "title": "Amazon CloudFront",
                    "description": "<fullname>Amazon CloudFront</fullname> <p>This is the <i>Amazon CloudFront API Reference</i>. This guide is for developers who need detailed information about CloudFront API actions, data types, and errors. For detailed information about CloudFront features, see the <i>Amazon CloudFront Developer Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudfront",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudfront-2020-05-31.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudfront/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudfront/2020-05-31/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudfront/2020-05-31/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudhsm": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-05-30",
        "versions": {
            "2014-05-30": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-05-30",
                    "x-release": "v4",
                    "title": "Amazon CloudHSM",
                    "description": "<fullname>AWS CloudHSM Service</fullname> <p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href=\"http://aws.amazon.com/cloudhsm/faqs-classic/\">AWS CloudHSM Classic FAQs</a>, the <a href=\"https://docs.aws.amazon.com/cloudhsm/classic/userguide/\">AWS CloudHSM Classic User Guide</a>, and the <a href=\"https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href=\"http://aws.amazon.com/cloudhsm/\">AWS CloudHSM</a>, the <a href=\"https://docs.aws.amazon.com/cloudhsm/latest/userguide/\">AWS CloudHSM User Guide</a>, and the <a href=\"https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\">AWS CloudHSM API Reference</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudhsm",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudhsm-2014-05-30.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudhsm/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudhsm/2014-05-30/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudhsm/2014-05-30/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudhsmv2": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-04-28",
        "versions": {
            "2017-04-28": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-04-28",
                    "x-release": "v4",
                    "title": "AWS CloudHSM V2",
                    "description": "For more information about AWS CloudHSM, see <a href=\"http://aws.amazon.com/cloudhsm/\">AWS CloudHSM</a> and the <a href=\"https://docs.aws.amazon.com/cloudhsm/latest/userguide/\">AWS CloudHSM User Guide</a>.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudhsmv2",
                    "x-aws-signingName": "cloudhsm",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudhsmv2-2017-04-28.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudhsmv2/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudhsmv2/2017-04-28/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudhsmv2/2017-04-28/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudsearch": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2013-01-01",
        "versions": {
            "2013-01-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2013-01-01",
                    "x-release": "v4",
                    "title": "Amazon CloudSearch",
                    "description": "<fullname>Amazon CloudSearch Configuration Service</fullname> <p>You use the Amazon CloudSearch configuration service to create, configure, and manage search domains. Configuration service requests are submitted using the AWS Query protocol. AWS Query requests are HTTP or HTTPS requests submitted via HTTP GET or POST with a query parameter named Action.</p> <p>The endpoint for configuration service requests is region-specific: cloudsearch.<i>region</i>.amazonaws.com. For example, cloudsearch.us-east-1.amazonaws.com. For a current list of supported regions and endpoints, see <a href=\"http://docs.aws.amazon.com/general/latest/gr/rande.html#cloudsearch_region\" target=\"_blank\">Regions and Endpoints</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudsearch",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudsearch-2013-01-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudsearch/"
                },
                "updated": "2020-03-29T15:19:43.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudsearch/2013-01-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudsearch/2013-01-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudsearchdomain": {
        "added": "2017-05-02T07:59:53.000Z",
        "preferred": "2013-01-01",
        "versions": {
            "2013-01-01": {
                "added": "2017-05-02T07:59:53.000Z",
                "info": {
                    "version": "2013-01-01",
                    "x-release": "v4",
                    "title": "Amazon CloudSearch Domain",
                    "description": "<p>You use the AmazonCloudSearch2013 API to upload documents to a search domain and search those documents. </p> <p>The endpoints for submitting <code>UploadDocuments</code>, <code>Search</code>, and <code>Suggest</code> requests are domain-specific. To get the endpoints for your domain, use the Amazon CloudSearch configuration service <code>DescribeDomains</code> action. The domain endpoints are also displayed on the domain dashboard in the Amazon CloudSearch console. You submit suggest requests to the search endpoint. </p> <p>For more information, see the <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide\">Amazon CloudSearch Developer Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudsearchdomain",
                    "x-aws-signingName": "cloudsearch",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudsearchdomain-2013-01-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudsearchdomain/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudsearchdomain/2013-01-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudsearchdomain/2013-01-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cloudtrail": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2013-11-01",
        "versions": {
            "2013-11-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2013-11-01",
                    "x-release": "v4",
                    "title": "AWS CloudTrail",
                    "description": "<fullname>CloudTrail</fullname> <p>This is the CloudTrail API Reference. It provides descriptions of actions, data types, common parameters, and common errors for CloudTrail.</p> <p>CloudTrail is a web service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. The recorded information includes the identity of the user, the start time of the Amazon Web Services API call, the source IP address, the request parameters, and the response elements returned by the service.</p> <note> <p>As an alternative to the API, you can use one of the Amazon Web Services SDKs, which consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .NET, iOS, Android, etc.). The SDKs provide programmatic access to CloudTrail. For example, the SDKs handle cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see <a href=\"http://aws.amazon.com/tools/\">Tools to Build on Amazon Web Services</a>.</p> </note> <p>See the <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html\">CloudTrail User Guide</a> for information about the data that is included with each Amazon Web Services API call listed in the log files.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cloudtrail",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cloudtrail-2013-11-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cloudtrail/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudtrail/2013-11-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cloudtrail/2013-11-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codeartifact": {
        "added": "2020-07-10T08:57:08.681Z",
        "preferred": "2018-09-22",
        "versions": {
            "2018-09-22": {
                "added": "2020-07-10T08:57:08.681Z",
                "info": {
                    "version": "2018-09-22",
                    "x-release": "v4",
                    "title": "CodeArtifact",
                    "description": "<p> AWS CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, and pip. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>AWS CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), and <b> <code>pip</code> </b>.</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in AWS Key Management Service (AWS KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> <li> <p> <code>maven</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the AWS account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codeartifact",
                    "x-aws-signingName": "codeartifact",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codeartifact-2018-09-22.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codeartifact/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeartifact/2018-09-22/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeartifact/2018-09-22/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codebuild": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-10-06",
        "versions": {
            "2016-10-06": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-10-06",
                    "x-release": "v4",
                    "title": "AWS CodeBuild",
                    "description": "<fullname>CodeBuild</fullname> <p>CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers. It provides prepackaged build environments for the most popular programming languages and build tools, such as Apache Maven, Gradle, and more. You can also fully customize build environments in CodeBuild to use your own build tools. CodeBuild scales automatically to meet peak build requests. You pay only for the build time you consume. For more information about CodeBuild, see the <i> <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html\">CodeBuild User Guide</a>.</i> </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codebuild",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codebuild-2016-10-06.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codebuild/"
                },
                "updated": "2020-05-07T20:22:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codebuild/2016-10-06/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codebuild/2016-10-06/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codecommit": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-04-13",
        "versions": {
            "2015-04-13": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-04-13",
                    "x-release": "v4",
                    "title": "AWS CodeCommit",
                    "description": "<fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codecommit",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codecommit-2015-04-13.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codecommit/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codecommit/2015-04-13/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codecommit/2015-04-13/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codedeploy": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-10-06",
        "versions": {
            "2014-10-06": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-10-06",
                    "x-release": "v4",
                    "title": "AWS CodeDeploy",
                    "description": "<fullname>AWS CodeDeploy</fullname> <p>AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances running in your own facility, serverless AWS Lambda functions, or applications in an Amazon ECS service.</p> <p>You can deploy a nearly unlimited variety of application content, such as an updated Lambda function, updated applications in an Amazon ECS service, code, web and configuration files, executables, packages, scripts, multimedia files, and so on. AWS CodeDeploy can deploy application content stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. You do not need to make changes to your existing code before you can use AWS CodeDeploy.</p> <p>AWS CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications, without many of the risks associated with error-prone manual deployments.</p> <p> <b>AWS CodeDeploy Components</b> </p> <p>Use the information in this guide to help you work with the following AWS CodeDeploy components:</p> <ul> <li> <p> <b>Application</b>: A name that uniquely identifies the application you want to deploy. AWS CodeDeploy uses this name, which functions as a container, to ensure the correct combination of revision, deployment configuration, and deployment group are referenced during a deployment.</p> </li> <li> <p> <b>Deployment group</b>: A set of individual instances, CodeDeploy Lambda deployment configuration settings, or an Amazon ECS service and network details. A Lambda deployment group specifies how to route traffic to a new version of a Lambda function. An Amazon ECS deployment group specifies the service created in Amazon ECS to deploy, a load balancer, and a listener to reroute production traffic to an updated containerized application. An EC2/On-premises deployment group contains individually tagged instances, Amazon EC2 instances in Amazon EC2 Auto Scaling groups, or both. All deployment groups can specify optional trigger, alarm, and rollback settings.</p> </li> <li> <p> <b>Deployment configuration</b>: A set of deployment rules and deployment success and failure conditions used by AWS CodeDeploy during a deployment.</p> </li> <li> <p> <b>Deployment</b>: The process and the components used when updating a Lambda function, a containerized application in an Amazon ECS service, or of installing content on one or more instances. </p> </li> <li> <p> <b>Application revisions</b>: For an AWS Lambda deployment, this is an AppSpec file that specifies the Lambda function to be updated and one or more functions to validate deployment lifecycle events. For an Amazon ECS deployment, this is an AppSpec file that specifies the Amazon ECS task definition, container, and port where production traffic is rerouted. For an EC2/On-premises deployment, this is an archive file that contains source content—source code, webpages, executable files, and deployment scripts—along with an AppSpec file. Revisions are stored in Amazon S3 buckets or GitHub repositories. For Amazon S3, a revision is uniquely identified by its Amazon S3 object key and its ETag, version, or both. For GitHub, a revision is uniquely identified by its commit ID.</p> </li> </ul> <p>This guide also contains information to help you get details about the instances in your deployments, to make on-premises instances available for AWS CodeDeploy deployments, to get details about a Lambda function deployment, and to get details about Amazon ECS service deployments.</p> <p> <b>AWS CodeDeploy Information Resources</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide\">AWS CodeDeploy User Guide</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/codedeploy/latest/APIReference/\">AWS CodeDeploy API Reference Guide</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/cli/latest/reference/deploy/index.html\">AWS CLI Reference for AWS CodeDeploy</a> </p> </li> <li> <p> <a href=\"https://forums.aws.amazon.com/forum.jspa?forumID=179\">AWS CodeDeploy Developer Forum</a> </p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codedeploy",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codedeploy-2014-10-06.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codedeploy/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codedeploy/2014-10-06/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codedeploy/2014-10-06/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codeguru-reviewer": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-09-19",
        "versions": {
            "2019-09-19": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-09-19",
                    "x-release": "v4",
                    "title": "Amazon CodeGuru Reviewer",
                    "description": "<p>This section provides documentation for the Amazon CodeGuru Reviewer API operations. CodeGuru Reviewer is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and recommends fixes in your Java and Python code.</p> <p>By proactively detecting and providing recommendations for addressing code defects and implementing best practices, CodeGuru Reviewer improves the overall quality and maintainability of your code base during the code review stage. For more information about CodeGuru Reviewer, see the <i> <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html\">Amazon CodeGuru Reviewer User Guide</a>.</i> </p> <p> To improve the security of your CodeGuru Reviewer API calls, you can establish a private connection between your VPC and CodeGuru Reviewer by creating an <i>interface VPC endpoint</i>. For more information, see <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/vpc-interface-endpoints.html\">CodeGuru Reviewer and interface VPC endpoints (Amazon Web Services PrivateLink)</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codeguru-reviewer",
                    "x-aws-signingName": "codeguru-reviewer",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codeguru-reviewer-2019-09-19.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codeguru-reviewer/"
                },
                "updated": "2020-05-11T19:05:17.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeguru-reviewer/2019-09-19/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeguru-reviewer/2019-09-19/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codeguruprofiler": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-07-18",
        "versions": {
            "2019-07-18": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-07-18",
                    "x-release": "v4",
                    "title": "Amazon CodeGuru Profiler",
                    "description": "<p> This section provides documentation for the Amazon CodeGuru Profiler API operations. </p> <p> Amazon CodeGuru Profiler collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance. Using machine learning algorithms, CodeGuru Profiler can help you find your most expensive lines of code and suggest ways you can improve efficiency and remove CPU bottlenecks. </p> <p> Amazon CodeGuru Profiler provides different visualizations of profiling data to help you identify what code is running on the CPU, see how much time is consumed, and suggest ways to reduce CPU utilization. </p> <note> <p>Amazon CodeGuru Profiler currently supports applications written in all Java virtual machine (JVM) languages and Python. While CodeGuru Profiler supports both visualizations and recommendations for applications written in Java, it can also generate visualizations and a subset of recommendations for applications written in other JVM languages and Python.</p> </note> <p> For more information, see <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html\">What is Amazon CodeGuru Profiler</a> in the <i>Amazon CodeGuru Profiler User Guide</i>. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codeguruprofiler",
                    "x-aws-signingName": "codeguru-profiler",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codeguruprofiler-2019-07-18.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codeguru-profiler/"
                },
                "updated": "2020-04-09T06:28:07.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeguruprofiler/2019-07-18/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codeguruprofiler/2019-07-18/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codepipeline": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-07-09",
        "versions": {
            "2015-07-09": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-07-09",
                    "x-release": "v4",
                    "title": "AWS CodePipeline",
                    "description": "<fullname>AWS CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the AWS CodePipeline API Reference. This guide provides descriptions of the actions and data types for AWS CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">AWS CodePipeline User Guide</a>.</p> <p>You can use the AWS CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">AWS CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with AWS CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with AWS CodePipeline, the expected sequence varies from the standard API user. To integrate with AWS CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into AWS CodePipeline. Partner actions are created by members of the AWS Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codepipeline",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codepipeline-2015-07-09.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codepipeline/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codepipeline/2015-07-09/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codepipeline/2015-07-09/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codestar": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-04-19",
        "versions": {
            "2017-04-19": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-04-19",
                    "x-release": "v4",
                    "title": "AWS CodeStar",
                    "description": "<fullname>AWS CodeStar</fullname> <p>This is the API reference for AWS CodeStar. This reference provides descriptions of the operations and data types for the AWS CodeStar API along with usage examples.</p> <p>You can use the AWS CodeStar API to work with:</p> <p>Projects and their resources, by calling the following:</p> <ul> <li> <p> <code>DeleteProject</code>, which deletes a project.</p> </li> <li> <p> <code>DescribeProject</code>, which lists the attributes of a project.</p> </li> <li> <p> <code>ListProjects</code>, which lists all projects associated with your AWS account.</p> </li> <li> <p> <code>ListResources</code>, which lists the resources associated with a project.</p> </li> <li> <p> <code>ListTagsForProject</code>, which lists the tags associated with a project.</p> </li> <li> <p> <code>TagProject</code>, which adds tags to a project.</p> </li> <li> <p> <code>UntagProject</code>, which removes tags from a project.</p> </li> <li> <p> <code>UpdateProject</code>, which updates the attributes of a project.</p> </li> </ul> <p>Teams and team members, by calling the following:</p> <ul> <li> <p> <code>AssociateTeamMember</code>, which adds an IAM user to the team for a project.</p> </li> <li> <p> <code>DisassociateTeamMember</code>, which removes an IAM user from the team for a project.</p> </li> <li> <p> <code>ListTeamMembers</code>, which lists all the IAM users in the team for a project, including their roles and attributes.</p> </li> <li> <p> <code>UpdateTeamMember</code>, which updates a team member's attributes in a project.</p> </li> </ul> <p>Users, by calling the following:</p> <ul> <li> <p> <code>CreateUserProfile</code>, which creates a user profile that contains data associated with the user across all projects.</p> </li> <li> <p> <code>DeleteUserProfile</code>, which deletes all user profile information across all projects.</p> </li> <li> <p> <code>DescribeUserProfile</code>, which describes the profile of a user.</p> </li> <li> <p> <code>ListUserProfiles</code>, which lists all user profiles.</p> </li> <li> <p> <code>UpdateUserProfile</code>, which updates the profile for a user.</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codestar",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codestar-2017-04-19.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codestar/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar/2017-04-19/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar/2017-04-19/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codestar-connections": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-12-01",
        "versions": {
            "2019-12-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-12-01",
                    "x-release": "v4",
                    "title": "AWS CodeStar connections",
                    "description": "<fullname>AWS CodeStar Connections</fullname> <p>This AWS CodeStar Connections API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Connections API. You can use the connections API to work with connections and installations.</p> <p> <i>Connections</i> are configurations that you use to connect AWS resources to external code repositories. Each connection is a resource that can be given to services such as CodePipeline to connect to a third-party repository such as Bitbucket. For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code change is made to your third-party code repository. Each connection is named and associated with a unique ARN that is used to reference the connection.</p> <p>When you create a connection, the console initiates a third-party connection handshake. <i>Installations</i> are the apps that are used to conduct this handshake. For example, the installation for the Bitbucket provider type is the Bitbucket app. When you create a connection, you can choose an existing installation or create one.</p> <p>When you want to create a connection to an installed provider type such as GitHub Enterprise Server, you create a <i>host</i> for your connections.</p> <p>You can work with connections by calling:</p> <ul> <li> <p> <a>CreateConnection</a>, which creates a uniquely named connection that can be referenced by services such as CodePipeline.</p> </li> <li> <p> <a>DeleteConnection</a>, which deletes the specified connection.</p> </li> <li> <p> <a>GetConnection</a>, which returns information about the connection, including the connection status.</p> </li> <li> <p> <a>ListConnections</a>, which lists the connections associated with your account.</p> </li> </ul> <p>You can work with hosts by calling:</p> <ul> <li> <p> <a>CreateHost</a>, which creates a host that represents the infrastructure where your provider is installed.</p> </li> <li> <p> <a>DeleteHost</a>, which deletes the specified host.</p> </li> <li> <p> <a>GetHost</a>, which returns information about the host, including the setup status.</p> </li> <li> <p> <a>ListHosts</a>, which lists the hosts associated with your account.</p> </li> </ul> <p>You can work with tags in AWS CodeStar Connections by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeStar Connections.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeStar Connections.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeStar Connections.</p> </li> </ul> <p>For information about how to use AWS CodeStar Connections, see the <a href=\"https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html\">Developer Tools User Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codestar-connections",
                    "x-aws-signingName": "codestar-connections",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codestar-connections-2019-12-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codestar-connections/"
                },
                "updated": "2020-05-06T20:09:09.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar-connections/2019-12-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar-connections/2019-12-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:codestar-notifications": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-10-15",
        "versions": {
            "2019-10-15": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-10-15",
                    "x-release": "v4",
                    "title": "AWS CodeStar Notifications",
                    "description": "<p>This AWS CodeStar Notifications API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Notifications API. You can use the AWS CodeStar Notifications API to work with the following objects:</p> <p>Notification rules, by calling the following: </p> <ul> <li> <p> <a>CreateNotificationRule</a>, which creates a notification rule for a resource in your account. </p> </li> <li> <p> <a>DeleteNotificationRule</a>, which deletes a notification rule. </p> </li> <li> <p> <a>DescribeNotificationRule</a>, which provides information about a notification rule. </p> </li> <li> <p> <a>ListNotificationRules</a>, which lists the notification rules associated with your account. </p> </li> <li> <p> <a>UpdateNotificationRule</a>, which changes the name, events, or targets associated with a notification rule. </p> </li> <li> <p> <a>Subscribe</a>, which subscribes a target to a notification rule. </p> </li> <li> <p> <a>Unsubscribe</a>, which removes a target from a notification rule. </p> </li> </ul> <p>Targets, by calling the following: </p> <ul> <li> <p> <a>DeleteTarget</a>, which removes a notification rule target (SNS topic) from a notification rule. </p> </li> <li> <p> <a>ListTargets</a>, which lists the targets associated with a notification rule. </p> </li> </ul> <p>Events, by calling the following: </p> <ul> <li> <p> <a>ListEventTypes</a>, which lists the event types you can include in a notification rule. </p> </li> </ul> <p>Tags, by calling the following: </p> <ul> <li> <p> <a>ListTagsForResource</a>, which lists the tags already associated with a notification rule in your account. </p> </li> <li> <p> <a>TagResource</a>, which associates a tag you provide with a notification rule in your account. </p> </li> <li> <p> <a>UntagResource</a>, which removes a tag from a notification rule in your account. </p> </li> </ul> <p> For information about how to use AWS CodeStar Notifications, see link in the CodeStarNotifications User Guide. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "codestar-notifications",
                    "x-aws-signingName": "codestar-notifications",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/codestar-notifications-2019-10-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/codestar-notifications/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar-notifications/2019-10-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/codestar-notifications/2019-10-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cognito-identity": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-06-30",
        "versions": {
            "2014-06-30": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-06-30",
                    "x-release": "v4",
                    "title": "Amazon Cognito Identity",
                    "description": "<fullname>Amazon Cognito Federated Identities</fullname> <p>Amazon Cognito Federated Identities is a web service that delivers scoped temporary credentials to mobile devices and other untrusted environments. It uniquely identifies a device and supplies the user with a consistent identity over the lifetime of an application.</p> <p>Using Amazon Cognito Federated Identities, you can enable authentication with one or more third-party identity providers (Facebook, Google, or Login with Amazon) or an Amazon Cognito user pool, and you can also choose to support unauthenticated access from your app. Cognito delivers a unique identifier for each user and acts as an OpenID token provider trusted by AWS Security Token Service (STS) to access temporary, limited-privilege AWS credentials.</p> <p>For a description of the authentication flow from the Amazon Cognito Developer Guide see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html\">Authentication Flow</a>.</p> <p>For more information see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html\">Amazon Cognito Federated Identities</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cognito-identity",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cognito-identity-2014-06-30.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cognito-identity/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-identity/2014-06-30/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-identity/2014-06-30/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cognito-idp": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-04-18",
        "versions": {
            "2016-04-18": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-04-18",
                    "x-release": "v4",
                    "title": "Amazon Cognito Identity Provider",
                    "description": "<p>Using the Amazon Cognito User Pools API, you can create a user pool to manage directories and users. You can authenticate a user to obtain tokens related to user identity and access policies.</p> <p>This API reference provides information about user pools in Amazon Cognito User Pools.</p> <p>For more information, see the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html\">Amazon Cognito Documentation</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cognito-idp",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cognito-idp-2016-04-18.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cognito-idp/"
                },
                "updated": "2020-03-17T09:20:43.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-idp/2016-04-18/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-idp/2016-04-18/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cognito-sync": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-06-30",
        "versions": {
            "2014-06-30": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-06-30",
                    "x-release": "v4",
                    "title": "Amazon Cognito Sync",
                    "description": "<fullname>Amazon Cognito Sync</fullname> <p>Amazon Cognito Sync provides an AWS service and client library that enable cross-device syncing of application-related user data. High-level client libraries are available for both iOS and Android. You can use these libraries to persist data locally so that it's available even if the device is offline. Developer credentials don't need to be stored on the mobile device to access the service. You can use Amazon Cognito to obtain a normalized user ID and credentials. User data is persisted in a dataset that can store up to 1 MB of key-value pairs, and you can have up to 20 datasets per user identity.</p> <p>With Amazon Cognito Sync, the data stored for each identity is accessible only to credentials assigned to that identity. In order to use the Cognito Sync service, you need to make API calls using credentials retrieved with <a href=\"http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html\">Amazon Cognito Identity service</a>.</p> <p>If you want to use Cognito Sync in an Android or iOS application, you will probably want to make API calls via the AWS Mobile SDK. To learn more, see the <a href=\"http://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/cognito-sync.html\">Developer Guide for Android</a> and the <a href=\"http://docs.aws.amazon.com/mobile/sdkforios/developerguide/cognito-sync.html\">Developer Guide for iOS</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cognito-sync",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cognito-sync-2014-06-30.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cognito-sync/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-sync/2014-06-30/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cognito-sync/2014-06-30/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:comprehend": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-11-27",
        "versions": {
            "2017-11-27": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-11-27",
                    "x-release": "v4",
                    "title": "Amazon Comprehend",
                    "description": "Amazon Comprehend is an AWS service for gaining insight into the content of documents. Use these actions to determine the topics contained in your documents, the topics they discuss, the predominant sentiment expressed in them, the predominant language used, and more.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "comprehend",
                    "x-aws-signingName": "comprehend",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/comprehend-2017-11-27.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/comprehend/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/comprehend/2017-11-27/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/comprehend/2017-11-27/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:comprehendmedical": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-10-30",
        "versions": {
            "2018-10-30": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-10-30",
                    "x-release": "v4",
                    "title": "AWS Comprehend Medical",
                    "description": " Amazon Comprehend Medical extracts structured information from unstructured clinical text. Use these actions to gain insight in your documents. ",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "comprehendmedical",
                    "x-aws-signingName": "comprehendmedical",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/comprehendmedical-2018-10-30.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/comprehendmedical/"
                },
                "updated": "2020-05-06T20:09:09.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/comprehendmedical/2018-10-30/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/comprehendmedical/2018-10-30/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:compute-optimizer": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-11-01",
        "versions": {
            "2019-11-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-11-01",
                    "x-release": "v4",
                    "title": "AWS Compute Optimizer",
                    "description": "Compute Optimizer is a service that analyzes the configuration and utilization metrics of your Amazon Web Services compute resources, such as Amazon EC2 instances, Amazon EC2 Auto Scaling groups, Lambda functions, and Amazon EBS volumes. It reports whether your resources are optimal, and generates optimization recommendations to reduce the cost and improve the performance of your workloads. Compute Optimizer also provides recent utilization metric data, in addition to projected utilization metric data for the recommendations, which you can use to evaluate which recommendation provides the best price-performance trade-off. The analysis of your usage patterns can help you decide when to move or resize your running resources, and still meet your performance and capacity requirements. For more information about Compute Optimizer, including the required permissions to use the service, see the <a href=\"https://docs.aws.amazon.com/compute-optimizer/latest/ug/\">Compute Optimizer User Guide</a>.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "compute-optimizer",
                    "x-aws-signingName": "compute-optimizer",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/compute-optimizer-2019-11-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/compute-optimizer/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/compute-optimizer/2019-11-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/compute-optimizer/2019-11-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:config": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-11-12",
        "versions": {
            "2014-11-12": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-11-12",
                    "x-release": "v4",
                    "title": "AWS Config",
                    "description": "<fullname>Config</fullname> <p>Config provides a way to keep track of the configurations of all the Amazon Web Services resources associated with your Amazon Web Services account. You can use Config to get the current and historical configurations of each Amazon Web Services resource and also to get information about the relationship between the resources. An Amazon Web Services resource can be an Amazon Compute Cloud (Amazon EC2) instance, an Elastic Block Store (EBS) volume, an elastic network Interface (ENI), or a security group. For a complete list of resources currently supported by Config, see <a href=\"https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources\">Supported Amazon Web Services resources</a>.</p> <p>You can access and manage Config through the Amazon Web Services Management Console, the Amazon Web Services Command Line Interface (Amazon Web Services CLI), the Config API, or the Amazon Web Services SDKs for Config. This reference guide contains documentation for the Config API and the Amazon Web Services CLI commands that you can use to manage Config. The Config API uses the Signature Version 4 protocol for signing requests. For more information about how to sign a request with this protocol, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\">Signature Version 4 Signing Process</a>. For detailed information about Config features and their associated actions or commands, as well as how to work with Amazon Web Services Management Console, see <a href=\"https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html\">What Is Config</a> in the <i>Config Developer Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "config",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/config-2014-11-12.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/config/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/config/2014-11-12/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/config/2014-11-12/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:connect": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-08-08",
        "versions": {
            "2017-08-08": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-08-08",
                    "x-release": "v4",
                    "title": "Amazon Connect Service",
                    "description": "<p>Amazon Connect is a cloud-based contact center solution that you use to set up and manage a customer contact center and provide reliable customer engagement at any scale.</p> <p>Amazon Connect provides metrics and real-time reporting that enable you to optimize contact routing. You can also resolve customer issues more efficiently by getting customers in touch with the appropriate agents.</p> <p>There are limits to the number of Amazon Connect resources that you can create. There are also limits to the number of requests that you can make per second. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p> <p>You can connect programmatically to an AWS service by using an endpoint. For a list of Amazon Connect endpoints, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/connect_region.html\">Amazon Connect Endpoints</a>.</p> <note> <p>Working with contact flows? Check out the <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/flow-language.html\">Amazon Connect Flow language</a>.</p> </note>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "connect",
                    "x-aws-signingName": "connect",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/connect-2017-08-08.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/connect/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connect/2017-08-08/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connect/2017-08-08/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:connect-contact-lens": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-08-21",
        "versions": {
            "2020-08-21": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-08-21",
                    "x-release": "v4",
                    "title": "Amazon Connect Contact Lens",
                    "description": "<p>Contact Lens for Amazon Connect enables you to analyze conversations between customer and agents, by using speech transcription, natural language processing, and intelligent search capabilities. It performs sentiment analysis, detects issues, and enables you to automatically categorize contacts.</p> <p>Contact Lens for Amazon Connect provides both real-time and post-call analytics of customer-agent conversations. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html\">Analyze conversations using Contact Lens</a> in the <i>Amazon Connect Administrator Guide</i>. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "connect-contact-lens",
                    "x-aws-signingName": "connect",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/connect-contact-lens-2020-08-21.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/contact-lens/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connect-contact-lens/2020-08-21/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connect-contact-lens/2020-08-21/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:connectparticipant": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-09-07",
        "versions": {
            "2018-09-07": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-09-07",
                    "x-release": "v4",
                    "title": "Amazon Connect Participant Service",
                    "description": "<p>Amazon Connect is a cloud-based contact center solution that makes it easy to set up and manage a customer contact center and provide reliable customer engagement at any scale.</p> <p>Amazon Connect enables customer contacts through voice or chat.</p> <p>The APIs described here are used by chat participants, such as agents and customers.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "connectparticipant",
                    "x-aws-signingName": "execute-api",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/connectparticipant-2018-09-07.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/connect/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connectparticipant/2018-09-07/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/connectparticipant/2018-09-07/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:cur": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-01-06",
        "versions": {
            "2017-01-06": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-01-06",
                    "x-release": "v4",
                    "title": "AWS Cost and Usage Report Service",
                    "description": "<p>The AWS Cost and Usage Report API enables you to programmatically create, query, and delete AWS Cost and Usage report definitions.</p> <p>AWS Cost and Usage reports track the monthly AWS costs and usage associated with your AWS account. The report contains line items for each unique combination of AWS product, usage type, and operation that your AWS account uses. You can configure the AWS Cost and Usage report to show only the data that you want, using the AWS Cost and Usage API.</p> <p>Service Endpoint</p> <p>The AWS Cost and Usage Report API provides the following endpoint:</p> <ul> <li> <p>cur.us-east-1.amazonaws.com</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "cur",
                    "x-aws-signingName": "cur",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/cur-2017-01-06.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/cur/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cur/2017-01-06/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/cur/2017-01-06/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:customer-profiles": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-08-15",
        "versions": {
            "2020-08-15": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-08-15",
                    "x-release": "v4",
                    "title": "Amazon Connect Customer Profiles",
                    "description": "<fullname>Amazon Connect Customer Profiles</fullname> <p>Welcome to the Amazon Connect Customer Profiles API Reference. This guide provides information about the Amazon Connect Customer Profiles API, including supported operations, data types, parameters, and schemas.</p> <p>Amazon Connect Customer Profiles is a unified customer profile for your contact center that has pre-built connectors powered by AppFlow that make it easy to combine customer information from third party applications, such as Salesforce (CRM), ServiceNow (ITSM), and your enterprise resource planning (ERP), with contact history from your Amazon Connect contact center.</p> <p>If you're new to Amazon Connect , you might find it helpful to also review the <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html\">Amazon Connect Administrator Guide</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "customer-profiles",
                    "x-aws-signingName": "profile",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/customer-profiles-2020-08-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/profile/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/customer-profiles/2020-08-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/customer-profiles/2020-08-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:databrew": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2017-07-25",
        "versions": {
            "2017-07-25": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2017-07-25",
                    "x-release": "v4",
                    "title": "AWS Glue DataBrew",
                    "description": "Glue DataBrew is a visual, cloud-scale data-preparation service. DataBrew simplifies data preparation tasks, targeting data issues that are hard to spot and time-consuming to fix. DataBrew empowers users of all technical levels to visualize the data and perform one-click data transformations, with no coding required.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "databrew",
                    "x-aws-signingName": "databrew",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/databrew-2017-07-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/databrew/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/databrew/2017-07-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/databrew/2017-07-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:dataexchange": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-07-25",
        "versions": {
            "2017-07-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-07-25",
                    "x-release": "v4",
                    "title": "AWS Data Exchange",
                    "description": "<p>AWS Data Exchange is a service that makes it easy for AWS customers to exchange data in the cloud. You can use the AWS Data Exchange APIs to create, update, manage, and access file-based data set in the AWS Cloud.</p><p>As a subscriber, you can view and access the data sets that you have an entitlement to through a subscription. You can use the APIS to download or copy your entitled data sets to Amazon S3 for use across a variety of AWS analytics and machine learning services.</p><p>As a provider, you can create and manage your data sets that you would like to publish to a product. Being able to package and provide your data sets into products requires a few steps to determine eligibility. For more information, visit the AWS Data Exchange User Guide.</p><p>A data set is a collection of data that can be changed or updated over time. Data sets can be updated using revisions, which represent a new version or incremental change to a data set.  A revision contains one or more assets. An asset in AWS Data Exchange is a piece of data that can be stored as an Amazon S3 object. The asset can be a structured data file, an image file, or some other data file. Jobs are asynchronous import or export operations used to create or copy assets.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "dataexchange",
                    "x-aws-signingName": "dataexchange",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/dataexchange-2017-07-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/dataexchange/"
                },
                "updated": "2020-04-27T20:04:05.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dataexchange/2017-07-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dataexchange/2017-07-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:datapipeline": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2012-10-29",
        "versions": {
            "2012-10-29": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2012-10-29",
                    "x-release": "v4",
                    "title": "AWS Data Pipeline",
                    "description": "<p>AWS Data Pipeline configures and manages a data-driven workflow called a pipeline. AWS Data Pipeline handles the details of scheduling and ensuring that data dependencies are met so that your application can focus on processing the data.</p> <p>AWS Data Pipeline provides a JAR implementation of a task runner called AWS Data Pipeline Task Runner. AWS Data Pipeline Task Runner provides logic for common data management scenarios, such as performing database queries and running data analysis using Amazon Elastic MapReduce (Amazon EMR). You can use AWS Data Pipeline Task Runner as your task runner, or you can write your own task runner to provide custom data management.</p> <p>AWS Data Pipeline implements two main sets of functionality. Use the first set to create a pipeline and define data sources, schedules, dependencies, and the transforms to be performed on the data. Use the second set in your task runner application to receive the next task ready for processing. The logic for performing the task, such as querying the data, running data analysis, or converting the data from one format to another, is contained within the task runner. The task runner performs the task assigned to it by the web service, reporting progress to the web service as it does so. When the task is done, the task runner reports the final success or failure of the task to the web service.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "datapipeline",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/datapipeline-2012-10-29.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/datapipeline/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/datapipeline/2012-10-29/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/datapipeline/2012-10-29/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:datasync": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-11-09",
        "versions": {
            "2018-11-09": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-11-09",
                    "x-release": "v4",
                    "title": "AWS DataSync",
                    "description": "<fullname>DataSync</fullname> <p>DataSync is a managed data transfer service that makes it simpler for you to automate moving data between on-premises storage and Amazon Simple Storage Service (Amazon S3) or Amazon Elastic File System (Amazon EFS). </p> <p>This API interface reference for DataSync contains documentation for a programming interface that you can use to manage DataSync.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "datasync",
                    "x-aws-signingName": "datasync",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/datasync-2018-11-09.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/datasync/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/datasync/2018-11-09/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/datasync/2018-11-09/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:dax": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2017-04-19",
        "versions": {
            "2017-04-19": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2017-04-19",
                    "x-release": "v4",
                    "title": "Amazon DynamoDB Accelerator (DAX)",
                    "description": "DAX is a managed caching service engineered for Amazon DynamoDB. DAX dramatically speeds up database reads by caching frequently-accessed data from DynamoDB, so applications can access that data with sub-millisecond latency. You can create a DAX cluster easily, using the AWS Management Console. With a few simple modifications to your code, your application can begin taking advantage of the DAX cluster and realize significant improvements in read performance.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "dax",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/dax-2017-04-19.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/dax/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dax/2017-04-19/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dax/2017-04-19/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:detective": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-10-26",
        "versions": {
            "2018-10-26": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-10-26",
                    "x-release": "v4",
                    "title": "Amazon Detective",
                    "description": "<p>Detective uses machine learning and purpose-built visualizations to help you analyze and investigate security issues across your Amazon Web Services (AWS) workloads. Detective automatically extracts time-based events such as login attempts, API calls, and network traffic from AWS CloudTrail and Amazon Virtual Private Cloud (Amazon VPC) flow logs. It also extracts findings detected by Amazon GuardDuty.</p> <p>The Detective API primarily supports the creation and management of behavior graphs. A behavior graph contains the extracted data from a set of member accounts, and is created and managed by an administrator account.</p> <p>Every behavior graph is specific to a Region. You can only use the API to manage graphs that belong to the Region that is associated with the currently selected endpoint.</p> <p>A Detective administrator account can use the Detective API to do the following:</p> <ul> <li> <p>Enable and disable Detective. Enabling Detective creates a new behavior graph.</p> </li> <li> <p>View the list of member accounts in a behavior graph.</p> </li> <li> <p>Add member accounts to a behavior graph.</p> </li> <li> <p>Remove member accounts from a behavior graph.</p> </li> </ul> <p>A member account can use the Detective API to do the following:</p> <ul> <li> <p>View the list of behavior graphs that they are invited to.</p> </li> <li> <p>Accept an invitation to contribute to a behavior graph.</p> </li> <li> <p>Decline an invitation to contribute to a behavior graph.</p> </li> <li> <p>Remove their account from a behavior graph.</p> </li> </ul> <p>All API actions are logged as CloudTrail events. See <a href=\"https://docs.aws.amazon.com/detective/latest/adminguide/logging-using-cloudtrail.html\">Logging Detective API Calls with CloudTrail</a>.</p> <note> <p>We replaced the term \"master account\" with the term \"administrator account.\" An administrator account is used to centrally manage multiple accounts. In the case of Detective, the administrator account manages the accounts in their behavior graph.</p> </note>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "detective",
                    "x-aws-signingName": "detective",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/detective-2018-10-26.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/detective/"
                },
                "updated": "2020-03-31T20:14:16.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/detective/2018-10-26/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/detective/2018-10-26/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:devicefarm": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-06-23",
        "versions": {
            "2015-06-23": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-06-23",
                    "x-release": "v4",
                    "title": "AWS Device Farm",
                    "description": "<p>Welcome to the AWS Device Farm API documentation, which contains APIs for:</p> <ul> <li> <p>Testing on desktop browsers</p> <p> Device Farm makes it possible for you to test your web applications on desktop browsers using Selenium. The APIs for desktop browser testing contain <code>TestGrid</code> in their names. For more information, see <a href=\"https://docs.aws.amazon.com/devicefarm/latest/testgrid/\">Testing Web Applications on Selenium with Device Farm</a>.</p> </li> <li> <p>Testing on real mobile devices</p> <p>Device Farm makes it possible for you to test apps on physical phones, tablets, and other devices in the cloud. For more information, see the <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/\">Device Farm Developer Guide</a>.</p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "devicefarm",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/devicefarm-2015-06-23.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/devicefarm/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/devicefarm/2015-06-23/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/devicefarm/2015-06-23/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:devops-guru": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-12-01",
        "versions": {
            "2020-12-01": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-12-01",
                    "x-release": "v4",
                    "title": "Amazon DevOps Guru",
                    "description": "<p> Amazon DevOps Guru is a fully managed service that helps you identify anomalous behavior in business critical operational applications. You specify the AWS resources that you want DevOps Guru to cover, then the Amazon CloudWatch metrics and AWS CloudTrail events related to those resources are analyzed. When anomalous behavior is detected, DevOps Guru creates an <i>insight</i> that includes recommendations, related events, and related metrics that can help you improve your operational applications. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html\">What is Amazon DevOps Guru</a>. </p> <p> You can specify 1 or 2 Amazon Simple Notification Service topics so you are notified every time a new insight is created. You can also enable DevOps Guru to generate an OpsItem in AWS Systems Manager for each insight to help you manage and track your work addressing insights. </p> <p> To learn about the DevOps Guru workflow, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html#how-it-works\">How DevOps Guru works</a>. To learn about DevOps Guru concepts, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/concepts.html\">Concepts in DevOps Guru</a>. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "devops-guru",
                    "x-aws-signingName": "devops-guru",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/devops-guru-2020-12-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/devops-guru/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/devops-guru/2020-12-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/devops-guru/2020-12-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:directconnect": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2012-10-25",
        "versions": {
            "2012-10-25": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2012-10-25",
                    "x-release": "v4",
                    "title": "AWS Direct Connect",
                    "description": "Direct Connect links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router. With this connection in place, you can create virtual interfaces directly to the Cloud (for example, to Amazon EC2 and Amazon S3) and to Amazon VPC, bypassing Internet service providers in your network path. A connection provides access to all Regions except the China (Beijing) and (China) Ningxia Regions. Amazon Web Services resources in the China Regions can only be accessed through locations associated with those Regions.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "directconnect",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/directconnect-2012-10-25.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/directconnect/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/directconnect/2012-10-25/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/directconnect/2012-10-25/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:discovery": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-11-01",
        "versions": {
            "2015-11-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-11-01",
                    "x-release": "v4",
                    "title": "AWS Application Discovery Service",
                    "description": "<fullname>AWS Application Discovery Service</fullname> <p>AWS Application Discovery Service helps you plan application migration projects. It automatically identifies servers, virtual machines (VMs), and network dependencies in your on-premises data centers. For more information, see the <a href=\"http://aws.amazon.com/application-discovery/faqs/\">AWS Application Discovery Service FAQ</a>. Application Discovery Service offers three ways of performing discovery and collecting data about your on-premises servers:</p> <ul> <li> <p> <b>Agentless discovery</b> is recommended for environments that use VMware vCenter Server. This mode doesn't require you to install an agent on each host. It does not work in non-VMware environments.</p> <ul> <li> <p>Agentless discovery gathers server information regardless of the operating systems, which minimizes the time required for initial on-premises infrastructure assessment.</p> </li> <li> <p>Agentless discovery doesn't collect information about network dependencies, only agent-based discovery collects that information.</p> </li> </ul> </li> </ul> <ul> <li> <p> <b>Agent-based discovery</b> collects a richer set of data than agentless discovery by using the AWS Application Discovery Agent, which you install on one or more hosts in your data center.</p> <ul> <li> <p> The agent captures infrastructure and application information, including an inventory of running processes, system performance information, resource utilization, and network dependencies.</p> </li> <li> <p>The information collected by agents is secured at rest and in transit to the Application Discovery Service database in the cloud. </p> </li> </ul> </li> </ul> <ul> <li> <p> <b>AWS Partner Network (APN) solutions</b> integrate with Application Discovery Service, enabling you to import details of your on-premises environment directly into Migration Hub without using the discovery connector or discovery agent.</p> <ul> <li> <p>Third-party application discovery tools can query AWS Application Discovery Service, and they can write to the Application Discovery Service database using the public API.</p> </li> <li> <p>In this way, you can import data into Migration Hub and view it, so that you can associate applications with servers and track migrations.</p> </li> </ul> </li> </ul> <p> <b>Recommendations</b> </p> <p>We recommend that you use agent-based discovery for non-VMware environments, and whenever you want to collect information about network dependencies. You can run agent-based and agentless discovery simultaneously. Use agentless discovery to complete the initial infrastructure assessment quickly, and then install agents on select hosts to collect additional information.</p> <p> <b>Working With This Guide</b> </p> <p>This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for Application Discovery Service. The topic for each action shows the API request parameters and the response. Alternatively, you can use one of the AWS SDKs to access an API that is tailored to the programming language or platform that you're using. For more information, see <a href=\"http://aws.amazon.com/tools/#SDKs\">AWS SDKs</a>.</p> <note> <ul> <li> <p>Remember that you must set your Migration Hub home region before you call any of these APIs.</p> </li> <li> <p>You must make API calls for write actions (create, notify, associate, disassociate, import, or put) while in your home region, or a <code>HomeRegionNotSetException</code> error is returned.</p> </li> <li> <p>API calls for read actions (list, describe, stop, and delete) are permitted outside of your home region.</p> </li> <li> <p>Although it is unlikely, the Migration Hub home region could change. If you call APIs outside the home region, an <code>InvalidInputException</code> is returned.</p> </li> <li> <p>You must call <code>GetHomeRegion</code> to obtain the latest Migration Hub home region.</p> </li> </ul> </note> <p>This guide is intended for use with the <a href=\"http://docs.aws.amazon.com/application-discovery/latest/userguide/\">AWS Application Discovery Service User Guide</a>.</p> <important> <p>All data is handled according to the <a href=\"http://aws.amazon.com/privacy/\">AWS Privacy Policy</a>. You can operate Application Discovery Service offline to inspect collected data before it is shared with the service.</p> </important>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "discovery",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/discovery-2015-11-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/discovery/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/discovery/2015-11-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/discovery/2015-11-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:dlm": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-01-12",
        "versions": {
            "2018-01-12": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-01-12",
                    "x-release": "v4",
                    "title": "Amazon Data Lifecycle Manager",
                    "description": "<fullname>Amazon Data Lifecycle Manager</fullname> <p>With Amazon Data Lifecycle Manager, you can manage the lifecycle of your Amazon Web Services resources. You create lifecycle policies, which are used to automate operations on the specified resources.</p> <p>Amazon DLM supports Amazon EBS volumes and snapshots. For information about using Amazon DLM with Amazon EBS, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html\">Automating the Amazon EBS Snapshot Lifecycle</a> in the <i>Amazon EC2 User Guide</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "dlm",
                    "x-aws-signingName": "dlm",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/dlm-2018-01-12.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/dlm/"
                },
                "updated": "2020-04-24T20:56:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dlm/2018-01-12/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dlm/2018-01-12/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:dms": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-01-01",
        "versions": {
            "2016-01-01": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-01-01",
                    "x-release": "v4",
                    "title": "AWS Database Migration Service",
                    "description": "<fullname>Database Migration Service</fullname> <p>Database Migration Service (DMS) can migrate your data to and from the most widely used commercial and open-source databases such as Oracle, PostgreSQL, Microsoft SQL Server, Amazon Redshift, MariaDB, Amazon Aurora, MySQL, and SAP Adaptive Server Enterprise (ASE). The service supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle to MySQL or SQL Server to PostgreSQL.</p> <p>For more information about DMS, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html\">What Is Database Migration Service?</a> in the <i>Database Migration Service User Guide.</i> </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "dms",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/dms-2016-01-01.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/dms/"
                },
                "updated": "2020-04-27T20:04:05.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dms/2016-01-01/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dms/2016-01-01/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:docdb": {
        "added": "2019-01-10T20:43:10.000Z",
        "preferred": "2014-10-31",
        "versions": {
            "2014-10-31": {
                "added": "2019-01-10T20:43:10.000Z",
                "info": {
                    "version": "2014-10-31",
                    "x-release": "v4",
                    "title": "Amazon DocumentDB with MongoDB compatibility",
                    "description": "Amazon DocumentDB API documentation",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "docdb",
                    "x-aws-signingName": "rds",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/docdb-2014-10-31.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/rds/"
                },
                "updated": "2020-03-29T15:19:43.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/docdb/2014-10-31/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/docdb/2014-10-31/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ds": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-04-16",
        "versions": {
            "2015-04-16": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-04-16",
                    "x-release": "v4",
                    "title": "AWS Directory Service",
                    "description": "<fullname>Directory Service</fullname> <p>Directory Service is a web service that makes it easy for you to setup and run directories in the Amazon Web Services cloud, or connect your Amazon Web Services resources with an existing self-managed Microsoft Active Directory. This guide provides detailed information about Directory Service operations, data types, parameters, and errors. For information about Directory Services features, see <a href=\"https://aws.amazon.com/directoryservice/\">Directory Service</a> and the <a href=\"http://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html\">Directory Service Administration Guide</a>.</p> <note> <p>Amazon Web Services provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, iOS, Android, etc.). The SDKs provide a convenient way to create programmatic access to Directory Service and other Amazon Web Services services. For more information about the Amazon Web Services SDKs, including how to download and install them, see <a href=\"http://aws.amazon.com/tools/\">Tools for Amazon Web Services</a>.</p> </note>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ds",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ds-2015-04-16.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ds/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ds/2015-04-16/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ds/2015-04-16/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:dynamodb": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2012-08-10",
        "versions": {
            "2012-08-10": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2012-08-10",
                    "x-release": "v4",
                    "title": "Amazon DynamoDB",
                    "description": "<fullname>Amazon DynamoDB</fullname> <p>Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.</p> <p>With DynamoDB, you can create database tables that can store and retrieve any amount of data, and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation, and use the AWS Management Console to monitor resource utilization and performance metrics.</p> <p>DynamoDB automatically spreads the data and traffic for your tables over a sufficient number of servers to handle your throughput and storage requirements, while maintaining consistent and fast performance. All of your data is stored on solid state disks (SSDs) and automatically replicated across multiple Availability Zones in an AWS region, providing built-in high availability and data durability. </p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "dynamodb",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/dynamodb-2012-08-10.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/dynamodb/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ebs": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2019-11-02",
        "versions": {
            "2019-11-02": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2019-11-02",
                    "x-release": "v4",
                    "title": "Amazon Elastic Block Store",
                    "description": "<p>You can use the Amazon Elastic Block Store (Amazon EBS) direct APIs to create Amazon EBS snapshots, write data directly to your snapshots, read data on your snapshots, and identify the differences or changes between two snapshots. If you’re an independent software vendor (ISV) who offers backup services for Amazon EBS, the EBS direct APIs make it more efficient and cost-effective to track incremental changes on your Amazon EBS volumes through snapshots. This can be done without having to create new volumes from snapshots, and then use Amazon Elastic Compute Cloud (Amazon EC2) instances to compare the differences.</p> <p>You can create incremental snapshots directly from data on-premises into volumes and the cloud to use for quick disaster recovery. With the ability to write and read snapshots, you can write your on-premises data to an snapshot during a disaster. Then after recovery, you can restore it back to Amazon Web Services or on-premises from the snapshot. You no longer need to build and maintain complex mechanisms to copy data to and from Amazon EBS.</p> <p>This API reference provides detailed information about the actions, data types, parameters, and errors of the EBS direct APIs. For more information about the elements that make up the EBS direct APIs, and examples of how to use them effectively, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-accessing-snapshot.html\">Accessing the Contents of an Amazon EBS Snapshot</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about the supported Amazon Web Services Regions, endpoints, and service quotas for the EBS direct APIs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/ebs-service.html\">Amazon Elastic Block Store Endpoints and Quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ebs",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ebs-2019-11-02.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ebs/"
                },
                "updated": "2020-03-11T18:02:18.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ebs/2019-11-02/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ebs/2019-11-02/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ec2": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2016-11-15",
        "versions": {
            "2016-11-15": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2016-11-15",
                    "x-release": "v4",
                    "title": "Amazon Elastic Compute Cloud",
                    "description": "<fullname>Amazon Elastic Compute Cloud</fullname> <p>Amazon Elastic Compute Cloud (Amazon EC2) provides secure and resizable computing capacity in the AWS Cloud. Using Amazon EC2 eliminates the need to invest in hardware up front, so you can develop and deploy applications faster. Amazon Virtual Private Cloud (Amazon VPC) enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. Amazon Elastic Block Store (Amazon EBS) provides block level storage volumes for use with EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance and used like a hard drive.</p> <p>To learn more, see the following resources:</p> <ul> <li> <p>Amazon EC2: <a href=\"http://aws.amazon.com/ec2\">AmazonEC2 product page</a>, <a href=\"http://aws.amazon.com/documentation/ec2\">Amazon EC2 documentation</a> </p> </li> <li> <p>Amazon EBS: <a href=\"http://aws.amazon.com/ebs\">Amazon EBS product page</a>, <a href=\"http://aws.amazon.com/documentation/ebs\">Amazon EBS documentation</a> </p> </li> <li> <p>Amazon VPC: <a href=\"http://aws.amazon.com/vpc\">Amazon VPC product page</a>, <a href=\"http://aws.amazon.com/documentation/vpc\">Amazon VPC documentation</a> </p> </li> <li> <p>AWS VPN: <a href=\"http://aws.amazon.com/vpn\">AWS VPN product page</a>, <a href=\"http://aws.amazon.com/documentation/vpn\">AWS VPN documentation</a> </p> </li> </ul>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ec2",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ec2-2016-11-15.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ec2/"
                },
                "updated": "2020-05-11T19:05:17.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ec2-instance-connect": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2018-04-02",
        "versions": {
            "2018-04-02": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2018-04-02",
                    "x-release": "v4",
                    "title": "AWS EC2 Instance Connect",
                    "description": "Amazon EC2 Instance Connect enables system administrators to publish one-time use SSH public keys to EC2, providing users a simple and secure way to connect to their instances.",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ec2-instance-connect",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ec2-instance-connect-2018-04-02.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ec2-instance-connect/"
                },
                "updated": "2020-02-28T16:47:57.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ec2-instance-connect/2018-04-02/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ec2-instance-connect/2018-04-02/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ecr": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2015-09-21",
        "versions": {
            "2015-09-21": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2015-09-21",
                    "x-release": "v4",
                    "title": "Amazon EC2 Container Registry",
                    "description": "<fullname>Amazon Elastic Container Registry</fullname> <p>Amazon Elastic Container Registry (Amazon ECR) is a managed container image registry service. Customers can use the familiar Docker CLI, or their preferred client, to push, pull, and manage images. Amazon ECR provides a secure, scalable, and reliable registry for your Docker or Open Container Initiative (OCI) images. Amazon ECR supports private repositories with resource-based permissions using IAM so that specific users or Amazon EC2 instances can access repositories and images.</p> <p>Amazon ECR has service endpoints in each supported Region. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/ecr.html\">Amazon ECR endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ecr",
                    "x-aws-signingName": "ecr",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ecr-2015-09-21.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ecr/"
                },
                "updated": "2020-04-28T19:55:13.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecr/2015-09-21/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecr/2015-09-21/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ecr-public": {
        "added": "2021-01-15T15:07:17.488Z",
        "preferred": "2020-10-30",
        "versions": {
            "2020-10-30": {
                "added": "2021-01-15T15:07:17.488Z",
                "info": {
                    "version": "2020-10-30",
                    "x-release": "v4",
                    "title": "Amazon Elastic Container Registry Public",
                    "description": "<fullname>Amazon Elastic Container Registry Public</fullname> <p>Amazon Elastic Container Registry (Amazon ECR) is a managed container image registry service. Amazon ECR provides both public and private registries to host your container images. You can use the familiar Docker CLI, or their preferred client, to push, pull, and manage images. Amazon ECR provides a secure, scalable, and reliable registry for your Docker or Open Container Initiative (OCI) images. Amazon ECR supports public repositories with this API. For information about the Amazon ECR API for private repositories, see <a href=\"https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html\">Amazon Elastic Container Registry API Reference</a>.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ecr-public",
                    "x-aws-signingName": "ecr-public",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ecr-public-2020-10-30.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ecr-public/"
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecr-public/2020-10-30/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecr-public/2020-10-30/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    },
    "amazonaws.com:ecs": {
        "added": "2020-02-28T16:47:57.000Z",
        "preferred": "2014-11-13",
        "versions": {
            "2014-11-13": {
                "added": "2020-02-28T16:47:57.000Z",
                "info": {
                    "version": "2014-11-13",
                    "x-release": "v4",
                    "title": "Amazon EC2 Container Service",
                    "description": "<fullname>Amazon Elastic Container Service</fullname> <p>Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster. You can host your cluster on a serverless infrastructure that is managed by Amazon ECS by launching your services or tasks on Fargate. For more control, you can host your tasks on a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances that you manage.</p> <p>Amazon ECS makes it easy to launch and stop container-based applications with simple API calls, allows you to get the state of your cluster from a centralized service, and gives you access to many familiar Amazon EC2 features.</p> <p>You can use Amazon ECS to schedule the placement of containers across your cluster based on your resource needs, isolation policies, and availability requirements. Amazon ECS eliminates the need for you to operate your own cluster management and configuration management systems or worry about scaling your management infrastructure.</p>",
                    "x-logo": {
                        "url": "https://api.apis.guru/v2/cache/logo/https_twitter.com_awscloud_profile_image.png",
                        "backgroundColor": "#FFFFFF"
                    },
                    "termsOfService": "https://aws.amazon.com/service-terms/",
                    "contact": {
                        "name": "Mike Ralphson",
                        "email": "mike.ralphson@gmail.com",
                        "url": "https://github.com/mermade/aws2openapi",
                        "x-twitter": "PermittedSoc"
                    },
                    "license": {
                        "name": "Apache 2.0 License",
                        "url": "http://www.apache.org/licenses/"
                    },
                    "x-providerName": "amazonaws.com",
                    "x-serviceName": "ecs",
                    "x-origin": [
                        {
                            "contentType": "application/json",
                            "url": "https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/ecs-2014-11-13.normal.json",
                            "converter": {
                                "url": "https://github.com/mermade/aws2openapi",
                                "version": "1.0.0"
                            },
                            "x-apisguru-driver": "external"
                        }
                    ],
                    "x-apiClientRegistration": {
                        "url": "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct"
                    },
                    "x-apisguru-categories": [
                        "cloud"
                    ],
                    "x-preferred": true
                },
                "externalDocs": {
                    "description": "Amazon Web Services documentation",
                    "url": "https://docs.aws.amazon.com/ecs/"
                },
                "updated": "2020-04-09T06:28:07.000Z",
                "swaggerUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.json",
                "swaggerYamlUrl": "https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.yaml",
                "openapiVer": "3.0.0"
            }
        }
    }}
    """
    # data1 = json.loads(data.replace('\r', '\\r').replace('\n', '\\n'),strict=False)

    with open("../data/guru_1.json", 'r') as fp:
        json_data = json.load(fp)
        print(json_data)
    result = getGuruFromJson(json_data)
    writeToExcel(result)


