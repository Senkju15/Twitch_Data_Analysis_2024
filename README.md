## 🎮 Analiza Danych: Top 1000 Streamerów Twitch (2024)

## 📌 O projekcie
Ten projekt to eksploracyjna analiza danych (EDA) skupiająca się na topowych 1000 streamerach na platformie Twitch. Celem było znalezienie odpowiedzi na pytania dotyczące zachowań widzów, popularności gier oraz tego, co przekłada się na największe zasięgi i przyrosty obserwujących.

## 🛠️ Technologie i Narzędzia
* **Baza Danych:** SQLite (DB Browser)
* **Język zapytań:** SQL
* **Wizualizacja:** Python (Pandas, Matplotlib) / Excel
* **Dane:** Plik CSV z rankingiem Twitch 2024

---

## 💡 Najciekawsze Wnioski (Key Insights)

Na podstawie analizy bazy danych odkryłem kilka ciekawych zależności:
1. **Eventy niszczą system:** Oficjalne kanały turniejowe (np. `twitchrivals`, `fortnite`, `riotgames`) deklasują indywidualnych streamerów pod kątem średniej liczby widzów i przyrostu followersów na stream (ponad 18 tys. nowych fanów na jedną transmisję dla konta Fortnite).
2. **Kiedy streamować?** Najpopularniejszymi dniami na odpalenie streama w topce nie jest weekend, a środek tygodnia: **Wtorek (183 kanały)** i **Środa (176 kanałów)**.
3. **Króluje kategoria "Just Chatting":** Aż 257 streamerów z top 1000 wybiera rozmowy z widzami jako swój główny kontent, co znacząco wyprzedza League of Legends (84) i GTA V (74).
4. **Maratony po portugalsku:** Streamerzy nadający w języku portugalskim mają zdecydowanie najdłuższe średnie transmisje, trwające ponad 9 godzin!

---

## 🔍 Próbka kodu SQL

Cały kod analizy znajduje się w pliku `zapytania.sql`. Oto jedno z zapytań, badające średni czas trwania streama w podziale na języki:

```sql
SELECT language, ROUND(AVG(avearge_stream_duration), 2) as sredni_czas_godziny
FROM streamers2024 
GROUP BY language 
ORDER BY COUNT(*) DESC 
LIMIT 5;

##
Źródło bazy danych: https://www.kaggle.com/datasets/hibrahimag1/top-1000-twitch-streamers-data-may-2024
