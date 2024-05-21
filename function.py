{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b8d68392",
   "metadata": {},
   "source": [
    "# Function "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "940e879d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a dictionary\n",
      "{'Car1': 'BMW', 'Car2': 'AUDi', 'Car3': 'KIA'}\n"
     ]
    }
   ],
   "source": [
    "print('This is a dictionary')\n",
    "\n",
    "def dictName(val1,val2,val3):\n",
    "    join_Name = f'{val1}{val2}{val3}'\n",
    "    result = {\n",
    "        'Car1':val1,\n",
    "        'Car2':val2,\n",
    "        'Car3':val3,\n",
    "    }\n",
    "    return result\n",
    "\n",
    "\n",
    "val1 = \"BMW\"\n",
    "val2 = \"AUDi\"\n",
    "val3 = \"KIA\"\n",
    "output = dictName(val1,val2,val3)\n",
    "\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7aef208",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "93cb8e66",
   "metadata": {},
   "outputs": [],
   "source": [
    "def my_function(f1,f2,f3):\n",
    "    joint_name = f'{f1},{f2},{f3}'\n",
    "    result = {'name1':f1,'name2':f2,'name3':f3}\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c2364a91",
   "metadata": {},
   "outputs": [],
   "source": [
    "f1 = \"c1\"\n",
    "f2 = \"c2\"\n",
    "f3 = \"c3\"\n",
    "output = my_function(f1,f2,f3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4b94793f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name1': 'c1', 'name2': 'c2', 'name3': 'c3'}\n"
     ]
    }
   ],
   "source": [
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "708ba274",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}