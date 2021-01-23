from os import listdir
from os.path import join
import shutil
from os import makedirs

CORPUS_FOLDER = "vlsp2020_train_set_02"
SAMPLE_FOLDER = "sample"
TRANSCRIPT_FOLDER = "sample/transcript"
N_TRAIN_SAMPLES = 5
N_TEST_SAMPLES = 5

N_SAMPLES = N_TRAIN_SAMPLES + N_TEST_SAMPLES


def create_dataset():
    shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
    makedirs(SAMPLE_FOLDER)
    TRAIN_FOLDER = join(SAMPLE_FOLDER, 'train')
    TEST_FOLDER = join(SAMPLE_FOLDER, 'test')

    shutil.rmtree(TRAIN_FOLDER, ignore_errors=True)
    makedirs(TRAIN_FOLDER)
    shutil.rmtree(TEST_FOLDER, ignore_errors=True)
    makedirs(TEST_FOLDER)


def create_sample():
    def extract_sample(sample_type, file_id):
        shutil.copyfile(join(CORPUS_FOLDER, file_id + ".wav"), join(SAMPLE_FOLDER, file_id + ".wav"))

    # def write_transcript(type, data):
    #     if type == 'train':
    #
    # TRAIN_TRANSCRIPT_FILE = join(SAMPLE_FOLDER, 'train.tsv')
    #
    # TEST_TRANSCRIPT_FILE = join(SAMPLE_FOLDER, 'test.tsv')
    # with open(TRAIN_TRANSCRIPT_FILE, 'w') as f:
    #     f.write('PATH\tDURATION\tTRANSCRIPT')


files = listdir(CORPUS_FOLDER)
text_files = [f for f in files if f.endswith(".txt")]

print('Total:', len(files))

for file in text_files[:N_SAMPLES]:
    shutil.copyfile(join(CORPUS_FOLDER, file), join(SAMPLE_FOLDER, file))
    file_id = file[:-4]
    print(file_id)
    sample_type = 'train'

if __name__ == '__main__':
    create_dataset()
    create_sample()
