import json

def load_data(file_path):
    try:
        with open(file_path) as file_handle:
            data = json.load(file_handle)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {str(e)}")
        return []

def format_movie(movie):
    rating = (
        "R"
        if "horror" in movie["classifications"]
        else "PG-13"
        if "thriller" in movie["classifications"]
        else None
    )

    domestic_box_office = format_currency(movie['box_office']['domestic'])
    international_box_office = format_currency(movie['box_office']['international'])

    box_office_sum = domestic_box_office + international_box_office

    box_office = (
        f"{box_office_sum:,} - $"
        if movie["box_office"]["domestic"].startswith("$")
        else f"{box_office_sum:,} - €"
        if movie["box_office"]["domestic"].startswith("€")
        else None
    )

    review = (
        movie["rotten_tomatoes_review"] + 5
        if movie["director"] == "John Carpenter"
        else movie["rotten_tomatoes_review"]
    )

    return {
        "title": movie["title"],
        "director": movie["director"],
        "release_year": movie["release_year"],
        "classifications": movie["classifications"],
        "rating": rating,
        "box_office": box_office,
        "review": review,
    }

def format_currency(currency_value):
    # Remove non-alphanumeric characters and convert to an integer
    return int(''.join(filter(str.isalnum, currency_value)))

def format_movies(movies):
    return [format_movie(movie) for movie in movies]

def main():
    file_path = "./data.json"
    data = load_data(file_path)
    formatted_movies = format_movies(data)
    print(json.dumps(formatted_movies, indent=2))

if __name__ == "__main__":
    main()
