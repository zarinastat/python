{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "94a06020",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_leap(year):\n",
    "    if not isinstance(year,int):\n",
    "        raise ValueError(\"Year must be an integer\")\n",
    "    \n",
    "    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "print(is_leap(2000))\n",
    "print(is_leap(1900))\n",
    "print(is_leap(2024))\n",
    "print(is_leap(2023))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "27bef273",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weird\n"
     ]
    }
   ],
   "source": [
    "n = int(input().strip())\n",
    "\n",
    "if n % 2 !=0:\n",
    "    print(\"Weird\")\n",
    "elif 2 <= n <= 5:\n",
    "    print(\"Not Weird\")\n",
    "elif 6 <= n <= 20:\n",
    "    print(\"Weird\")\n",
    "else:\n",
    "    print(\"Not Weird\")    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3052924b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2]\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"a =\"))\n",
    "b = int(input(\"b =\"))\n",
    "\n",
    "if a % 2 != 0:\n",
    "    a += 1\n",
    "\n",
    "if b % 2 != 0:\n",
    "    b -= 1\n",
    "\n",
    "print(list(range(a, b + 1, 2)))        "
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
