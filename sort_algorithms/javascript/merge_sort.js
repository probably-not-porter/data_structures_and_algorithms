// Merge Sort
// Javascript
// Porter L

function mergeSort(Arr){
    console.log('merge sort');
    var len = Arr.length;
    if(len <2)
       return Arr;

    var mid = Math.floor(len/2),
        left = Arr.slice(0,mid),
        right =Arr.slice(mid);

    return merge(mergeSort(left),mergeSort(right));
 }
 function merge(left, right){

    var result = [];
    var l = 0;
    var r = 0;

    while(l < left.length && r < right.length){
       if(left[l] < right[r]){
         result.push(left[l++]);
       }
       else{
         result.push(right[r++]);
      }
    }  

    return result.concat(left.slice(l)).concat(right.slice(r));
  } 