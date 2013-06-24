Its created to solve the below challenge
"""This webapp just consists of a admin page and a creative writing page.

There will be sessions of creative writing where there will be several participants. The participants will be visiting the creating writing page.
The admin will start the session from the admin page. When the admin start the session she will set the time limit for the session, like 2mins and the time given for each person to give a input sentence, like 15 seconds

When the session is started, whoever visits the creative writing page will be shown the timer in the frozen state. There will be a "start the story" button.
Each user is identified by their cookies and they can give themselves a nick name in the creative writing page without the page refreshing.

When one of the users hit the "start the story" button, the timer will start and will show up on the all the users pages. The user who hit the button will have 15 seconds to enter the first sentence.
After he enters the first sentence all the users are shown what the story starting is, which is basically that sentence. One of the other guy is now passed the buck to enter a sentence and given the time limit.
If he does not enter the sentence within that time, the buck is again passed to some other person. This sentence is added to the first sentence and shown to every guy.

People keep building the story, till the final time is over. The final story is shown in the admin page, with separation as to which nick gave which sentence.

You can get creative with the implementation as well!"""

HOW TO RUN DEMO!!

1) After extraction go to cmd and make current working directory to "mysite"
2)run command "python manage.py runserver". close chrome and reopen it.
3) go  to "127.0.0.1:8000/story/admin" and click geturl button
4)now you will see a string of length three ex: "kmk".
5)now go to "127.0.0.1:8000/story/kmk" where kmk is your random string.
6)it will ask your name enter it.
7)now open incognito and go to  "127.0.0.1:8000/story/kmk".enter other name.
8)you will see a string below indicates who is the active user. the active user only add lines to story.
9)after time completion you will see "game over" or "123failed"  on the same page in a block
10)now go to  "127.0.0.1:8000/story/admin" and click viewstory to view who contributed to story.
11)for now total time is set to 180 seconds and 15 seconds per user. i dnt set options for that.