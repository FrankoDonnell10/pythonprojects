#Import Libraries
import requests
import openpyxl

#Function to generate url endpoint for api
def GetEndpoints():
    apis = []
    baseEndpoint = "https://fantasy.premierleague.com/api/leagues-classic/530116/standings"    
    for i in range(1, 8):
        if i == 1 :
          print(baseEndpoint)
          apis.append(baseEndpoint)
        else:
            apiEndpoint = baseEndpoint + "?page=" + str(i)
            print(apiEndpoint)
            apis.append(apiEndpoint)
    return apis

#Function to get responses from API
def GetAPIResponse(APIEndpointURL):
    response = requests.get(APIEndpointURL).json()
    return response
    
#Convert API response to JSON
def ConvertToJson(data):
    response = data.json()

#Get all response jsons and write to excel
def GetAndWriteDataToExcel():
    apis = GetEndpoints()
    for api in apis:
        response = GetAPIResponse(api)
        writeJsonToExcel(sheet1,response)
