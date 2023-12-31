��    .      �              �     �               /     ;     P     f     t     |     �     �     �     �     �     �     �     �          "  	   5     ?     P     e     t     �     �     �     �     �     �     �     �          &     8     G     W     k     {     �     �     �     �     �     �  �  �  �  �  I     �   d     �  "   �  �     2   �  
   �  �   �  �   �  �   :     �     	  �   (  .   �  W   �  Y   1  {   �  
     �    B   �       R  2  R   �  C   �  G       d     {  V   �  N   �  �   '  g   �  Y   N  T   �  /   �     -     ?  m   L  e   �  h      �   �  �   0     �     �     �   ABOUT_MESSAGE ACTION_DECLINED ALLOW_NOTIFICATIONS ALL_TICKETS API_COMMAND_RESPONSE CONFIRM_CLEAR_HISTORY CONTINUE_EXAM DECLINE DESCRIBE_YOUR_PROBLEM DONATE_MESSAGE DROP_PASSED_TICKETS_HISTORY EXAM EXAM_FAILED EXAM_FINISHED EXAM_PASSED EXAM_STARTED EXISTING_API_TOKEN EXPLAIN_TRANSLATION_ERROR GENERATE_NEW_TOKEN GRPC_INFO HISTORY_IS_CLEAR HISTORY_IS_NOT_CLEAR HTTP_REST_INFO LANGUAGE_SELECTED MESSAGE_TOO_LONG NEW_API_TOKEN NEW_USER_START_MESSAGE NO NOTIFICATIONS_ARE_OFF NOTIFICATIONS_ARE_ON PROBLEM_IN_PROGRESS PROBLEM_RESOLVED_MESSAGE REISSUED_TOKEN REPLY_BOT_MESSAGE SELECT_BUTTONS SELECT_CATEGORY SELECT_NEW_LANGUAGE SESSION_IS_OVER START_MESSAGE TRANSLATION_PROBLEM_IN_PROGRESS UNKNOWN_ACTION WHICH_ANSWER_CHOSEN WRITE_ME_BUTTON WRITE_ME_BUTTON_RESPONSE YES Project-Id-Version:  1.0.0
Report-Msgid-Bugs-To: p.a.anokhin@gmail.com
POT-Creation-Date: 2023-10-26 18:02+0400
PO-Revision-Date: 2023-10-24 15:27+0400
Last-Translator: Pavel Anokhin <p.a.anokhin@gmail.com>
Language: tr
Language-Team: tr <LL@li.org>
Plural-Forms: nplurals=1; plural=0;
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.13.0
 Komutların listesi:

/start - başlat
/about - bot hakkında bilgi
/language - dili değiştir
/notifications - bildirimleri açar/kapatır
/clearhistory - geçilen testlerin geçmişini temizler
/problem - soruda bir sorun var (soruyu yanıtlamanız gerekiyor)

Geliştirici iseniz ücretsiz API (REST ve GRPC) sağlıyorum. Ayrıntılar için /api komutunu gönderin

<a href="https://github.com/pavelan0khin/drive-bot-ge">Bot kaynak kodu</a> da mevcuttur. İstediğiniz şekilde kullanın

Teşekkür etmek isterseniz projeye destek olmak için bağışta bulunabilirsiniz. Ayrıntılar /thanks komutuyla elde edilebilir

Bu bot birçok dili desteklemektedir ancak çeviri Google Translate aracılığıyla yapılmıştır. Bir hata bulursanız ve düzeltmeye yardımcı olmak istiyorsanız /translatemebetter komutunu gönderebilir ve hatanın çeviride tam olarak nerede olduğunu açıklayabilirsiniz. İşlem reddedildi. Aşağıdaki herhangi bir tuşa tekrar basabilirsiniz Veritabanına yeni bilet eklendiğinde ve değişiklik yapıldığında haberdar olmak ister misiniz? Reklam göndermeyeceğim :) ❓Tüm sorular Tam olarak neyle ilgileniyorsunuz? Bilet geçmişinizi gerçekten temizlemek istiyor musunuz? Bu, daha önce geçtiğiniz soruları tekrar alacağınız anlamına gelir Tamam soruları cevaplamaya devam edebilirsiniz :) ❌ Reddet Bu biletteki sorunun ne olduğunu açıklayın?

Lütfen sorunun tamamını tek bir mesajda açıklayın. Medya dosyaları (henüz) desteklenmemektedir, bu nedenle lütfen yalnızca metin kullanın. En güzel teşekkür, projeye parayla destek olmaktır :) İsterseniz size uygun olan miktarı gönderebilirsiniz, detaylar aşağıda:

