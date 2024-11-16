import pyperclip

f = open('prompts.txt', encoding='utf8')
g = []
n = 1
m = 0
tempstring = ''
tempstring1 = ''
tempstring2 = ''
tempstring3 = ''
for line in f.readlines():
    line = line[:-1]
    if n == 1:
        tempstring = line
        g.append({line : {}})
    elif n == 2:
        tempstring1 = line
    elif n == 3:
        tempstring2 = line
    elif n == 4:
        tempstring3 = line
    elif n == 5:
        g[m][tempstring][tempstring1] = line
    elif n == 6:
        g[m][tempstring][tempstring2] = line
    elif n == 7:
        g[m][tempstring][tempstring3] = line
    
    n +=1
    
    if n ==8:
        m +=1
        n = 1

pyperclip.copy(g)
spam = pyperclip.paste()
dict = [{'Your car breaks down unexpectedly. What’s your plan?': {'Use your emergency fund to cover the repair costs.': 'Excellent! Emergency funds exist for situations just like this. Your foresight pays off.', 'Charge it to a credit card and figure out payments later.': 'Credit cards can help, but watch out for high interest. Building an emergency fund could save you next time.', 'Skip the repair and start walking to work.': 'Walking is admirable, but delaying critical repairs could lead to bigger expenses in the long run.'}}, {'You get an unexpected $500 bonus at work. What do you do?': {'Add it to your emergency fund or use it to pay down debt.': 'Great choice! Allocating unexpected money to long-term goals or debt is a solid financial strategy.', "Buy the latest gadget you've been eyeing.": "It's fun to treat yourself, but think about whether this aligns with your financial priorities.", 'Put it in your checking account for daily expenses.': 'A practical approach, but without a plan, it might get spent without much to show for it.'}}, {'Your electricity bill is higher than usual this month. How do you respond?': {'Look at your budget and reduce spending in other areas to cover the increase.': 'Well done! Adjusting your budget shows strong financial discipline.', 'Pay the bill late to avoid cutting back on anything else.': 'Careful! Late payments can lead to fees and hurt your credit score over time.', 'Ignore the extra cost and hope your next paycheck covers it.': "Ignoring the issue might cause bigger problems later. It's better to plan ahead."}}, {"Your phone stops working. What's your plan?": {'Check for repair options or see if insurance covers it.': 'Excellent! Exploring cost-effective options first can save you money.', 'Buy a new phone using your savings.': 'Replacing a phone can be necessary, but using savings should be weighed carefully.', 'Finance the latest model through your carrier.': 'Financing spreads out payments but often includes hidden costs or interest.'}}, {'Your laptop dies, and you need one for school or work. How do you handle it?': {'Look for refurbished or second-hand options within your budget.': 'Smart choice! Refurbished tech often meets your needs without breaking the bank.', 'Purchase the newest model on a payment plan.': 'A new model is tempting, but payment plans can cost more in the long run—plan wisely.', 'Borrow one temporarily while you save for a replacement.': 'Great short-term solution! Avoiding immediate costs gives you time to save.'}}, {'You get a $50 gift card for your birthday. How do you use it?': {'Treat yourself to something fun you wouldn’t normally buy.': 'Great way to enjoy a gift without dipping into your budget!', 'Use it to buy essentials, saving your own money for other expenses.': 'Practical move! Stretching the value of a gift helps your budget overall.', 'Sell the card online for cash to put toward your savings.': 'Creative! Converting it to cash for savings shows strong financial foresight.'}}, {'Your phone bill suddenly includes a $20 fee you weren’t expecting. What do you do?': {'Call the provider to ask about the charge and dispute it if needed.': 'Nice work! Advocating for yourself can save you money.', 'Ignore it and pay the full bill to avoid hassle.': 'Easy, but this could lead to paying more in the long run without addressing the issue.', 'Pay less this month, skipping the extra fee, and hope they don’t notice.': 'Be careful! Skipping payments could result in late fees or service interruptions.'}}, {'You’re at the grocery store, and your favorite snacks are on sale. What do you do?': {'Stock up, as it will save money later.': 'Smart if you have room in your budget and the snacks won’t go to waste.', 'Buy a little more than usual but not too much.': 'Balanced choice! Treating yourself within reason keeps you on track.', 'Stick to your list and ignore the sale.': 'Disciplined! Sticking to your plan avoids impulse spending.'}}, {'Your boss asks if you want to work overtime for an extra $200 this week. Do you accept?': {'Take the extra work and use the money toward savings or debt.': 'Good move! Using extra income wisely gets you ahead.', 'Say no because you value your free time more.': 'It’s important to value your time, but consider balancing short-term sacrifice for long-term gains.', 'Accept but spend the extra money on something fun.': 'Earning extra is great, but spending it all right away might not help your goals.'}}, {'Your shoes wear out, and you need a new pair. How do you handle it?': {'Look for durable, reasonably-priced options within your budget.': 'Solid choice! Balancing cost and quality pays off in the long run.', 'Buy the cheapest pair you can find to save money.': 'Cheap now, but you might end up spending more if they wear out quickly.', 'Splurge on a premium brand because they’ll last longer.': 'Investing in quality can save money over time, but make sure it’s within your budget.'}}, {'You notice your favorite restaurant has started offering a loyalty program. What do you do?': {'Sign up if you eat there regularly and it could save you money.': 'Great! Loyalty programs can help if you’re already a regular customer.', 'Skip it because you don’t want to commit to spending more.': 'Smart! Avoiding unnecessary commitments keeps spending in check.', 'Sign up but only use it sparingly when it fits your budget.': 'Balanced! Using it occasionally while staying within budget works well.'}}, {'You see a $30 subscription charge for a service you forgot about. What’s your plan?': {'Cancel the subscription immediately and try to get a refund.': 'Smart! Canceling and requesting a refund is a proactive way to save money.', 'Review your usage to decide if it’s worth keeping before taking action.': 'Good strategy! Evaluating its value helps you make an informed decision.', 'Let it renew for now and make a note to reassess next month.': 'Be careful—letting it renew without a clear plan might lead to wasted money later.'}}]