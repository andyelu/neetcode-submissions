class DynamicArray {

    private int[] data;
    private int size;
    private int capacity;

    public DynamicArray(int capacity) {
        data = new int[capacity];
        size = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return data[i];
    }

    public void set(int i, int n) {
        data[i] = n;
    }

    public void pushback(int n) {
        if (size == data.length) {
            resize();
        }

        data[size] = n;
        size++;
    }

    public int popback() {
        int res = data[size-1];
        data[size-1] = 0;
        size--;
        return res;
    }

    private void resize() {
        int[] temp = new int[capacity *= 2];
        for (int i = 0; i < size; i++) {
            temp[i] = data[i];
        }

        data = temp;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
