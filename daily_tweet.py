# This branch of the bot is the most important: once a day, the bot tweets about one member of Congress' political donations.
# Specifically, it tweets about: who that Congressperson represents, how much money they've raised so far for the current election cycle,
# which organizations and sectors are their biggest contributors, and how to get in contact with them.

from config import *

import random, time
from crpapi import CRP

# this function randomly selects a congressperson's CID from a text file
# randomizer was inspired by the one here: https://www.codespeedy.com/how-to-get-a-random-line-from-a-text-file-in-python/
# Full list of Congressperson's CIDs found here: https://www.opensecrets.org/open-data/api-documentation
def find_a_CID():
        s=open("cid.txt", "r")
        m=s.readlines()
        l=[]
        for i in range(0,len(m)-1):
            x=m[i]
            z=len(x)
            a=x[:z-1]
            l.append(a)
        l.append(m[i+1])
        random_cid =random.choice(l)
        s.close()
        return random_cid

# This next part of the code utilises The Center for Responsive Politics Python client library to access OpenSecret's API. You can find its documentation on Github here: https://github.com/robrem/opensecrets-crpapi
# Sign up for an API Key here: https://www.opensecrets.org/api/admin/index.php?function=signup
def get_cand_data():
        random_cid = find_a_CID()
        crp = CRP(crp_api_key)
        cand = crp.fetch('getLegislators', id=random_cid, congno='116')
        contrib = crp.fetch('candContrib', cid=random_cid, cycle="2020")
        summ = crp.fetch('candSummary', cid=random_cid, cycle="2020")
        ind = crp.fetch('candIndustry', cid=random_cid, cycle="2020")
        return cand, contrib, summ, ind

