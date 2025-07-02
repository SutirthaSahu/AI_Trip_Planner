import os
from dotenv import load_dotenv
from typing import List

from langchain.tools import tool

from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool

class PlaceSearchTool:
    
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()
    
    def _setup_tools(self):
        "Setup all tools for the place search tool"

        @tool
        def search_attractions(place:str) -> str:
            """  Search attractions for a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google : {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \n Following are the attractions of the {place} : {tavily_result}"

        @tool
        def search_restaurants(place:str) -> str:
            """  Search restraurants for a place"""
            try:
                restaurant_result = self.google_places_search.google_search_restraurants(place)
                if restaurant_result:
                    return f"Following are the attractions of {place} as suggested by google : {restaurant_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restraurants(place)
                return f"Google cannot find the details due to {e}. \n Following are the attractions of the {place} : {tavily_result}"

        
        @tool
        def search_activities(place:str) -> str:
            """  Search activities for a place"""
            try:
                activities_result = self.google_places_search.google_search_activity(place)
                if activities_result:
                    return f"Following are the activities for a {place} as suggested by google : {activities_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \n Following are the attractions of the {place} : {tavily_result}"

        @tool
        def search_transportation(place:str) -> str:
            """  Search avaliable transportation for a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the transportation avaliable for the {place} as suggested by google : {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \n Following are the avaliabe transportation for the {place} : {tavily_result}"
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]
