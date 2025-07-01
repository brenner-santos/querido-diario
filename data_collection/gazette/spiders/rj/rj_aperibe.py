from datetime import date

from gazette.spiders.base.dioenet import BaseDioenetSpider


class RjAperibeSpider(BaseDioenetSpider):
    TERRITORY_ID = "3300159"
    name = "rj_aperibe"
    BASE_URL = "https://plenussistemas.dioenet.com.br/list/aperibe"
    power = "executive_legislative"
    start_date = date(2024, 11, 26)
    