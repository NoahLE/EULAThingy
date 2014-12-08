from django.db.models.loading import get_model
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

from eulathingy.thingys.models import ThingyString


ThingySection = get_model('thingys', 'ThingySection')


def generate_strings(file_path, file_name, thingy):
    """

    :param content:
    :return:
    """
    reader = PlaintextCorpusReader(file_path, [file_name])
    sentences = reader.sents()
    for sentence in sentences:
        yield ThingyString(
            doc=thingy,
            string=(' '.join(word for word in sentence))
        )
