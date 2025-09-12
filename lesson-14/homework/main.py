{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d0e93168",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "def parse_students(filename=\"students.json\"):\n",
    "    try:\n",
    "        with open(filename, \"r\", encoding=\"utf-8\") as file:\n",
    "            data = json.load(file)\n",
    "\n",
    "        print(\"Students Details:\")\n",
    "        for student in data.get(\"students\", []):  # students ro'yxati ichida\n",
    "            print(f\"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\")\n",
    "    except FileNotFoundError:\n",
    "        print(f\"❌ File {filename} not found.\")\n",
    "    except json.JSONDecodeError:\n",
    "        print(\"❌ Invalid JSON format.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "08bc6409",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_weather(city=\"Tashkent\", api_key=\"YOUR_API_KEY_HERE\"):\n",
    "    url = f\"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric\"\n",
    "    try:\n",
    "        response = requests.get(url)\n",
    "        response.raise_for_status()\n",
    "        data = response.json()\n",
    "\n",
    "        print(f\"Weather in {city}:\")\n",
    "        print(\"Temperature:\", data[\"main\"][\"temp\"], \"°C\")\n",
    "        print(\"Humidity:\", data[\"main\"][\"humidity\"], \"%\")\n",
    "        print(\"Condition:\", data[\"weather\"][0][\"description\"])\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        print(\"❌ API request failed:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "070b21db",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_books(filename=\"books.json\"):\n",
    "    try:\n",
    "        with open(filename, \"r\", encoding=\"utf-8\") as f:\n",
    "            return json.load(f)\n",
    "    except (FileNotFoundError, json.JSONDecodeError):\n",
    "        return {\"books\": []}\n",
    "\n",
    "def save_books(data, filename=\"books.json\"):\n",
    "    with open(filename, \"w\", encoding=\"utf-8\") as f:\n",
    "        json.dump(data, f, indent=4)\n",
    "\n",
    "def add_book(title, author, year):\n",
    "    data = load_books()\n",
    "    data[\"books\"].append({\"title\": title, \"author\": author, \"year\": year})\n",
    "    save_books(data)\n",
    "    print(\"✅ Book added successfully!\")\n",
    "\n",
    "def update_book(title, new_author=None, new_year=None):\n",
    "    data = load_books()\n",
    "    for book in data[\"books\"]:\n",
    "        if book[\"title\"] == title:\n",
    "            if new_author:\n",
    "                book[\"author\"] = new_author\n",
    "            if new_year:\n",
    "                book[\"year\"] = new_year\n",
    "            save_books(data)\n",
    "            print(\"✅ Book updated successfully!\")\n",
    "            return\n",
    "    print(\"❌ Book not found.\")\n",
    "\n",
    "def delete_book(title):\n",
    "    data = load_books()\n",
    "    data[\"books\"] = [book for book in data[\"books\"] if book[\"title\"] != title]\n",
    "    save_books(data)\n",
    "    print(\"✅ Book deleted successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0f57fb0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommend_movie(genre, api_key=\"YOUR_OMDB_API_KEY\"):\n",
    "    url = f\"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}\"\n",
    "    try:\n",
    "        response = requests.get(url)\n",
    "        response.raise_for_status()\n",
    "        data = response.json()\n",
    "\n",
    "        if \"Search\" not in data:\n",
    "            print(\"❌ No movies found for this genre.\")\n",
    "            return\n",
    "\n",
    "        movie = random.choice(data[\"Search\"])\n",
    "        print(\"🎬 Recommended Movie:\")\n",
    "        print(\"Title:\", movie[\"Title\"])\n",
    "        print(\"Year:\", movie[\"Year\"])\n",
    "        print(\"IMDb ID:\", movie[\"imdbID\"])\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        print(\"❌ API request failed:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4eb8eec2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acb054a4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ea78cb4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8dd74476",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54a7ea3f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6745ff1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46d307ce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57f5ccb7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15fedd64",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a876f876",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3607d26",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6e36f32",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdafaed9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48ba812f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83806a91",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3746d1ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
