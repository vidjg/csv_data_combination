# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:57:10 2018

@author: sqian
"""


import pandas as pd


# Definition of the method
def combine_csv(location, list):
    data = pd.read_csv(location + list[0], encoding='latin-1')
    if len(list) > 1:
        for file in list[1:]:
            complete_location = location + file
            temp = pd.read_csv(complete_location)
            data = data.append(temp, ignore_index=True)
    return data


# Main Function
if __name__ == '__main__':
    # Initializing
    file_location = 'C:/Users/sqian/OneDrive - WBG/Documents/07-05 - FAO Combination/'
    file_list = ["Emissions_Agriculture_Manure_left_on_pasture_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Manure_Management_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Rice_Cultivation_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Synthetic_Fertilizers_E_All_Data_(Normalized).csv",
                 "Emissions_Land_Use_Burning_Biomass_E_All_Data_(Normalized).csv",
                 "Emissions_Land_Use_Cropland_E_All_Data_(Normalized).csv",
                 "Emissions_Land_Use_Forest_Land_E_All_Data_(Norm).csv",
                 "Emissions_Land_Use_Grassland_E_All_Data_(Normalized).csv",
                 "Emissions_Land_Use_Land_Use_Total_E_All_Data_(Normalized).csv",
                 "Employment_Indicators_E_All_Data_(Norm).csv", "Environment_AirClimateChange_E_All_Data.csv",
                 "Environment_Emissions_by_Sector_E_All_Data_(Normalized).csv",
                 "Environment_Emissions_intensities_E_All_Data_(Normalized).csv", "Environment_Energy_E_All_Data.csv",
                 "Environment_Fertilizers_E_All_Data_(Normalized).csv",
                 "Environment_LandCover_E_All_Data_(Normalized).csv", "Environment_LandUse_E_All_Data_(Normalized).csv",
                 "Environment_LivestockPatterns_E_All_Data_(Normalized).csv",
                 "Environment_Manure_E_All_Data_(Normalized).csv", "Environment_Pesticides_E_All_Data_(Normalized).csv",
                 "Environment_Soil_E_All_Data.csv", "Environment_Temperature_change_E_All_Data_(Normalized).csv",
                 "Environment_Water_E_All_Data.csv", "Exchange_rate_E_All_Data_(Normalized).csv",
                 "Food_Aid_Shipments_WFP_E_All_Data_(Normalized).csv", "Food_Security_Data_E_All_Data_(Normalized).csv",
                 "FoodBalanceSheets_E_All_Data_(Normalized).csv", "FoodSupply_Crops_E_All_Data_(Normalized).csv",
                 "FoodSupply_LivestockFish_E_All_Data_(Normalized).csv", "Forestry_E_All_Data_(Normalized).csv",
                 "Forestry_Trade_Flows_E_All_Data_(Normalized).csv",
                 "Indicators_from_Household_Surveys_E_All_Data_(Normalized).csv",
                 "Inputs_FertilizersArchive_E_All_Data_(Normalized).csv",
                 "Inputs_FertilizersNutrient_E_All_Data_(Normalized).csv",
                 "Inputs_FertilizersProduct_E_All_Data_(Normalized).csv",
                 "Inputs_FertilizersTradeValues_E_All_Data_(Normalized).csv",
                 "Inputs_LandUse_E_All_Data_(Normalized).csv", "Inputs_Pesticides_Trade_E_All_Data_(Normalized).csv",
                 "Inputs_Pesticides_Use_E_All_Data_(Normalized).csv",
                 "Investment_CapitalStock_E_All_Data_(Normalized).csv",
                 "Investment_CountryInvestmentStatisticsProfile__E_All_Data_(Normalized).csv",
                 "Investment_CreditAgriculture_E_All_Data_(Normalized).csv",
                 "Investment_ForeignDirectInvestment_E_All_Data_(Normalized).csv",
                 "Investment_GovernmentExpenditure_E_All_Data_(Normalized).csv",
                 "Investment_Machinery_E_All_Data_(Normalized).csv",
                 "Investment_MachineryArchive_E_All_Data_(Normalized).csv",
                 "Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).csv",
                 "Population_E_All_Data_(Normalized).csv", "Price_Indices_E_All_Data_(Normalized).csv",
                 "Prices_E_All_Data_(Normalized).csv", "Prices_Monthly_E_All_Data_(Normalized).csv",
                 "PricesArchive_E_All_Data.csv", "Producción_Cultivos_S_Todos_los_Datos.csv",
                 "Production_Crops_E_All_Data_(Normalized).csv",
                 "Production_CropsProcessed_E_All_Data_(Normalized).csv",
                 "Production_Indices_E_All_Data_(Normalized).csv", "Production_Livestock_E_All_Data_(Normalized).csv",
                 "Production_LivestockPrimary_E_All_Data_(Normalized).csv",
                 "Production_LivestockProcessed_E_All_Data_(Normalized).csv",
                 "Trade_Crops_Livestock_E_All_Data_(Normalized).csv", "Trade_DetailedTradeMatrix_E_All_Data_(Norm).csv",
                 "Trade_Indices_E_All_Data_(Normalized).csv", "Trade_LiveAnimals_E_All_Data_(Normalized).csv",
                 "Value_of_Production_E_All_Data_(Normalized).csv", "ASTI_Research_Spending_E_All_Data_(Norm).csv",
                 "ASTI_Researchers_E_All_Data_(Norm).csv", "CommodityBalances_Crops_E_All_Data_(Normalized).csv",
                 "CommodityBalances_LivestockFish_E_All_Data_(Normalized).csv",
                 "ConsumerPriceIndices_E_All_Data_(Normalized).csv", "Deflators_E_All_Data_(Normalized).csv",
                 "Development_Assistance_to_Agriculture_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Agriculture_total_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Burning_crop_residues_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Burning_Savanna_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Crop_Residues_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Cultivated_Organic_Soils_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Energy_E_All_Data_(Norm).csv",
                 "Emissions_Agriculture_Enteric_Fermentation_E_All_Data_(Normalized).csv",
                 "Emissions_Agriculture_Manure_applied_to_soils_E_All_Data_(Normalized).csv"]

    combined_data = combine_csv(file_location, file_list)
    combined_data.to_csv(file_location + "combined_data.csv", index=False)
