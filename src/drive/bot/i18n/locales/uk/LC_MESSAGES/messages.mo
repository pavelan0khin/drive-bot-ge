��    .      �              �     �               /     ;     P     f     t     |     �     �     �     �     �     �     �     �          "  	   5     ?     P     e     t     �     �     �     �     �     �     �     �          &     8     G     W     k     {     �     �     �     �     �     �  �  �  ^  �  d   =  �   �     e  &     �   �  c   s     �  '  �      �   &       &   )  �   P  (     �   A  �   �  �   `       �  1  Y     5   \  �  �  {   T  �   �  �  b          *  v   /  v   �  2     �   P!  �   �!  �   w"  P   #  !   R#     t#  �   �#  �   4$  �   �$  �   H%  �   A&     ,'  $   F'     k'   ABOUT_MESSAGE ACTION_DECLINED ALLOW_NOTIFICATIONS ALL_TICKETS API_COMMAND_RESPONSE CONFIRM_CLEAR_HISTORY CONTINUE_EXAM DECLINE DESCRIBE_YOUR_PROBLEM DONATE_MESSAGE DROP_PASSED_TICKETS_HISTORY EXAM EXAM_FAILED EXAM_FINISHED EXAM_PASSED EXAM_STARTED EXISTING_API_TOKEN EXPLAIN_TRANSLATION_ERROR GENERATE_NEW_TOKEN GRPC_INFO HISTORY_IS_CLEAR HISTORY_IS_NOT_CLEAR HTTP_REST_INFO LANGUAGE_SELECTED MESSAGE_TOO_LONG NEW_API_TOKEN NEW_USER_START_MESSAGE NO NOTIFICATIONS_ARE_OFF NOTIFICATIONS_ARE_ON PROBLEM_IN_PROGRESS PROBLEM_RESOLVED_MESSAGE REISSUED_TOKEN REPLY_BOT_MESSAGE SELECT_BUTTONS SELECT_CATEGORY SELECT_NEW_LANGUAGE SESSION_IS_OVER START_MESSAGE TRANSLATION_PROBLEM_IN_PROGRESS UNKNOWN_ACTION WHICH_ANSWER_CHOSEN WRITE_ME_BUTTON WRITE_ME_BUTTON_RESPONSE YES Project-Id-Version:  1.0.0
Report-Msgid-Bugs-To: p.a.anokhin@gmail.com
POT-Creation-Date: 2023-10-26 18:02+0400
PO-Revision-Date: 2023-10-24 15:27+0400
Last-Translator: Pavel Anokhin <p.a.anokhin@gmail.com>
Language: uk
Language-Team: uk <LL@li.org>
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.13.0
 Список команд:

/start - початок
/about - інформація про бот
/language - змінити мову
/notifications - вкл/викл повідомлення
/clearhistory - очистити історію пройдених тестів
/problem - проблема з питанням (потрібно реплайнути питання)

Якщо ви розробник, я надаю безкоштовний API (REST та GRPC).Надіслати команду /api, щоб дізнатися подробиці

Також доступний <a href='https://github.com/pavelan0khin/drive-bot-ge'>початковий код</a> бота.Використовуйте його так, як самі вважаєте за потрібне

Якщо хочете сказати спасибі, можете пожертвувати на підтримку проекту. Реквізити можна отримати за командою /thanks

Цей бот підтримує кілька мов, але переклад був здійснений через Google-перекладач. Якщо ви знайшли помилку і хочете допомогти виправити її, можете надіслати команду /translatemebetter і описати, де саме в перекладі помилка Скасував. Можете знову натиснути будь-яку кнопку нижче Бажаєте отримувати повідомлення про додавання нових квитків до бази та зміни? Рекламу надсилати не буду :) ❓ Усі питання Що саме вас цікавить? Ви дійсно хочете очистити історію квитків? Це означає, що вам знову траплятимуться вже пройдені раніше питання. Добре, можете продовжувати відповідати на запитання :) ❌ Скасувати Опишіть, що не так із цим квитком?

