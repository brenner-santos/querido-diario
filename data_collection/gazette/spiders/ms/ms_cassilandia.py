from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class MsCassilandiaSpider(BaseDioenetSpider):
    TERRITORY_ID = "5002902"
    name = "ms_cassilandia"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/cassilandia"
    power = "executive_legislative"
    start_date = date(2013, 3, 28)
    