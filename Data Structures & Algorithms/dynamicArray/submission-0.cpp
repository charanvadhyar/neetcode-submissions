class DynamicArray {

private :
  int* data ;
  int length;
  int capacity;
public:

    DynamicArray(int capacity) {
     this -> capacity = capacity;
     data = new int[capacity];
     length = 0;

    }

    int get(int i) {
        return data[i];

    }

    void set(int i, int n) {
        data[i] = n;

    }

    void pushback(int n) {
        if(length == capacity)
            resize();
        data[length] = n;
        length ++;

    }

    int popback() {
        length --;
        return data[length];

    }

    void resize() {
        int new_capacity = capacity *2;
        int* newData = new int[new_capacity];
        for(int i=0;i<length;i++)
        {
            newData[i] = data[i];
        }

        delete[] data;
        data = newData;
        capacity = new_capacity;

    }

    int getSize() {
        return length;

    }

    int getCapacity() {
        return capacity;

    }
};
