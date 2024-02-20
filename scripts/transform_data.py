from dataclasses import dataclass, asdict
import json


NEIGHBORHOOD_NAME_MAP = {
    "BOM RETIRO": "Bom Retiro",
    "CONSOLAÇÃO": "Consolação",
    "SANTA CECILIA": "Santa Cecília",
    "BELA VISTA": "Bela Vista",
    "CAMBUCI": "Cambuci",
    "LIBERDADE": "Liberdade",
    "REPUBLICA": "República",
    "SÉ": "Sé",
    "CIDADE TIRADENTES": "Cidade Tiradentes",
    "ERMELINO": "Ermelino Matarazzo",
    "PONTE RASA": "Ponte Rasa",
    "GUAIANASES": "Guaianases",
    "LAJEADO": "Lajeado",
    "ITAIM PAULISTA": "Itaim Paulista",
    "VILA CURUÇA": "Vila Curuçá",
    "CIDADE LIDER": "Cidade Líder",
    "ITAQUERA": "Itaquera",
    "JOSé BONIFÁCIO": "José Bonifácio",
    "PARQUE DO CARMO": "Parque do Carmo",
    "IGUATEMI": "Iguatemi",
    "SÃO MATEUS": "São Mateus",
    "SÃO RAFAEL": "São Rafael",
    "JARDIM HELENA": "Jardim Helena",
    "SÃO MIGUEL": "São Miguel Paulista",
    "VILA JACUI": "Vila Jacuí",
    "CACHOEIRINHA": "Cachoeirinha",
    "CASA VERDE": "Casa Verde",
    "LIMÃO": "Limão",
    "BRASILANDIA": "Brasilândia",
    "FREGUESIA DO O": "Freguesia do Ó",
    "JAÇANÃ": "Jaçanã",
    "TREMEMBÉ": "Tremembé",
    "ANHANGUERA": "Anhanguera",
    "PERUS": "Perus",
    "JARAGUA": "Jaraguá",
    "PIRITUBA": "Pirituba",
    "SÃO DOMINGOS": "São Domingos",
    "MANDAQUI": "Mandaqui",
    "SANTANA": "Santana",
    "TUCURUVI": "Tucuruvi",
    "VILA GUILHERME": "Vila Guilherme",
    "VILA MARIA": "Vila Maria",
    "VILA MEDEIROS": "Vila Medeiros",
    "BUTANTA": "Butantã",
    "MORUMBI": "Morumbi",
    "RAPOSO TAVARES": "Raposo Tavares",
    "RIO PEQUENO": "Rio Pequeno",
    "VILA SONIA": "Vila Sônia",
    "ALTO DE PINHEIROS": "Alto de Pinheiros",
    "BARRA FUNDA": "Barra Funda",
    "ITAIM BIBI": "Itaim Bibi",
    "JAGUARA": "Jaguará",
    "JAGUARE": "Jaguaré",
    "JARDIM PAULISTA": "Jardim Paulista",
    "LAPA": "Lapa",
    "PERDIZES": "Perdizes",
    "PINHEIROS": "Pinheiros",
    "VILA LEOPOLDINA": "Vila Leopoldina",
    "CURSINO": "Cursino",
    "IPIRANGA": "Ipiranga",
    "SACOMÃ": "Sacomã",
    "AGUA RASA": "Água Rasa",
    "ARICANDUVA": "Aricanduva",
    "BELÉM": "Belém",
    "BRAS": "Brás",
    "CARRÃO": "Carrão",
    "MOOCA": "Mooca",
    "PARI": "Pari",
    "TATUAPÉ": "Tatuapé",
    "VILA FORMOSA": "Vila Formosa",
    "ARTUR ALVIM": "Artur Alvim",
    "CANGAÍBA": "Cangaíba",
    "PENHA": "Penha",
    "VILA MATILDE": "Vila Matilde",
    "JABAQUARA": "Jabaquara",
    "MOEMA": "Moema",
    "SAUDE": "Saúde",
    "VILA MARIANA": "Vila Mariana",
    "SÃO LUCAS": "São Lucas",
    "SAPOPEMBA": "Sapopemba",
    "VILA PRUDENTE": "Vila Prudente",
    "CAMPO LIMPO": "Campo Limpo",
    "CAPÃO REDONDO": "Capão Redondo",
    "VILA ANDRADE": "Vila Andrade",
    "CIDADE DUTRA": "Cidade Dutra",
    "GRAJAÚ": "Grajaú",
    "SOCORRO": "Socorro",
    "JARDIM ANGELA": "Jardim Ângela",
    "JARDIM SÃO LUIZ": "Jardim São Luíz",
    "MARSILAC": "Marsilac",
    "PARELHEIROS": "Parelheiros",
    "CAMPO BELO": "Campo Belo",
    "CAMPO GRANDE": "Campo Grande",
    "CIDADE ADEMAR": "Cidade Ademar",
    "PEDREIRA": "Pedreira",
    "SANTO AMARO": "Santo Amaro",
    "MariaNA": "Mariana",
}


@dataclass
class NeighborhoodDengueStats:
    name: str
    number_of_cases: int
    incidence_coefficient: float


def transform_data_to_json(raw_data):

    raw_data = raw_data.replace(",", ".")
    for name, normalized_name in NEIGHBORHOOD_NAME_MAP.items():
        raw_data = raw_data.replace(name, normalized_name)

    lines = raw_data.split("\n")

    stats = []
    for line in lines:
        # Finding the first numeric value to determine the end of the region name

        parts = line.split()
        for i, part in enumerate(parts):
            if part.replace(".", "", 1).isdigit():
                region_name = " ".join(parts[:i])
                numeric_parts = parts[i:]
                break

        number_cases = int(numeric_parts[-2])
        incidence = float(numeric_parts[-1])

        data = NeighborhoodDengueStats(region_name, number_cases, incidence)
        stats.append(asdict(data))

    return json.dumps(stats)


if __name__ == "__main__":

    # Attempt to read the file contents
    with open("../data/raw_table.txt", "r", encoding="utf8") as file:
        contents = file.read()

        json_data = transform_data_to_json(contents)

        with open("../data/sao_paulo_dengue.json", "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