{requisites} Vay be, görünüşe bakılırsa tüm biletleri gözden geçirmişsin ve başka bilet kalmamış. Bana /clearhistory komutunu gönder, geçmişi temizleyeyim ve yeni bir başlangıç yapalım :) 📚 Sınav ❌Sınav başarısız oldu :( Test tamamlandı
Toplam soru sayısı: {total_tickets}

Doğru yanıtlandı: {total_valid}
Yanlış yanıtlandı: {total_invalid} ✅ Sınav başarıyla tamamlandı, tebrikler! Sınav başladı, başarılar. Bitirmek istiyorsanız "❌ Reddet" butonuna tıklayın. Simgeniz: <code>{api_token}</code>

Aşağıdaki butona tıklayarak değiştirebilirsiniz Çeviri hatasının nerede olduğunu açıklayın? Medya dosyaları (henüz) desteklenmediğinden yalnızca metin kullanın Yeni jeton GRPC sözleşmesi <a href='https://github.com/pavelan0khin/drive-bot-ge/pavelan0khin/drive-bot-proto/blob/main/proto/client.proto'>burada</a> bulunur

Bu sözleşme otomatik olarak şu yollarla kurulabilecek bir Python paketi oluşturur:

<code>pip install drive-bot-proto</code>

Diğer diller için sözleşme dosyasını indirebilir ve paketleri kendiniz <a href='grpcgenerator.com'>oluşturabilirsiniz</a>

grpc isteklerinin gönderileceği adres: {grpc_api_address}

Yetkilendirmek için bot aracılığıyla oluşturabileceğiniz bir jeton kullanmanız gerekir (komut /api -> API Token). Belirtecin meta verilere şu şekilde iletilmesi gerekir: anahtar - 'authorization', değer - YOUR_API_TOKEN
 Geçmişiniz temizlendi, sınavlarınıza tekrar girebilirsiniz :) Tamam, geçmiş silinmeyecek API belgeleri OpenAPI ve redoc formatlarında mevcuttur:

- <a href='{openapi_url}'>OpenAPI</a>
- <a href='{redoc_url}'>Redoc</a>

Yetkilendirmek için bir jeton (komut /api -> API Token) vermeniz ve bunu aşağıdaki biçimde 'Authorization' başlığına iletmeniz gerekir: <code>Token YOUR_API_TOKEN</code>

API için ücret almıyoruz Seçilen dil Türkçedir. /language komutunu kullanarak dili değiştirebilirsiniz Mesaj çok uzun. Lütfen bunu 3.500 karakterde tutmaya çalışın. Simgeniz: <code>{api_token}</code>

HTTP REST'te kullanmak için, bunu 'Authorization' anahtarındaki istek başlıklarına aşağıdaki biçimde iletin: <code>Token {api_token}</code>

GRPC'de kullanmak için belirteci 'authorization' anahtarındaki istek meta verilerine aşağıdaki biçimde iletin: <code>{api_token}</code> Hello! Choose language Hayir Bildirimler devre dışı bırakıldı. Açmak için /notifications komutunu gönderin Bildirimler etkinleştirildi. Kapatmak için /notifications komutunu gönderin Mesaj için teşekkürler. Mümkün olduğunca çabuk neyin yanlış olduğunu görmeye çalışacağım. Sorun çözüldüğünde bildirim almak istiyorsanız aşağıdaki butona tıklayın Daha önce biletle ilgili bir sorun hakkında mesaj göndermiştiniz. Bir yanıt aldınız:

{response} Yeniden yayınlanan jetonunuz: <code>{api_token</code>

Eski jeton artık geçerli değil Sorun yaşadığınız yerdeki mesaja biletle birlikte cevap vermeniz gerekmektedir. Bir mod seçin ve aşağıdaki düğmeye basın Bir kategori seç Bir dil seç Görünüşe göre bu soruyu gönderdiğim testi daha önce reddetmişsiniz, buna cevap vermenin bir yolu yok Merhaba! Aşağıdaki herhangi bir düğmeyi seçin. Daha fazla bilgi için /about komutunu kullanın Mesaj için teşekkürler. Neyin yanlış olduğunu mümkün olduğunca çabuk görmeye çalışacağım Hata! Şu anda orada olmaması gereken bir düğmeye tıklamışsınız gibi görünüyor. Eğer durum buysa, benim hatam - düzeltmek için /start komutunu gönderin İpucu: Seçtiğiniz cevap kalın harflerle işaretlenmiştir. Doğru cevap yeşil emojiyle, diğer cevaplar kırmızı emojiyle işaretlenmiştir. Bana yaz Tamam sana yazacağım Evet 