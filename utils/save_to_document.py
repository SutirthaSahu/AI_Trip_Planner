import os
import datetime

def save_documents(response_text:str, directory: str = "./output"):
    """
    Export travel plan to markdown file with proper formatting
    """
    os.makedirs(directory, exist_ok=True)

    markdown_content = f""" 🌍 AI Travel Plan

    ---------
    {response_text}
    ---------

    *This travel plan is created by AI. Please verify all information, especially prices, operating hours, and travel requirements before your trip.*
    """

    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{directory}/AI_Travel_Plan_{timestamp}.md"

        print(filename)

        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(markdown_content)
        
        print(f"Markdown file saved : {filename}")
        return filename
    
    except Exception as e:
        print(f"Error saving markdown file : {e}")
        return None