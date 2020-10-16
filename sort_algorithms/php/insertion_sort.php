<?php
// Insertion Sort
// PHP
// Porter L

function insertionSort($Arr)
{
    for($x=0;$x<count($Arr);$x++){
        $num = $Arr[$x];
        $y = $x-1;
        while($y>=0 && $Arr[$y] > $num){
            $Arr[$y+1] = $Arr[$y];
            $y--;
        }
        $Arr[$y+1] = $num;
    }
    return $Arr;
}

// Example
$test_array = array(2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3);
echo "Original Array : ";
echo implode(', ',$test_array );
echo "\nSorted Array : ";
echo implode(', ',insertionSort($test_array));
echo "\n";

?>