import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3,APIC

def add_album_art( songs_path, image_path):
    print("Starting to insert album-cover")
    for (root, _, files) in os.walk(songs_path):
        for file in files:
            try:
                # mp3 load
                audio_file_path = os.path.join(root, file)
                audio_file = MP3(audio_file_path, ID3=ID3)
                # image load
                with open(image_path, 'rb') as f:
                    image_data = f.read()
                # load org ID3 tag
                if 'APIC:' in audio_file.tags:
                    audio_file.tags['APIC:'].data = image_data
                else:
                    # create new ID3 tag
                    audio_file.tags.add(
                        APIC(
                            encoding=0,  # UTF-8
                            mime='image/jpeg',
                            type=3,
                            data=image_data
                        )
                    )
                audio_file.save()
            except Exception as e:
                print("error: ", e)
