{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "45f32af5",
   "metadata": {},
   "source": [
    "| year | rank | company                | revenue | profit |\n",
    "| :--- | :--- | :---                   | :---    | :---   |\n",
    "| 1955 | 229  | Norton                 | 135.0   | N.A.   |\n",
    "| 1955 | 291  | Schlitz Brewing        | 100.0   | N.A.   |\n",
    "| 1955 | 295  | Pacific Vegetable Oil  | 97.9    | N.A.   |\n",
    "| 1955 | 297  | Liebmann Breweries     | 96.0    | N.A.   |\n",
    "| 1955 | 353  | Minneapolis-Moline     | 77.4    | N.A.   |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e49d893e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74.1 ms ± 7.41 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)\n",
      "65.8 ms ± 3.59 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import random\n",
    "\n",
    "random.seed(8)\n",
    "int_list = []\n",
    "float_list = []\n",
    "\n",
    "\n",
    "for i in range(0, 1000):\n",
    "    int_list.append(random.randint(0, 5000))\n",
    "    float_list.append(random.uniform(0.1, 100.0))\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "def selection_sort(data):\n",
    "    for scanIndex in range(0, len(data)):\n",
    "        minIndex = scanIndex\n",
    "        for compIndex in range(scanIndex + 1, len(data)):\n",
    "            if data[compIndex] < data[minIndex]:\n",
    "                minIndex = compIndex\n",
    "        if minIndex != scanIndex:\n",
    "            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "%timeit -n 10 selection_sort (int_list)\n",
    "%timeit -n 10 selection_sort (float_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92d4a621",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b191829",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
