import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
from contrato import OutputSeaImpQuotesSchema
import re 
from inferred_schema import imp_sea_quotes_schema

def extract_data(dir_arquivo: str) -> pd.DataFrame:
    df = pd.read_excel(dir_arquivo)

    return df

def column_names_to_snake_case(columns_names_list: list) -> list:
    columns_names_list = re.sub(r'[^a-zA-Z0-9]', ' ', columns_names_list)
    columns_names_list = columns_names_list.strip().replace(' ', '_')

    return columns_names_list.lower()

@pa.check_types(lazy=True)
def validate_schema(dataframe: pd.DataFrame) -> DataFrame[OutputSeaImpQuotesSchema]:
    return dataframe

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    ...

def load_data_to_database(df: pd.DataFrame) -> pd.DataFrame:
    ...

if __name__ == '__main__':
    url_arquivo = 'data/cotacoes.xls'
    
    dataframe = extract_data(url_arquivo)
    new_columns = [column_names_to_snake_case(col) for col in dataframe.columns]
    dataframe.columns = new_columns

    # print(dataframe)

    # dataframe_inferred_schema = pa.infer_schema(dataframe)
    
    # with open("inferred_schema.py", "w") as file:
    #     file.write(dataframe_inferred_schema.to_script())

    try:
        imp_sea_quotes_schema.validate(dataframe, lazy=True)
    except pa.errors.SchemaError as exc:
        print(exc)



