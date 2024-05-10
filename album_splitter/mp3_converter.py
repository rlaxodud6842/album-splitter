import os
from pydub import AudioSegment

def convert_wav_to_mp3(input_folder):
    # MP3를 저장할 하위 폴더 생성
    output_folder = os.path.join(input_folder, "covered")
    os.makedirs(output_folder, exist_ok=True)
    print("making covered folder")

    # 입력 폴더 내의 모든 파일 순회
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.wav'):  # WAV 파일인지 확인
                wav_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")

                # WAV 파일을 MP3로 변환
                sound = AudioSegment.from_wav(wav_file_path)
                sound.export(output_file_path, format="mp3")
    return output_folder
