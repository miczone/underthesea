from os import listdir
from os.path import join
import shutil
from os import makedirs
import os
import librosa

# set your environment variable ORIGIN_FOLDER to path contain VLSP2020 ASR dataset
ORIGIN_FOLDER = os.environ['ORIGIN_FOLDER']
CORPUS_FOLDER = join(ORIGIN_FOLDER, "vlsp2020_train_set_02")
SAMPLE_FOLDER = join(ORIGIN_FOLDER, "SAMPLE-1")
TRANSCRIPT_FOLDER = join(SAMPLE_FOLDER, "transcript")
N_TRAIN_SAMPLES = 5
N_DEV_SAMPLES = 5
N_TEST_SAMPLES = 5

N_SAMPLES = N_TRAIN_SAMPLES + N_DEV_SAMPLES + N_TEST_SAMPLES


def create_dataset():
    shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
    makedirs(SAMPLE_FOLDER)
    TRAIN_FOLDER = join(SAMPLE_FOLDER, 'train')
    DEV_FOLDER = join(SAMPLE_FOLDER, 'dev')
    TEST_FOLDER = join(SAMPLE_FOLDER, 'test')

    for folder in [TRAIN_FOLDER, DEV_FOLDER, TEST_FOLDER]:
        shutil.rmtree(folder, ignore_errors=True)
        makedirs(folder)


def create_sample():
    def extract_sample(sample_type, file_id):
        wav_file = join(SAMPLE_FOLDER, sample_type, file_id + ".wav")
        shutil.copyfile(join(CORPUS_FOLDER, file_id + ".wav"), wav_file)
        duration = str(librosa.get_duration(filename=wav_file))

        with open(join(CORPUS_FOLDER, file_id + ".txt")) as f:
            transcript = f.read().strip()
        return wav_file, duration, transcript

    def write_transcript(transcript_file, data):
        with open(transcript_file, 'w') as f:
            f.write('PATH\tDURATION\tTRANSCRIPT\n')
            for item in data:
                content = '\t'.join(item) + '\n'
                f.write(content)

    files = listdir(CORPUS_FOLDER)
    text_files = [f for f in files if f.endswith(".txt")]

    print('Total:', len(files))
    data = {
        "train": [],
        "dev": [],
        "test": []
    }
    for i, file in enumerate(text_files[:N_SAMPLES]):
        file_id = file[:-4]
        print(file_id)
        if i < N_TRAIN_SAMPLES:
            sample_type = 'train'
        elif i < N_TRAIN_SAMPLES + N_DEV_SAMPLES:
            sample_type = 'dev'
        else:
            sample_type = 'test'
        file_data = extract_sample(sample_type, file_id)
        data[sample_type].append(file_data)

    for type in ["train", "dev", "test"]:
        write_transcript(join(SAMPLE_FOLDER, f'{type}.tsv'), data[type])


if __name__ == '__main__':
    create_dataset()
    create_sample()
