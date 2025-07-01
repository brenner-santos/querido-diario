from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class RsBarraDoRibeiroSpider(BaseDioenetSpider):
    TERRITORY_ID = "4301909"
    name = "rs_barra_do_ribeiro"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/barra-do-ribeiro"
    power = "executive_legislative"
    start_date = date(2022, 7, 28)
    