# Now we want more specific detail. Numbers will have to be formatted to be more legible, and states and party denominations will have to be spelled out.
def format_tweets():
        cand, contrib, summ, ind = get_cand_data()

        name = cand['legislator']['@attributes']['firstlast']

        phone = cand['legislator']['@attributes']['phone']
        website = cand['legislator']['@attributes']['website']
        twitter = cand['legislator']['@attributes']['twitter_id']
        cycle_contrib = contrib['contributors']['@attributes']['cycle']
        # source_contrib = contrib['contributors']['@attributes']['source']

        contrib1 = contrib['contributors']['contributor'][0]['@attributes']['org_name']
        contrib2 = contrib['contributors']['contributor'][1]['@attributes']['org_name']
        contrib3 = contrib['contributors']['contributor'][2]['@attributes']['org_name']

        contrib1_total_edited = '{:,.2f}'.format(float(contrib['contributors']['contributor'][0]['@attributes']['total']))
        contrib2_total_edited = '{:,.2f}'.format(float(contrib['contributors']['contributor'][1]['@attributes']['total']))
        contrib3_total_edited = '{:,.2f}'.format(float(contrib['contributors']['contributor'][2]['@attributes']['total']))

        # cycle_summ = summ['summary']['@attributes']['cycle']
        state = summ['summary']['@attributes']['state']
        party = summ['summary']['@attributes']['party']
        chamber = summ['summary']['@attributes']['chamber']
        first_elected = summ['summary']['@attributes']['first_elected']
        next_election = summ['summary']['@attributes']['next_election']
        # source_summ = summ['summary']['@attributes']['source']
        last_updated_summ = summ['summary']['@attributes']['last_updated']

        raised_edited = '{:,.2f}'.format(float(summ['summary']['@attributes']['total']))
        spent_edited = '{:,.2f}'.format(float(summ['summary']['@attributes']['spent']))
        cash_on_hand_edited = '{:,.2f}'.format(float(summ['summary']['@attributes']['cash_on_hand']))

        # cycle_ind = ind['industries']['@attributes']['cycle']
        # source_ind = ind['industries']['@attributes']['source']
        last_updated_ind = ind['industries']['@attributes']['last_updated']

        ind1 = ind['industries']['industry'][0]['@attributes']['industry_name']
        ind2 = ind['industries']['industry'][1]['@attributes']['industry_name']
        ind3 = ind['industries']['industry'][2]['@attributes']['industry_name']

        ind1_total_edited = '{:,.2f}'.format(float(ind['industries']['industry'][0]['@attributes']['total']))
        ind2_total_edited = '{:,.2f}'.format(float(ind['industries']['industry'][1]['@attributes']['total']))
        ind3_total_edited = '{:,.2f}'.format(float(ind['industries']['industry'][2]['@attributes']['total']))

        relative = round(float(summ['summary']['@attributes']['total']) / 63179) # 63,179 is the real median American household income as of 2018

        if party == "D":
            full_party = "a Democratic"
        if party == "R":
            full_party = "a Republican"
        if party == "I":
            full_party = "an Indepedent"

        if chamber == "H":
            chamber = "representative"
        if chamber == "S":
            chamber = "senator"

        if state == "AL":
            state = "Alabama"
        if state == "AK":
            state = "Alaska"
        if state == "AZ":
            state = "Arizona"
        if state == "AR":
            state = "Arkansas"
        if state == "CA":
            state = "California"
        if state == "CO":
            state = "Colorado"
        if state == "CT":
            state = "Connecticut"
        if state == "DE":
            state = "Delaware"
        if state == "FL":
            state = "Florida"
        if state == "GA":
            state = "Georgia"
        if state == "HI":
            state = "Hawaii"
        if state == "id":
            state = "idaho"
        if state == "IL":
            state = "Illinois"
        if state == "IN":
            state = "Indiana"
        if state == "IA":
            state = "Iowa"
        if state == "KS":
            state = "Kansas"
        if state == "KY":
            state = "Kentucky"
        if state == "LA":
            state = "Louisiana"
        if state == "ME":
            state = "Maine"
        if state == "MD":
            state = "Maryland"
        if state == "MA":
            state = "Massachusetts"
        if state == "MI":
            state = "Michigan"
        if state == "MN":
            state = "Minnesota"
        if state == "MS":
            state = "Mississippi"
        if state == "MO":
            state = "Missouri"
        if state == "MT":
            state = "Montana"
        if state == "NE":
            state = "Nebraska"
        if state == "NV":
            state = "Nevada"
        if state == "NH":
            state = "New Hampshire"
        if state == "NJ":
            state = "New Jersey"
        if state == "NM":
            state = "New Mexico"
        if state == "NY":
            state = "New York"
        if state == "NC":
            state = "North Carolina"
        if state == "ND":
            state = "North Dakota"
        if state == "OH":
            state = "Ohio"
        if state == "OK":
            state = "Oklahoma"
        if state == "OR":
            state = "Oregon"
        if state == "PA":
            state = "Pennsylvania"
        if state == "RI":
            state = "Rhode Island"
        if state == "SC":
            state = "South Carolina"
        if state == "SD":
            state = "South Dakota"
        if state == "TN":
            state = "Tennessee"
        if state == "TX":
            state = "Texas"
        if state == "UT":
            state = "Utah"
        if state == "VT":
            state = "Vermont"
        if state == "VA":
            state = "Virginia"
        if state == "WA":
            state = "Washington"
        if state == "WV":
            state = "West Virginia"
        if state == "WI":
            state = "Wisconsin"
        if state == "WY":
            state = "Wyoming"