Будь ласка, опишіть всю проблему в одному повідомленні. Медіафайли не підтримуються (поки що), тому використовуйте тільки текст Найкраща благордарність — підтримати проект грошима :) Якщо вам подобається, можете надіслати будь-яку зручну для вас суму, нижче реквізити:

{requisites} Ого, схоже, що ви пройшли всі квитки і більше не залишилося. Надішліть команду /clearhistory, я очищу історію і почнемо все з чистого листа :) 📚 Іспит ❌ Іспит провалений :( <b>Тест завершено</b>

Усього запитань: {total_tickets}

Відповідно правильно: {total_valid}
Відповідно неправильно: {total_invalid} ✅ Іспит зданий, вітаю! Тест почався, удачі. Якщо захочете закінчити, натисніть кнопку «❌ Скасувати» Ваш токен: <code>{api_token}</code>

Ви можете перевипустити його, натиснувши кнопку нижче Опишіть, де помилка в перекладі? Медіафайли не підтримуються (поки що), тому використовуйте лише текст Новий токен Контракт GRPC знаходиться <a href='https://github.com/pavelan0khin/drive-bot-ge/pavelan0khin/drive-bot-proto/blob/main/proto/client.proto'>тут</a>

Цей контракт автоматично генерує пакет Python, який можна встановити за допомогою:

<code>pip install drive-bot-proto</code>

Для інших мов ви можете завантажити файл контракту та самостійно <a href='grpcgenerator.com'>генерувати</a> пакети

Адреса для надсилання запитів grpc: {grpc_api_address}

Для авторизації потрібно використовувати токен, який можна згенерувати через бота (команда /api -> API Token). Токен має бути передано до метаданих таким чином: ключ – «authorization», значення – YOUR_API_TOKEN Історія очищена, можете знову проходити іспити :) Окей, історія не буде очищена Документація API доступна у форматах OpenAPI та redoc:

- <a href='{openapi_url}'>OpenAPI</a>
- <a href='{redoc_url}'>Redoc</a>

Для авторизації вам потрібно видати токен (команда /api -> API Token) і передати його в заголовку «Authorization» у такій формі: <code>Token YOUR_API_TOKEN</code>

Ми не стягуємо плату за API Обрано мову - українську. Ви можете змінити мову через команду /language Повідомлення занадто довге. Будь ласка, спробуйте зберегти його до 3500 символів. Ваш токен: <code>{api_token}</code>

Для використання в HTTP REST передайте його в заголовках запиту в ключі «Authorization» у такій формі: <code>Token {api_token}</code>

Для використання в GRPC передайте токен до метаданих запиту в ключі 'authorization' в такій формі: <code>{api_token}</code> Hello! Choose language Ні Повідомлення вимкнено. Щоб увімкнути, надішліть команду /notifications Повідомлення увімкнено. Щоб вимкнути, надішліть команду /notifications Спасибі за повідомлення. Я намагатимусь подивитися, в чому справа, якнайшвидше. Якщо хочете отримати повідомлення, коли проблема буде вирішена, натисніть кнопку нижче Раніше ви надсилали повідомлення про проблему з квитком. Вам надійшла відповідь:

{response} Ваш повторно виданий токен: <code>{api_token}</code>

Старий токен більше не дійсний Необхідно реплайнути повідомлення з тим квитком, де у вас виникла проблема Виберіть режим та натисніть на кнопку нижче Оберіть категорію Виберіть мову Мабуть, ви раніше скасували тест, в рамках якого я надіслав це питання, відповісти не вийде Привіт! Обирай будь-яку кнопку нижче. Інформація доступна за командою /about Спасибі за повідомлення. Я постараюся подивитися, в чому справа, якнайшвидше Упс, схоже, ви натиснули на кнопку, якої зараз бути не повинно. Якщо це так, то моя помилка - надішліть команду /start, щоб все відремонтувати Підказка: вибрана вами відповідь позначається жирним шрифтом. Правильна відповідь відзначена зеленим емодзи, решта — червоною Напишіть мені Гаразд, я вам напишу Так 