<?php
// Selection Sort
// PHP
// Porter L

function bubbleSort($Arr){
    for ($x = 0; $x < count($Arr) - 1; $x++){
        for ($y = 0; $y < count($Arr) - $x - 1; $y++){
            if ($Arr[$y] > $Arr[$y + 1]){
                $b = $Arr[$y];
                $Arr[$y] = $Arr[$y + 1];
                $Arr[$y + 1] = $b;
            }
        }
    }
    return $Arr;
}

// Example
$test_array = array(2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3);
echo "Original Array : ";
echo implode(', ',$test_array );
echo "\nSorted Array : ";
echo implode(', ',bubbleSort($test_array));
echo "\n";

?>