# program to take 10 sample phishing emails and find the most common hostname

email = ["jackpotwin@lottery.com",
         "claimtheprize@mymoney.com",
         "youarethewinner@lottery.com",
         "luckywinner@mymoney.com",
         "spinthewheel@flipkart.com",
         "dealwinner@snapdeal.com"
         "luckywinner@snapdeal.com"
         "luckyjackpot@americanlottery.com"
         "claimtheprize@lootolottery.com"
         "youarelucky@mymoney.com"]

hosts = {}

for i in email:
    host = i.split('@')[1]
    if host not in hosts:
        hosts[host] = 1
    else:
        hosts[host] += 1

print(hosts)
