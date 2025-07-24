{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3d900948-2b4d-48a3-bb8d-59e3ffa977c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First : a Last : n\n"
     ]
    }
   ],
   "source": [
    "text = 'automation'\n",
    "print('First :',text[0] , 'Last :',text[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "beb93667-2fd0-45f8-8b9d-9e07a742f2d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed : automatio\n"
     ]
    }
   ],
   "source": [
    "print('Reversed :' , text[:-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce674279-54df-4a93-adfb-aca5f55652d8",
   "metadata": {},
   "source": [
    "**string[start : stop : step]**\n",
    "\n",
    "So, text[::-1] means:\n",
    "\n",
    "**start** → empty → means start from the beginning (or end if step is negative)\n",
    "\n",
    "**stop** → empty → means stop at the end (or beginning if step is negative)\n",
    "\n",
    "**step** → -1 → step is -1, which means go backwards by one character each time.\n",
    "\n",
    "So, when you do [::-1], Python goes through the string from end to start, producing a reversed version."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "15532ae3-84c8-4cf2-bfeb-4a3bb86213f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed :  noitamotua\n"
     ]
    }
   ],
   "source": [
    "print('Reversed : ' , text[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e5684fed-3ad6-4171-a944-524598de710f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Count of  u: 1\n"
     ]
    }
   ],
   "source": [
    "print(\"Count of  u:\" ,text.count('u'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "91781c5e-3c84-4e76-a44c-30a0016beec7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO WORLD\n"
     ]
    }
   ],
   "source": [
    "greet = 'Hello'\n",
    "name = 'World'\n",
    "combined = greet + \" \" + name\n",
    "print(combined.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e959a48-e4fc-4b06-bde2-bc64b6ff2b04",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
