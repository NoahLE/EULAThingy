from django.conf import settings
from elasticsearch.client import Elasticsearch
import queries

__ELASTICSEARCH = None


def __es_conn__():
    global __ELASTICSEARCH
    if __ELASTICSEARCH is None:
        __ELASTICSEARCH = Elasticsearch(
            hosts=settings.ES_HOSTS
        )
    return __ELASTICSEARCH


def add_rated_sentence(thingy_sentence):
    """

    :param thingy_sentence:
    :return:
    """
    document_fields = {
        'sentence_id': thingy_sentence.id,
        'sentence_content': thingy_sentence.content,
        'sentence_rating': thingy_sentence.rating
    }
    catgeory = thingy_sentence.thingy_section.category

    client = __es_conn__()
    index = 'category_{}'.format(catgeory)
    client.index(
        index, 'sentence_rating',
        document_fields, id=thingy_sentence.id
    )


def get_prediction(category, content):
    """

    :param category:
    :param content:
    :return:
    """
    index = 'category_{}'.format(category)
    query = queries.ES_PREDICTIONS_QUERY.format(
        content.split()
    )
    client = __es_conn__()
    results = client.search(
        index, 'sentence_rating', query, queries.ES_PREDICTIONS_PARAMS
    )

    total_score = 0
    number_of_entries = 0
    for result in results['hits']['hits']:
        number_of_entries += 1
        total_score += result['sentence_rating']

    return total_score / number_of_entries