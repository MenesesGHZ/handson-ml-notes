import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix,table


def plot_housing_data(housing,pairplot_attributes):
    print("\n* GENERATING FIGURES...")

    # Pairplot to observe relationships between attributes (a good complement for a correlation matrix)
    scatter_matrix(housing[pairplot_attributes],figsize=(12,12))
    plt.savefig("figures/pairplot_between_attributes.png")

    # Plotting correlation table (In this case is use the `standard correlation coefficient` = Pearson's R)
    #table(pairplot_attributes,housing.corr()[pairplot_attributes]) 

    # Plotting California Housing Prices
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100,
             label="population", c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
    plt.legend()
    plt.savefig("figures/california_map_hosing_prices.png")    
    
    # Show figures
    plt.show()
    print("\n* FIGURES HAVE BEEN SAVED AND SHOWN at `figures/` *\n")

