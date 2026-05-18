Przykładowe zapytania SQL:

***1.Kto ma średnio najwięcej widzów na streamie?*** 



SELECT name, avg\_viewers\_per\_stream 

FROM streamers2024 

ORDER BY avg\_viewers\_per\_stream DESC 

LIMIT 10;



\-- Wyniki:

\-- 1. name: twitchrivals | avg\_viewers\_per\_stream: 481615

\-- 2. name: ow\_esports | avg\_viewers\_per\_stream: 400009

\-- 3. name: gcxevent | avg\_viewers\_per\_stream: 387406

\-- 4. name: fortnite | avg\_viewers\_per\_stream: 352166

\-- 5. name: rocketleague | avg\_viewers\_per\_stream: 349645

\-- 6. name: riotgames | avg\_viewers\_per\_stream: 346968

\-- 7. name: evo | avg\_viewers\_per\_stream: 338908

\-- 8. name: att | avg\_viewers\_per\_stream: 261664

\-- 9. name: echo\_esports | avg\_viewers\_per\_stream: 249671

\-- 10. name: gaules | avg\_viewers\_per\_stream: 235565







***2.Jakie gry są najczęściej "głównymi grami" streamerów? (Top 5)***



SELECT most\_streamed\_game, COUNT(\*) as liczba\_streamerow 

FROM streamers2024 

GROUP BY most\_streamed\_game 

ORDER BY liczba\_streamerow DESC 

LIMIT 5

;



\-- Wyniki:

\-- 1. most\_streamed\_game: Just Chatting | liczba\_streamerow: 257

\-- 2. most\_streamed\_game: League of Legends | liczba\_streamerow: 84

\-- 3. most\_streamed\_game: Grand Theft Auto V | liczba\_streamerow: 74

\-- 4. most\_streamed\_game: VALORANT | liczba\_streamerow: 60

\-- 5. most\_streamed\_game: Casino | liczba\_streamerow: 36











***3.W jakie dni streamerzy najczęściej odpalają transmisje?***



SELECT most\_active\_day, COUNT(\*) as liczba\_kanalow 

FROM streamers2024 

GROUP BY most\_active\_day 

ORDER BY liczba\_kanalow DESC;



\-- Wyniki:

\-- 1. most\_active\_day: Tuesday | liczba\_kanalow: 183

\-- 2. most\_active\_day: Wednesday | liczba\_kanalow: 176

\-- 3. most\_active\_day: Thursday | liczba\_kanalow: 144

\-- 4. most\_active\_day: Saturday | liczba\_kanalow: 132

\-- 5. most\_active\_day: Sunday | liczba\_kanalow: 129

\-- 6. most\_active\_day: Monday | liczba\_kanalow: 118

\-- 7. most\_active\_day: Friday | liczba\_kanalow: 117











***4.Kto zdobywa najwięcej followersów na jednym streamie? (Top 5 najszybciej rosnących)***



SELECT name, followers\_gained\_per\_stream 

FROM streamers2024 

ORDER BY followers\_gained\_per\_stream DESC 

LIMIT 5;



\-- Wyniki:

\-- 1. name: fortnite | followers\_gained\_per\_stream: 18889

\-- 2. name: quackitytoo | followers\_gained\_per\_stream: 18808

\-- 3. name: kaicenat | followers\_gained\_per\_stream: 18405

\-- 4. name: legendus\_shaka | followers\_gained\_per\_stream: 16467

\-- 5. name: kingsleagueamericas | followers\_gained\_per\_stream: 13617







***5.Jaki jest średni czas trwania streama w zależności od języka? (Top 10 języków)***



SELECT language, ROUND(AVG(average\_stream\_duration), 2) as sredni\_czas\_godziny

FROM streamers2024 

GROUP BY language 

ORDER BY COUNT(\*) DESC 

LIMIT 10;



\-- Wyniki:

\-- 1. language: English | sredni\_czas\_godziny: 5.93

\-- 2. language: Russian | sredni\_czas\_godziny: 5.97

\-- 3. language: Spanish | sredni\_czas\_godziny: 4.43

\-- 4. language: Portuguese | sredni\_czas\_godziny: 9.14

\-- 5. language: Japanese | sredni\_czas\_godziny: 6.15

\-- 6. language: French | sredni\_czas\_godziny: 5.29

\-- 7. language: German | sredni\_czas\_godziny: 5.83

\-- 8. language: Chinese | sredni\_czas\_godziny: 6.9

\-- 9. language: Polish | sredni\_czas\_godziny: 5.59

\-- 10. language: Italian | sredni\_czas\_godziny: 4.73







***6.Suma wszystkich wyświetleń (total views) dla top 5 kanałów?***



SELECT name, total\_views 

FROM streamers2024 

ORDER BY total\_views DESC 

LIMIT 5;



\-- Wyniki:

\-- 1. name: ninja | total\_views: 572000000

\-- 2. name: shroud | total\_views: 571000000

\-- 3. name: xqc | total\_views: 525000000

\-- 4. name: summit1g | total\_views: 505000000

\-- 5. name: lirik | total\_views: 422000000







***7.Ile jest poszczególnych "typów" streamerów?***



SELECT type, COUNT(\*) as liczba 

FROM streamers2024 

GROUP BY type;



\-- Wyniki:

\-- 1. type: esports | liczba: 57

\-- 2. type: personality | liczba: 942









