{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b9b0eaff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "49b84b6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {\n",
    "    \"id\":[1,2,3],\n",
    "    \"name\":[\"Benjamin Sisko\",\"Jadzia Dax\",\"Kira Nerys\"],\n",
    "    \"species\":[\"Human\",\"Trill\",\"Bajoran\"],\n",
    "    \"age\":[40,300,29]\n",
    "\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f387a621",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>name</th>\n",
       "      <th>species</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Benjamin Sisko</td>\n",
       "      <td>Human</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jadzia Dax</td>\n",
       "      <td>Trill</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Kira Nerys</td>\n",
       "      <td>Bajoran</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id            name  species  age\n",
       "0   1  Benjamin Sisko    Human   40\n",
       "1   2      Jadzia Dax    Trill  300\n",
       "2   3      Kira Nerys  Bajoran   29"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(d)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6e30ef76",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[df['name'] == \"Jadzia Dax\", 'name'] = \"Ezri Dax\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c33e94ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>name</th>\n",
       "      <th>species</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Benjamin Sisko</td>\n",
       "      <td>Human</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Ezri Dax</td>\n",
       "      <td>Trill</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Kira Nerys</td>\n",
       "      <td>Bajoran</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id            name  species  age\n",
       "0   1  Benjamin Sisko    Human   40\n",
       "1   2        Ezri Dax    Trill  300\n",
       "2   3      Kira Nerys  Bajoran   29"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c03abddf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Kira Nerys</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         name  age\n",
       "2  Kira Nerys   29"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[2:3,[\"name\",\"age\"]]"
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
