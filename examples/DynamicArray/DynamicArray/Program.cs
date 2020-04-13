using System;
using System.Collections.Generic;

namespace DynamicArray
{
    class Program
    {
        static void Main(string[] args)
        {
            DynamicArray<int> array = new DynamicArray<int>(5);


            array.append(1);
            array.append(2);
            array.append(3);
            array.append(4);
            array.append(5);
            array.append(6);

            Console.WriteLine("size : " + array.size);
            array.remove();

            Console.WriteLine("size : " + array.size);
            Console.ReadLine();
        }
    }

    public class DynamicArray<T>
    {
        public object[] data;
        public int size;
        public int initialCapacity;

        public DynamicArray(int initialCapacity)
        {
            this.initialCapacity = initialCapacity;
            data = new Object[initialCapacity];
        }

        public void set(int i, T e)
        {
            data[i] = e;
            size += 1;
        }

        public T get(int i)
        {
            return (T)data[i];
        }

        /// <summary>
        /// yeni veri ekleme
        /// </summary>
        /// <param name="e"></param>
        public void append(T e)
        {
            if (size == initialCapacity)
            {
                this.resize();
            }

            data[size] = e;
            size++;
        }

        /// <summary>
        /// diziyi yeniden boyutlandır
        /// </summary>
        public void resize() 
        {

            Object[] newData = new Object[initialCapacity * 2];
            for (int i = 0; i < initialCapacity; i++)
            {
                newData[i] = data[i];
            }
            data = newData;
            initialCapacity = initialCapacity * 2;
        }

        /// <summary>
        /// son eklenen elemanı siler
        /// </summary>
        public void remove()
        {
            int length = data.Length - 1;

            for (int j = length; j > 0; j--)
            {
                if (data[j] != null)
                {
                    data[j] = null;
                    break;
                }
            }

            size--;
        }

        /// <summary>
        /// indeksi verilen veri silinir
        /// </summary>
        /// <param name="i"></param>
        public void remove(int i)
        {
            for (int j = i; j < size - 1; j++)
            {
                data[j] = data[j + 1];
            }
            size--;
        }
    }
}
