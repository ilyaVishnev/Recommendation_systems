


def prefilter_items(data_train, item_features, take_n_popular=5000):

    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_5000 = popularity.sort_values('n_sold', ascending=False).head(take_n_popular)
    return top_5000