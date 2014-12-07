from django.db.models.loading import get_model
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from eulathingy.thingys.models import ThingySentence


ThingySection = get_model('thingys', 'ThingySection')


def generate_parts(file_path, file_name, thingy):
    """

    :param content:
    :return:
    """
    reader = PlaintextCorpusReader(file_path, [file_name])
    paragraphs = reader.paras()
    for paragraph in paragraphs:
        if _is_section_valid(paragraph):
            sentences = [s for s in paragraph]

            total_content = ' '.join(' '.join(w for w in s) for s in sentences)
            section = ThingySection(
                content=total_content,
                thingy=thingy
            )

            thingy_sentences = []
            for sentence in sentences:
                sentence = ThingySentence(
                    content=' '.join(sentence),
                    thingy_section=section
                )
                thingy_sentences.append(sentence)

            yield section, thingy_sentences


def _is_section_valid(section):
    num_sents = len(section)
    if not num_sents:
        return False
    elif num_sents == 1:
        sentence = section[0]
        num_words = len(sentence)
        if num_words <= 10:
            return False
        elif all(word.isupper() for word in sentence):
            return False
    return True
