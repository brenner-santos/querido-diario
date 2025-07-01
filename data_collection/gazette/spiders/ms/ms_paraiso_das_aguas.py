from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class MsParaisoDasAguasSpider(BaseDioenetSpider):
    TERRITORY_ID = "5006275"
    name = "ms_paraiso_das_aguas"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/paraiso-das-aguas"
    power = "executive_legislative"
    start_date = date(2022, 11, 9)
    