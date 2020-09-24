{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'function_2c' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-ee8e8f0dccc9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mS1\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m100\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1000\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m-\u001b[0m\u001b[1;36m50\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'seminars'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Seminars'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'CLS'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'cLs'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Borrel'\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mvar_1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunction_2c\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m50\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'add'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[0mvar_2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunction_2b\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Seminars'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Borrel'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'C'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'function_2c' is not defined"
     ]
    }
   ],
   "source": [
    "from assignnment_2b import function_2b\n",
    "from assignment_2c import function_2c\n",
    "\"\"\"\n",
    "Used the imported functions (function_2b and function_2c) and the documentation\n",
    "provided by your teammates to generate the correct answers below. You can use\n",
    "the following numbers and strings as input for the 2 functions:\n",
    "[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']\n",
    "Run the script to see if you succeeded! PS: Multiple combinations are possible,\n",
    "just give a correct one.\n",
    "\"\"\"\n",
    "S1 ={5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel'}\n",
    "\n",
    "var_1 = function_2c(-50, 5, 10, 1000)['add']\n",
    "\n",
    "var_2 = function_2b('Seminars','Borrel')['C']\n",
    "\n",
    "var_3 = str(function_2c(5, 10, 1000, -50)['multiply']) + function_2b('cls','')['L']\n",
    "\n",
    "if var_1 == 950:\n",
    "    print(\"Good job!\")\n",
    "\n",
    "if var_2 == \"SeminarsBorrel\":\n",
    "    print(\"Well done!\")\n",
    "\n",
    "if var_3 == \"10000cls\":\n",
    "    print(\"Excellent!\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
