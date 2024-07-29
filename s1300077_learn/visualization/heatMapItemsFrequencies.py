import plotly.express as px

class heatMapItemsFrequencies:
    def __init__(self, itemsFrequenciesDictionary):
        if isinstance(itemsFrequenciesDictionary, dict):
            self.data = itemsFrequenciesDictionary
        else:
            self.data = {
                (row['longitude'], row['latitude']): row['frequency']
                for _, row in itemsFrequenciesDictionary.iterrows()
            }

        self._createHeatmap()

    def _createHeatmap(self):
        longitudes = [point[0] for point in self.data.keys()]
        latitudes = [point[1] for point in self.data.keys()]
        frequencies = list(self.data.values())

        fig = px.scatter_mapbox(
            lat=latitudes,
            lon=longitudes,
            color=frequencies,
            size=[10] * len(frequencies),
            color_continuous_scale="Viridis",
            zoom=10,
        )

        fig.update_layout(mapbox_style="open-street-map")
        fig.show()