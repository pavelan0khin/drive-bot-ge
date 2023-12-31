��    .      �              �     �               /     ;     P     f     t     |     �     �     �     �     �     �     �     �          "  	   5     ?     P     e     t     �     �     �     �     �     �     �     �          &     8     G     W     k     {     �     �     �     �     �     �  �  �  �  �  R   �  �   �     l  $   �  �   �  ;   ,     h  �   u  �   2  �   �     �     �     �  $   @  Z   e  e   �  �   &  
   �  �  �  9   �  !   �  d    b   q  M   �  L  "     o     �  V   �  X   �  �   :  e      d   f  5   �  4        6  
   F  p   Q  n   �  i   1  �   �  �   <  
   �     �     �   ABOUT_MESSAGE ACTION_DECLINED ALLOW_NOTIFICATIONS ALL_TICKETS API_COMMAND_RESPONSE CONFIRM_CLEAR_HISTORY CONTINUE_EXAM DECLINE DESCRIBE_YOUR_PROBLEM DONATE_MESSAGE DROP_PASSED_TICKETS_HISTORY EXAM EXAM_FAILED EXAM_FINISHED EXAM_PASSED EXAM_STARTED EXISTING_API_TOKEN EXPLAIN_TRANSLATION_ERROR GENERATE_NEW_TOKEN GRPC_INFO HISTORY_IS_CLEAR HISTORY_IS_NOT_CLEAR HTTP_REST_INFO LANGUAGE_SELECTED MESSAGE_TOO_LONG NEW_API_TOKEN NEW_USER_START_MESSAGE NO NOTIFICATIONS_ARE_OFF NOTIFICATIONS_ARE_ON PROBLEM_IN_PROGRESS PROBLEM_RESOLVED_MESSAGE REISSUED_TOKEN REPLY_BOT_MESSAGE SELECT_BUTTONS SELECT_CATEGORY SELECT_NEW_LANGUAGE SESSION_IS_OVER START_MESSAGE TRANSLATION_PROBLEM_IN_PROGRESS UNKNOWN_ACTION WHICH_ANSWER_CHOSEN WRITE_ME_BUTTON WRITE_ME_BUTTON_RESPONSE YES Project-Id-Version:  1.0.0
Report-Msgid-Bugs-To: p.a.anokhin@gmail.com
POT-Creation-Date: 2023-10-26 18:02+0400
PO-Revision-Date: 2023-10-24 15:27+0400
Last-Translator: Pavel Anokhin <p.a.anokhin@gmail.com>
Language: az
Language-Team: az <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.13.0
 Əmrlərin siyahısı:

/start - start
/about - bot haqqında məlumat
/language - dili dəyişdirin
/notifications - bildirişləri yandırın/söndürün
/clearhistory - keçmiş testlərin tarixini silin
/problem - sualda problem var (sualı cavablandırmaq lazımdır)

Əgər siz tərtibatçısınızsa, mən pulsuz API (REST və GRPC) təqdim edirəm. Ətraflı məlumat üçün /api əmrini göndərin

<a href='https://github.com/pavelan0khin/drive-bot-ge'>Botun mənbə kodu</a> da mövcuddur. İstədiyiniz şəkildə istifadə edin

Əgər təşəkkür etmək istəyirsinizsə, layihəni dəstəkləmək üçün ianə verə bilərsiniz. Təfərrüatları /thanks əmri ilə əldə etmək olar

Bu bot bir neçə dili dəstəkləyir, lakin tərcümə Google Translate vasitəsilə həyata keçirilib. Əgər səhv tapsanız və onu düzəltməyə kömək etmək istəyirsinizsə, /translatemebetter əmrini göndərə və tərcümədə səhvin tam olaraq harada olduğunu təsvir edə bilərsiniz. Aksiya rədd edildi. Aşağıdakı istənilən düyməni yenidən basa bilərsiniz Məlumat bazasına yeni biletlər əlavə edildikdə və dəyişikliklər edildikdə xəbərdar olmaq istəyirsiniz? Reklam göndərməyəcəyəm :) ❓ Bütün suallar Sizi tam olaraq nə maraqlandırır? Həqiqətən bilet tarixçənizi təmizləmək istəyirsiniz? Bu o deməkdir ki, əvvəllər keçmiş sualları yenidən alacaqsınız Yaxşı, suallara cavab verməyə davam edə bilərsiniz :) ❌ Rədd et Bu biletin nə olduğunu təsvir edin? Zəhmət olmasa bütün problemi bir mesajda təsvir edin. Media faylları (hələ) dəstəklənmir, ona görə də yalnız mətndən istifadə edin. Ən yaxşı təşəkkür layihəyə pulla dəstək olmaqdır :) İstəsəniz sizə uyğun olan istənilən məbləği göndərə bilərsiniz, təfərrüatlar aşağıdadır:

