#!/usr/bin/python

import pprint
from tabulate import tabulate
from tweety.bot import Twitter
from colorama import Fore, Back, Style

markets_list = [
    "krugermacro",
    "fiskantes",
    "mattigags"
]

def colorize(nick):
    value = sum(ord(c) for c in nick)
    all_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW,
                  Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                  Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX,
                  Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                  Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX]
    index = value % len(all_colors)
    color = all_colors[index]
    colored_nick = color + nick + Style.RESET_ALL
    return colored_nick

def display(table):
    max_nick_len = max(len(nick) for nick, _ in table)
    for nick, msg in table:
        nick_part = " " * (max_nick_len - len(nick)) + colorize(nick)
        line = f"{nick_part} | {msg}"
        print(line)

# Also add colors to nicks for differentiating them
table = [
    ["hjkejke", "jdkjsjksd"],
    ["hjkejke", "jdkjsjksd"],
    ["hjkejke", "jdkjsjksd"],
    ["gentaaoooooo", "jdkjsjksd dsdskjdsjkds kjsds"],
    ["sssarae", "jdkjsjksd"],
    ["nnfnfbe", "jdkjsjksd"],
]

table = []
for nick in markets_list:
    tweets = Twitter(nick).get_tweets()
    for post in tweets:
        #if post.is_retweet:
        #    msg += "RT"
        #print(tweets[0].to_dict())
        msg = post.tweet_body

        #print(post.is_retweet, nick, msg)
        #try:
        #    pprint.pprint(post.to_dict())
        #except TypeError:
        #    pass

        timest = post.created_on
        table.append([nick, msg])
display(table)

