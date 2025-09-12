{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3d33ee83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"orange\", \"mango\"]\n",
    "print(fruits[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9b707039",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Concatenated list: [1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1, 2, 3]\n",
    "list2 = [4, 5, 6]\n",
    "\n",
    "combined_list = list1 + list2\n",
    "print(\"Concatenated list:\", combined_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bddcdf20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First: 10\n",
      "Last: 50\n",
      "Middle: [20, 30, 40]\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40, 50]\n",
    "\n",
    "first_element = numbers[0]\n",
    "last_element = numbers[-1]\n",
    "middle_elements = numbers[1:4]\n",
    "\n",
    "print(\"First:\", first_element)\n",
    "print(\"Last:\", last_element)\n",
    "print(\"Middle:\", middle_elements)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "85c09271",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 30, 50]\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40, 50]\n",
    "first = numbers[0]\n",
    "middle = numbers[len(numbers)//2]\n",
    "last = numbers[-1]\n",
    "new_list = [first, middle, last]\n",
    "print(new_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a0738082",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Inception', 'Interstellar', 'Titanic', 'Avatar', 'Gladiator')\n"
     ]
    }
   ],
   "source": [
    "movies = [\"Inception\", \"Interstellar\", \"Titanic\", \"Avatar\", \"Gladiator\"]\n",
    "movies_tuple = tuple(movies)\n",
    "print(movies_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2a3ed14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "cities = [\"London\", \"New York\", \"Paris\", \"Tokyo\"]\n",
    "print(\"Paris\" in cities)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "22183f19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3]\n",
    "duplicated = numbers * 2\n",
    "print(duplicated)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f5432141",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[40, 20, 30, 10]\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40]\n",
    "numbers[0], numbers[-1] = numbers[-1], numbers[0]\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "361905e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 5, 6, 7, 8)\n"
     ]
    }
   ],
   "source": [
    "numbers = tuple(range(1, 11))\n",
    "slice_tuple = numbers[3:8]  # index 3 to 7 inclusive of 3, exclusive of 8\n",
    "print(slice_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fe71f130",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "colors = [\"red\", \"blue\", \"green\", \"blue\", \"yellow\", \"blue\"]\n",
    "count_blue = colors.count(\"blue\")\n",
    "print(count_blue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "32c50341",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "animals = (\"tiger\", \"lion\", \"elephant\")\n",
    "index_lion = animals.index(\"lion\")\n",
    "print(index_lion)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "21aa64cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "tuple1 = (1, 2, 3)\n",
    "tuple2 = (4, 5, 6)\n",
    "merged = tuple1 + tuple2\n",
    "print(merged)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c844d952",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "my_list = [10, 20, 30]\n",
    "my_tuple = (1, 2, 3, 4)\n",
    "print(len(my_list))\n",
    "print(len(my_tuple))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2dce17cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 10, 15, 20, 25]\n"
     ]
    }
   ],
   "source": [
    "numbers_tuple = (5, 10, 15, 20, 25)\n",
    "numbers_list = list(numbers_tuple)\n",
    "print(numbers_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4dd5093c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max: 20\n",
      "Min: 5\n"
     ]
    }
   ],
   "source": [
    "numbers = (10, 5, 20, 8)\n",
    "print(\"Max:\", max(numbers))\n",
    "print(\"Min:\", min(numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "167bfb4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('cherry', 'banana', 'apple')\n"
     ]
    }
   ],
   "source": [
    "words = (\"apple\", \"banana\", \"cherry\")\n",
    "reversed_words = words[::-1]\n",
    "print(reversed_words)"
   ]
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
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
