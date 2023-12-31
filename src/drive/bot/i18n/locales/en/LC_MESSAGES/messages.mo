��    .      �              �     �               /     ;     P     f     t     |     �     �     �     �     �     �     �     �          "  	   5     ?     P     e     t     �     �     �     �     �     �     �     �          &     8     G     W     k     {     �     �     �     �     �     �  �  �  D  �  B   �
  p        �  #   �  s   �  '   7     _  �   k  �     �   �  	   A     K  x   e  (   �  U     T   ]  ^   �  	     �    1   �  "   �  O  �  Y   J  C   �  /  �          /  J   2  J   }  �   �  f   d  O   �  G     (   c     �     �  o   �  @      J   a  �   �  �   ;     �     �     �   ABOUT_MESSAGE ACTION_DECLINED ALLOW_NOTIFICATIONS ALL_TICKETS API_COMMAND_RESPONSE CONFIRM_CLEAR_HISTORY CONTINUE_EXAM DECLINE DESCRIBE_YOUR_PROBLEM DONATE_MESSAGE DROP_PASSED_TICKETS_HISTORY EXAM EXAM_FAILED EXAM_FINISHED EXAM_PASSED EXAM_STARTED EXISTING_API_TOKEN EXPLAIN_TRANSLATION_ERROR GENERATE_NEW_TOKEN GRPC_INFO HISTORY_IS_CLEAR HISTORY_IS_NOT_CLEAR HTTP_REST_INFO LANGUAGE_SELECTED MESSAGE_TOO_LONG NEW_API_TOKEN NEW_USER_START_MESSAGE NO NOTIFICATIONS_ARE_OFF NOTIFICATIONS_ARE_ON PROBLEM_IN_PROGRESS PROBLEM_RESOLVED_MESSAGE REISSUED_TOKEN REPLY_BOT_MESSAGE SELECT_BUTTONS SELECT_CATEGORY SELECT_NEW_LANGUAGE SESSION_IS_OVER START_MESSAGE TRANSLATION_PROBLEM_IN_PROGRESS UNKNOWN_ACTION WHICH_ANSWER_CHOSEN WRITE_ME_BUTTON WRITE_ME_BUTTON_RESPONSE YES Project-Id-Version:  1.0.0
Report-Msgid-Bugs-To: p.a.anokhin@gmail.com
POT-Creation-Date: 2023-10-26 18:02+0400
PO-Revision-Date: 2023-10-24 15:27+0400
Last-Translator: Pavel Anokhin <p.a.anokhin@gmail.com>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.13.0
 List of commands:

/start - start
/about - information about the bot
/language - change language
/notifications - turn notifications on/off
/clearhistory - clear the history of passed tests
/problem - there is a problem with the question (you need to reply the question)

If you are a developer, I provide free API (REST and GRPC).Send /api command for details

The <a href='https://github.com/pavelan0khin/drive-bot-ge'>bot source code</a> is also available. Use it any way you want

If you want to say thank you, you can donate to support the project. Details can be obtained by command /thanks

This bot supports several languages, but translation has been made via Google Translate. If you find a mistake and want to help fix it, you can send the command /translatemebetter and describe where exactly the error is in the translation The action has been declined. You can press any button below again Want to be notified when new tickets are added to the database and changes are made? I won't send advertising :) ❓ All questions What exactly are you interested in? Do you really want to clear your ticket history? This means that you will get the previously passed questions again Ok, you can keep answering questions :) ❌ Decline Describe what's wrong with this ticket?

Please describe the entire problem in one message. Media files are not supported (yet), so please use text only. The best gratitude is to support the project with money :) If you like, you can send any amount convenient for you, the details are below:

{requisites} Wow, looks like you've gone through all the tickets and there are no more left. Send me the /clearhistory command, I'll clear the history and we'll start fresh :) 📚 Exam ❌ The exam is failed :( Test completed
Total questions: {total_tickets}

Answered correctly: {total_valid}
Incorrectly answered: {total_invalid} ✅ The exam is passed, congratulations! The test has begun, good luck. If you want to finish, click the "❌ Decline" button. Your token: <code>{api_token}</code>

You can change it by clicking the button below Describe where the translation error is? Media files are not supported (yet), so use text only New token GRPC contract is located <a href='https://github.com/pavelan0khin/drive-bot-ge/pavelan0khin/drive-bot-proto/blob/main/proto/client.proto'>here</a>

This contract automatically generates a Python package that can be installed via:

<code>pip install drive-bot-proto</code>

For other languages, you can download the contract file and <a href='grpcgenerator.com'>generate</a> packages yourself

Address for sending grpc requests: {grpc_api_address}

To authorize, you need to use a token, which you can generate through the bot (command /api -> API Token). The token must be passed to metadata as follows: key - 'authorization', value - YOUR_API_TOKEN History cleared, you can take your exams again :) Okay, the history won't be cleared API documentation is available in OpenAPI and redoc formats:

- <a href='{openapi_url}'>OpenAPI</a>
- <a href='{redoc_url}'>Redoc</a>

To authorize, you need to issue a token (command /api -> API Token) and pass it in the 'Authorization' header in the following form: <code>Token YOUR_API_TOKEN</code>

We don't charge for API requests The selected language is English. You can change the language using the /language command The message is too long. Please try to keep it to 3,500 characters. Your token: <code>{api_token}</code>

For use in HTTP REST, pass it in the request headers in the 'Authorization' key in the following form: <code>Token {api_token}</code>

For use in GRPC, pass the token to the request metadata in the 'authorization' key in the following form: <code>{api_token}</code> Hello! Choose language No Notifications are disabled. To turn it on, send the /notifications command Notifications are enabled. To turn it off, send the command /notifications Thank you for message. I'll try to see what's wrong as quickly as possible. If you want to be notified when the problem is resolved, click the button below You previously sent a message about a problem with a ticket. You have received a response:

{response} Your reissued token: <code>{api_token}</code>

The old token is no longer valid You need to reply the message with the ticket where you had the problem Select a mode and press the button below Select a category Select a language Apparently you have previously declined the test under which I sent this question, there is no way to answer it Hello! Choose any button below. Use /about command for more info Thank you for message. I'll try to see what's wrong as quickly as possible Oops, looks like you clicked on a button that shouldn't be there right now. If that's the case, my mistake - send the /start command to fix it Hint: the answer you have chosen is marked in bold. The correct answer is marked with a green emoji, the other answers are marked with a red emoji Write me Okay, I'll write to you Yes 