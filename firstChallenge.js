/**
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
let sum = 0;
 for(var i = 1; i < 1000; i++) {
     if(i % 3 == 0) {
         sum += i
         console.log(i)
         continue ;
         
     }
     if(i % 5 ==0 ) {
         sum += i
        console.log(i)
         continue ;
         
         
     }
 }

console.log(sum)
/**
 * My first attempt was a failure, because I forgot to exclude 1000 from the loop. Next time, I did not miss the chance to complete the challenge!
 */