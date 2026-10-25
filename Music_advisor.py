playlist = {}

def add_song():
    song = input("Song name: ")
    genre = input("Genre: ")
    playlist.setdefault(genre, []).append(song)

def show_playlist():
    for genre, songs in playlist.items():
        print(f"\n{genre}:")
        for song in songs:
            print("-", song)

while True:
    print("\n1. Add Song")
    print("2. Show Playlist")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_song()
    elif choice == "2":
        show_playlist()
    elif choice == "3":
        break
