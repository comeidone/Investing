import requests

body = "curr_id=18949&smlID=1167004&header=HRA+Cronologia+Dati&st_date=22%2F12%2F2019&end_date=20%2F12%2F2020&interval_sec=Weekly&sort_col=date&sort_ord=ASC&action=historical_data"

header= {'Host': 'it.investing.com',
'Connection': 'keep-alive',
'Content-Length': '171',
'Accept': 'text/plain, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
'Content-Type':'application/x-www-form-urlencoded',
'Origin': 'https://it.investing.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://it.investing.com/equities/hera-spa-historical-data',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'it,it-IT;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cookie': 'PHPSESSID=sgt73nf8put85n5fsn76b61rc6; geoC=IT; adBlockerNewUserDomains=1608485659; StickySession=id.44754091682.301it.investing.com; udid=eb7eab3d8add89b33f9d8f2a113796eb; smd=eb7eab3d8add89b33f9d8f2a113796eb-1608485659; logglytrackingsession=7a5f8a7c-f220-44f9-b7cc-cc6845dad5ca; _ga=GA1.2.1417124385.1608485659; _gid=GA1.2.1406125074.1608485660; __gads=ID=00a902785c98a817:T=1608485665:S=ALNI_Mb77u037_zZoad_MGVCQ7psKHRqgQ; G_ENABLED_IDPS=google; _fbp=fb.1.1608485663058.1803946350; r_p_s_n=1; SKpbjs-unifiedid=%7B%22TDID%22%3A%22856ceece-619b-40bd-a45b-3595258cfcc0%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-12-20T17%3A34%3A32%22%7D; adsFreeSalePopUp=3; gtmFired=OK; OptanonAlertBoxClosed=2020-12-20T17:35:01.204Z; eupubconsent-v2=CO-u3CfO-u3CfAcABBENBFCsAP_AAH_AAChQHLtf_X_fb3_j-_59_9t0eY1f9_7_v20zjgeds-8Nyd_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6IkVqTPsbk2Mr7NKJ7PEinMbe2dYGH9_n9XTuZKY79_s___z__-__v__77f_r-3_3_vp9X---_e4HLgEmGpfARZiWOBJNGlUKIEIVxIdACACihGFomsICVwU7K4CP0EDABAagIwIgQYgoxZBAAAAAElEQEgB4IBEARAIAAQAqQEIACNAEFgBIGAQACgGhYARQBCBIQZHBUcpgQESLRQTyRgCUXexhhCGUWAFAo_oAAAA.f_gAD_gAAAAA; usprivacy=1YNN; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2218949%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A18%3A%22%2Fequities%2Fhera-spa%22%3B%7D%7D%7D%7D; _pbjs_userid_consent_data=1752044293385998; SKpbjs-unifiedid_last=Sun%2C%2020%20Dec%202020%2017%3A35%3A23%20GMT; id5id.1st_212_nb=0; SKpbjs-id5id=%7B%22created_at%22%3A%222020-12-20T17%3A34%3A32Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMO93Yfh50mgiJ0PYNvsuqXOK_uDLWwAo-ORdJeeg%22%2C%22universal_uid%22%3A%22ID5-ZHMO93Yfh50mgiJ0PYNvsuqXOK_uDLWwAo-ORdJeeg%22%2C%22signature%22%3A%22ID5_AZB4jegIAW20Dfg-OV3zsqK9lGbynFABe1GLaFiOllhUZUgjwdIcGinEGGEtnaiXIDmr5nceaJQW1odx1P-xejM%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%7D; SKpbjs-id5id_last=Sun%2C%2020%20Dec%202020%2017%3A35%3A23%20GMT; outbrain_cid_fetch=true; nyxDorf=NjExfGQ2N28%2Bdj0wN2BmZzJ9YTg3MQ%3D%3D; OptanonConsent=isIABGlobal=false&datestamp=Sun+Dec+20+2020+18%3A39%3A45+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.7.0&hosts=&consentId=d66bb36d-cac2-4f3a-96e8-47d419d3d09c&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&AwaitingReconsent=false&geolocation=IT%3B75; OB-USER-TOKEN=ebecadd6-a90f-430e-bd76-f55ade48841b; GED_PLAYLIST_ACTIVITY=W3sidSI6IkdKaTAiLCJ0c2wiOjE2MDg0ODYxMTksIm52IjoxLCJ1cHQiOjE2MDg0ODU3MTksImx0IjoxNjA4NDg2MTE4fSx7InUiOiJWWjBFIiwidHNsIjoxNjA4NDg1Njk4LCJudiI6MCwidXB0IjoxNjA4NDg1NjYxLCJsdCI6MTYwODQ4NTY2MX1d'
}

r = requests.post(
    "https://it.investing.com/instruments/HistoricalDataAjax",headers=header, data=body)

f = open("investing.xlsx", "w")
f.write(r.text)
f.close()