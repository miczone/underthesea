from os.path import join

from underthesea.datasets.vlsp2020_dp import VLSP2020_DP_SAMPLE
from underthesea.file_utils import MODELS_FOLDER
from underthesea.models.dependency_parser_extend import DependencyParserExtend
from underthesea.models.modules.embeddings import TokenEmbeddings, StackEmbeddings
from underthesea.trainers.dependency_parser_trainer_extend import DependencyParserTrainerExtend

corpus = VLSP2020_DP_SAMPLE()

embeddings = StackEmbeddings([
    TokenEmbeddings()
])
parser = DependencyParserExtend(embeddings=embeddings, init_pre_train=True)
trainer: DependencyParserTrainerExtend = DependencyParserTrainerExtend(parser, corpus)
trainer.train(
    base_path=join(MODELS_FOLDER, 'parsers', 'vi-dp-sample-extend'),
    max_epochs=3,
    mu=.9  # optimizer parameters
)
