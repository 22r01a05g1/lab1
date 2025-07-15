{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYuxPeaboXmY2yYVgQ0G3q"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aBvgY_TGAaAc",
        "outputId": "d9134ab0-8cb3-41de-9aaa-63b3fe40f51a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " -------welcome to the shopping cart-----\n",
            "1. Add_item\n",
            "2. Remove_item\n",
            "3. View_cart\n",
            "4. Exit\n",
            "Enter your choice: 2\n",
            "Enter the item to remove:shirt\n",
            "shirt has been removed from the cart.\n",
            "\n",
            " -------welcome to the shopping cart-----\n",
            "1. Add_item\n",
            "2. Remove_item\n",
            "3. View_cart\n",
            "4. Exit\n",
            "Enter your choice: 3\n",
            "Enter the item to view:pant\n",
            "Items in your cart:\n",
            "tshirt\n",
            "pant\n",
            "saree\n",
            "\n",
            " -------welcome to the shopping cart-----\n",
            "1. Add_item\n",
            "2. Remove_item\n",
            "3. View_cart\n",
            "4. Exit\n",
            "Enter your choice: 1\n",
            "Enter the item to add: silk\n",
            "silk has been added to the cart.\n",
            "\n",
            " -------welcome to the shopping cart-----\n",
            "1. Add_item\n",
            "2. Remove_item\n",
            "3. View_cart\n",
            "4. Exit\n",
            "Enter your choice: 3\n",
            "Enter the item to view:silk\n",
            "Items in your cart:\n",
            "tshirt\n",
            "pant\n",
            "saree\n",
            "silk\n",
            "\n",
            " -------welcome to the shopping cart-----\n",
            "1. Add_item\n",
            "2. Remove_item\n",
            "3. View_cart\n",
            "4. Exit\n"
          ]
        }
      ],
      "source": [
        "cart_item = [\"shirt\" , \"tshirt\" , \"pant\" , \"saree\"]\n",
        "while True:\n",
        "   print(\"\\n -------welcome to the shopping cart-----\")\n",
        "   print(\"1. Add_item\")\n",
        "   print(\"2. Remove_item\")\n",
        "   print(\"3. View_cart\")\n",
        "   print(\"4. Exit\")\n",
        "   choice = input(\"Enter your choice: \")\n",
        "   if choice == \"1\":\n",
        "      item = input(\"Enter the item to add: \")\n",
        "      cart_item.append(item)\n",
        "      print(f\"{item} has been added to the cart.\")\n",
        "   elif choice == \"2\":\n",
        "        item = input(\"Enter the item to remove:\")\n",
        "        if item in cart_item:\n",
        "         cart_item.remove(item)\n",
        "        print(f\"{item} has been removed from the cart.\")\n",
        "   elif choice == \"3\":\n",
        "        item = input(\"Enter the item to view:\")\n",
        "        if not cart_item:\n",
        "           print(\"Cart is empty\")\n",
        "        else:\n",
        "           print(\"Items in your cart:\")\n",
        "           for i ,item in enumerate(cart_item, start=1):\n",
        "            print(f\"{item}\")\n",
        "   elif choice == \"4\":\n",
        "      print(\"Thanks you for shopping\")\n",
        "      break\n",
        "   else:\n",
        "     print(\"invalid choice\")\n"
      ]
    }
  ]
}