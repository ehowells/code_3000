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
    merged =  pd.merge(anon_df, aux_df, on=['age', 'zip3', 'gender'], how='inner')
    counts = merged.groupby('anon_id')['matched_name'].nunique()

    unique_ids = counts[counts == 1].index

    return merged[merged['anon_id'].isin(unique_ids)]


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return matches_df['anon_id'].nunique() / len(anon_df)