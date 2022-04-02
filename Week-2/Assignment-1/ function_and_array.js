function max(numbers) {
    let temp = numbers[0];
    for (let i = 0; i < numbers.length; i++){
        if (numbers[i] > temp){
            temp = numbers[i];
        }
    }

    return temp;

}

console.log( max([1, 2, 4, 5]) ); // should print 5
console.log( max([5, 2, 7, 1, 6]) ); // should print 7

/*
=======================================================================
 */

function findPosition(numbers, target) {
    let index = 0;
    for(let i = 0; i < numbers.length; i++){
        if (numbers[i] == target){
            return index;
        }

        index ++;
    }

    return -1; 
}

console.log( findPosition([5, 2, 7, 1, 6], 5) ); // should print 0
console.log( findPosition([5, 2, 7, 1, 6], 7) ); // should print 2
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); // should print 2 (the first one) 
console.log( findPosition([5, 2, 7, 1, 6], 8) ); // should print -1