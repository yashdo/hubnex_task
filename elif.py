{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b6760e7e-6a77-4b73-8806-d26fa4ead031",
   "metadata": {},
   "source": [
    "# join text"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f60addad-0941-4e56-94f4-479c420efc5c",
   "metadata": {},
   "source": [
    "### join a multple strings whith help of function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "93fde824-118e-41ab-8cbe-3e80539c175f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def join_text (*args,separator=''):\n",
    "    return separator.join(args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b3afa057-2735-47ab-bdb1-ad52b576c66e",
   "metadata": {},
   "outputs": [],
   "source": [
    "t1 = \"Class\"\n",
    "t2 = \"room\"\n",
    "\n",
    "joined_text = join_text(t1,t2, separator=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c169ca2d-9d4e-4693-9b80-2404cbb9354d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Class room\n"
     ]
    }
   ],
   "source": [
    "print(joined_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be44e336-d596-4e27-b439-6bf7a05257fa",
   "metadata": {},
   "source": [
    "# trim text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "215cc84a-826b-4700-bfaf-6f60968831fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def trim(text, side = 'both'):\n",
    "    if side == 'left':\n",
    "        return text.lstrip()\n",
    "    elif side == 'right':\n",
    "        return text.rstrip()\n",
    "    elif side == 'both':\n",
    "        return text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1d5b6723-e435-430c-8643-09a988f3a43c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "trimmed(both side): classroom\n"
     ]
    }
   ],
   "source": [
    "text = \"        classroom     \"\n",
    "\n",
    "trimmed_text_both = trim(text)\n",
    "print('trimmed(both side):',trimmed_text_both)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ae03676-8f92-4bc9-8b09-8ea11bd7dcd5",
   "metadata": {},
   "source": [
    "# substitute text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "bb86ed80-dc4d-417b-a0c2-885a018a431b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def substitute_text(text,old,new):\n",
    "    return text.replace(old,new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "faa7417e",
   "metadata": {},
   "outputs": [],
   "source": [
    "real_text = \"I am buying a Ferrari tomorrow\"\n",
    "old_text = \"Ferrari\"\n",
    "new_text = \"BMW\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "12e4e5b1-d52a-4329-b373-8580a07ba925",
   "metadata": {},
   "outputs": [],
   "source": [
    "substituted_text = substitute_text(real_text,old_text,new_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0ed1402e-3803-4cf6-b54f-cdfdacdfebf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am buying a Ferrari tomorrow\n",
      "I am buying a BMW tomorrow\n"
     ]
    }
   ],
   "source": [
    "print(real_text)\n",
    "print(substituted_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "698bc75f-840f-4d96-96fc-a6fe70076147",
   "metadata": {},
   "source": [
    "# cut text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9d626a21-9403-43a0-964c-7b1d037cb773",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cut_text(text,start,end):\n",
    "    return text[start:end]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "915f0e42",
   "metadata": {},
   "outputs": [],
   "source": [
    "real_text = \"I am buying a Ferrari tomorrow\"\n",
    "start_position = 14\n",
    "end_position = 22"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "83b58463-cb97-4163-8d8b-8ac58af01fc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "cut_portion = cut_text(real_text,start_position,end_position)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5c39c357-f9a0-48dc-8087-bd83b9d24a41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am buying a Ferrari tomorrow\n",
      "Ferrari \n"
     ]
    }
   ],
   "source": [
    "print(real_text)\n",
    "print(cut_portion)"
   ]
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