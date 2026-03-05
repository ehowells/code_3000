import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    return pd.merge(anon_df, aux_df, on=['age', 'zip3', 'gender'], how='right')
    # raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    raise NotImplementedError

# anon, aux = load_data("mod06_data/anonymized.csv", "mod06_data/auxiliary.csv")
# print(link_records(anon, aux))

# print(anon.shape)
# print(aux.shape)
# print(link_records(anon, aux).shape)
