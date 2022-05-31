# I think this program uses a lot of conditional statements. It's able to generate instrumentation and melodies
# based on the moods and categories that people choose. Music theory can also help associate certain music with
# certain emotions. For example, major chords are upbeat or happy, minor chords are sad, and diminished chords
# are suspenseful. It can also determine the speed of a song based on how it's categorized; a suspenseful or happy
# song would have a higher bpm (beats per minute) whereas a chill/relaxed song would have a lower bpm.Based on the input
# of the user, the program turns simple terms like happy, relaxed, sad, suspenseful, etc to come up with a melody for a
# piece of music. Additionally, it uses subcategories and genres to select the specific instrumentation in the song.
# A rock song may use electric guitar and a lot of drums while a classical piece would use a lot of piano and other
# string instruments.

# In my code, I'm using the basic outline of the word auto-generator we coded in class, and applying it to different
# pieces of music based on the emotions they convey. The user can input the emotion of the piece they want, and the
# random generator will take another piece with that emotion to create its own music.

# I think some outliers for this project may be other musical elements that my code cannot generate. Soundraw AI can
# create the tempo, lengths of the note, different instruments, and dynamics of the piece whereas my code can only
# produce note names. I think if I included note values (length of each note) it may better coincide with the emotion
# it was trying to convey. I also think that only using one piece of music that subjectively portrayed a certain
# emotion may not be the most reliable way to create a piece.


# For each generation the code makes, I played the notes on an online keyboard so you can hear exactly what it would
# sound like if it could produce audio

import random

global text
global word


def run_main():

    print("Would you like your song to be happy, sad or relaxed?")
    user_input = input().lower()

    def pick_music():

        global text
# for each input, I took sheet music from a disney song that I felt corresponded to that emotion. For the input sad,
# I used the song Part of your World from The Little Mermaid. For happy, I chose I Just Can't Wait to be King from
# The Lion King, and for relaxed, I used I see the Light from Tangled
        if user_input == "sad":
            text = "e f# g g rest f# g a a rest e f# g g f# g f# g a a rest f# g a a g a g rest e g a b b a a rest " \
                   "g a b b b b rest a g f# d rest g a b rest rest e g b rest rest e g a rest rest g g g g a b d d d" \
                   "rest d d d d e g d e g a g g g g a b d d d d rest g a rest rest d d d e g rest rest a rest rest " \
                   "f# g a b g a b b g a b d c c b d c c b g d c b g"
            return text
        elif user_input == "happy":
            text = "d d e g a b a g rest d e g g a g r d e g g g bf a g g bf bf bf a g rest d e g g e bf a g rest g" \
                   " b g g g g rest d e g g g g g b g a rest e g bf a g d a g g rest e g g g a g rest e g g g b a"\
                   "d d e g a b a g rest d e g g a g r d e g g g bf a g g bf bf bf a g rest d e g g e bf a g rest g" \
                   " b g g g g rest d e g g g g g b g a rest e g bf a g d a g g rest e g g g a g rest e g g g b a"
            return text
        elif user_input == "relaxed":
            text = "a g f#rest e f# e c# d a rest a g f# rest e f# e c# d rst b a g rest a d a d f# e a r g f# d e " \
                   "rest rest a g f# rest e f# e c# d a rest a g f# rest e f# e c# d rest b a g rest d c# b a rest d" \
                   " d c# b f# a rest b c# d g g f# a rest d e e e a g g f# rest b c# d g g f# a rest d e f# g f# e " \
                   "d rest b c# d g g f# a r d e f# e e d rest a g f# rest e f# e c# d a"
            return text
        else:
            print("invalid answer.")

    def generation():

        global text

        words = text.split(" ")

        next_words = dict()

        for i in range(len(words) - 1):
            word = words[i]

            if word not in next_words.keys():
                next_words[word] = []
            next_words[word].append(words[i + 1])

        print(words[0])

        print(next_words)

        for i in range(100):
            word = random.choice(next_words[word])
            print(word, end=' ')

    pick_music()
    generation()


run_main()

