{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1bb83f24",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4114880d",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = [12.23, 13.32, 100, 36.32]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ba2a7d99",
   "metadata": {},
   "outputs": [],
   "source": [
    "array_1d = np.array(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ccb049b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List: [12.23, 13.32, 100, 36.32]\n",
      "One-dimensional NumPy array: [ 12.23  13.32 100.    36.32]\n"
     ]
    }
   ],
   "source": [
    "print(\"Original List:\", my_list)\n",
    "print(\"One-dimensional NumPy array:\", array_1d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0635bc51",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = np.arange(2, 11).reshape(3, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a1a07c9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3x3 Matrix (2-10):\n",
      "[[ 2  3  4]\n",
      " [ 5  6  7]\n",
      " [ 8  9 10]]\n"
     ]
    }
   ],
   "source": [
    "print(\"3x3 Matrix (2-10):\")\n",
    "print(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "855812b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7404baeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Null Vector:\n",
      "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "null_vector = np.zeros(10)\n",
    "print(\"Original Null Vector:\")\n",
    "print(null_vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cea2fff6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After updating sixth value to 11:\n",
      "[ 0.  0.  0.  0.  0. 11.  0.  0.  0.  0.]\n"
     ]
    }
   ],
   "source": [
    "null_vector[5] = 11\n",
    "print(\"After updating sixth value to 11:\")\n",
    "print(null_vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5e097d3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "31b8d238",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35\n",
      " 36 37]\n"
     ]
    }
   ],
   "source": [
    "array = np.arange(12, 38)  # yuqori chegara kiritilmaydi\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a9caebb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "37c14f17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4])\n",
    "print(\"Original array:\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8331514d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array converted to float type: [1. 2. 3. 4.]\n"
     ]
    }
   ],
   "source": [
    "arr_float = arr.astype(float)\n",
    "print(\"Array converted to float type:\", arr_float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cc8e542d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "30e911a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "celsius = np.array([0, 12, 45.21, 34, 99.91])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "128350b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "fahrenheit = celsius * 9/5 + 32\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2a58dde1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Values in Fahrenheit degrees: [ 32.     53.6   113.378  93.2   211.838]\n",
      "Values in Centigrade degrees: [ 0.   12.   45.21 34.   99.91]\n"
     ]
    }
   ],
   "source": [
    "print(\"Values in Fahrenheit degrees:\", fahrenheit)\n",
    "print(\"Values in Centigrade degrees:\", celsius)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d22e5811",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2f363152",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [10 20 30]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([10, 20, 30])\n",
    "print(\"Original array:\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9769eb0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "values_to_append = [40, 50, 60, 70, 80, 90]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "cffe2e7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After append values to the end of the array: [10 20 30 40 50 60 70 80 90]\n"
     ]
    }
   ],
   "source": [
    "arr_appended = np.append(arr, values_to_append)\n",
    "print(\"After append values to the end of the array:\", arr_appended)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a04a7e37",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "14b972d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random array: [90  5 71 14 73 49 24 58 21 57]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.randint(0, 100, size=10)\n",
    "print(\"Random array:\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "6f2d8b87",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_value = np.mean(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "04735f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "median_value = np.median(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f1e226d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "std_value = np.std(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "21b36f7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean: 46.2\n",
      "Median: 53.0\n",
      "Standard Deviation: 27.161737794183935\n"
     ]
    }
   ],
   "source": [
    "print(\"Mean:\", mean_value)\n",
    "print(\"Median:\", median_value)\n",
    "print(\"Standard Deviation:\", std_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d38a9401",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5604640d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3x3x3 Random Array:\n",
      " [[[0.04547066 0.39043373 0.15212001]\n",
      "  [0.95592072 0.25414136 0.57293193]\n",
      "  [0.06274499 0.76163794 0.70971274]]\n",
      "\n",
      " [[0.37886763 0.63793112 0.87669443]\n",
      "  [0.56825062 0.82480882 0.23288283]\n",
      "  [0.29789434 0.11722448 0.25280881]]\n",
      "\n",
      " [[0.90623491 0.92560506 0.72975713]\n",
      "  [0.50100587 0.43748364 0.51746005]\n",
      "  [0.41476161 0.57759473 0.15942898]]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(3, 3, 3)\n",
    "print(\"3x3x3 Random Array:\\n\", arr)"
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
