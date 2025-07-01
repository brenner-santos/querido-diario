from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class SpPraiaGrandeSpider(BaseDioenetSpider):
    TERRITORY_ID = "3541000"
    name = "sp_praia_grande"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/praia-grande"
    power = "executive_legislative"
    start_date = date(2024, 12, 6)
    