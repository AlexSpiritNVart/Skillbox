violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
quantity_songs = int(input('Количество песен: '))
names_of_songs = [input(f'Название {song+1} песни: ') for song in range(quantity_songs)]
print(names_of_songs)
total_time = 0
for song in names_of_songs:
    total_time += violator_songs[song]
print(round(total_time, 2))
