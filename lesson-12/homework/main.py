{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f3e12628",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "from concurrent.futures import ThreadPoolExecutor\n",
    "\n",
    "def is_prime(n):\n",
    "    if n < 2:\n",
    "        return False\n",
    "    for i in range(2, int(math.sqrt(n)) + 1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "def primes_in_range(start, end):\n",
    "    return [n for n in range(start, end + 1) if is_prime(n)]\n",
    "\n",
    "def main():\n",
    "    start_range = 1\n",
    "    end_range = 30\n",
    "    num_threads = 3\n",
    "     \n",
    "    step = (end_range - start_range + 1) // num_threads\n",
    "    ranges = []\n",
    "    for i in range(num_threads):\n",
    "        start = start_range + i * step\n",
    "        end = end_range if i == num_threads - 1 else start + step - 1\n",
    "        ranges.append((start, end))\n",
    "    primes = []\n",
    "    with ThreadPoolExecutor(max_workers=num_threads) as executor:\n",
    "        results = executor.map(lambda r: primes_in_range(r[0], r[1]), ranges)\n",
    "        for sublist in results:\n",
    "            primes.extend(sublist)\n",
    "\n",
    "\n",
    "    primes.sort()\n",
    "    print(\"Prime numbers:\", primes)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "30339922",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Natijalar (har qator uchun so'z soni): [5, 4, 5]\n",
      "Umumiy so'zlar soni: 14\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "\n",
    "def count_words(part, result, index):\n",
    "    words = part.split()\n",
    "    result[index] = len(words)\n",
    "\n",
    "def main():\n",
    "\n",
    "    text = \"\"\"Python is simple and powerful.\n",
    "    Multithreading makes it faster.\n",
    "    Python is fun to learn.\"\"\"\n",
    "\n",
    "    parts = text.split(\"\\n\")\n",
    "    \n",
    "    result = [0] * len(parts)  # Har bir thread natijasi\n",
    "    threads = []\n",
    "\n",
    "    for i, part in enumerate(parts):\n",
    "        t = threading.Thread(target=count_words, args=(part, result, i))\n",
    "        threads.append(t)\n",
    "        t.start()\n",
    "\n",
    "    for t in threads:\n",
    "        t.join()  \n",
    "\n",
    "    print(\"Natijalar (har qator uchun so'z soni):\", result)\n",
    "    print(\"Umumiy so'zlar soni:\", sum(result))\n",
    "      \n",
    "if __name__ == \"__main__\":\n",
    "    main()      "
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
