import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('streamers2024.csv')

#Wykres 1 
top_gry = df['most_streamed_game'].value_counts().head(10)


plt.figure(figsize=(10, 6))
top_gry.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Najczęściej Streamowanych Kategorii w 2024', fontsize=14)
plt.ylabel('Liczba streamerów', fontsize=12)
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()


plt.savefig('wykres_gry_python.png')
plt.close()

#wykres 2 
top_followers = df.nlargest(10, 'followers_gained_per_stream')

plt.figure(figsize=(10, 6))
plt.barh(top_followers['name'], top_followers['followers_gained_per_stream'], color='lightgreen', edgecolor='black')
plt.gca().invert_yaxis() 
plt.title('Top 10 Streamerów: Nowi Followersci na Stream', fontsize=14)
plt.xlabel('Średnia liczba zdobytych obserwujących', fontsize=12)
plt.tight_layout()

plt.savefig('wykres_followersi_python.png')
plt.close()

print("Wykresy zapisały się w folderze jako pliki .png")