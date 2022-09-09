
function solution(str){
   if(str.length % 2 != 0)
   {
     str += "_" ;
   }
   return str.split(/([^\s]{0,2})/g).filter(el => 
   {
    return el != ""
   })

  return r
}

// Link: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
