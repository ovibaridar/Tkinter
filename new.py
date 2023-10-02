from serpapi import GoogleSearch


def google_search(question):
    # Replace 'YOUR_API_KEY' with your actual SerpApi API key
    api_key = 'af415ecbc27375bba67ee556d2a0ff89129456b4'

    # Create a GoogleSearch object with your API key
    search = GoogleSearch({"q": question, "api_key": api_key})

    # Perform the search
    results = search.get_dict()

    # Extract the answer (featured snippet) from the results
    answer = results.get("answer_box", "")

    return answer


if __name__ == "__main__":
    search_query = input("Enter your question: ")
    answer = google_search(search_query)

    if answer:
        print("Answer:")
        print(answer)
    else:
        print("No answer found.")
