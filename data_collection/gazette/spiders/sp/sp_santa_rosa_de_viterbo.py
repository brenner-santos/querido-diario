from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class SpSantaRosaDeViterboSpider(BaseDioenetSpider):
    TERRITORY_ID = "3547601"
    name = "sp_santa_rosa_de_viterbo"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/santa-rosa-de-viterbo"
    power = "executive_legislative"
    start_date = date(2022, 7, 20)
    