# Now with some templates, we can cretate the daily tweets.
        tweet1 = (
        "Hi! Today is " + name + " (" + party + " - " + state
        + ") day at the Money in Politics bot. Read this thread to learn a little about "
        + "this member of Congress' campaign contributions."
        )

        tweet2 = (
        "First elected in " + first_elected + ", " + name + " is " + full_party + " " + chamber + " for the state of " + state + ". " +  name + "'s next election is in " + next_election + "."
        )

        tweet3 = (
        "As of " + last_updated_summ + ", " + name + " has raised $" + raised_edited
        + " in the current election cycle. That amount is roughly the equivalent of " + str(relative) + " times the real median American household income. They have $" + cash_on_hand_edited + " on hand."
        )

        tweet4 = (
        "For the " + cycle_contrib + " cycle, "+ name + "'s top three contributors are: "
        + contrib1 + " ($" + contrib1_total_edited + "), " + contrib2 + " ($" + contrib2_total_edited
        + "), and " + contrib3 + " ($" + contrib3_total_edited + ")."
        )

        tweet5 = (
        "As of " + last_updated_ind + " the three industries that have donated the most to "
        + name + " in the current financial cycle are: " + ind1 + " ($" + ind1_total_edited + "), " + ind2 + " ($" + ind2_total_edited + "), and "
        + ind3 + " ($" + ind3_total_edited + ")."
        )

        tweet6 = (
        "If you want to get in touch with " + name + " 's office, you can call them at " + phone + " or visit their website at " + website
        + " . You can tweet them @" + twitter + "."
        )

        return tweet1, tweet2, tweet3, tweet4, tweet5, tweet6

# Now we want to tweet those formatted tweets, but we want them to come out as a thread. Tweepy allows us to reply to tweets,
# but we need to find the previous tweet. So we simply search the bot's timeline for tweets, and find the tweet id of the last one and reply to it.
# This has to be done every time we want to add a tweet to the thread.
def tweet_stuff():
        tweet1, tweet2, tweet3, tweet4, tweet5, tweet6 = format_tweets()

        api.update_status(status=tweet1)

        last_tweet = api.user_timeline(screen_name="donations_bot", count = 1)[0]
        last_tweet_id = last_tweet.id

        api.update_status(status=tweet2, in_reply_to_status_id=last_tweet_id)

        last_tweet = api.user_timeline(screen_name="donations_bot", count = 1)[0]
        last_tweet_id = last_tweet.id

        api.update_status(status=tweet3, in_reply_to_status_id=last_tweet_id)

        last_tweet = api.user_timeline(screen_name="donations_bot", count = 1)[0]
        last_tweet_id = last_tweet.id

        api.update_status(status=tweet4, in_reply_to_status_id=last_tweet_id)

        last_tweet = api.user_timeline(screen_name="donations_bot", count = 1)[0]
        last_tweet_id = last_tweet.id


        api.update_status(status=tweet5, in_reply_to_status_id=last_tweet_id)

        last_tweet = api.user_timeline(screen_name="donations_bot", count = 1)[0]
        last_tweet_id = last_tweet.id


        api.update_status(status=tweet6, in_reply_to_status_id=last_tweet_id)

# Now we just run all the functions within a larger function, interspersed by some text to make sense of it all.
def daily_tweet():
        random_cid = find_a_CID()
        print ("And we're back!!!")
        find_a_CID()
        print("Found a CID!")
        time.sleep(1)
        print("Now we're going to fetch campaign finance data about " + random_cid + "...")
        get_cand_data()
        print("Got all the data from Open Secrets, formatting tweets now...")
        format_tweets()
        print("We know what we want to tweet, let's publish them...")
        tweet_stuff()
        print("Thread has been published!")
        time.sleep(1)
        print("Going to sleep now for a day...")
        # Goes to sleep after a thread was successfully published.
        time.sleep(86400)

while True:
        try:
            daily_tweet()
# All of our smaller functions were placed into a larger function and run as one because it makes error handling a little easier.
# There are many reasons why our code might break and a thread might not be published, either in full or at all:
# congressperson already tweeted about, congressperson retired early, etc...
# So should that occur, the function just passes on to another congressperson.
        except:
            print("Error, will run again in 10 seconds...")
            time.sleep(10)
            pass

# Congrats for reading through this entire branch of the bot's documentation!