{requisites} Vay, deyəsən bütün biletləri keçmisiniz və daha heç nə qalmadı. Mənə /clearhistory əmrini göndər, mən tarixi təmizləyəcəm və təzə başlayaq :) 📚 İmtahan ❌ İmtahan uğursuz oldu :( Test tamamlandı
Ümumi suallar: {total_tickets}

Düzgün cavab verildi: {total_valid}
Yanlış cavab verildi: {total_invalid} ✅ İmtahan keçdi, təbrik edirik! Sınaq başladı, uğurlar. Bitirmək istəyirsinizsə, "❌ Rədd et" düyməsini basın. Tokeniniz: <code>{api_token}</code>

Aşağıdakı düyməni klikləməklə onu dəyişə bilərsiniz Tərcümə xətasının harada olduğunu təsvir edin? Media faylları (hələ) dəstəklənmir, ona görə də yalnız mətndən istifadə edin Yeni token GRPC müqaviləsi <a href='https://github.com/pavelan0khin/drive-bot-ge/pavelan0khin/drive-bot-proto/blob/main/proto/client.proto'>burada</a> yerləşir.

Bu müqavilə avtomatik olaraq aşağıdakılar vasitəsilə quraşdırıla bilən Python paketini yaradır:

<code>pip install drive-bot-proto</code>

Digər dillər üçün siz müqavilə faylını endirə və paketləri özünüz <a href='grpcgenerator.com'>yara bilərsiniz</a>

grpc sorğularının göndərilməsi üçün ünvan: {grpc_api_address}

Avtorizasiya etmək üçün siz bot vasitəsilə yarada biləcəyiniz işarədən istifadə etməlisiniz (komanda /api -> API Token). Token metadataya aşağıdakı kimi ötürülməlidir: açar - 'authorization', dəyər - YOUR_API_TOKEN Tarix təmizləndi, yenidən imtahan verə bilərsiniz :) Tamam, tarix təmizlənməyəcək API sənədləri OpenAPI və redoc formatlarında mövcuddur:

- <a href='{openapi_url}'>OpenAPI</a>
- <a href='{redoc_url}'>Redoc</a>

Avtorizasiya etmək üçün siz token (əmr /api -> API Token) verməli və onu aşağıdakı formada “Authorization” başlığına keçirməlisiniz: <code>Token YOUR_API_TOKEN</code>

API üçün ödəniş almırıq Seçilmiş dil ingilis dilidir. /language əmrindən istifadə edərək dili dəyişə bilərsiniz Mesaj çox uzundur. Lütfən, onu 3500 simvoldan çox saxlamağa çalışın. Tokeniniz: <code>{api_token}</code>

HTTP REST-də istifadə üçün onu 'Authorization' düyməsindəki sorğu başlıqlarına aşağıdakı formada ötürün: <code>Token {api_token}</code>

GRPC-də istifadə üçün tokeni 'authorization' açarında sorğu metadatasına aşağıdakı formada ötürün: <code>{api_token}</code> Hello! Choose language Yox Bildirişlər deaktiv edilib. Onu yandırmaq üçün /notifications əmrini göndərin Bildirişlər aktivləşdirilib. Onu söndürmək üçün əmr /notifications göndərin Mesaj üçün təşəkkür edirik. Mümkün qədər tez nəyin səhv olduğunu görməyə çalışacağam. Problem həll edildikdə xəbərdar olmaq istəyirsinizsə, aşağıdakı düyməni basın Siz əvvəllər biletlə bağlı problem barədə mesaj göndərmisiniz. Cavab aldınız:

{response} Yenidən buraxılmış nişanınız: <code>{api_token}</code>

Köhnə nişan artıq etibarlı deyil Mesaja problemin olduğu biletlə cavab verməlisiniz Bir rejimi seçin və aşağıdakı düyməni basın Kateqoriya seç Dil seçin Görünür, siz əvvəllər bu sualı göndərdiyim testdən imtina etmisiniz, ona cavab vermək mümkün deyil. Salam! Aşağıdakı istənilən düyməni seçin. Ətraflı məlumat üçün /about əmrindən istifadə edin Mesaj üçün təşəkkür edirik. Mümkün qədər tez nəyin səhv olduğunu görməyə çalışacağam Ups, deyəsən, hazırda orada olmamalı olan düyməyə klikləmisiniz. Əgər belədirsə, mənim səhvim - onu düzəltmək üçün /start əmrini göndərin İpucu: seçdiyiniz cavab qalın hərflərlə qeyd olunub. Düzgün cavab yaşıl emoji ilə, digər cavablar isə qırmızı emoji ilə qeyd olunur Mənə yaz Yaxşı, sənə yazacam Bəli 