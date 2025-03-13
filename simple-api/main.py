from fastapi import FastAPI
import random
   
app = FastAPI()

side_hustle = [
    "Freelancing - Start Offering Your Skill online!",
    "Dropshipping - sell without handing inventory!",
    "E-commerce - Start Your Own store!",
    "Online Courses - Share Your Knowledge and earn money!",
    "Blogging - create content and earn through ads and sponsorship!",
    "youtube channel - Monetize vedeios through ads and sponsorship!"
]

money_quotes = [
    "Too many people spend money they earned..to buy things they don't want..to impress people that they don't like. --Will Rogers",
    "A wise person should have money in their head, but not in their heart. --Jonathan Swift",
    "Wealth consists not in having great possessions, but in having few wants. --Epictetus",
    "Money often costs too much. --Ralph Waldo Emerson",
    "Everyday is a bank account, and time is our currency. No one is rich, no one is poor, we've got 24 hours each. --Christopher Rice",
    "It's how you deal with failure that determines how you achieve success. --David Feherty"
    ]

@app.get("/side_hustles")
def get_side_hustles():
    """Return a random side Hustle idea"""
    return {"side_hustle": random.choice(side_hustle)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quote"""
   
    return{"moneyquote" : random.choice(money_quotes)}




