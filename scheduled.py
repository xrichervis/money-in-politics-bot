# This branch of the bot tweets facts surrounding American campaign finance. I hoped this would break up some of the
# monotony of the daily_tweet and hope to upload new tweets come September.
# One of the biggest topics I would love the bot to breach is the concept of "dark money".

from config import *

import pause, datetime

# White House Race 2016; June tweets
WHR0 = "For the month of June, the Money in Politics bot will be periodically tweeting facts about the 2016 presidential election."
WHR1 = "The 2008 presidential election was the most expensive presidential race in US history, with $2.8 billion being spent, including campaign committee and outside spending. (Source: Center for Responsive Politics)"
WHR2 = "Including campaign committee and outside spending, it’s estimated that $2.4 billion was spent in the 2016 presidential race. (Source: Center for Responsive Politics)"
WHR3 = "Democrats and Republicans spent approximately the same amount of money in the 2016 election (congressional and presidential). (Source: Center for Responsive Politics)"
WHR4 = "From July 2015 through October 2016, Donald Trump received free media worth more than $5.9 billion. Clinton received less than half that figure, a little under $2.8 billion. (Source: mediaQuant, Inc.)"
WHR5 = "Including party and outside spending, Donald Trump’s 2016 campaign cost almost $398 million. Hillary Clinton’s campaign cost $768 million. (Source: Center for Responsive Politics)"

# "Last Congressional Race" 2018 midterm elecitons; July tweets
LCR0 = "For the month of July, the Money in Politics bot will be periodically tweeting facts about the 2018 congressional elections."
LCR1 = "The 2018 congressional election was the most expensive US midterm election ever, with more than $5.7 billion being spent. For comparison, $3.8 billion was spent in 2014 in the last US midterm election. (Source: Center for Responsive Politics)"
LCR2 = "In the 2018 election cycle, the average House congressional candidate who won his or her election spent $2,056,494. The average loser spent $959,794. (Source: Center for Responsive Politics)"
LCR3 = "In the 2018 election cycle, the average Senate congressional candidate who won his or her election spent $15,753,167. The average loser spent $9,976,736. (Source: Center for Responsive Politics)"
LCR4 = "In the 2018 election cycle, the least expensive winning House congressional campaign cost $231,921. (Source: Center for Responsive Politics)"
LCR5 = "In the 2018 election cycle, the least expensive winning Senate congressional campaign cost $3,354,107. (Source: Center for Responsive Politics)"
LCR6 = "In the 2018 election cycle, the average House congressional winner took $718,781 from political action committees. (Source: Center for Responsive Politics)"
LCR7 = "In the 2018 election cycle, the average Senate congressional winner took $1,996,169 from political action committees. (Source: Center for Responsive Politics)"

# Campaign trends over the last 30 years; August tweets
CT0 = "For the month of August, the Money in Politics bot will be periodically tweeting facts how campaign finance has evolved in the last 30 years."
CT1 = "In 2018, the average House congressional candidate who won their election spent $2,056,494. In 1990, the average winner spent $407,556. (Source: Center for Responsive Politics)"
CT2 = "In 2018, the average Senate congressional candidate who won their election spent $15,753,167. In 1990, the average winner spent $3,870,621. (Source: Center for Responsive Politics)"
CT3 = "Between 2000 and 2018, over 85% of House congressional races were won by the candidate who spent the most amount of money. (Source: Center for Responsive Politics)"
CT4 = "Between 2000 and 2018, over 72% of Senate congressional races were won by the candidate who spent the most amount of money. (Source: Center for Responsive Politics)"
CT5 = "In the 20 years before the 2010 Citizens United ruling, outside spending - money not coming directly from a campaign - totalled just $750 million. In the 10 years since the ruling, $4.5 billion has been spent by non-party independent groups. (Source: Center for Responsive Politics)"

# June tweet days
whr_day_0 =  datetime.datetime(2020, 6, 1, 17)
whr_day_1 =  datetime.datetime(2020, 6, 2, 17)
whr_day_2 =  datetime.datetime(2020, 6, 7, 17)
whr_day_3 =  datetime.datetime(2020, 6, 13, 17)
whr_day_4 =  datetime.datetime(2020, 6, 19, 17)
whr_day_5 =  datetime.datetime(2020, 6, 25, 17)

# July tweet days
lcr_day_0 = datetime.datetime(2020, 7, 1, 17)
lcr_day_1 = datetime.datetime(2020, 7, 2, 17)
lcr_day_2 = datetime.datetime(2020, 7, 6, 17)
lcr_day_3 = datetime.datetime(2020, 7, 10, 17)
lcr_day_4 = datetime.datetime(2020, 7, 14, 17)
lcr_day_5 = datetime.datetime(2020, 7, 19, 17)
lcr_day_6 = datetime.datetime(2020, 7, 23, 17)
lcr_day_7 = datetime.datetime(2020, 7, 27, 17)

# August tweet days
ct_day_0 = datetime.datetime(2020, 8, 1, 17)
ct_day_1 = datetime.datetime(2020, 8, 2, 17)
ct_day_2 = datetime.datetime(2020, 8, 7, 17)
ct_day_3 = datetime.datetime(2020, 8, 13, 17)
ct_day_4 = datetime.datetime(2020, 8, 19, 17)
ct_day_5 = datetime.datetime(2020, 8, 25, 17)


def send_scheduled_tweet():

        #June tweets
        print("Going to sleep until the first tweet is due...")

        pause.until(whr_day_0)

        api.update_status(status=WHR0)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(whr_day_1)

        api.update_status(status=WHR1)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(whr_day_2)

        api.update_status(status=WHR2)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(whr_day_3)

        api.update_status(status=WHR3)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(whr_day_4)

        api.update_status(status=WHR4)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(whr_day_5)

        api.update_status(status=WHR5)
        print("Tweet sent out, going to sleep until the next tweet is due...")


        #July tweets
        pause.until(lcr_day_0)

        api.update_status(status=LCR0)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(lcr_day_1)

        api.update_status(status=LCR1)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(lcr_day_2)

        api.update_status(status=LCR2)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(lcr_day_3)

        api.update_status(status=LCR3)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(lcr_day_4)

        api.update_status(status=LCR4)
        print("Tweet sent out, going to sleep until the next tweet is due...")
        pause.until(lcr_day_5)

        api.update_status(status=LCR5)

        pause.until(lcr_day_6)

        api.update_status(status=LCR6)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(lcr_day_7)

        api.update_status(status=LCR7)
        print("Tweet sent out, going to sleep until the next tweet is due...")


        #August tweets
        pause.until(ct_day_0)

        api.update_status(status=CT0)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(ct_day_1)

        api.update_status(status=CT1)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(ct_day_2)

        api.update_status(status=CT2)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(ct_day_3)

        api.update_status(status=CT3)
        print("Tweet sent out, going to sleep until the next tweet is due...")

        pause.until(ct_day_4)

        api.update_status(status=CT4)
        print("Tweet sent out, going to sleep until the next tweet is due...")
        pause.until(ct_day_5)

        api.update_status(status=CT5)
        print("No more tweets, all done!")

while True:
    try:
        send_scheduled_tweet()
    except:
        print("An error has seemed to occur...")
        pass
