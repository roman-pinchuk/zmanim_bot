from typing import Callable


def get_translate(data: dict, _: Callable) -> dict:
    """
    input data structure:
    {
        'masehet': '...',
        'daf': '...(int)'
    }

    output data structure (words in `` are translated):
    {
        'title': `...`.
        'data': {
            `Masehet`: `...`,
            `Daf`: `...`
        }
    }
    """
    talmud_books = {
        'Brachos': _('Brachos'),
        'Shabbos': _('Shabbos'),
        'Eruvin': _('Eruvin'),
        'Pesachim': _('Pesachim'),
        'Shekalim': _('Shekalim'),
        'Yoma': _('Yoma'),
        'Sukah': _('Sukah'),
        'Beitzah': _('Beitzah'),
        'Rosh Hashana': _('Rosh Hashana'),
        'Taanis': _('Taanis'),
        'Megilah': _('Megilah'),
        'Moed Katan': _('Moed Katan'),
        'Chagigah': _('Chagigah'),
        'Yevamos': _('Yevamos'),
        'Kesuvos': _('Kesuvos'),
        'Nedarim': _('Nedarim'),
        'Nazir': _('Nazir'),
        'Sotah': _('Sotah'),
        'Gitin': _('Gitin'),
        'Kidushin': _('Kidushin'),
        'Bava Kama': _('Bava Kama'),
        'Bava Metzia': _('Bava Metzia'),
        'Bava Basra': _('Bava Basra'),
        'Sanhedrin': _('Sanhedrin'),
        'Makos': _('Makos'),
        'Shevuos': _('Shevuos'),
        'Avodah Zarah': _('Avodah Zarah'),
        'Horayos': _('Horayos'),
        'Zevachim': _('Zevachim'),
        'Menachos': _('Menachos'),
        'Chulin': _('Chulin'),
        'Bechoros': _('Bechoros'),
        'Erchin': _('Erchin'),
        'Temurah': _('Temurah'),
        'Kerisos': _('Kerisos'),
        'Meilah': _('Meilah'),
        'Nidah': _('Nidah'),
    }

    masehet = talmud_books.get(data['masehet'])
    localized_data = {
        'title': _('DAF YOMI'),
        'data': {
            _('Masehet'): masehet,
            _('Daf'): data['daf']
        }
    }
    return localized_data
