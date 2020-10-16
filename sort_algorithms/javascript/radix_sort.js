// Radix Sort
// Javascript
// Porter L

function radixSort(Arr){
    console.log('radix sort');
    let largest = Math.max(...Arr) * 10;
    let divisor = 10;

    while (divisor < largest) {
        let buckets = [...Array(10)].map(() => []);

        for (let num of Arr){
            buckets[Math.floor((num % divisor) / (divisor / 10))].push(num);
        }
        Arr = [].concat.apply([], buckets);
        divisor *= 10;
    }
    return Arr;
}