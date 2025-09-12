{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "56f1a5ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Cannot divide by zero!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x = 10 / 0\n",
    "except ZeroDivisionError:\n",
    "    print(\"Error: Cannot divide by zero!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "08ca0482",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Error: That was not a valid integer!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    n = int(input(\" Enter an integer: \"))\n",
    "    print(\"You entered:\", n)\n",
    "except ValueError:\n",
    "    print(\" Error: That was not a valid integer!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2f5dbebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: File not found!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    with open(\"non_existing_file.txt\", \"r\") as f:\n",
    "        print(f.read())\n",
    "except FileNotFoundError:\n",
    "    print(\"Error: File not found!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9f5b1032",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'b'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      2\u001b[39m     a = \u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33m Enter first number: \u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      3\u001b[39m     b = \u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mEnter second number: \u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m     result = \u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43ma\u001b[49m\u001b[43m)\u001b[49m + b \n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m:\n\u001b[32m      6\u001b[39m     \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33m Error: Both inputs must be numerical!\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: 'b'"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    a = input(\" Enter first number: \")\n",
    "    b = input(\"Enter second number: \")\n",
    "    result = int(a) + b \n",
    "except TypeError:\n",
    "    print(\" Error: Both inputs must be numerical!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3ba20e9a",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'with' statement on line 2 (2065674221.py, line 3)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mexcept PermissionError:\u001b[39m\n                           ^\n\u001b[31mIndentationError\u001b[39m\u001b[31m:\u001b[39m expected an indented block after 'with' statement on line 2\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    with open(\"/etc/shadow\", \"r\") as f:  \n",
    "except PermissionError:\n",
    "    print(\"Error: Permission denied!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "da6ed429",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: List index out of range!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    lst = [1, 2, 3]\n",
    "    print(lst[5])\n",
    "except IndexError:\n",
    "    print(\"Error: List index out of range!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f5976713",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (1209534440.py, line 2)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[9]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mprint(\"You entered:\", n)\u001b[39m\n    ^\n\u001b[31mIndentationError\u001b[39m\u001b[31m:\u001b[39m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\" Enter a number (press Ctrl+C to cancel): \"))\n",
    "    print(\"You entered:\", n)\n",
    "except KeyboardInterrupt:\n",
    "    print(\"\\n Error: Input cancelled by user!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7c5afe73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Arithmetic error occurred!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    result = 10 / 0\n",
    "except ArithmeticError:\n",
    "    print(\"Error: Arithmetic error occurred!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4be74862",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'file_with_encoding_issue.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[11]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mfile_with_encoding_issue.txt\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mascii\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      3\u001b[39m         \u001b[38;5;28mprint\u001b[39m(f.read())\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mUnicodeDecodeError\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'file_with_encoding_issue.txt'"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    with open(\"file_with_encoding_issue.txt\", \"r\", encoding=\"ascii\") as f:\n",
    "        print(f.read())\n",
    "except UnicodeDecodeError:\n",
    "    print(\"Error: Unicode decoding failed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "19e4e998",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: List object has no attribute 'push'\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    lst = [1, 2, 3]\n",
    "    lst.push(4)  # Python list has no push() method\n",
    "except AttributeError:\n",
    "    print (\"Error: List object has no attribute 'push'\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ac4769ce",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'example.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[13]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mexample.txt\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      2\u001b[39m     content = f.read()\n\u001b[32m      3\u001b[39m     \u001b[38;5;28mprint\u001b[39m(content)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'example.txt'"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    content = f.read()\n",
    "    print(content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f6737343",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'example.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[14]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m n = \u001b[32m5\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mexample.txt\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(n):\n\u001b[32m      4\u001b[39m         line = f.readline()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'example.txt'"
     ]
    }
   ],
   "source": [
    "n = 5\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    for i in range(n):\n",
    "        line = f.readline()\n",
    "        print(line, end=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e45f5538",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "This is appended text.\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"a\") as f:\n",
    "    f.write(\"\\nThis is appended text.\")\n",
    "\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "82170799",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "This is appended text.\n"
     ]
    }
   ],
   "source": [
    "n = 5\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.readlines()\n",
    "    print(\"\".join(lines[-n:]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fef0ee5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['\\n', 'This is appended text.']\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines_list = f.readlines()\n",
    "print(lines_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4ae5941c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "This is appended text.\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    content = f.read()\n",
    "print(content)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "36a45f93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['', 'This is appended text.']\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    array = [line.strip() for line in f]\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "07b5aa26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Longest word: appended\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    words = f.read().split()\n",
    "    longest = max(words, key=len)\n",
    "print(\"Longest word:\", longest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "839deca1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of lines: 2\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    line_count = sum(1 for line in f)\n",
    "print(\"Number of lines:\", line_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "09301cc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'This': 1, 'is': 1, 'appended': 1, 'text.': 1})\n"
     ]
    }
   ],
   "source": [
    "from collections import Counter\n",
    "\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    words = f.read().split()\n",
    "freq = Counter(words)\n",
    "print(freq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e73b2170",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File size in bytes: 24\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "size = os.path.getsize(\"example.txt\")\n",
    "print(\"File size in bytes:\", size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "97963a36",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = [\"apple\", \"banana\", \"cherry\"]\n",
    "with open(\"output.txt\", \"w\") as f:\n",
    "    for item in my_list:\n",
    "        f.write(item + \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "84faba3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f1, open(\"copy.txt\", \"w\") as f2:\n",
    "    f2.write(f1.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8f01efac",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'file1.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[27]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mfile1.txt\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f1, \u001b[38;5;28mopen\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mfile2.txt\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mr\u001b[39m\u001b[33m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f2, \u001b[38;5;28mopen\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mcombined.txt\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mw\u001b[39m\u001b[33m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f_out:\n\u001b[32m      2\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m line1, line2 \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mzip\u001b[39m(f1, f2):\n\u001b[32m      3\u001b[39m         f_out.write(line1.strip() + \u001b[33m\"\u001b[39m\u001b[33m \u001b[39m\u001b[33m\"\u001b[39m + line2)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'file1.txt'"
     ]
    }
   ],
   "source": [
    "with open(\"file1.txt\", \"r\") as f1, open(\"file2.txt\", \"r\") as f2, open(\"combined.txt\", \"w\") as f_out:\n",
    "    for line1, line2 in zip(f1, f2):\n",
    "        f_out.write(line1.strip() + \" \" + line2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1523923a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.readlines()\n",
    "    print(random.choice(lines))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fffb5f65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "f = open(\"example.txt\", \"r\")\n",
    "print(f.closed)  \n",
    "f.close()\n",
    "print(f.closed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "241d40fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['', 'This is appended text.']\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = [line.strip() for line in f]\n",
    "print(lines)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "bb41665f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of words: 4\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    text = f.read().replace(\",\", \" \")\n",
    "    word_count = len(text.split())\n",
    "print(\"Number of words:\", word_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5e46844e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['\\n', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', 'p', 'p', 'e', 'n', 'd', 'e', 'd', ' ', 't', 'e', 'x', 't', '.']\n"
     ]
    }
   ],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    chars = [char for char in f.read()]\n",
    "print(chars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dcf4d608",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "for letter in string.ascii_uppercase:\n",
    "    with open(f\"{letter}.txt\", \"w\") as f:\n",
    "        f.write(f\"This is file {letter}.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e86b7629",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "letters_per_line = 5\n",
    "with open(\"alphabet.txt\", \"w\") as f:\n",
    "    for i in range(0, 26, letters_per_line):\n",
    "        f.write(\"\".join(string.ascii_uppercase[i:i+letters_per_line]) + \"\\n\")"
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
